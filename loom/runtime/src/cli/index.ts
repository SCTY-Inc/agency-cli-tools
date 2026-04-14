import { runAutoCommand } from '../commands/auto'
import { runBrandCommand } from '../commands/brand'
import { runInspectCommand } from '../commands/inspect'
import { runLabCommand } from '../commands/lab'
import { runOpsCommand } from '../commands/ops'
import { runPublishCommand } from '../commands/publish'
import { runRetryCommand } from '../commands/retry'
import { runReviewCommand } from '../commands/review'
import { runWorkflowCommand } from '../commands/run'

function print(data: unknown, json: boolean): void {
  if (json) {
    process.stdout.write(`${JSON.stringify(data, null, 2)}\n`)
    return
  }

  if (typeof data === 'string') {
    process.stdout.write(`${data}\n`)
    return
  }

  process.stdout.write(`${JSON.stringify(data, null, 2)}\n`)
}

function errorMessage(error: unknown): string {
  return error instanceof Error ? error.message : String(error)
}

function helpText(): string {
  return [
    'Loom Runtime CLI',
    '',
    'Usage:',
    '  loom <command> [options]',
    '',
    'Commands:',
    '  auto --brand <id> [--workflow social.post] [--topic "..."] [--dry-run]',
    '  brand <init|show|validate> ...',
    '  run <workflow> --brand <id> [--pillar <id>] [--format <id>] [--brief-file <path>] ...',
    '  review <list|show|approve|reject> ...',
    '  publish <run_id> [--platforms twitter,linkedin] [--dry-run]',
    '  inspect <run|artifact> ...',
    '  retry <run_id> [--from <step>]',
    '  lab <card|render> ...',
    '  ops <health|auth check --brand <id>|auth refresh|migrate>',
    '',
    'Workflows:',
    '  social.post',
    '  blog.post',
    '  outreach.touch',
    '  respond.reply',
    '',
    'Examples:',
    '  loom auto --brand givecare',
    '  loom auto --brand scty --topic "AI adoption gap" --dry-run',
    '  loom ops auth check --brand givecare',
    '  loom run social.post --brand givecare --topic "caregiver benefits gap"',
    '  loom run social.post --brand givecare --pillar care-economy --topic "$470B unpaid care labor"',
    '  loom run social.post --brand givecare --format infographic --topic "caregiver workforce"',
    '  loom run blog.post --brand givecare --pillar policy --topic "paid leave"',
    '  loom run social.post --brand givecare --brief-file ../protocols/examples/brief.v1.rich.json',
    '  loom lab card --brand givecare --type quote --headline "Care is infrastructure"',
    '  loom lab render --brand givecare --figure statement --gravity high --ground cream --platform linkedin --headline "Care is infrastructure" --body "63M provide unpaid care." --image watershed',
    '  loom publish run_123 --platforms twitter,linkedin --dry-run',
  ].join('\n')
}

export async function runCli(argv: string[] = process.argv.slice(2)): Promise<number> {
  const json = argv.includes('--json')
  const filtered = argv.filter((arg) => arg !== '--json')
  const [command, ...args] = filtered

  try {
    if (!command || command === 'help' || command === '--help' || command === '-h') {
      if (json) {
        print({ status: 'ok', command: 'help', data: { help: helpText() } }, true)
      } else {
        print(helpText(), false)
      }
      return 0
    }

    let data: unknown
    switch (command) {
      case 'auto':
        data = await runAutoCommand(args)
        break
      case 'brand':
        data = await runBrandCommand(args)
        break
      case 'run':
        data = await runWorkflowCommand(args)
        break
      case 'review':
        data = await runReviewCommand(args)
        break
      case 'publish':
        data = await runPublishCommand(args)
        break
      case 'inspect':
        data = await runInspectCommand(args)
        break
      case 'retry':
        data = await runRetryCommand(args)
        break
      case 'ops':
        data = await runOpsCommand(args)
        break
      case 'lab':
        data = await runLabCommand(args)
        break
      default:
        throw new Error(`Unknown command: ${command}`)
    }

    if (json) {
      print({ status: 'ok', command, data }, true)
    } else {
      print(data, false)
    }
    return 0
  } catch (error) {
    if (json) {
      print({ status: 'error', error: { message: errorMessage(error) } }, true)
    } else {
      process.stderr.write(`${errorMessage(error)}\n`)
    }
    return 1
  }
}
