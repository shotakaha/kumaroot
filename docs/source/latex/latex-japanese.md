# 日本語とLaTeX

日本語はマルチバイトコードであるため、LaTeXでコンパイルするのが難しかったみたいです。
それに対処する歴史的な紆余曲折から日本語版LaTeXにはさまざまな派生品が存在します。
この歴史の詳細に関しては、三重大学の奥村さんのウェブサイトをはじめ、ググってみるとよいでしょう。

## 2020年ころの話

日本語のLaTeX文書の作成には ``(u)pLaTeX + dvipdfmx`` もしくは``LuaLaTeX`` を使います。
とくに``LuaLaTeX``はDVIファイルを作成せずに、直接PDFファイルを作ることができます。

```bash
$ lualatex --help  # ヘルプを表示
$ lualatex hoge    # LuaLaTeXの場合
```

{command}`latexmk`という便利なコンパイル用のコマンドもあります。
LaTeXでは目次や索引の生成のために複数回コンパイルする必要がありますが、
それをよしなに取り扱ってくれます。
{file}`latexmkrc`を作成し、``$pdf_mode = 4;``と書いておきます。

```bash
$ latexmk  # 設定をlatexmkrcから読み込む
```


## 2015年ころの話

```{warning}
【2021-01-18に追記】
(u)pLaTeXを使うのは少し昔の話。
2020年からはLuaLaTeXを使うのをオススメします。
```

日本語のLaTeX文書の作成には ``(u)pLaTeX`` と ``dvipdfmx`` を使います。
{command}`(u)platex` コマンドでLaTeX文書をコンパイルしDVIファイルを作成、
そして{command}`dvipdfmx` コマンドでDVIファイルをPDFファイルに変換する、
とう二段構えの処理をします。

```bash
$ platex hoge.tex
$ dvipdfmx hoge.dvi
```

これをまとめて処理してくれるのが{command}`ptex2pdf`コマンドです。
（おそらく）MacTeXをインストールすると勝手についてきます。

```bash
$ ptex2pdf -h          # ヘルプを表示
$ ptex2pdf -l hoge     # platex + dvipdfmx の場合
$ ptex2pdf -l -u hoge  # uplatex + dvipdfmx の場合
```

ただのスクリプト（Luaで書かれてるみたい）なので、気になる人は中を見てみるとよいでしょう。

```bash
$ which ptex2pdf
/Library/TeX/texbin/ptex2pdf

$ less /Library/TeX/texbin/ptex2pdf
```
