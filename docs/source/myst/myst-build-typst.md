# Typstしたい（``myst build --typst``）

```yaml
exports:
  - format: typst
```

Typst形式で出力したいファイルのフロントマターに``format: typst``を追記します。

```console
$ myst build --typst
# ==> _build/exports/ファイル名_typst/ファイル名.pdf
```

``build --typst``オプションで、ページごとに``.typ``ファイルと``.pdf``ファイルが生成されます。
日本語フォントも利用できます。

:::{note}

LaTeXを使ったPDF生成と比べて、日本語フォントもデフォルトで埋め込まれます。
しかし、フォントは別に指定したほうがよさそうです。
（フォントを指定する方法はあとで調べます）

:::
