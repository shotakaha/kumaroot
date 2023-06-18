# 自由に欧文フォントしたい（``fontspec``）

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

## リファレンス

- {command}`texdoc fontspec`
- {command}`texdoc luatexja-fontspec`
