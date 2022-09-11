# 数式を使いたい（``amsmath``）

```latex
\usepackage{amsmath, amssymb}
```

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

## 複数行の数式を整列させたい

```latex
\begin{align}
z_{1} & = ax + by
z_{2} & = cx + dy
\end{align}
```

## ベクトルや行列を表示したい

[physicsパッケージ](./latex-physics.md)を使うべきです。
