# ドット文字したい（`DotGothic16`）

```console
$ brew install --cask font-dotgothic16
```

Googleフォントにある[DotGothic16](https://fonts.google.com/specimen/DotGothic16)を使います。
Homebrewでインストールできます。

```latex
% プリアンブル
\usepackage{luatexja-fontspec}

% 欧文フォント
\setmainfont{DotGothic16}
\setsansfont{DotGothic16}
\setmonofont{DotGothic16}

% 和文フォントの設定
\setmainjfont{DotGothic16}
\setsansjfont{DotGothic16}
\setmonojfont{DotGothic16}
```

1スタイル（Regular 400）しかないので、
すべての書体を同じに設定します。
