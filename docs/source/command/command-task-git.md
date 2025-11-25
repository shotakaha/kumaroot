# Git用タスク

```console
$ task status
$ task log
$ task push
$ task push:tags
```

[git](../git/git-usage.md)を使ったタスクです。

## タスク設定

```yaml
tasks:

  # ============================================================================
  # Git management tasks - Manage Git
  # ============================================================================

  status:
    desc: Show git status
    cmds:
      - git status

  log:
    desc: Show recent commits (last 10)
    cmds:
      - git log --oneline -10

  push:
    desc: Push commits to remote (main branch)
    cmds:
      - git push origin main

  push:tags:
    desc: Push commits and tags to remote
    cmds:
      - git push origin main --tags
```

`task`コマンドに依存しすぎて、
`git status`の代わりに`task status`と打ってしまうことがあったのですが、
だいぶ楽になりました。
