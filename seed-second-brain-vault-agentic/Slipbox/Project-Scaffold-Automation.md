---
date: 2026-04-11
tags: [automation, workflow, linear, github, cursor, swiftbar, obsidian]
---
# Project Scaffold Automation

A one-command workflow that bootstraps a full local project workspace from a Linear project. Triggered via a Cowork skill (`/project-scaffold`) — generates a shell script that runs everything automatically.

## What it does

Given a Linear project name, the scaffold:

1. **Creates a GitHub repo** (`harsh20k/{repo-slug}`, public) via `gh repo create`
2. **Clones it** into `/Users/harsh/Artifacts/{repo-slug}` via `gh repo clone`
3. **Drops a Cursor launcher** on the Desktop — `{ProjectName}.sh` that runs `open -a Cursor`
4. **Writes a README** distilled from the Linear project description, commits and pushes
5. **Creates a `notes/` folder** with the Obsidian `.obsidian` config copied in (ready to open as a vault)
6. **Adds an entry to SwiftBar** in `CursorProjects.sh` after the `echo "Projects"` line:
   
   ```
   echo "👾 {ProjectName} | bash='/Users/harsh/Desktop/{ProjectName}.sh' terminal=false"
   ```

## Key paths

| Thing                  | Path                                                                      |
| ---------------------- | ------------------------------------------------------------------------- |
| Local repos            | `/Users/harsh/Artifacts/`                                                 |
| Cursor launchers       | `/Users/harsh/Desktop/{ProjectName}.sh`                                   |
| SwiftBar plugin        | `/Users/harsh/Documents/SwiftbarPlugins/CursorProjects.sh`                |
| Obsidian config source | `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Notes/.obsidian` |

## How to invoke

Say **"scaffold [Linear project name]"** in Cowork. It fetches the Linear project, generates a `scaffold-{repo-slug}.sh` in the workspace folder, then you run it once in your terminal.

## Notes

- Uses `gh` CLI (already authenticated) — no credential prompts
- `gh repo clone` instead of `git clone` avoids SSH config issues
- GitHub username is `harsh20k`
- The generated script uses `set -e` so it stops cleanly on any error

## Related notes
- [[Connect to GitHub SSH]]
