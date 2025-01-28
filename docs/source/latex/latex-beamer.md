# スライドしたい（`beamer`）

```latex
\documentclass[t]{beamer}
\usepackage{luatexja}

\begin{document}

\section{スライド1}
\begin{frame}
  \frametitle{スライド1}
\end{frame}

\section{スライド2}
\begin{frame}
  \frametitle{スライド2}
\end{frame}

\end{document}
```

`beamer`クラスでスライド形式の文書を作成できます。
`frame`環境が1枚のスライドに相当します。
いくつもの`frame`を使って、スライド資料を構成します。

[luatexjaパッケージ](./latex-luatexja.md)で日本語を扱えるようになります。
