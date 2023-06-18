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

## TeXのディストリビューション

- (1978) TeX
- (1984) LaTeX
- (1990) pTeX -> pLaTeX
- (1993) LaTeX2e
- (1997) pdfTeX
- (2004) XeTeX
- (2007) LuaTeX
- (2007) upTeX -> TeX Live 2012
- (2008) e-pTeX -> TeX Live 2011
- (2011) ConTeXt

## 日本語の文字と文字コード

1716年　康熙字典
:   約47000文字。
    漢字の字体は康熙字典を正字とするのが伝統的な考え方だそう。
    でも、この字典にも不統一・不適切なところはあり、
    世間でもさまざまな俗字・略字が使われていた。

1946年　当用漢字
:   1850文字。

1949年　当用漢字字体表
:   1850文字。

1951年　人名用漢字別表
:   92文字を追加。

1978年　情報交換用漢字符号系（JIS C6226）
:   6802文字。
    78JIS

1981年　当用漢字に代わって常用漢字を制定
:   1945文字。
    人名用漢字も追加され、新字体がさらに増加。

1983年　JIS C 6226改訂
:   6877文字。
    83JIS。
    多くの字の構成要素が新字体風に変更された。
    78JISか83ISかによって字体が違うことになった。

1987年　JIS X 0208と改称
:   （文字数変わらず？）

1990年　JIS X 0208「情報交換用漢字符号」に改称
:   6879文字。

1997年　JIS X 0208「7ビット及び8ビットの2バイト情報交換用符号化漢字集合」に改称
:   （文字数変わらず？）
    JISコード (ISO-2022-JP)、シフトJIS (CP932)、EUC-JPが生まれた

2000年　JIS X 0213「7ビット及び8ビットの2バイト情報交換用符号化**拡張**漢字集合」
:   11223文字。
    JIS X 0208を大幅に拡張した。
    JIS2000。
    表外漢字字体表の改訂。

2004年　JIS X 0213改訂
:   （文字数増えた？）
    JIS2004。

2010年　常用漢字表の改訂
:   常用漢字だがシフトJISやEUC-JPで表現できない漢字が生まれてしまう。
    Unicodeの利用に拍車がかかる。


## OpenTypeフォント

OpenTypeフォントは従来の**PostScript Type 1 形式**と
**TrueType**形式を包含する新しいフォント形式です。

フォント名に
スタンダード（``Std``）はAdobe-Japan1-3（9354グリフ）対応を含み、
プロ（``Pro``）はAdobe-Japan1-3（15444グリフ）対応や
Adobe-Japan1-5（20316グリフ）対応したものです。
プロ6（``Pr6N``）はAdobe-Japan1-6（23058グリフ）に対応です。
