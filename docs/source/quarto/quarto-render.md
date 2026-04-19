# ビルドしたい（`quarto render`）

```console
$ quarto render
```

`quarto render`コマンドで、`.qmd`ファイルをビルドして、指定された形式に変換できます。
変換形式はファイルごとに[frontmatter](./quarto-frontmatter.md)で指定できます。

## HTMLしたい（`quarto render --to html`）

```console
$ quarto render FILE.qmd --to html
```

`--to html`オプションで、`.qmd`ファイルをHTML形式に変換できます。
HTML形式は、ウェブサイトやブログなどのオンラインコンテンツに適しています。
変換されたファイルは`_site`ディレクトリに生成され、ブラウザで直接閲覧できます。

## Typstしたい（`quarto render --to typst`）

```console
$ quarto render FILE.qmd --to typst
```

`--to typst`オプションで、`.qmd`ファイルをTypst形式を介してPDFに変換できます。
印刷物などの高品質なドキュメントに適しています。

:::{note}

ローカルでPDFを生成するには、Typstのインストールが必要です。
変換中に生成される（はずの）`Typst`ファイルは残りません。

:::
