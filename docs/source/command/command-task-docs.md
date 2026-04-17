# ドキュメント用タスク（`task docs`）

```console
$ task docs:serve
$ task docs:build
```

`docs:serve`は、ドキュメントをローカルでプレビューするタスク、
`docs:build`は、静的HTMLをビルドするタスクに割り当てています。

どのプロジェクトでも同じタスク名でドキュメント関連の操作ができるようになります。

## Sphinxしたい

```yaml
tasks:
  docs:
    desc: Preview docs locally
    dir: docs
    cmds:
      - uv run make livehtml

  docs:build:
    desc: Build docs as static HTML
    dir: docs
    cmds:
      - uv run make html

  docs:pdf:
    desc: Build docs as PDF
    dir: docs
    cmds:
      - uv run make latexpdf
```

`make livehtml`は、`sphinx-autobuild`を使ってSphinxドキュメントをライブプレビューする設定です。
通常は、ドキュメントのあるディレクトリ（`docs`）に移動してから`make livehtml`コマンドを実行する必要があります。
このタスクを設定すると、どのディレクトリからでも`task doc`で確認できるようになります。

:::{seealso}

- [](../sphinx/sphinx-usage.md)
- [](../sphinx/sphinx-build.md)
- [](../sphinx/sphinx-autobuild.md)

:::


## MkDocsしたい

```yaml
tasks:
  # Documentation
  docs:
    desc: Preview docs locally
    cmds:
      - uv run mkdocs serve -o

  docs:build:
    desc: Build docs as static HTML
    cmds:
      - uv run mkdocs build
```

:::{seealso}

- [](../mkdocs/mkdocs-usage.md)

:::

## Zensicalしたい

```yaml
tasks:
  # Documentation
  docs:
    desc: Preview docs locally
    cmds:
      - uv run zensical serve -o

  docs:build:
    desc: Build docs as static HTML
    cmds:
      - uv run zensical build
```

:::{seealso}

- [](../zensical/zensical-usage.md)

:::
