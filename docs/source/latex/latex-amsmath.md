# 数式したい（``amsmath``）

```latex
\usepackage{amsmath, amssymb}
\usepackage{mathtools, amssymb}
```

数式を表示する場合は``amsmath``パッケージを使います。
``mathtools``パッケージは``amsmath``の不具合を修正した拡張したパッケージです。
ヘビーに使わないのであれば、どちらを使ってもよいと思います。

``amssymb``は数式用フォント（AMSFonts）を読み込むために必要です。

## 数式を本文中で使いたい（``$...$``）

```latex
ピタゴラスの定理 $a^{2} + b^{2} = c^{2}$ は
```

インラインで表示する場合は``$...$``で数式を囲みます。

## 数式をブロックで表示したい

```latex
\begin{equation}
a^{2} + b^{2} = c^{2}
\end{equation}
```

## 数式モードでテキストしたい

```latex
$N_{\text{SK}^{\text{obs}}}$
```

``\text``コマンドを使って、数式中のテキストを立体（ローマン体）に変更できます。
関数名は斜体（イタリック体）で表示しますが、添え字などは立体（ローマン体）で表示することが多いです。

## 複数行の数式を整列させたい

```latex
\begin{align}
z_{1} & = ax + by
z_{2} & = cx + dy
\end{align}
```

## ベクトルや行列を表示したい

```latex
\Hat{A}
\Bar{A}
\Vec{A}
\dot{x}
\ddot{x}
```

[physicsパッケージ](./latex-physics.md)も参照すべきです。
