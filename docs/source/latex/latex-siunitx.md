# 物理量したい（`siunitx`）

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
\unit{\mega\electronvolt}
\unit{\giga\electronvolt}
\unit{\tera\electronvolt}

% 省略した単位名
\unit{\eV}
\unit{\MeV}
\unit{\GeV}
\unit{\TeV}
```

「電子ボルト（`eV`）」は非SI単位系ですが、慣例的に利用してもよい単位のひとつです。
素粒子物理学で使うエネルギーの単位で、メガ（`M`）、ギガ（`G`）、テラ（`T`）の接頭辞と合わせることが多いです。
これらの接頭辞も含めて、話し言葉で使うような流れで表現できるようになっています。

## 基本単位したい

```latex
% メートル（長さ）
\unit{m}
\unit{\meter}
\unit{\metre}

% キログラム（質量）
\unit{kg}
\unit{\kilogram}
\unit{\kilo\gram}

% 秒（時間）
\unit{s}
\unit{\second}

% アンペア（電流）
\unit{A}
\unit{\ampere}

% ケルビン（熱力学温度）
\unit{K}
\unit{\kelvin}

% モル（物質量）
\unit{mol}
\unit{\mole}

% カンデラ（光度）
\unit{cd}
\unit{\candela}
```

SI基本単位は7つあり、いずれも`siunitx`で定義されています。
ひとつの単位に対して、`s`と`\second`のように、記号と単位名の両方で定義されています。
また、`\meter`と`\metre`はどちらも使えるようになっています。

## 組立単位したい

```latex
% ニュートン（力）
\unit{\newton}
\unit{kg.m.s^{-1}}
\unit{\kilogram \meter \per\second}
\unit[per-mode=symbol]{\kilogram \meter \per\second}
```

組み立て単位は、基本単位を組み合わせて定義される単位です。
`\newton`のように専用のマクロが用意されているものもあれば、
基本単位を`\per`などでつなげて自分で組み立てることもできます。
詳しくは`texdoc siunitx`してドキュメントを参照してください。

## 指数したい（`\num`）

```latex
% 数式モードを使った場合
$6.02 \times 10^{23}$

% siunitxを使った場合
\num{6.02e23}
```

指数表示は`e`（や`E`、`d`、`D`）を使った方法で記述できます。
通常の数式モードに比べて、はるかに簡単です。

## 掛け算したい（`\qtyproduct`）

```latex
% 数式モード
$1.6 \text{cm} \times 2.3 \text{cm} \times 3.4 \text{cm}$

% siunitx
\qtyproduct{1.6 x 2.3 x 3.4}{\cm}
```

`\qtyproduct`を使って、連続する物理量の掛け算を表示できます。
数式モードの場合、掛け算の記号を表示するために`\times`が必要ですが、`siunitx`の場合は`x（エックス）`でOKです。
また、単位を`\text`で書く必要もありません。

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

単位に2乗（`\square`）や3乗（`\cubic`）をつけるためのマクロも定義されています。
また、任意のべき乗を指定できるマクロもあります。

英語で物理量を説明するのに合わせて設計されているようで、
単位の前につけるか、後につけるか、マクロ名が変化します。

## 表組したい（`S[table-format]`）

```latex
\begin{table}
  \caption{測定データ}
  \begin{tabular}{S[table-format=3.2] S[table-format=3.1]}
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

## 誤差したい

```latex
\qty{1.0(2)}{\GeV}
\qty{125.25(17)}{\GeV}
```

測定値の末尾に括弧で誤差を添える書き方（例：$1.0(2)$ GeV = $1.0 \pm 0.2$ GeV）ができます。
実験物理でよく使う表記なので、そのまま`\qty`に渡せると楽です。

## 範囲したい（`\qtyrange`）

```latex
\qtyrange{10}{20}{\GeV}
\numrange{10}{20}
```

`\qtyrange{最小}{最大}{単位}`でエネルギー範囲や質量範囲などを表現できます。
単位のない数値だけの範囲には`\numrange`が使えます。

## 複数の値を並べたい（`\SIlist`）

```latex
\SIlist{10;20;30}{\GeV}
```

セミコロン区切りで複数の値を渡すと、単位を重複させずに列挙してくれます。
パラメーターを並べて紹介したいときに便利です。

## 角度したい（`\ang`）

```latex
\ang{90}
\ang{-30}
\ang{12;30;15}
```

`\ang{角度}`で度（°）表記の角度を書けます。
セミコロン区切りで度・分・秒を指定することもできます。

## 書式設定したい（`\sisetup`）

```latex
\sisetup{round-mode=places, round-precision=2}
\qty{3.14159}{\meter}
```

`\sisetup`で有効数字の丸め方などをまとめて設定できます。
文書全体やプリアンブルで一度指定しておけば、以降の`\qty`や`\num`すべてに反映されます。

## 単位を定義したい（`\DeclareSIUnit`）

```latex
\DeclareSIUnit\jpsi{J/\psi}

\unit{\jpsi}
```

素粒子名のように`siunitx`に用意されていない単位も、`\DeclareSIUnit`で自分で登録できます。
プリアンブルで一度定義しておけば、本文中では`\unit{\jpsi}`のように短く書けます。
