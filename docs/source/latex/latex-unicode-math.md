# 数式フォントしたい（`unicode-math`）

```latex
% プリアンブル
\usepackage{amsmath}
\usepackage{fontspec}
\setmainfont{フォント名}

% 数学関係のパッケージやフォント設定後に読み込む
\usepackage{unicode-math}
\setmathfont{フォント名}
```

`unicode-math`は数式でUnicodeフォントが使えるようになるパッケージです。
[amspathパッケージ](./latex-amsmath.md)などの数式関係の設定や
その他のフォント設定の後に読み込むことが推奨されています。

`\setmathfont{}`でOpenTypeフォントを指定します。
デフォルトはLatin Modern Mathになっています。

## 積分したい（`∫`）

```latex
\begin{equation}
∫dx = x
\end{equation}
```

Unicode文字がそのまま使えるので`\int`を`∫`で書くことができます。

数学記号には読み方がよくわからない記号もあったりします。
そのような場合にそのまま入力（もしくはコピペ）できるのは、
便利かなと思います。
