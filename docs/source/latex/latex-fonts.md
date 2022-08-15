# フォントの設定

LaTeX美文書作成入門（第8版）の第12章（欧文フォント）と第13章（和文フォント）を読んで、
自分なりに理解した要素をまとめてみました。

膨大なフォントサンプル集（欧文基本14書体、欧文基本35書体、TeX Gyreフォント集などなど）も
紹介されているので、この2つの章は何度も参照するとよいです。

## フォントの5要素

1. エンコーディング
1. ファミリー
1. ウェイト
1. シェープ
1. サイズ

## エンコーディングを切り替えたい

エンコーディングはTeX内部の**文字マッピング**のことです[^encoding]。
古いLaTeXは``OT1``（7bit）、モダンなLaTeXは``TU``（32bit）がデフォルトです。
(u)pLaTeXを使う場合は[fontenc](latex-fontenc.md)パッケージを使って``T1``（8bit）に変更したほうがよいそうです。

[^encoding]: UTF-8やシフトJISのようなファイルのエンコーディングとはまったく別物だそうです。

```latex
% プリアンブル
% \usepackage[utf8]{inputenc}    % 2018年4月以前は必要だった
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[deluxe, uplatex, jis2004]{otf}
```

欧文フォントは、``OT1``エンコーディングはComputer Modern系、
``TU``エンコーディングはLatin Modern系のフォントがデフォルトになっています。
和文フォントは2019年まではIPAexフォント、2020年からは原ノ味フォントがデフォルトになっています。

## ファミリーを切り替えたい

欧文フォントは **セリフ体（rm）** / **サンセリフ体（ss）** / **タイプライタ体（tt）** の3種類、
和文フォントは **明朝体（mc）** / **ゴシック体（gt）** / **丸ゴシック体（mg）** の3種類があります。



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

## 和文フォントのプリセットを切り替える

```latex
\usepackage[haranoaji]{luatexja-preset}    % TeXLive 2020のデフォルト
\usepackage[ipaex]{luatexja-preset}
\usepackage[sourcehan]{luatexja-preset}
\usepackage[hiragino-pro, hiragino-pron]{luatexja-preset}

```

## フォントのサンプル

- Computer Modern（cmr / cmss/ cmtt）
- Latin Modern（lmr / lmss / lmtt）
- 欧文基本14書体
  - Times（ptm）
  - Helvetica（phv）
  - Courier（pcr）
  - pifont（psy / pzd）
- 欧文基本35書体
  - Helvetica Narrow（phv）
  - New Century Schoolbook（pnc）
  - Avant Garde（pag）
  - Palatino（pplx）
  - Bookman
  - Zapf Chancery
- TeX Gyreフォント集
  - Adventor
  - Bonum
  - Chorus
  - Cursor
  - Heros
  - Pagella
  - Schola
  - Termes
- その他のフォント
  - Garamond
  - Charter
  - Bera
  - Cabin
  - Optima (Classico)
  - Inconsolata
  - Crimson, Cochineal
  - Noto
  - Open Sans
  - Comic Neue
  - Source Serif Pro, Source Sans Pro, Source Code Pro
- レガシーな数式用フォント
  - mathptmx : Times系
  - mathpazo : Palatino
  - newtxtext, newtxmath
  - newpxtext, newpxmath
  - STIX2フォント

## 和文フォント

明朝体＝セリフ体
ゴシック体＝サンセリフ体

- ヒラギノ角ゴシック（W0-W9）
- IPA/IPAex明朝・ゴシック
- Adobe源ノ明朝・源ノ角ゴシック
- 原ノ味フォント

TeXLive 2019までIPAexフォント
TeXLive 2020から原ノ味フォント

## 日本語の文字と文字コード

- 1716　康熙時点（約47000文字）
- 1946　当用漢字（1850文字）
- 1949　当用漢字字体表
- 1951　人名用漢字別表（92文字）
- 1978　JIS C6226（情報交換用漢字符号系）（78JIS）（6802文字）
- 1981　当用漢字→常用漢字（1945文字）、人名用漢字
- 1983　JIS C 6226改訂（83JIS）（6877文字）
- 1987　JIS X 0208と改称
- 1990　JIS X 0208改訂（情報交換用漢字符号）（6879文字）
- 1997　JIS X 0208改訂（7ビット及び8ビットの2バイト情報交換用符号化漢字集合）
  - JIS (ISO-2022-JP)
  - Shift JIS (CP932)
  - EUC-JP
- 2000　JIS X 0213（JIS2000）（11223文字）
- 2004　JIS X 0213改訂（JIS2004）
-
