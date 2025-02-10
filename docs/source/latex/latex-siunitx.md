# 物理量したい（``siunitx``）

```latex
\usepackage{siunitx}

\qty{数量}{単位}
\unit{単位}
```

物理量は、数値は斜体（イタリック）、単位は立体（ローマン）で書くことになっています。
標準の数式モードでも書けますが、記述量が増えてしまいます。
`siunitx`パッケージを使うと、そんな物理量が簡単に書けてしまいます。

物理量（`\qty`）や単位（`\unit`）のほかに、
数値（`\num`）、角度（`\ang`）、複素数（`\complexnum`）などのコマンドが定義されています。
SI基本単位系はもちろん、`\micro`や`\nano`などのSI接頭辞、`\ohm`や`\hertz`など組み立て単位なども定義されています。
詳細はドキュメントを参照してください（`$ texdoc siunitx`）

```latex
\usepackage{physics}
\usepackage{siunitx}
\AtBeginDocument{\RenewCommandCopy\qty\SI}
```

`\qty`コマンドは、[physicsパッケージ](./latex-physics.md)と干渉します。

`physics`パッケージの`\qty`は`\pqty`コマンドで代用（というかこちらのほうが個人的に推奨）できるため、
`siunitx`を優先するように置き換えます。

## 物理量したい（`\qty`）

```latex
SuperKEKB加速器は周長が約\qty{3}{\km}の加速器です。
Belle II 測定器は重さが約\qty{1400}{\tonne}、縦横高さがそれぞれ約\qtyproduct{8 x 8 x 8}{\meter}の巨大な装置です。
\qty{7}{\GeV}の電子ビームと\qty{4}{\GeV}の陽電子ビームを衝突させ、大量のB中間子を生成します。
```

`\qty{数値}{単位}`コマンドで物理量をお手軽に表現できます。
単位は国際単位系（SI単位系）とその組立単位、また非SI単位系ですが慣習的に使っている単位などが利用できます。

:::{note}

ドキュメントを確認すると
v2では`\SI`と`\si`コマンドでしたが、
v3からはそれぞれ`\qty`と`\unit`にしたそうです。
以前のコマンドはまだ使えるようですが、新しい文書には
新しいコマンドを使うとよいと思います。

:::

## パーセントしたい（`\percent`）

```latex
% エスケープが必要
30\%

% 表記ゆれがなくなる
\qty{30}{\percent}
```

パーセント記号も単位として用意されています。
エスケープする必要がなくなってよいと思います。

## 電子ボルトしたい（`\unit`）

```latex
% 単位名
\unit{\electronvolt}
\unit{\megaelectronvolt}
\unit{\gigaelectronvolt}
\unit{\teraelectronvolt}

% 省略した単位名
\unit{\eV}
\unit{\MeV}
\unit{\GeV}
\unit{\TeV}
```

「電子ボルト（``eV``）」は非SI単位系ですが、慣例的に利用してもよい単位のひとつです。
素粒子物理学で使うエネルギーの単位で、メガ（``M``）、ギガ（``G``）、テラ（``T``）の接頭辞と合わせることが多いです。
これらの接頭辞も含めて、話し言葉で使うような流れで表現できるようになっています。

## 組立単位したい

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
\unit{\newton}
\unit{kg.m.s^{-1}}
\unit{\kilogram \meter \per\second}
\unit[per-mode=symbol]{\kilogram \meter \per\second}
```

ひとつの単位に対して、表示するためのマクロは複数あります。
執筆時にソースが読みやすくなるように、使い分けるのがよいと思います。
詳しくは``texdoc siunitx``してドキュメントを参照してください。

## 指数したい（`\num`）

```latex
% 数式モードを使った場合
$6.02 \times 10^{23}$

% siunitxを使った場合
\num{6.02e23}
```

指数表示は``e``（や``E``、``d``、``D``）を使った方法で記述できます。
通常の数式モードに比べて、はるかに簡単です。

## 掛け算したい（`\qtyproduct`）

```latex
% 数式モード
$1.6 \text{cm} \times 2.3 \text{cm} \times 3.4 \text{cm}$

% siunitx
\qtyproduct{1.6 x 2.3 x 3.4}{\cm}
```

``\qtyproduct``を使って、連続する物理量の掛け算を表示できます。
数式モードの場合、掛け算の記号を表示するために``\times``が必要ですが、``siunitx``の場合は``x（エックス）``でOKです。
また、単位を``\text``で書く必要もありません。

## べき乗したい

```latex
% 2乗
\unit{m^{2}}
\unit{\square\meter}
\unit{\meter\squared}

% 3乗
\unit{m^{3}}
\unit{\cubic\meter}
\unit{\meter\cubed}

% N乗
\unit{\meter\tothe{N}}
\unit{\raiseto{N}\meter}
```

単位に2乗（``\square``）や3乗（``\cubic``）をつけるためのマクロも定義されています。
また、任意のべき乗を指定できるマクロもあります。

英語で物理量を説明するのに合わせて設計されているようで、
単位の前につけるか、後につけるか、マクロ名が変化します。

## 表組したい（`S[table-format]`）

```latex
\begin{table}
  \caption{測定データ}
  \begin{tabular}[S[table-format=3.2] S[table-format=3.1]]
    \toprule
    { 長さ (cm)} & {質量 (kg)}\\
    \midrule
    12.34 & 5.6\\
    123.45 & 45.6\\
    1.23 & 0.9\\
    \bottomrule
  \end{tabular}
\end{table}
```

`S`列で表中の数値を揃えることができます。
`table-format`オプションで揃えたい桁数を指定できます。
