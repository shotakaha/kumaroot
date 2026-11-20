# 和文フォントしたい（`luatexja-fontspec`）

```latex
% プリアンブル
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

`luatexja-fontspec`で和文フォントを自由に設定できます。
このパッケージを読み込むと、
[luatexja](./latex-luatexja.md)と
[fontspec](./latex-fontspec.md)も読み込まれるため、
和文フォントと欧文フォントを統一的に設定できます。
上の例のフォントは、事前にインストールしておく必要があります。

## 本文フォントしたい（`\setmainjfont`）

```latex
% プリアンブル
\setmainfont{フォント名}
\setmainjfont{フォント名}
```

`\setmainjfont{}`で和文の本文フォント（明朝体）を変更できます。
太字や細字は、オプションで指定できます。

```latex
\setmainjfont[BoldFont=フォント名（太字）]{フォント名}
```

## 見出しフォントしたい（`\setsansjfont`）

```latex
% プリアンブル
\setsansfont{フォント名}
\setsansjfont{フォント名}
```

`\setsansjfont{}`で和文のゴシック体（`\gtfamily`）を変更できます。
`\section{}`などの見出しにこのフォントが使われるかどうかは、文書クラスによって異なります。

## 等幅フォントしたい（`\setmonojfont`）

```latex
% プリアンブル
\setmonofont{フォント名}
\setmonojfont{フォント名}
```

`\setmonojfont{}`で、`verbatim`環境や`\verb`で使われる和文フォント（`\jttdefault`）を変更できます。
`verbatim`環境や[minted環境](./latex-minted.md)で表示されるフォントです。

## 依存パッケージ

```console
$ kpsewhich luatexja-fontspec.sty | xargs cat | grep RequirePackage
\RequirePackage{l3keys2e,luatexja}
\RequirePackage{fontspec}[2024-05-10]% v2.9e
\RequirePackage{luatexja-fontspec-29e} % v2.9e
```
