# フォーマット変換したい（``pandoc``）

```console
$ brew install pandoc
```

さまざまはファイル形式を変換するコマンドです。

## PDFに変換したい

```console
$ pandoc input.md -o output.pdf
```

ファイルの拡張子から形式を自動で判断できます。

## 形式を指定して変換したい（``--to / -t``）

```console
$ pandoc input.docx --to gfm -o output.md
$ pandoc input.docx -t gfm -o output.md
```

``--to gfm``するとGitHub Flavored Markdownで出力されます。
``--to markdown``するとPandocフレーバーで出力されます。


## メディアを取り出したい（``--extract-media``）

```console
$ pandoc input.docx -t gfm -o output.md --extract-media=パス
```

``--extract-media=パス``オプションを使って、Word文書から図を抽出できます。
ファイル名は、先頭の図から順番に採番されます。
この場合のように、出力された``.md``ファイルにはこの画像へのパスが挿入されます。

## サポートされているファイル形式を確認したい

```console
$ pandoc --list-input-formats    # 入力形式
$ pandoc --list-output-formats   # 出力形式
```

## ``org-mode``を``reST``に変換したい

```console
$ pandoc -f org source/FILENAME.txt -o source/FILENAME.rst
```

Emacsの``org-mode``は``reST``形式へエクスポート（``ox-rst``）できるはずですが、なぜかうまく動かないので{command}`pandoc`を使って変換します。
今回の例の場合、Org文書の拡張子を``.txt``としているため``-f org``を使って入力形式をを教えています。
出力ファイルは拡張子で``reST``形式（``-o FILENAME.rst``）と自動判別してくれるので、指定していません。

:::{seealso}

毎回、手動で変換するのは面倒くさいのでシェルスクリプトのワンライナーを考えてみました。

```console
$ for f in source/*.txt; do pandoc -f org -t rst $f -o "source/`basename $f .txt`.rst"; done
```

:::

## MarkdownをLuaLaTeXでPDFにしたい

```bash
pandoc test.md -o test.pdf --pdf-engine=lualatex -V documentclass=jlreq
```

ドキュメントクラスを指定して、LaTeXファイルに変換できます。

```bash
pandoc -s test.md -o test.tex -V documentclass=jlreq
```
