# agentcy-compass

Part of the agentcy monorepo — invoke via `agentcy compass` or `agentcy-compass`.

A CLI-first toolkit for managing brand identity, competitive intelligence, content production, and social publishing—all from your terminal.

## Current surfaces (monorepo)

- repo: `agentcy`
- Python distribution/package: `agentcy-compass`
- Python import root: `brand_os` (unchanged until explicit refactor)
- installed CLI: `agentcy-compass`
- dispatcher alias: `agentcy compass ...`
- writer contract: `brief.v1.writer = { repo: "brand-os", module: "agentcy-compass" }`

The package and CLI are Agentcy-branded, but canonical protocol lineage still keeps the historical `writer.repo` value for compatibility.

Boundary note:
- canonical ownership: `brief.v1`
- preferred stage surfaces: `brand`, `signals`, `intel`, `plan`
- secondary surfaces: `produce`, `eval`, `publish`, `monitor`
- deprecated persona surface: use `agentcy-vox` for persona authoring/testing/export

Use `agentcy-compass catalog --json` to inspect those boundaries machine-readably. Compatible data-producing commands now also honor a global `--json` flag in addition to the legacy `-f json` form, and `agentcy-compass --json-envelope ...` wraps successful compatible outputs in a normalized `{status, command, data}` envelope.

agentcy-compass treats brands as code: version-controlled configurations, reproducible content pipelines, and automated quality gates. Instead of scattered tools and manual processes, you get a unified system where brand guidelines inform every piece of content.

## Why agentcy-compass?

**The Problem**: Brand management is fragmented. Voice guidelines live in PDFs nobody reads. Content creation happens in silos. Publishing requires logging into five different platforms. Quality is inconsistent.

**The Solution**: agentcy-compass unifies the entire brand operations pipeline:

```
brand.yml → persona → intel → plan → produce → eval → publish → monitor
     ↑                                          ↓
     └──────────── learnings ←─────────────────┘
```

Each stage feeds into the next. Intelligence informs strategy. Strategy shapes content. Evaluation catches drift. Learnings improve future output.

## Installation

```bash
# Install with uv (recommended)
uv sync

# Install all optional dependencies
uv sync --all-extras

# Or install specific capabilities
uv sync --extra persona    # AI persona generation
uv sync --extra intel      # Competitive scraping
uv sync --extra publish    # Social publishing
uv sync --extra video      # Video generation
```

## Quick Start

```bash
# 1. Initialize a new brand
agentcy compass brand init acme

# 2. Inspect boundaries / install expectations
agentcy-compass catalog --json

# 3. Generate a canonical plan/brief path
agentcy compass plan run "Launch our new API" --brand acme --json

# 4. Ask for a normalized Compass-local success envelope
agentcy-compass --json-envelope config profiles

# 5. Evaluate against brand guidelines
agentcy compass --json eval grade "Your draft content here" --brand acme

# 6. Queue and publish
agentcy compass --json queue add "Your approved content" --brand acme --platform twitter
agentcy compass publish post --brand acme
```

## Core Concepts

### Brands as Configuration

Every brand is a directory with declarative config files:

```
brands/
└── acme/
    ├── brand.yml      # Voice, visual, platform config
    ├── rubric.yml     # Quality evaluation criteria
    └── assets/        # Logos, fonts, reference images
```

```yaml
# brand.yml
name: acme
description: "Developer tools that spark joy"

voice:
  tone: friendly
  vocabulary: technical
  patterns:
    - "We believe..."
    - "Here's the thing:"
  avoid_phrases:
    - "revolutionary"
    - "game-changing"

platforms:
  twitter:
    enabled: true
    max_length: 280
  linkedin:
    enabled: true
    max_length: 3000
```

### Personas

Personas are AI-generated brand voices that can be used for content generation, chat interfaces, and consistency testing.

```bash
# Create from description
agentcy compass persona create "A witty tech journalist who explains complex topics simply"

# Create from a real person's writing style
agentcy compass persona create "Paul Graham" --from-person

# Create from a professional role
agentcy compass persona create "Senior DevRel Engineer" --from-role

# Chat interactively
agentcy compass persona chat my-persona

# Export to different formats
agentcy compass persona export my-persona --to system_prompt
agentcy compass persona export my-persona --to ollama
```

### Evaluation Rubrics

Define quality gates with weighted dimensions:

```yaml
# rubric.yml
name: content-quality
pass_threshold: 0.7

dimensions:
  - name: clarity
    description: Is the content clear and easy to understand?
    weight: 1.0
    threshold: 0.7

  - name: brand_voice
    description: Does it match our established voice?
    weight: 1.2
    threshold: 0.8

  - name: engagement
    description: Will this resonate with our audience?
    weight: 1.0
    threshold: 0.7

red_flags:
  - Offensive content
  - Competitor mentions
  - Unverified claims
```

