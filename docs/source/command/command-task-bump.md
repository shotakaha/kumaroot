# バージョン管理用タスク（`task bump`）

```console
$ task version      # 最新のタグを確認
$ task bump:check
$ task bump:auto
$ task bump:patch   # x.y.Z → x.y.(Z+1)
$ task bump:minor   # x.Y.z → x.(Y+1).0
$ task bump:major   # X.y.z → (X+1).0.0
```

[commitizen](../python/python-commitizen.md)を使ったタスクです。

## タスク設定

```yaml
tasks:

  # ==== ==== ==== ==== ====
  # Version Management Tasks
  # - Semantic versioning with commitizen
  # - Bump version based on Conventional Commits
  # - Auto-generate CHANGELOG.md with --changelog
  # - Preview next version bump with --dry-run
  # ==== ==== ==== ==== ====

  version:
    desc: Show current version
    cmds:
      - git tag --list | sort -V | tail -n 1
    silent: true

  bump:check:
    desc: Preview next version bump (dry-run)
    cmds:
      - echo "Preview of next version bump"
      - uv run cz bump --check-consistency --changelog --dry-run

  bump:auto:
    desc: Auto bump version based on commit messages
    cmds:
      - uv run cz bump --check-consistency --changelog

bump:patch:
    desc: Bump patch version (--increment patch)
    cmds:
      - uv run cz bump --check-consistency --changelog --increment patch

  bump:minor:
    desc: Bump minor version (--increment minor)
    cmds:
      - uv run cz bump --check-consistency --changelog --increment minor

  bump:major:
    desc: Bump major version (--increment major)
    cmds:
      - uv run cz bump --check-consistency --changelog --increment major
```

:::{note}

`uv run`の部分は各自の実行環境に置き換えてください。

:::
