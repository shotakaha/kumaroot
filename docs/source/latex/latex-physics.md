# 物理記号したい（`physics`）

```latex
\usepackage{physics}
```

[physics](https://www.ctan.org/pkg/physics)パッケージを使って、物理学に関係した数式記号を簡単に記述できるようになります。

大学で物理学や数学のレポートを作成する場合、ベクトル、微分記号、ブラケット記号などを多用しますが、標準の数式環境だけで書くのはなかなか大変です。

:::{hint}

実際に`amsmath`で定義されている数式記号だけを使って書くのはものすごく大変でした。
学生のときに一番知っておきたかったパッケージです。

:::

:::{note}

調べてみると[physics](https://www.ctan.org/pkg/physics)パッケージは（LaTeX的に）内部のお行儀が悪いようです。
また、2012年に開発が止まっています。

代替パッケージ案もいくつか提案されているようです。
そのあたりは[このQiita記事](https://qiita.com/Yarakashi_Kikohshi/items/131e2324f401c3effb84)が詳しいので、参考にしてください。

:::

## ベクトルしたい

```latex
\vb{a}    % ベクトルを太字で表現
\va{a}    % 矢印を使って表現
\vu{a}    % 単位ベクトル（^）
```

## 微分記号したい

```latex
\dd
\dd{x}
\dd[2]{x}
```

```latex
\dv{x}
\dv{f}{x}
```

```latex
\pdv{x}
\pdv{f}{x}
\pdv[n]{f}{x}  % n階の偏微分
```

## ブラケットしたい（`\innerproduct`）

```latex
\ket{\psi}
\bra{\psi}
\braket{\phi}{\psi}
```

量子力学のブラ・ケット記法を簡単に書けます。
`\braket`は内積（`\innerproduct`）のショートハンドです。

## 内積・外積したい（`\crossproduct`）

```latex
\vb{a} \vdot \vb{b}    % 内積
\vb{a} \cross \vb{b}   % 外積
```

`\vdot`（内積）と`\cross`（外積）で、ベクトル演算子を書けます。
`\cdot`や`\times`を毎回書くよりも、意味が伝わりやすくなります。

## ベクトル微分演算子したい（`\divergence`）

```latex
\grad{f}       % 勾配
\div{\vb{E}}   % 発散
\curl{\vb{B}}  % 回転
\laplacian{f}  % ラプラシアン
```

電磁気学で頻出のナブラ演算子（$\nabla$）を使った記号をまとめて用意しています。

## 期待値したい（`\expectationvalue`）

```latex
\ev{H}        % 期待値
\ev{H}{\psi}  % 状態を明示した期待値
\vev{H}       % 真空期待値
```

`\ev`（期待値）や`\vev`（真空期待値）で、演算子の期待値を簡単に書けます。
場の理論のレポートでよく使う記号です。

## 絶対値・ノルムしたい（`\absolutevalue`）

```latex
\abs{x}       % 絶対値
\norm{\vb{v}} % ノルム
```

括弧の大きさは中身に応じて自動調整されます。

## 括弧を自動調整したい（`\pqty`）

```latex
\pqty{x + y}  % 丸括弧
\bqty{x + y}  % 角括弧
\Bqty{x + y}  % 波括弧
```

中身の大きさに応じて括弧のサイズを自動調整してくれるコマンドです。

:::{caution}

`physics`パッケージには括弧を自動調整する`\qty`コマンドもありますが、
`siunitx`も同じ名前の`\qty`（[物理量したい](./latex-siunitx.md)を参照）を定義しています。
両方を読み込むと名前が衝突するため、括弧の自動調整には`\qty`ではなく`\pqty`を使うことをオススメします。

:::

## 交換子したい（`\commutator`）

```latex
\comm{A}{B}   % 交換子
\acomm{A}{B}  % 反交換子
```

量子力学の演算子代数でよく使う交換子・反交換子を書けます。

## 行列要素したい（`\matrixelement`）

```latex
\mel{\phi}{H}{\psi}
```

$\langle \phi | H | \psi \rangle$のような行列要素を、ブラケット記法と同じ感覚で書けます。

## 行列したい（`\matrixquantity`）

```latex
\mqty(1 & 0 \\ 0 & 1)   % 括弧の種類を選べる
\pmqty{1 & 0 \\ 0 & 1}  % 丸括弧
```

`\mqty`は括弧の種類を引数で選べる汎用コマンドです。
丸括弧だけでよい場合は`\pmqty`を使うと簡潔に書けます。

`physics`パッケージでは、同じコマンドに長い形式（`\matrixquantity`）と短い形式（`\mqty`）があります。
`\matrixquantity`は`\mqty`の正式な名前で、`\mqty`はその短縮形です。
`\pmqty`は`\mqty()`と同じ意味で、長い形式はありません。

## 評価したい（`\evaluated`）

```latex
\evaluated{\partialderivative{f}{x}}_{x=0}  % 偏微分の値
```

`\evaluated`で、微分の結果を特定の点で評価した値を書けます。
短い形の`\eval`でも書けます。

## 誤差したい（`\order`）

```latex
\order{x^2}  % O(x^2)
```

`\order`で、近似の誤差の大きさを表す記号（ランダウの記号）を書けます。

## 汎関数微分したい（`\functionalderivative`）

```latex
\functionalderivative{F}{\phi(x)}
```

`\functionalderivative`で、汎関数微分を書けます。
短い形の`\fdv`でも書けます。

## 実部・虚部したい（`\real` / `\imaginary`）

```latex
\real{z}       % 実部
\imaginary{z}  % 虚部
```

`\real`で実部、`\imaginary`で虚部を書けます。
短い形の`\Re`と`\Im`でも書けます。
