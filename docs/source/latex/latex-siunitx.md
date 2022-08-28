# siunitx

```latex
\usepackage{siunitx}
```

数値や単位を簡単に書くことができるパッケージです。

数値（``\num``）、角度（``\ang``）、単位（``\unit``/``\qty``）、複素数（``\complexnum``）などのマクロが定義されています。
また、``\micro``や``\nano``などのSI接頭辞、``\ohm``や``\hertz``など物理量なども定義されています。
ここには書ききれないので``texdoc siunitx``してドキュメントを参照してください。

## 指数を表示したい

```latex
$6.02 \times 10^{23}$  % 数式モードを使った場合
\num{6.02e23}  % siunitxを使った場合
```

## 掛け算を表示したい

```latex
$1.6 \times 2.3 \times 3.4$   % 数式モード
\numproduct{1.6 x 2.3 x 3.4}  % siunitx
```

数式モードの場合、掛け算の記号を表示するために``\times``と書く必要がありますが、``siunitx``の場合は``x``でOKです。

## 単位を表示したい

```latex
\unit{m}, \unit{\meter}, \unit{\metre}  % メートル
\unit{kg}, \unit{\kilogram}, \unit{\kilo\gram}  % キログラム
\unit{s}, \unit{\second}  % 秒
\unit{A}, \unit{\ampere}  % アンペア

\unit{N}, \unit{\newton}  % ニュートン
\unit{kg.m.s^{-1}}
\unit{\kilogram\meter\per\second}
\unit[per-mode=symbol]{\kilogram\meter\per\second}
```
