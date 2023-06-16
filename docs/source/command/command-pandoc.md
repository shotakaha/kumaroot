# フォーマット変換したい（``pandoc``）

```console
$ brew install pandoc
```

```console
$ pandoc 入力ファイル名 -o 出力ファイル名
```

入力ファイルの形式を、出力ファイルの形式に変換できます。
形式は拡張子から自動判別してくれます。

## 形式を指定して変換したい（``--from`` / ``--to``）

```console
$ pandoc 入力ファイル名 -o 出力ファイル名 -f 入力形式 -t 出力形式
```

拡張子がない場合や、拡張子でファイル形式を自動判別できない場合、``--from``や``--to``オプションを使って明示的に指定できます。
変換できるファイル形式は``--list-input-formats`` / ``--list-output-formats`` / ``--list-extensions`` で確認できます。
入力形式は64種類、出力形式は43種類に対応しています。

:::{note}

``-o 出力ファイル名``を指定しない場合は、変換結果が標準出力に表示されます。

```console
$ pandoc 入力ファイル名 -t 出力形式
```

上記コマンドで、どのように変換されるかを簡単に確認できます。

:::

## メディアを取り出したい（``--extract-media``）

```console
$ pandoc 入力ファイル名 -o 出力ファイル名 --extract-media=ディレクトリ名
```

``--extract-media``オプションを使って、入力ファイルに貼られている画像を抽出し、指定したディレクトリに保存できます。
ファイル名は、先頭の図から順番に採番され、力されたファイルはこの画像へのパスを参照します。

## WordをMarkdownに変換したい

```console
$ pandoc input.docx -o output.md -t gfm --extract-media=media
```

Word文書をMarkdownに変換しています。
Markdownの変換形式は数種類あります。
ここではGitHub Flavored Markdownに変換しています。

## Wordの変更履歴を残したい

```console
$ pandoc 入力ファイル名.docx -o output.md -t gfm --extract-media=media --track-changes=all
```

Wordの変更履歴を残す場合は``--track-changes``オプションを使います。

## WordをLaTeXに変換したい

```console
$ pandoc 入力ファイル名.docx -o output.tex --extract-media=media -V documentclass=jlreq -s
$ pandoc 入力ファイル名.docx -o output.pdf --pdf-engine=lualatex -V documentclass=jlreq -s
```

``-s / --standalone``オプションをつけると、出力ファイルに必要な情報も追加で書き出されます。
LaTeXの場合は、ドキュメントクラストプリアンブルが書き出されます。
デフォルトのドキュメントクラスは``article``です。
日本語LaTeXの場合は``-V documentclass``で変更するとよいでしょう。

また、``--pdf-engine``を適切に設定すると、日本語PDFを直接作成できます。

## LaTeXをTypstに変換したい

```console
$ pandoc 入力ファイル名.tex -o 出力ファイル名.typ -s
$ typst compile 出力ファイル名.typ
$ open 出力ファイル名.pdf
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
