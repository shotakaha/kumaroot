# フォントを設定したい（``fontspec``）

```latex
\usepackage{fontspec}
\setmainfont{Source Serif Pro}
\setsansfont{Source Sans Pro}
\setmonofont{Source Code Pro}
```

フォントをカスタマイズするためのパッケージです。
LuaLaTeXとXeLaTeXでOpenTypeフォントが自由に指定できるようになります。

TeXLive2020以降では、欧文フォントは**Latin Modern系**、
和文フォントは**原ノ味系**がデフォルトになっているそうなので、
かならず必要な設定というわけではないかもしれません。

## 和文フォントを設定したい

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

和文フォントを設定する場合、``fontspec``の代わりに``luatexja-fontspec``を使います。
欧文フォントの設定に加えて、``\set****jfont``を使って和文フォントを設定します。

## リファレンス

- {command}`texdoc fontspec`
- {command}`texdoc luatexja-fontspec`
