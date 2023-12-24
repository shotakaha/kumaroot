# PDFしたい（``myst build --pdf``）

```yaml
---
exports:
  - format: pdf
    template: テンプレート名
    output: exports/ファイル名.pdf
---
```

PDF形式で出力したいページのフロントマターに``format: pdf``と``template: テンプレート名``を指定します。
出力ファイル名はオプションです。

```console
$ myst build --pdf
```

デフォルトではLaTeX環境を使ってPDFを作成します。
ファイルは{file}`_build/exports/`に生成されます。

:::{note}

日本語フォントの対応はあとで調べます。

:::

[Exporting to PDF](https://myst-tools.org/docs/mystjs/creating-pdf-documents)

## テンプレートを変更したい

```console
$ myst templates list --pdf
$ myst templates list --tex
```

利用できるテンプレート一覧を確認できます。
