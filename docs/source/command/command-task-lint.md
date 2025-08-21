# リンターしたい（`task lint`）

```console
$ task lint
$ task link:check
$ task lint:pre-commit
```

## タスクの設定

```yaml
tasks:
  lint:
    desc: Format code with ruff
    cmds:
      - uv run ruff format src tests

  lint:check:
    desc: Check code formatting without changes
    cmds:
      - uv run ruff format --check src tests

  lint:pre-commit:
    desc: Run all pre-commit hooks
    cmds:
      - uv run pre-commit run --all-files
```
