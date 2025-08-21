# リリース用タスク（`task release`）

```console
$ task release
$ task release:full
```

## タスクの設定

```yaml
tasks:
  release:
    desc: Create GitLab release for current tag
    cmds:
      - git push origin main
      - git push origin --tags
      - glab release create {{.CLI_ARGS | default "$(git describe --tags)"}} --name "{{.CLI_ARGS | default "$(git describe --tags)"}}"

  release:full:
    desc: Complete release workflow (test -> format -> bump -> release)
    cmds:
      - task: test
      - task: lint
      - task: lint:pre-commit
      - task: version:bump
      - task: release
```
