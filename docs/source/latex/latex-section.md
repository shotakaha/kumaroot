# 見出ししたい（``\section``）

```latex
\section{章見出し}
\subsection{節見出し}
```

見出しには``\section``コマンドを使います。
節見出しには``\subsection``、その他にも``\subsubsection``、``\paragraph``、``\subparagraph``のコマンドがあります。

## 見出しを変更したい（``\thesection``）

```latex
\renewcommand{\thesection}{第\arabic{section}章}
\renewcommand{\thesubsection}{第\arabic{section}.\arabic{subsection}節}
```

見出しの書式を変更する場合は``\thesection``コマンドを再定義します。
章番号のデフォルトは数字（`\arabic{section}`）ですが、ローマ数字（`\roman{section}`）やアルファベット（\alph{section}`）などに変更できます。

節見出し（`\thesubsection`）などの見出しも同様に書式を変更できます。
