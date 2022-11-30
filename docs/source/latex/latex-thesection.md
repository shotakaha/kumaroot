# 章見出しを変更したい（``\thesection``）

```latex
\renewcommand{\thesection}{第\arabic{section}章}
\renewcommand{\thesubsection}{第\arabic{section}.\arabic{subsection}節}
```

章見出しの書式を変更する場合は、``\thesection``コマンドを再定義します。
