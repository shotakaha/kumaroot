# 見出ししたい（`\section`）

```latex
\part{部}
\chapter{章}
\section{節}
\subsection{項}
\subsubsection{目}
\paragraph{段落}
\subparagraph{小段落}
```

見出しは、自分で**太字**などにせず、専用のコマンドを使います。
見出しはレベルがあり
部（`\part{}`）、
章（`\chapter{}`）、
節（`\section{}`）、
項（`\subsection{}`）、
目（`\subsubsection{}`）
の順番に並んでいます。

ドキュメントクラスによってデフォルトの見出しレベルが異なります。

また、見出しではないですが、
段落（`\paragraph{}`）と
小段落（`\subparagraph{}`）を指定するコマンドもあります。

## 見出しを変更したい（`\thesection`）

```latex
\renewcommand{\thesection}{第\arabic{section}章}
\renewcommand{\thesubsection}{第\arabic{section}.\arabic{subsection}節}
```

`\thesection`を再定義して、見出しの書式を変更できます。
章番号のデフォルトはアラビア数字（`\arabic{section}`）ですが、
ローマ数字（`\roman{section}`）や
アルファベット（`\alph{section}`）などに変更できます。

同様に`\thesubsection`を再定義して、節見出しの書式を変更できます。
また[titlesecパッケージ](./latex-titlesec.md)など、
見出しを変更するためのパッケージもあります。
