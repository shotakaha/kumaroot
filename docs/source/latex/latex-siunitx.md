# 物理量したい（``siunitx``）

```latex
\usepackage{siunitx}

\qty{数量}{単位}
\unit{単位}

```

物理量は、数値は斜体（イタリック）、単位は立体（ローマン）で書くことになっています。
``siunitx``はそれを簡単に書くことができるパッケージです。

物理量（``\qty``）や単位（``\unit``）のほかに、数値（``\num``）、角度（``\ang``）、複素数（``\complexnum``）などのマクロが定義されています。
SI単位系はもちろん、``\micro``や``\nano``などのSI接頭辞、``\ohm``や``\hertz``など組み立て単位なども定義されています。
ここには書ききれないので``texdoc siunitx``してドキュメントを参照してください。

:::{note}

過去の記事を読むと``\si``と``\SI``コマンドを使っているものが多いですが、
v3から``\unit``と``\qty``が推奨コマンドになったようです。

:::

:::{seealso}

[physicsパッケージ](./latex-physics.md)と一緒に使う場合は、``\qty``コマンドが干渉します。
physicsパッケージは``\pqty``コマンドで代用（というかこちらのほうが個人的に推奨）できるので、
次のように``\qty``コマンドを``\SI``コマンドにしておきます。

```latex
\usepackage{physics}
\usepackage{siunitx}
\AtBeginDocument{\RenewCommandCopy\qty\SI}
```

:::

## 物理量したい

```latex
\qty{3}{km}
\qtylist{1;2;3}{kg}    % 1 kg, 2 kg and 3 kg
\qtyproduct{8 x 8 x 8}{m}  % 8 m x 8 m x 8 m
\qtyrange[]{10}{30}{m} % 10 to 30 m
```

## 指数を表示したい

```latex
% 数式モードを使った場合
$6.02 \times 10^{23}$

% siunitxを使った場合
\num{6.02e23}
```

``\num``を使って指数を表示できます。
通常の数式モードに比べて、はるかに簡単に書くことができます。

## 掛け算を表示したい

```latex
% 数式モード
$1.6 \times 2.3 \times 3.4$

% siunitx
\numproduct{1.6 x 2.3 x 3.4}
```



数式モードの場合、掛け算の記号を表示するために``\times``と書く必要がありますが、``siunitx``の場合は``x（エックス）``でOKです。

## 単位を表示したい

```latex
% メートル
\unit{m}
\unit{\meter}
\unit{\metre}

% キログラム
\unit{kg}
\unit{\kilogram}
\unit{\kilo\gram}

% 秒
\unit{s}
\unit{\second}

% アンペア
\unit{A}
\unit{\ampere}

% ニュートン
\unit{N}
\unit{\newton}
\unit{kg.m.s^{-1}}
\unit{\kilogram\meter\per\second}
\unit[per-mode=symbol]{\kilogram\meter\per\second}
```
