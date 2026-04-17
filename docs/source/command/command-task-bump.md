# バージョン管理用タスク（`task version`）

```console
$ task bump:check
$ task bump:auto
$ task bump:patch
$ task bump:minor
$ task bump:major
```

[commitizen](../python/python-commitizen.md)を使ったタスクです。

## タスク設定

```yaml
tasks:

  # ============================================================================
  # Version management tasks - Manage versions with commitizen
  # ============================================================================

  bump:check:s
    desc: Preview next version bump
    cmds:
      - echo "Preview of next version bump"
      - uv run cz bump --check-consistency --changelog --dry-run

  bump:patch:
    desc: Bump patch version. Use this daily.
    cmds:
      - uv run cz bump --check-consistency --changelog --increment patch

  bump:minor:
    desc: Bump minor version. Use once when the month changed.
    cmds:
      - uv run cz bump --check-consistency --changelog --increment minor

  bump:major:
    desc: Bump major version. Use once when the year changed.
    cmds:
      - uv run cz bump --check-consistency --changelog --increment major
```

:::{note}

`uv run`の部分は各自の実行環境に置き換えてください。

:::
