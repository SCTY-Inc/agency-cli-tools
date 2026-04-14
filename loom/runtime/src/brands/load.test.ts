import { mkdtempSync, mkdirSync, writeFileSync, rmSync, realpathSync } from 'fs'
import { tmpdir } from 'os'
import { join } from 'path'
import { afterEach, describe, expect, test } from 'vitest'
import { loadBrandFoundation } from './load'
import { resolveRuntimePaths } from '../core/paths'

const roots: string[] = []
const originalCwd = process.cwd()

function createWorkspace(): string {
  const root = mkdtempSync(join(tmpdir(), 'loom-brand-'))
  roots.push(root)
  mkdirSync(join(root, 'brands', 'givecare'), { recursive: true })
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
  palette:
    background: "#FDF9EC"
    primary: "#3D1600"
    accent: "#FF9F00"
response_playbooks:
  - id: skeptical-comment
    trigger: skepticism
    approach: Clarify the claim and add evidence.
outreach_playbooks:
  - id: intro
    trigger: first-touch
    approach: Lead with a sharp observation and one ask.
`.trim(),
  )
  return root
}

afterEach(() => {
  process.chdir(originalCwd)
  while (roots.length > 0) {
    rmSync(roots.pop()!, { recursive: true, force: true })
  }
})

describe('loadBrandFoundation', () => {
  test('loads a first-principles brand foundation from brand.yml', () => {
    const root = createWorkspace()

    const brand = loadBrandFoundation('givecare', { root })

    expect(brand.id).toBe('givecare')
    expect(brand.channels.blog.objective).toContain('longform')
    expect(brand.responsePlaybooks).toHaveLength(1)
    expect(brand.visual.palette.accent).toBe('#FF9F00')
    expect(brand.pillars).toEqual([
      {
        id: 'care-economy',
        perspective: 'Caregiving is infrastructure and should be discussed as such.',
        signals: ['caregiver benefits', 'care deserts'],
        format: 'analysis',
        frequency: 'weekly',
      },
    ])
  })

  test('rejects unsupported handle keys', () => {
    const root = createWorkspace()
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
handles:
  mastodon: '@givecare'
visual:
  palette:
    background: "#FDF9EC"
    primary: "#3D1600"
    accent: "#FF9F00"
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

    expect(() => loadBrandFoundation('givecare', { root })).toThrow('Invalid brand foundation: handles.mastodon is not a supported platform')
  })

  test('resolves the workspace root when invoked from the agent directory', () => {
    const root = createWorkspace()
    const agentDir = join(root, 'agent')
    mkdirSync(agentDir, { recursive: true })
    process.chdir(agentDir)

    const paths = resolveRuntimePaths()

    expect(paths.root).toBe(realpathSync(root))
    expect(paths.brandsDir).toBe(join(realpathSync(root), 'brands'))
  })
})
