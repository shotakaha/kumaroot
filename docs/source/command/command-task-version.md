# バージョン管理用タスク（`task version`）

```console
$ task version
$ task version:bump
```

## タスク設定

```yaml
tasks:
  version:
    desc: Preview version bump with changelog
    cmds:
      - cz bump --check-consistency --dry-run

  version:bump:
    desc: Bump version and update changelog
    cmds:
      - cz bump --changelog --check-consistency
```
