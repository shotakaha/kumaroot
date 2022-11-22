# 和文フォントを設定したい（``luatexja-fontspec``）

```latex
\documentclass{jlreq}
\usepackage{luatexja-fontspec}
\setmainjfont{明朝体のフォント}
\setsansjfont{サンセリフ体のフォント}
\setmonojfont{モノスペース体のフォント}
```

プリセット（[luatexja-preset](./latex-luatexja-preset.md）以外のフォントを使いたい場合、``luatexja-fontspec``パッケージを読み込みます。
``setmainjfont`` / ``setsansjfont`` / ``setmonofont`` で明朝体（主に本文）、サンセリフ体（主に見出し）、モノスペース体（主にコードブロックなど）をそれぞれ自由に設定できます。
