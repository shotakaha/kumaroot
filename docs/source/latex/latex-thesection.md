# 章見出しを変更したい（``\thesection``）

```latex
\renewcommand{\thesection}{第\arabic{section}章}
\renewcommand{\thesubsection}{第\arabic{section}.\arabic{subsection}節}
```

章見出しの書式を変更する場合は、``\thesection``コマンドを再定義します。
章番号のデフォルトは数字（`\arabic{section}`）ですが、ローマ数字（`\roman{section}`）、アルファベット（\alph{section}`）などに変更できます。

節見出し（`\thesubsection`）などの見出しも同様に書式が変更できます。
