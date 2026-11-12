import { readFile } from 'node:fs/promises'

const REQUEST_TIMEOUT_MS = 15000
const TICKET_KEY = /[A-Z][A-Z0-9]+-\d+/i
const targetBranch = process.env.TARGET_BRANCH ?? 'main'

function readRequiredEnv(name) {
  const value = process.env[name]
  if (!value) throw new Error(`${name} is not set`)
  return value
}

async function getJson(url, headers) {
  const response = await fetch(url, { headers, signal: AbortSignal.timeout(REQUEST_TIMEOUT_MS) })
  if (!response.ok) throw new Error(`GET ${url} answered ${response.status}`)
  return response.json()
}

async function findMergedOnGitLab() {
  const sha = readRequiredEnv('CI_COMMIT_SHA')
  const api = readRequiredEnv('CI_API_V4_URL')
  const project = readRequiredEnv('CI_PROJECT_ID')
  const candidates = await getJson(
    `${api}/projects/${project}/repository/commits/${sha}/merge_requests`,
    { 'PRIVATE-TOKEN': readRequiredEnv('SCM_TOKEN') },
  )
  const found = candidates.find(
    candidate =>
      candidate.state === 'merged' &&
      candidate.target_branch === targetBranch &&
      [candidate.merge_commit_sha, candidate.squash_commit_sha, candidate.sha].includes(sha),
  )
  if (!found) return null
  return {
    title: found.title,
    url: found.web_url,
    sourceBranch: found.source_branch,
    description: found.description,
  }
}

async function findMergedOnGitHub() {
  const event = JSON.parse(await readFile(readRequiredEnv('GITHUB_EVENT_PATH'), 'utf8'))
  const pullRequest = event.pull_request
  if (!pullRequest?.merged || pullRequest.base.ref !== targetBranch) return null
  return {
    title: pullRequest.title,
    url: pullRequest.html_url,
    sourceBranch: pullRequest.head.ref,
    description: pullRequest.body,
  }
}

async function findMergedOnBitbucket() {
  const sha = readRequiredEnv('BITBUCKET_COMMIT')
  const repository = readRequiredEnv('BITBUCKET_REPO_FULL_NAME')
  const page = await getJson(
    `https://api.bitbucket.org/2.0/repositories/${repository}/pullrequests?state=MERGED&sort=-updated_on&pagelen=25`,
    { Authorization: `Bearer ${readRequiredEnv('SCM_TOKEN')}` },
  )
  const found = page.values.find(
    candidate =>
      candidate.destination.branch.name === targetBranch &&
      candidate.merge_commit &&
      sha.startsWith(candidate.merge_commit.hash),
  )
  if (!found) return null
  return {
    title: found.title,
    url: found.links.html.href,
    sourceBranch: found.source.branch.name,
    description: found.description,
  }
}

function findMergedPullRequest() {
  if (process.env.GITLAB_CI) return findMergedOnGitLab()
  if (process.env.GITHUB_ACTIONS) return findMergedOnGitHub()
  if (process.env.BITBUCKET_BUILD_NUMBER) return findMergedOnBitbucket()
  throw new Error('Run this in GitLab CI, GitHub Actions, or Bitbucket Pipelines.')
}

const convertInlineMarkdown = line =>
  line
    .replace(/`([^`]+)`/g, '{{$1}}')
    .replace(/\*\*([^*]+)\*\*/g, '*$1*')
    .replace(/!?\[([^\]]*)\]\(([^)]+)\)/g, '[$1|$2]')

function convertMarkdownToJiraWiki(markdown) {
  const converted = []
  let insideCodeFence = false
  for (const line of markdown.replace(/<!--[\s\S]*?-->/g, '').split('\n')) {
    const fence = line.match(/^\s*```(\w*)\s*$/)
    if (fence) {
      insideCodeFence = !insideCodeFence
      converted.push(insideCodeFence && fence[1] ? `{code:${fence[1]}}` : '{code}')
      continue
    }
    if (insideCodeFence) {
      converted.push(line)
      continue
    }
    if (/^\s*\|[\s:|-]+\|\s*$/.test(line) && line.includes('-')) {
      const headerRow = converted.pop() ?? ''
      const cells = headerRow.trim().replace(/^\||\|$/g, '').split('|')
      converted.push(`|| ${cells.map(cell => cell.trim()).join(' || ')} ||`)
      continue
    }
    const heading = line.match(/^(#{1,6})\s+(.*)$/)
    const bullet = line.match(/^(\s*)[-*+]\s+(.*)$/)
    const numbered = line.match(/^(\s*)\d+[.)]\s+(.*)$/)
    if (heading) {
      converted.push(`h${heading[1].length}. ${convertInlineMarkdown(heading[2])}`)
    } else if (bullet) {
      const depth = Math.floor(bullet[1].length / 2) + 1
      converted.push(`${'*'.repeat(depth)} ${convertInlineMarkdown(bullet[2])}`)
    } else if (numbered) {
      const depth = Math.floor(numbered[1].length / 2) + 1
      converted.push(`${'#'.repeat(depth)} ${convertInlineMarkdown(numbered[2])}`)
    } else {
      converted.push(convertInlineMarkdown(line))
    }
  }
  return converted.join('\n').replace(/\n{3,}/g, '\n\n').trim()
}

async function postToJiraWebhook(payload) {
  const response = await fetch(readRequiredEnv('JIRA_AUTOMATION_URL'), {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Automation-Webhook-Token': readRequiredEnv('JIRA_AUTOMATION_TOKEN'),
    },
    body: JSON.stringify(payload),
    signal: AbortSignal.timeout(REQUEST_TIMEOUT_MS),
  })
  if (!response.ok) throw new Error(`The Jira webhook answered ${response.status}`)
}

async function main() {
  const pullRequest = await findMergedPullRequest()
  if (!pullRequest) {
    console.log(`No pull request merged into ${targetBranch} produced this commit. Nothing posted.`)
    return
  }
  const keyMatch = `${pullRequest.sourceBranch} ${pullRequest.title}`.match(TICKET_KEY)
  if (!keyMatch) throw new Error(`No ticket key in the branch or title of ${pullRequest.url}`)
  const summary = (pullRequest.description ?? '').trim()
  if (!summary) throw new Error(`The description of ${pullRequest.url} is empty`)
  const ticketKey = keyMatch[0].toUpperCase()
  await postToJiraWebhook({
    issues: [ticketKey],
    mergeRequestUrl: pullRequest.url,
    comment: [
      `QA summary for [${pullRequest.title}|${pullRequest.url}], merged into ${targetBranch}.`,
      '',
      convertMarkdownToJiraWiki(summary),
    ].join('\n'),
  })
  console.log(`Sent the QA summary for ${pullRequest.url} to ${ticketKey}.`)
}

main().catch(error => {
  console.error(error.message)
  process.exitCode = 1
})