## Command Reference

### Brand Management

```bash
agentcy compass brand init <name>        # Create new brand from template
agentcy compass brand list               # List all brands
agentcy compass brand show <name>        # Display brand config
agentcy compass brand edit <name>        # Open config in editor
agentcy compass brand validate <name>    # Validate brand configuration
```

### Persona Operations

```bash
agentcy compass persona create <desc>    # Generate persona with AI
agentcy compass persona list             # List available personas
agentcy compass persona show <name>      # Display persona details
agentcy compass persona chat <name>      # Interactive conversation
agentcy compass persona ask <name> <q>   # One-shot query
agentcy compass persona export <name>    # Export to various formats
agentcy compass persona enrich <name>    # Enrich with external data
agentcy compass persona mix <a> <b>      # Blend two personas
agentcy compass persona test <name>      # Test consistency
agentcy compass persona optimize <name>  # Automated improvement
agentcy compass persona drift <name>     # Check for voice drift
agentcy compass persona learn <name>     # Generate improvements from history
```

### Competitive Intelligence

```bash
agentcy compass intel scrape <brand>     # Scrape competitor content
agentcy compass intel analyze <brand>    # Extract patterns and hooks
agentcy compass intel hooks <brand>      # List discovered hooks
agentcy compass intel outliers <brand>   # Find standout content
```

### Signal Monitoring

```bash
agentcy compass signals fetch <brand>    # Fetch latest signals
agentcy compass signals filter <file>    # Filter by keywords
agentcy compass signals relevance <q>    # Score signal relevance
```

### Marketing Planning

```bash
agentcy compass plan outline <brief>     # Generate plan outline
agentcy compass plan research <brand>    # Research stage
agentcy compass plan strategy <brand>    # Strategy stage
agentcy compass plan creative <brand>    # Creative stage
agentcy compass plan activation <brand>  # Activation stage
```

### Canonical `brief.v1` handoff

`agentcy-compass` is the canonical writer for `brief.v1` in the Agentcy family. The authoritative schema, lineage rules, and examples live at the parent `protocols/` layer; repo-local docs and tests here only prove that `agentcy compass` emits loom-consumable output without taking on execution ownership.

```bash
agentcy compass plan run "Increase caregiver response to a fall planning checklist." \
  --brand GiveCare \
  --voice-pack-input ../protocols/examples/voice_pack.v1.minimal.json \
  --brief-v1-output ./tmp/brief.v1.json \
  --policy-verdict approved \
  --policy-confidence 0.91
```

This writes a canonical `brief.v1` payload that:
- keeps `writer` fixed to `{ "repo": "brand-os", "module": "agentcy-compass" }`
- carries through the referenced `voice_pack_id` lineage for downstream loom handoff
- stays aligned with `../protocols/brief.v1.schema.json` and the parent `protocols/examples/` fixtures

### Content Production

```bash
agentcy compass produce copy <topic>     # Generate platform copy
agentcy compass produce thread <topic>   # Generate Twitter thread
agentcy compass produce image <prompt>   # Generate image
agentcy compass produce video <brief>    # Video surface exists but returns an explicit unsupported error in this build
agentcy compass produce explore <topic>  # Full multi-platform flow
```

### Content Evaluation

```bash
agentcy compass eval grade <rubric> <content>   # Grade against rubric
agentcy compass eval heal <brand> <content>     # Auto-fix issues
agentcy compass eval learnings <brand>          # View accumulated learnings
```

### Publishing

```bash
agentcy compass publish post --brand <b>        # Post from queue
agentcy compass publish platforms               # List platform status

agentcy compass queue add <content> --brand <b> # Add to queue
agentcy compass queue list --brand <b>          # View queue
agentcy compass queue show <id> --brand <b>     # Item details
agentcy compass queue clear --brand <b>         # Clear queue
```

### Monitoring

```bash
agentcy compass monitor report <brand>   # Generate brand report
agentcy compass monitor email <brand>    # Send report via email
```

### Configuration

```bash
agentcy compass config env               # Check environment variables
agentcy compass config profiles          # Show current configuration
```

## Architecture

