# 公開用タスク（`task publish`）

```console
$ task publish:test
$ task publish:prod
```

## タスクの設定

```yaml
tasks:
  publish:test:
    desc: Publish to TestPyPI
    dotenv: ['.env']
    cmds:
      - uv build
      - UV_PUBLISH_TOKEN=${TESTPYPI_API_TOKEN} UV_PUBLISH_URL=https://test.pypi.org/legacy/ uv publish

  publish:prod:
    desc: Publish to production PyPI
    dotenv: ['.env']
    cmds:
      - uv build
      - UV_PUBLISH_TOKEN=${PYPI_API_TOKEN} uv publish
```
