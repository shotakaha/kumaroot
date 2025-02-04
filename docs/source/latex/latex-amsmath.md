# 数式したい（`amsmath`）

```latex
\usepackage{amsmath, amssymb}
\usepackage{mathtools, amssymb}
```

数式を表示する場合は`amsmath`パッケージを使います。
`amssymb`は数式用フォント（AMSFonts）を読み込むために必要です。

`mathtools`パッケージは`amsmath`の不具合を修正した拡張したパッケージです。
ヘビーに使わないのであれば、どちらを使ってもよいと思います。

## インラン数式したい（`$...$`）

```latex
ピタゴラスの定理 $a^{2} + b^{2} = c^{2}$ は
```

`$...$`で、本文中に数式を出力できます。
この出力形式を**インライン数式**と呼びます。
インライン数式には数式番号はつきません。

## ディスプレイ数式したい（`\[...\]` / `equation`）

```latex
\[
a^{2} + b^{2} = c^{2}
\]
```

`\[...\]`もしくは`equation`環境で囲んだ数式は、別行立てで出力できます。
この形式を**ディスプレイ数式**と呼びます。

`equation`環境の数式は自動で採番され、数式番号が表示されます。

```latex
\begin{equation}
a^{2} + b^{2} = c^{2}
\end{equation}
```

また`equation`環境でも同様のことができます。
ひとつの文書の中で、どちらかの記法に統一するとよいと思います。

## 文章テキストしたい（`\text`）

```latex
\begin{equation}
E = mc^{2} \quad \text{（$E$はエネルギー）}
\end{equation}
```

`\text{}`で、数式中に文章テキストを挿入できます。
この場合には、本文用フォントが適用されます。

:::{note}

数式環境の中では、数式用フォントが適用されます。
`\mathrm{}`を使うと、数式用フォントの立体が適用されます。
変数名の添え字などはこちらを使うとよいです。

:::

## 整列したい（`align`）

```latex
\begin{align}
z_{1} & = ax + by\\
z_{2} & = cx + dy
\end{align}
```

`align`環境で、複数行の数式を整列できます。
`&`で整列する位置を設定し、行末の`\\`で次の行に移動します。
行ごとに数式番号が出力されます。

:::{note}

昔は`eqarray`環境を使っていましたが、現在は非推奨となっています。

:::

## 黒板太字したい（`\mathbb`）

```latex
\mathbb{ABCdef7890}
```

:::{math}
\mathbb{ABCdef7890}
:::

`\mathbb{}`で文字スタイルを黒板文字（blackboard bold）に変更できます。

## 筆記体したい（`\mathcal`）

```latex
\mathcal{ABCdef7890}
```

:::{math}
\mathcal{ABCdef7890}
:::

`\mathcal{}`で文字スタイルを筆記体（caligraphy）に変更できます。

## 花文字したい（`\mathscr`）

```latex
\mathscr{ABCdef7890}
```

:::{math}
\mathscr{ABCdef7890}
:::

`\mathscr{}`で文字スタイルを花文字（script font）に変更できます。

## ドイツ文字したい（`\mathfrak`）

```latex
\mathfrak{ABCdef7890}
```

:::{math}
\mathfrak{ABCdef7890}
:::

`\mathfrak{}`で文字スタイルをドイツ文字（fraktur）に変更できます。

## ベクトルや行列を表示したい

```latex
\Hat{A}
\Bar{A}
\Vec{A}
\dot{x}
\ddot{x}
```

[physicsパッケージ](./latex-physics.md)も参照すべきです。

## 依存パッケージ

```console
$ kpsewhich amsmath.sty | xargs cat | rg RequirePackage
\RequirePackage{amstext}[1995/01/25]
\RequirePackage{amsbsy}[1995/01/20]
\RequirePackage{amsopn}[1995/01/20]
```

```console
$ kpsewhich amssymb.sty | xargs cat | rg RequirePackage
\RequirePackage{amsfonts}[1995/01/01]
```

```console
$ kpsewhich mathtools.sty | xargs cat | rg RequirePackage
\RequirePackage{keyval,calc}
\RequirePackage{mhsetup}[2021/03/18]
\RequirePackage{amsmath}[2016/11/05]
  \RequirePackage{graphicx}%
```

`mathtools`の中で`amsmath`が読み込まれています。