```
src/brand_os/
├── cli.py              # Main CLI entry point
├── loop.py             # Autonomous execution daemon
├── loop_cli.py         # Loop/decision/policy CLI
├── core/               # Shared utilities
│   ├── brands.py       # Brand loading and discovery
│   ├── config.py       # Configuration management
│   ├── decision.py     # Decision logging + audit trail
│   ├── policy.py       # Policy engine + guardrails
│   ├── learning.py     # Outcome tracking + metrics
│   ├── llm.py          # LLM interface (Gemini, Anthropic, Claude CLI)
│   └── storage.py      # Storage paths
│
├── agents/             # Specialized AI agents
│   ├── base.py         # Agent protocol + BaseAgent
│   ├── market.py       # Market analyst (LLM-powered)
│   └── threat.py       # Threat assessor
│
├── actions/            # Execution targets
│   ├── write.py        # File output (audit trail)
│   └── notify.py       # Slack/email notifications
│
├── workflows/          # Approval workflows
│   └── approval.py     # Central decision review state machine
│
├── adapters/           # Format converters
│   ├── brandos.py      # Internal format
│   ├── persona.py      # Persona format
│   └── social.py       # Social platform formats
│
├── persona/            # Persona management
│   ├── bootstrap.py    # Initial generation
│   ├── chat.py         # Conversation interface
│   ├── crud.py         # CRUD operations
│   ├── drift.py        # Drift detection
│   ├── enrichment.py   # External data enrichment
│   ├── exporters.py    # Format exporters
│   ├── learning.py     # Improvement suggestions
│   ├── optimization.py # DSPy/GEPA optimization
│   └── storage.py      # Shared persona path helpers
│
├── intel/              # Competitive intelligence
│   ├── pipeline.py     # Scraping pipeline
│   ├── hooks.py        # Hook extraction
│   ├── outliers.py     # Outlier detection
│   └── scrapers/       # Platform scrapers
│
├── signals/            # Signal ingestion
│   ├── schema.py       # Unified Signal model
│   ├── relevance.py    # Relevance scoring
│   ├── history.py      # Signal history
│   └── sources/        # Data sources for loop
│       ├── rss.py      # RSS/Atom feeds
│       └── reddit.py   # Reddit posts
│
├── plan/               # Marketing planning
│   ├── stages/         # Planning stages
│   └── plugins/        # SEO, social plugins
│
├── produce/            # Content production
│   ├── copy.py         # Text generation
│   ├── queue.py        # Production queue
│   ├── image/          # Image generation
│   │   └── providers/  # Gemini active, Reve returns explicit unsupported status in this build
│   └── video/          # Video generation entrypoint (currently explicit unsupported status)
│
├── eval/               # Evaluation
│   ├── grader.py       # Rubric grading
│   ├── heal.py         # Auto-fixing
│   ├── learnings.py    # Learning accumulation
│   └── rubric.py       # Rubric parsing
│
├── publish/            # Social publishing
│   ├── queue.py        # Publishing queue
│   ├── rate_limit.py   # Rate limiting
│   └── platforms/      # Platform publishers
│
├── monitor/            # Monitoring
│   ├── reports.py      # Report generation
│   └── emailer.py      # Email delivery
│
└── server/             # API surface
    ├── api.py          # FastAPI REST API
    └── mcp.py          # MCP stub (raises NotImplementedError in this build)
```

## Environment Variables

| Variable | Purpose | Required For |
|----------|---------|--------------|
| `GOOGLE_API_KEY` | Gemini LLM and image generation | Core features |
| `OPENAI_API_KEY` | OpenAI/LiteLLM models | Alternative LLM |
| `ANTHROPIC_API_KEY` | Anthropic Claude models | Alternative LLM |
| `EXA_API_KEY` | Persona enrichment | `persona enrich` |
| `APIFY_TOKEN` | Web scraping | `intel scrape` |
| `TWITTER_CONSUMER_KEY` | Twitter publishing | `publish` (Twitter) |
| `TWITTER_CONSUMER_SECRET` | Twitter publishing | `publish` (Twitter) |
| `TWITTER_ACCESS_TOKEN` | Twitter publishing | `publish` (Twitter) |
| `TWITTER_ACCESS_SECRET` | Twitter publishing | `publish` (Twitter) |
| `LINKEDIN_ACCESS_TOKEN` | LinkedIn publishing | `publish` (LinkedIn) |
| `RESEND_API_KEY` | Email reports | `monitor email` |

Check your configuration:

```bash
agentcy compass config env
```

## Workflows

### Daily Content Pipeline

```bash
# Morning: gather intelligence
agentcy compass signals fetch acme
agentcy compass intel analyze acme

# Midday: produce content
agentcy compass produce explore "Today's key insight" --brand acme --platforms twitter,linkedin

# Review queue
agentcy compass queue list --brand acme

# Evaluate before publishing
agentcy compass eval grade brands/acme/rubric.yml "$(agentcy compass queue show abc123 --brand acme -f json | jq -r .content)"

# Publish
agentcy compass publish post --brand acme --all
```

### Brand Launch

```bash
# Setup
agentcy compass brand init newbrand
agentcy compass persona create "Description of new brand voice" --as newbrand-voice

# Define quality standards
# Edit brands/newbrand/rubric.yml

# Generate launch content
agentcy compass plan outline "Product launch for developer audience"
agentcy compass produce thread "Introducing our new product" --brand newbrand

# Test persona consistency
agentcy compass persona test newbrand-voice
```

