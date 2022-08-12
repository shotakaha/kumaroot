# pandocコマンドの使い方

``Org-mode``や``Markdown``をすでに使っている場合、``reST形式``の書式を新しく覚えるのは、やはりめんどうです。
そのような場合は{command}`pandoc`コマンドを使った、以下のようなワークフローを考えることができます。

1. Emacsの``Org-mode``で文章を作成する。ただし``QuickLook``できるように``.txt形式`` で保存する
1. {command}`pandoc` を使って``reST形式``に変換する
1. ``Sphinx``を使ってHTMLとPDFの文書を作成する

```{caution}
複数のマシンを使う場合、環境の構築に手間がかかったりするので
``reST形式``を覚える方が近道だったりするかもしれません。
```

以下では ``org-mode``と``HTML``から``reST``形式変換する例を挙げておきます。
残念ながらWordファイル（``doc`` or ``docx``）を``reST``形式に直接変換することはできませんが [#]_ 、
Word から HTML に書き出せば ``reST`` に変換することができます。

.. [#]
   逆（rest -> Word）はできるみたいです

## ``org-mode``を``reST``に変換したい

``org-mode``は``reST``形式へエクスポート（``ox-rst``）できるはずですが、なぜかうまく動かないので{command}`pandoc`を使って変換します。
今回の例の場合、Org文書の拡張子が``.txt``となっているので、
``-f org``を使って{command}`pandoc`に入力フォーマットを教えています。
出力ファイルは拡張子で``reST``形式（``-o FILENAME.rst``）と分かるので、
出力フォーマットを指定する必要はありません。

```bash
$ pandoc -f org source/FILENAME.txt -o source/FILENAME.rst
```

毎回、手動で変換するのは面倒くさいのでシェルスクリプトの
ワンライナーを考えてみました。

```bash
$ for f in source/*.txt; do pandoc -f org -t rst $f -o "source/`basename $f .txt`.rst"; done
```

## HTMLを``reST``に変換したい

この場合は、入力フォーマットも出力フォーマットも、
ファイルの拡張子から判別できるのでオプションは必要ありません。

```bash
$ pandoc source/FILENAME.html -o source/FILENAME.rst
```
