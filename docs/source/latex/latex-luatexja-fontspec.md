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
\usepackage{luatexja-fontspec}

% 欧文フォントの設定
\setmainfont{KiwiMaru-Regular}
\setsansfont{ReggaeOne-Regular}
\setmonofont{HackGen35Console-Regular}

% 和文フォントの設定
\setmainjfont{KiwiMaru-Regular}
\setsansjfont{ReggaeOne-Regular}
\setmonojfont{HackGen35Console-Regular}
```

上記の例は、変更が分かりやすいようにすべて別のフォントを設定しています。

実用的なことを考えると、本文用フォントと見出し用フォントは同じファミリーの異なったウェイトを設定すると、簡単に統一感を出せてよいと思います。
