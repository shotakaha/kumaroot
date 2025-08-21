# ドキュメント用タスク（`task doc`）

```console
$ task doc
$ task doc:build
```

## MkDocs設定

```yaml
tasks:
  # Documentation
  doc:
    desc: Serve documentation locally
    cmds:
      - uv run mkdocs serve -o

  doc:build:
    desc: Build documentation as static HTML
    cmds:
      - uv run mkdocs build
```

## Sphinx設定

```yaml
tasks:
  doc:
    desc: Serve documentation locally
    dir: docs
    cmds:
      - poetry run make livehtml

  doc:build:
    desc: Build documentation as static HTML
    dir: docs
    cmds:
      - poetry run make html

  doc:pdf:
    desc: Build documentation as PDF
    dir: docs
    cmds:
      - poetry run make latexpdf
```

`make livehtml`は、`sphinx-autobuild`を使ってSphinxドキュメントをライブプレビューする設定です。
通常は、ドキュメントのあるディレクトリ（`docs`）に移動してから`make livehtml`コマンドを実行する必要があります。
このタスクを設定すると、どのディレクトリからでも`task doc`で確認できるようになります。
