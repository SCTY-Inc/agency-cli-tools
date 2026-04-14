/**
 * Social asset renderer.
 *
 * Two-phase pipeline:
 *   1. Gemini generates art-only image (no text, no logos)
 *   2. Canvas composites text + logo on top deterministically
 *
 * Falls back to solid-color canvas when no API key is set.
 */

import { existsSync, readFileSync, writeFileSync } from 'fs'
import { join } from 'path'
import { createCanvas, Image, type CanvasRenderingContext2D } from 'canvas'
import type { BrandFoundation, SocialPlatform } from '../domain/types'
import { ensureParentDir, type RuntimePaths } from '../core/paths'
import { ensureFontsRegistered } from './fonts'
import { generateImage } from './gemini'

ensureFontsRegistered()

// ── Types ──

interface RenderSocialAssetsOptions {
  brand: BrandFoundation
  paths: RuntimePaths
  runId: string
  headline: string
  body: string
  cta?: string
  sourceImagePath: string
  contentType?: string
}

interface PlatformSpec {
  platform: SocialPlatform
  width: number
  height: number
  aspect: string
  layout: 'wide' | 'square' | 'tall'
}

const PLATFORM_SPECS: PlatformSpec[] = [
  { platform: 'facebook',  width: 1200, height: 1200, aspect: '1:1',  layout: 'square' },
  { platform: 'instagram', width: 1080, height: 1350, aspect: '4:5',  layout: 'tall' },
  { platform: 'linkedin',  width: 1200, height: 1200, aspect: '1:1',  layout: 'square' },
  { platform: 'threads',   width: 1080, height: 1350, aspect: '4:5',  layout: 'tall' },
  { platform: 'twitter',   width: 1600, height: 900,  aspect: '16:9', layout: 'wide' },
]

// ── Helpers ──


function wrapText(ctx: CanvasRenderingContext2D, text: string, maxWidth: number): string[] {
  const words = text.split(/\s+/).filter(Boolean)
  const lines: string[] = []
  let current = ''
  for (const word of words) {
    const candidate = current ? `${current} ${word}` : word
    if (ctx.measureText(candidate).width <= maxWidth) {
      current = candidate
    } else {
      if (current) lines.push(current)
      current = word
    }
  }
  if (current) lines.push(current)
  return lines
}

// ── Phase 1: Gemini generates art-only image ──

function buildArtPrompt(
  spec: PlatformSpec,
  brand: BrandFoundation,
  headline: string,
): string {
  // Prefer the brand's curated image_prompt over generic composition tokens
  if (brand.visual.imagePrompt) {
    const base = brand.visual.imagePrompt.replace(/\[SUBJECT\]/gi, headline)
    // Override aspect ratio to match platform
    return base
      .replace(/1:1 square/gi, `${spec.aspect} at ${spec.width}x${spec.height}`)
      + '\nIMPORTANT: No text, no words, no letters, no logos, no brand names. Background visual only.'
  }

  // Fallback: build from brand visual tokens
  const lines: string[] = []
  lines.push(`A ${spec.aspect} abstract visual at ${spec.width}x${spec.height} pixels.`)
  if (brand.visual.style) lines.push(brand.visual.style)
  if (brand.visual.composition?.length) lines.push(`Composition: ${brand.visual.composition.join(', ')}.`)
  if (brand.visual.texture?.length) lines.push(`Texture: ${brand.visual.texture.join(', ')}.`)
  lines.push(`Palette: background ${brand.visual.palette.background}, primary ${brand.visual.palette.primary}, accent ${brand.visual.palette.accent}.`)
  if (brand.visual.negative?.length) lines.push(`Avoid: ${brand.visual.negative.join('. ')}.`)
  lines.push('IMPORTANT: No text, no words, no letters, no logos, no brand names. Background visual only.')
  return lines.join('\n')
}

// ── Phase 2: Canvas composites text + logo on top ──

function compositeAsset(
  artImage: Image | undefined,
  spec: PlatformSpec,
  brand: BrandFoundation,
  headline: string,
): Buffer {
  const { width, height } = spec
  const canvas = createCanvas(width, height)
  const ctx = canvas.getContext('2d')
  const palette = brand.visual.palette
  const margin = Math.round(width * 0.06)

  // Full-bleed background
  ctx.fillStyle = palette.background
  ctx.fillRect(0, 0, width, height)

  // Full-bleed art image
  if (artImage) {
    const imgScale = Math.max(width / artImage.width, height / artImage.height)
    const dw = artImage.width * imgScale
    const dh = artImage.height * imgScale
    ctx.drawImage(artImage, (width - dw) / 2, (height - dh) / 2, dw, dh)
  }

  // Headline — bottom-left, on the image
  ctx.textBaseline = 'top'
  const headSize = spec.layout === 'wide'
    ? Math.round(height * 0.09)
    : Math.round(width * 0.07)
  ctx.font = `400 ${headSize}px "Alegreya", Georgia, serif`
  ctx.fillStyle = palette.primary
  const maxW = width - margin * 2
  const lines = wrapText(ctx, headline, maxW).slice(0, 3)
  const lineH = headSize * 1.05
  const blockH = lines.length * lineH
  const cursorY = height - margin - blockH

  for (let i = 0; i < lines.length; i++) {
    ctx.fillText(lines[i], margin, cursorY + i * lineH)
  }

  return canvas.toBuffer('image/png')
}

// ── Public API ──

function outputPath(paths: RuntimePaths, runId: string, platform: SocialPlatform): string {
  return join(paths.artifactsDir, runId, `${platform}.png`)
}

export async function renderSocialAssets(options: RenderSocialAssetsOptions): Promise<Record<SocialPlatform, string>> {
  const hasApiKey = !!(process.env.GEMINI_API_KEY || process.env.GOOGLE_API_KEY)

  // Generate art image (or use source image fallback)
  let artImage: Image | undefined
  if (hasApiKey) {
    const artPrompt = buildArtPrompt(
      { platform: 'linkedin', width: 1200, height: 1200, aspect: '1:1', layout: 'square' },
      options.brand,
      options.headline,
    )
    const artBytes = await generateImage(artPrompt)
    if (artBytes) {
      artImage = new Image()
      artImage.src = artBytes
    }
  }
  if (!artImage && options.sourceImagePath && existsSync(options.sourceImagePath)) {
    artImage = new Image()
    artImage.src = readFileSync(options.sourceImagePath)
  }

  const assets = {} as Record<SocialPlatform, string>

  for (const spec of PLATFORM_SPECS) {
    const png = compositeAsset(artImage, spec, options.brand, options.headline)
    const path = outputPath(options.paths, options.runId, spec.platform)
    ensureParentDir(path)
    writeFileSync(path, png)
    assets[spec.platform] = path
  }

  return assets
}
