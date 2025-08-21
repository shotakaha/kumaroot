# デフォルト用タスク（`task default`）

```console
$ task
```

## タスク設定

```yaml
tasks:
  default:
    desc: Show available tasks
    cmds:
      - task --list
    silent: true
```

デフォルト（`default`）のタスクに`task --list`を設定しておくと便利です。
