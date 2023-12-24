# Typstしたい（``myst build --typst``）

```yaml
---
exports:
  - format: typst
  - format: pdf
  - format: docx
---
```

Typst形式で出力したいファイルのフロントマターに``format: typst``を追記します。

:::{note}

出力形式は複数指定できます。

:::

```console
$ myst build --typst
```

ファイルは{file}`_build/exports/ページ名_typst/`に必要なファイルが生成されます。
日本語フォントも利用できます。

:::{note}

LaTeXを使ったPDF生成と比べて、日本語フォントもデフォルトで埋め込まれます。
しかし、フォントは別に指定したほうがよさそうです。
（フォントを指定する方法はあとで調べます）

:::

## テンプレートを変更したい

```console
$ myst templates list --typst
```

利用できるテンプレート一覧を確認できます。
