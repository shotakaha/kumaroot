# 自由に和文フォントしたい（`luatexja-fontspec`）

```latex
\usepackage{luatexja-fontspec}

\setmainjfont{和文フォント／本文}
\setsansjfont{和文フォント／見出し}
\setmonojfont{和文フォント／コードブロック}

\setmainfont{欧文フォント／本文}
\setsansfont{欧文フォント／見出し}
\setmonofont{欧文フォント／コードブロック}
```

`luatexja-fontspec`は
[luatexja](./latex-luatexja.md)と
[fontspec](./latex-fontspec.md)を組み合わせて、
和文フォントと欧文フォントを統一的に設定するためのパッケージです。
`luatexja-fontspec`を読み込むと、`fontspec`パッケージも同時に読み込まれます。

`setmainfont` / `setsansfont` / `setmonofont`で欧文フォント、
`setmainjfont` / `setsansjfont` / `setmonojfont`で和文フォントを設定できます。
プリセット（[luatexja-preset](./latex-luatexja-preset.md)）以外のフォントを指定できます。
フォント名は自分のパソコンのフォントブックにあるものを探してください。

```latex
\documentclass[a4paper]{article}
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

:::{note}
本文はセリフ体（明朝体）、見出しはサンセリフ体（ゴシック体）、コードブロックはモノスペース体（等幅体）を使うことが多いです。
:::
