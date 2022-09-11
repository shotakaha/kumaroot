# フォントを設定したい（``fontspec``）

LuaLaTeXやXeLaTeXなどのモダンLaTeXでは、フォントを自由に変更できるようになりました。
逆に(u)pLaTeXで変更するのはなかなか大変なので、考えないことをオススメします。

## LuaLaTeXの場合

```latex
\usepackage{latexja-fontspec}

% 欧文フォントの設定
\setmainfont{ReggaeOne-Regular}
\setsansfont{ReggaeOne-Regular}
\setmonofont{PixelMPlus10-Regular}

% 和文フォントの設定
\setmainjfont{ReggaeOne-Regular}
\setsansjfont{ReggaeOne-Regular}
\setmonojfont{PixelMPlus10-Regular}
```

```{toctree}
latex-fontspec
```

## (u)pLaTeXの場合

```latex
% プリアンブル
% \usepackage[utf8]{inputenc}    % 2018年4月以前は必要だった
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[deluxe, uplatex, jis2004]{otf}
```

ドキュメントクラスに``jsarticle``系や``beamer``を使う場合は、
フォントのエンコーディング（文字マッピング）を``T1``に再設定しておきます。
``jlreq``を使う場合、この設定は必要ありません。

また、(u)pLaTeXの場合、フォント一式を変更するのはめんどくさいです。
TeX Live 2020以降は和文デフォルトが原ノ味フォントになっているため、
わざわざ変更する必要はありません。

```{toctree}
latex-fontenc
latex-otf
```

以下では、LaTeX美文書作成入門（第8版）の第12章（欧文フォント）と第13章（和文フォント）を読んで、
自分なりに理解した要素をまとめてみました。

膨大なフォントサンプル集（欧文基本14書体、欧文基本35書体、TeX Gyreフォント集などなど）も
紹介されているので、この2つの章は何度も参照するとよさそうです。

## フォントの5要素

LaTeXのフォントは次の5つの要素で、表示方法が決まっています。

1. エンコーディング
1. ファミリー
1. ウェイト
1. シェープ
1. サイズ

```{note}
ここで書いた**エンコーディング**とはTeX内部の**文字マッピング**のことです。
UTF-8やシフトJISのようなファイルのエンコーディングとはまったく別物だそうです。
```

## エンコーディングを切り替えたい

```latex
\usepackage[T1]{fontenc}
```

古いLaTeXは``OT1``（7bit）、モダンなLaTeXは``TU``（32bit）がデフォルトです。
(u)pLaTeXを使う場合、[fontenc](latex-fontenc.md)パッケージを使って``T1``（8bit）に変更することが推奨されています。

## ファミリーを切り替えたい

```latex
\usepackage{lmodern}
```

欧文フォントは **セリフ体（rm）** / **サンセリフ体（ss）** / **タイプライタ体（tt）** の3種類、
和文フォントは **明朝体（mc）** / **ゴシック体（gt）** / **丸ゴシック体（mg）** の3種類があります。

欧文フォントは、``OT1``エンコーディングはComputer Modern系、
``TU``エンコーディングはLatin Modern系のフォントがデフォルトになっています。
和文フォントは2019年まではIPAexフォント、2020年からは原ノ味フォントがデフォルトになっています。

本文中で局所的にファミリー（書体）を切り替えることができます。

```latex
% 欧文フォント
{\rmfamily ...} または \textrm{...}    % セリフ体（デフォルト）
{\sffamily ...} または \textsf{...}    % サンセリフ体
{\ttfamily ...} または \texttt{...}    % タイプライタ体
% 和文フォント
{\mcfamily ...} または \textmc{...}    % 明朝体
{\gtfamily ...} または \textgt{...}    % ゴシック体
{\mgfamily ...} または \textmg{...}    % 丸ゴシック体
```

## ウェイトを切り替えたい

フォントによっては複数のウェイト（太さ）を持っているものがあります。
本文中で局所的にウェイト（太さ）を切り替えることができます。
LaTeX内ではウェイトを**シリーズ**と呼ぶみたいです。

```latex
{\mdseries ...} または \textmd{...}    % Medium（デフォルト）
{\bfseries ...} または \textbf{...}    % Boldface
{\bxseries ...} または \textbx{...}    % Bold Extended
```

## シェープを切り替えたい

本文中で局所的にシェープを切り替えることができます。

欧文の場合、強調する場合にイタリック体を使うことがあります。
和文の場合、使うところはあんまりないかなと個人的に思っています。

```latex
{\upseries ...} または \textup{...}    % Upright（デフォルト）
{\itseries ...} または \textit{...}    % Italic
{\slseries ...} または \textsl{...}    % Slanted
{\scseries ...} または \textsc{...}    % Small Caps
```

## 文字サイズを切り替えたい

本文中で局所的に文字サイズを切り替えることができます。

```latex
\tiny
\scriptsize
\footnotesize
\small
\normalsize
\large
\Large
\LARGE
\huge
\Huge
```


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
