import { mkdirSync, mkdtempSync, rmSync, writeFileSync } from 'fs'
import { tmpdir } from 'os'
import { join } from 'path'
import { afterEach, describe, expect, test } from 'vitest'
import { loadBrandFoundation } from '../brands/load'
import { buildCardLabHtml } from './build'

const roots: string[] = []

function createWorkspace(): string {
  const root = mkdtempSync(join(tmpdir(), 'loom-lab-'))
  roots.push(root)
  mkdirSync(join(root, 'brands', 'givecare'), { recursive: true })
  writeFileSync(
    join(root, 'brands', 'givecare', 'logo.png'),
    Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9Wn7n6cAAAAASUVORK5CYII=', 'base64'),
  )
  writeFileSync(
    join(root, 'brands', 'givecare', 'brand.yml'),
    `
id: givecare
name: GiveCare
positioning: Care as infrastructure.
audiences:
  - id: caregivers
    summary: Family caregivers balancing work and care.
offers:
  - id: invisiblebench
    summary: Benchmarking and care tooling.
proof_points:
  - 63 million Americans are caregivers.
pillars:
  - id: care-economy
    perspective: Caregiving is infrastructure and should be discussed as such.
    signals:
      - caregiver benefits
      - care deserts
    format: analysis
    frequency: weekly
voice:
  tone: Warm, direct, specific.
  style: Human, plainspoken.
  do:
    - Name the problem directly.
  dont:
    - Use therapeutic cliches.
channels:
  social:
    objective: Build signal and authority.
  blog:
    objective: Publish durable longform thinking.
  outreach:
    objective: Start useful conversations.
  respond:
    objective: Reply with clarity and care.
visual:
  logo: logo.png
  palette:
    background: "#FDF9EC"
    primary: "#3D1600"
    accent: "#FF9F00"
  typography:
    headline: "Alegreya, serif, bold"
    body: "Inter, sans-serif, regular"
    accent: "Gabarito, sans-serif, bold"
  motif: Soft concentric rings.
  layout: calm-editorial
response_playbooks:
  - id: skeptical-comment
    trigger: skepticism
    approach: Clarify the claim and add evidence.
outreach_playbooks:
  - id: intro
    trigger: first-touch
    approach: Lead with a sharp observation and one ask.
`.trim(),
    'utf8',
  )
  return root
}

afterEach(() => {
  while (roots.length > 0) {
    rmSync(roots.pop()!, { recursive: true, force: true })
  }
})

describe('buildCardLabHtml', () => {
  test('builds a self-contained interactive card lab document', () => {
    const root = createWorkspace()
    const brand = loadBrandFoundation('givecare', { root })

    const html = buildCardLabHtml({
      brand,
      brandAssetBasePath: join(root, 'brands', 'givecare'),
      initialCardType: 'quote',
      initialHeadline: 'Care is infrastructure',
      initialBody: 'Invisible labor should be visible labor.',
      initialPlatform: 'linkedin',
    })

    expect(html).toContain('<title>GiveCare Card Lab</title>')
    expect(html).toContain('Generate 20 Variations')
    expect(html).toContain('Head to head')
    expect(html).toContain('Choose between two directions')
    expect(html).toContain('Prefer left')
    expect(html).toContain('Current leaning')
    expect(html).toContain('Care is infrastructure')
    expect(html).toContain('data:image/png;base64,')
    expect(html).toContain('Copy top preset JSON')
  })
})
