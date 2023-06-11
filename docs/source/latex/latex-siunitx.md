# 単位や物理量を表示したい（``siunitx``）

```latex
\usepackage{siunitx}
```

数値や単位を簡単に書くことができるパッケージです。

数値（``\num``）、角度（``\ang``）、単位（``\unit``/``\qty``）、複素数（``\complexnum``）などのマクロが定義されています。
また、``\micro``や``\nano``などのSI接頭辞、``\ohm``や``\hertz``など物理量なども定義されています。
ここには書ききれないので``texdoc siunitx``してドキュメントを参照してください。

:::{seealso}

[physicsパッケージ](./latex-physics.md)と一緒に使う場合は、``\qty``コマンドが干渉します。
physicsパッケージは``\pqty``コマンドで代用（というかこちらのほうが個人的に推奨）できるので、次のように``\qty``コマンドを``\SI``コマンドに寄せておくとよいです。

```latex
\usepackage{physics}
\usepackage{siunitx}
\AtBeginDocument{\RenewCommandCopy\qty\SI}
```

:::

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
