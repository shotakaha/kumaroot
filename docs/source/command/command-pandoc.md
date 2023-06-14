# フォーマット変換したい（``pandoc``）

```console
$ brew install pandoc
```

さまざまはファイル形式を変換するコマンドです。

## Markdownに変換したい

```console
$ pandoc 入力ファイル名 -o 出力ファイル名
$ pandoc input.docx -o output.md
```

あるファイル形式を別のファイル形式に変換できます。
入力ファイルの形式、出力ファイルの形式は拡張子から自動判別できます。

## 形式を指定して変換したい（``--from`` / ``--to``）

```console
$ pandoc 入力ファイル名 -o 出力ファイル名 -f 入力ファイルの形式 -t 出力ファイルの形式
$ pandoc input.docx --to gfm -o output.md
$ pandoc input.docx -t gfm -o output.md
```

拡張子がない場合や、拡張子でファイル形式を自動判別できない場合、``--from``や``--to``オプションを使って明示的に指定できます。
変換できるファイル形式は``--list-input-formats`` / ``--list-output-formats`` / ``--list-extensions`` で確認できます。

``--to gfm``するとGitHub Flavored Markdownで出力されます。
``--to markdown``するとPandocフレーバーで出力されます。

## メディアを取り出したい（``--extract-media``）

```console
$ pandoc 入力ファイル名.docx -o 出力ファイル名 --extract-media=ディレクトリ名
$ pandoc input.docx -o output.md --extract-media=media
```

``--extract-media``オプションを使って、Word文書から図を抽出し、指定したディレクトリに保存できます。
ファイル名は、先頭の図から順番に採番され、力されたファイルはこの画像へのパスを参照します。

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
