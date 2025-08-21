# テストしたい（`task test`）

```console
$ task test
```

## タスクの設定

```yaml
tasks:
  test:
    desc: Run all tests
    cmds:
      - uv run pytest tests/

  test:unit:
    desc: Run unit tests only
    cmds:
      - uv run pytest tests/unit/

  test:integration:
    desc: Run integration tests only
    cmds:
      - uv run pytest tests/integration/

  test:ci:
    desc: Simulate complete CI pipeline locally
    cmds:
      - task: test:unit
      - echo "Checking code formatting..."
      - uv run format --check src tests
      - echo "Running pre-commit hooks..."
      - task: lint:pre-commit
```
