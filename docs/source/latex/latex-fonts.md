# フォントの設定

LaTeX美文書作成入門（第8版）の第12章（欧文フォント）と第13章（和文フォント）を再読し、フォント設定に対する理解を深めたいと思います。

レガシーLaTeX

```latex
% プリアンブル
% \usepackage[utf8]{inputenc}    % 2018年4月以前は必要だった
\usepackage[T1]{f ntenc}
\usepackage{lmodern}
\usepackage[deluxe, uplatex, jis2004]{otf}
```

モダンLaTeX

```latex
% プリアンブル
\usepackage{fontspec}
\setmainfont{Source Serif Pro}
\setsansfont{Source Sans Pro}
\setmonofont{Source Code Pro}

\usepackage{microtype}
```


## フォントの5要素

エンコーディング
:   TeX内部の文字へのマッピング。
    ``OT1``（7ビット）→``T1``（8ビット）→``TU``（32ビット）という歴史がある。
    モダンLaTeXは``TU``エンコーディングがデフォルトになっている。
    レガシーLaTeXは``T1``エンコーディングを指定するのが妥当。

ファミリ
:   セリフ体、サンセリフ体、モノスペース体（タイプライタ体）のように関連するフォントの集まり。
    ``OT1``では``Computer Modern Roman (cmr)``、``Computer Modern Sans Serif (cmss)``、``Computer Modern Typewriter Type (cmtt)``がデフォルト。
    ``TU``では``Latin Modern Roman (lmr)``、``Latin Modern Sans Serif (lmss)``、``Latin Modern Typewriter Type (lmtt)`` がデフォルト。
    フォントはLatin Medernに変えるのを推奨。
    美文書作成入門は``Latin Modern Roman``、``Souce Sans Pro``、``Source Code Pro``を使っている。


## ファミリーを切り替えたい

```latex
{\rmfamily ...} または \textrm{...}    % セリフ体（デフォルト）
{\sffamily ...} または \textsf{...}    % サンセリフ体
{\ttfamily ...} または \texttt{...}    % タイプライタ体
```

``\{rm ...}``、``\{sf ...}``、``\{tt ...}``という書き方は非推奨。

## シリーズを切り替えたい

シリーズ（＝ウェイト）はフォントによってあったりなかったり。

```latex
{\mdseries ...} または \textmd{...}    % Medium（デフォルト）
{\bfseries ...} または \textbf{...}    % Boldface
{\bxseries ...} または \textbx{...}    % Bold Extended
```

## シェープを切り替えたい

```latex
{\upseries ...} または \textup{...}    % Upright（デフォルト）
{\itseries ...} または \textit{...}    % Italic
{\slseries ...} または \textsl{...}    % Slanted
{\scseries ...} または \textsc{...}    % Small Caps
```

## サイズを切り替えたい

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
