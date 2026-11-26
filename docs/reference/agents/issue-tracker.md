# Issue tracker: GitHub

Issues and PRDs for DeepPharma live as GitHub issues in `quantumquirkxyz/DeepPharma`. Use the `gh` CLI for tracker operations.

## Conventions

- Create: `gh issue create --title "..." --body "..."`
- Read: `gh issue view <number> --comments`
- List: `gh issue list --state open --json number,title,body,labels,comments`
- Comment: `gh issue comment <number> --body "..."`
- Apply or remove labels: `gh issue edit <number> --add-label "..."` / `--remove-label "..."`
- Close: `gh issue close <number> --comment "..."`

When a skill says to publish to the issue tracker, create a GitHub issue. Pull requests are not a request surface for triage.

## Repository identity and provider

- Provider: GitHub
- Repository: `quantumquirkxyz/DeepPharma`
- Remote evidence: `origin` points to `https://github.com/quantumquirkxyz/DeepPharma.git`
- Required CLI: `gh`
- Permissions: verify authentication and repository access before mutating remote issues or labels
