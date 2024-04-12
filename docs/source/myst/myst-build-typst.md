# Typstしたい（``myst build --typst``）

```console
$ myst build --typst
```

``myst build --typst``で、``format: typst``を指定したファイルをTypst形式で出力し、PDFに変換できます。
このオプションを利用するには[Typst](../typst/typst-usage.md)が必要です。

## フロントマター

```yaml
---
title: Typstにしたいファイル
exports:
  - format: typst
    template: テンプレート名
    output: exports/出力ファイル名.pdf
---
```

各ファイルのフロントマターに``exports.format: typst``を指定します。
利用するテンプレートと、出力先のファイル名も指定できます。
指定しない場合は、{file}`_build/exports/ページ名_typst/`に必要なファイルが生成されます。

:::{note}

LaTeXを使ったPDF生成と比べて、日本語フォントもデフォルトで埋め込まれます。
しかし、フォントは別に指定したほうがよさそうです。
（フォントを指定する方法はあとで調べます）

:::

## テンプレートを変更したい

```console
$ myst templates list --typst
$ myst templates list --typst --pdf
```

利用できるテンプレート名を確認できます。

## リファレンス

- [Exporting documents](https://mystmd.org/guide/documents-exports)
- [Rendering PDFs with Typst](https://mystmd.org/guide/creating-pdf-documents#rendering-pdfs-with-typst)
