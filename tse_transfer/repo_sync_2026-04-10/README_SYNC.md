## Repo Sync Bundle

This directory preserves the current working truth for the active TSE line and
the separate Sovereign line so they can be restored on another machine.

Contents:
- `snapshots/tse-submission-private/`
  - working-tree snapshot of the TSE canonical repository, copied without
    `.git`
- `snapshots/sovereign-pfdo-paper/`
  - working-tree snapshot of the Sovereign repository, copied without `.git`
- `tse-submission-private.bundle`
  - full git bundle export of the TSE repository
- `sovereign-pfdo-paper.bundle`
  - full git bundle export of the Sovereign repository

Source states captured in this sync:
- `tse-submission-private`
  - branch: `fix/tse-jss-disclosure-final-seal`
  - commit: `5d2aafc8963d05e46661f193d31401e21a4e250b`
- `sovereign-pfdo-paper`
  - branch: `main`
  - commit: `4ab47f147aff7289e2cba6798e811cb48f3c06b8`

Related render-transfer materials already live separately in:
- `../tse_render_2026-04-09/`

Suggested restore on another machine:

```bash
cd ~/GitHub/joy7758/tse_transfer/repo_sync_2026-04-10

git clone tse-submission-private.bundle tse-submission-private
git clone sovereign-pfdo-paper.bundle sovereign-pfdo-paper
```

If you only need the files and not the history, use the `snapshots/` copies
directly.