### Competitive Analysis

```bash
# Scrape competitors
agentcy compass intel scrape acme

# Find what's working for them
agentcy compass intel hooks acme
agentcy compass intel outliers acme

# Apply learnings to your content
agentcy compass produce copy "Similar topic" --brand acme
```

## API Server

Run the REST API for integrations:

```bash
# Install server dependencies
uv sync --extra server

# Start server
uvicorn brand_os.server.api:app --reload
```

The MCP entrypoint is present for surface completeness, but it is still an explicit stub in this build:

```bash
python -m brand_os.server.mcp
# NotImplementedError: MCP server is not implemented in this build
```

## Autonomous Loop (24/7 Operation)

agentcy-compass can run autonomously, continuously monitoring signals and generating analysis.

Unsupported decision types now escalate for human review instead of returning fake-success placeholders.

### Quick Deploy

```bash
# 1. Clone
git clone https://github.com/amadad/agentcy.git
cd agentcy/compass

# 2. Choose an LLM path for planning
export GOOGLE_API_KEY=your_gemini_key
# or use local Claude Code CLI instead of Gemini rate limits:
export BRANDOPS_LLM_PROVIDER=claude-cli
export CLAUDE_MODEL=sonnet

# 3. Install and create a brand
uv sync
agentcy compass brand init mycompany

# 4. Configure the brand
nano brands/mycompany/brand.yml
```

Add to `brand.yml`:
```yaml
name: mycompany
industry: "B2B SaaS"
target_audience: "CTOs at mid-size companies"
keywords:
  - AI
  - automation
  - enterprise
```

```bash
# 5. Discover relevant subreddits (optional)
agentcy compass signals discover-subreddits --brand mycompany

# 6. Start the loop
agentcy compass loop start
```

### Docker Deployment

```bash
# Create brand first (required)
uv sync && agentcy compass brand init mycompany
# Edit brands/mycompany/brand.yml

# Create .env file
echo "GOOGLE_API_KEY=your_key" > .env
echo "SLACK_WEBHOOK_URL=your_webhook" >> .env  # optional

# Run
docker compose up -d

# View logs
docker compose logs -f loop
```

### What the Loop Does

Each cycle (default: 5 minutes):
1. **Fetches signals** from RSS feeds and Reddit
2. **Analyzes** with LLM (trends, opportunities, risks)
3. **Evaluates** decisions against policy (confidence thresholds)
4. **Executes** allowed decisions (writes to `~/.agentcy-compass/outputs/`)
5. **Escalates** uncertain decisions (Slack notification)
6. **Logs outcomes** for self-improvement

### Loop Commands

```bash
agentcy compass loop start                    # Start autonomous loop
agentcy compass loop start --brand mycompany  # Single brand only
agentcy compass loop test mycompany           # Test one cycle

agentcy compass decision list                 # View all decisions
agentcy compass decision pending              # Decisions needing review
agentcy compass decision approve <id>         # Approve escalated decision

agentcy compass policy show mycompany         # View policy config
agentcy compass policy test mycompany         # Test policy evaluation

agentcy compass learn metrics mycompany       # View learning metrics
agentcy compass learn recommendations myco    # Get improvement suggestions
```

### Policy Configuration

Control autonomous behavior in `brand.yml`:

```yaml
policy:
  enabled: true
  default_verdict: escalate  # allow, escalate, deny
  global_min_confidence: 0.7

  always_allow:
    - signal_action
  always_escalate:
    - budget_allocation

  rules:
    - name: content-auto-publish
      decision_types: [content_publish]
      min_confidence: 0.8
      max_per_hour: 5
      cooldown_minutes: 10
```

### Requirements

| Component | Required | Notes |
|-----------|----------|-------|
| `GOOGLE_API_KEY` | Yes | For LLM analysis (Gemini) |
| `ANTHROPIC_API_KEY` | Alt | Alternative LLM (Claude) |
| `SLACK_WEBHOOK_URL` | No | For escalation alerts |
| Brand config | Yes | At least one brand in `brands/` |

Without an LLM API key, signals will be fetched but no analysis/decisions will be generated.

## Documentation

| Document | Purpose |
|----------|---------|
| [ROADMAP.md](ROADMAP.md) | Implementation phases from current state to full vision |
| [SIGNAL_STRATEGY.md](SIGNAL_STRATEGY.md) | Signal intelligence positioning and phased build plan |
| [AGENTS.md](AGENTS.md) | Agent architecture and multi-agent coordination |
| [GATEWAY.md](GATEWAY.md) | Gateway coordination layer design |
| [CLAUDE.md](CLAUDE.md) | Development guidelines and conventions |

## Development

```bash
# Install dev dependencies
uv sync --extra dev

# Run tests
pytest

# Lint
ruff check src/

# Format
ruff format src/
```

## License

MIT
