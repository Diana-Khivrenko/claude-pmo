# CI setup per platform

The script `scripts/post-qa-summary-to-jira.mjs` is the same on every platform. It needs Node 20 or later and no packages. It finds the merged pull request, reads the ticket key from the source branch or the title, converts the description from Markdown to Jira wiki markup, and posts it to the webhook.

Every variable below is a **secret**: the person adds it in the code host's settings themselves. It never goes into the repository, the chat or a file Claude writes.

The examples use `main` as the target branch. For another branch, set `TARGET_BRANCH` and change the branch in the pipeline file.

## GitLab CI

1. A token for reading merge requests: Settings, Access tokens, Add new token, role Reporter, scope `read_api`.
2. Settings, CI/CD, Variables, three variables, each Masked and Protected:
   - `JIRA_AUTOMATION_URL`: the webhook URL from the Jira flow
   - `JIRA_AUTOMATION_TOKEN`: the secret from the Jira flow
   - `SCM_TOKEN`: the token from step 1

   Protected variables reach only protected branches, so the target branch must be protected. To share them across projects, add them on the group.
3. The job in `.gitlab-ci.yml`. `stage` must be a stage the pipeline already defines:

```yaml
qa summary to jira:
  stage: deploy
  image: node:24
  needs: []
  interruptible: false
  allow_failure: true
  rules:
    - if: $CI_PIPELINE_SOURCE == "push" && $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
  variables:
    GIT_DEPTH: 1
    TARGET_BRANCH: $CI_DEFAULT_BRANCH
  script:
    - node scripts/post-qa-summary-to-jira.mjs
```

## GitHub Actions

1. Settings, Secrets and variables, Actions, New repository secret: `JIRA_AUTOMATION_URL` and `JIRA_AUTOMATION_TOKEN`. For several repositories, organization secrets instead. No source-control token is needed, GitHub hands the pull request to the job.
2. The workflow file `.github/workflows/qa-summary-to-jira.yml`:

```yaml
name: QA summary to Jira

on:
  pull_request:
    types: [closed]
    branches: [main]

jobs:
  post:
    if: github.event.pull_request.merged == true
    runs-on: ubuntu-latest
    continue-on-error: true
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 24
      - run: node scripts/post-qa-summary-to-jira.mjs
        env:
          JIRA_AUTOMATION_URL: ${{ secrets.JIRA_AUTOMATION_URL }}
          JIRA_AUTOMATION_TOKEN: ${{ secrets.JIRA_AUTOMATION_TOKEN }}
```

Pull requests from forks do not receive repository secrets, so the job fails for them without posting.

## Bitbucket Pipelines

1. A token for reading pull requests: Repository settings, Security, Access tokens, Create, scope Pull requests: Read. Bitbucket shows it once.
2. Repository settings, Pipelines, Repository variables, three variables with Secured ticked: `JIRA_AUTOMATION_URL`, `JIRA_AUTOMATION_TOKEN`, `SCM_TOKEN`. To share them, Workspace settings, Pipelines, Workspace variables.
3. The step in `bitbucket-pipelines.yml`. If `main` already has a pipeline, append the step to it:

```yaml
pipelines:
  branches:
    main:
      - step:
          name: QA summary to Jira
          image: node:24
          clone:
            depth: 1
          script:
            - node scripts/post-qa-summary-to-jira.mjs || echo "QA summary was not posted"
```

The script looks through the 25 most recently merged pull requests for the one whose merge commit is `BITBUCKET_COMMIT`.

## On every platform

A failed post never fails the pipeline (`allow_failure`, `continue-on-error`, `|| echo`). The reason stays in the job log.

## When it does not work

| What you see | Cause and fix |
|---|---|
| `JIRA_AUTOMATION_URL is not set` | The variable is missing, misspelled, or protected while the branch is not. Check the variable list and the branch protection. |
| The webhook answers 401 or 403 | The secret is wrong or was regenerated. Copy it again from the Incoming webhook step. |
| The webhook answers 200, no comment | Open the flow's Audit log. Either the ticket key does not exist, or the condition found the pull request link already in the comments. |
| No ticket key in the branch or title | Put the key, such as `PROJ-123`, in the branch name or the pull request title. |
| The description is empty | The pull request has no description, so there is nothing to post. |
| Nothing posted on a real merge | The commit is not a merge into the target branch, or `TARGET_BRANCH` names a different branch. |
| An API call answers 401 or 404 | `SCM_TOKEN` lacks read access to pull requests, or has expired. |
