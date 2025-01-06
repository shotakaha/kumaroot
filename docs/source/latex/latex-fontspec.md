# 欧文フォントしたい（`fontspec`）

```latex
% lualatex
% プリアンブル
\usepackage{fontspec}
\setmainfont{Source Serif Pro}
\setsansfont{Source Sans Pro}
\setmonofont{Source Code Pro}
```

`fontspec`でフォントを自由に設定できます。
LuaLaTeXとXeLaTeXでOpenTypeフォントが自由に指定できるようになります。

TeXLive2020以降では、欧文フォントは**Latin Modern系**、
和文フォントは**原ノ味系**がデフォルトになっているそうなので、
かならず必要な設定というわけではないかもしれません。

セリフ体
:   Source Serif Pro

サンセリフ体
:   Source Sans Pro

タイプライタ体
:   Source Code Pro
