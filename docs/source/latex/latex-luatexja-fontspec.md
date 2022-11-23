# 和文フォントを設定したい（``luatexja-fontspec``）

```latex
\documentclass{jlreq}
\usepackage{luatexja-fontspec}
\setmainjfont{明朝体のフォント}
\setsansjfont{サンセリフ体のフォント}
\setmonojfont{モノスペース体のフォント}
```

プリセット（[luatexja-preset](./latex-luatexja-preset.md）以外のフォントを使いたい場合、``luatexja-fontspec``パッケージを読み込みます。
このとき``fontspec``パッケージも同時に読み込まれます。

フォント名は自分のパソコンのフォントブックにあるものを探してください。
``setmainjfont`` / ``setsansjfont`` / ``setmonofont`` で明朝体（主に本文）、サンセリフ体（主に見出し）、モノスペース体（主にコードブロックなど）をそれぞれ自由に設定できます。

```latex
\usepackage{latexja-fontspec}

% 欧文フォントの設定
\setmainfont{ReggaeOne-Regular}
\setsansfont{ReggaeOne-Regular}
\setmonofont{PixelMPlus10-Regular}

% 和文フォントの設定
\setmainjfont{ReggaeOne-Regular}
\setsansjfont{ReggaeOne-Regular}
\setmonojfont{PixelMPlus10-Regular}
```
