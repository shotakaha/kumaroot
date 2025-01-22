# Markdownしたい（`markdown`）

```latex
% プリアンブル
\usepackage{markdown}


% 本文
\begin{markdown}

# Markdown Package

`markdown`環境内の文章は、Markdown形式で入力します。

\end{markdown}

Markdown環境の外はLaTeX形式なので、
数式は、いつもどおりのLaTeXコマンドで作成できます。

\begin{equation}
E = mc^{2}
\end{equation}
```

`markdown`パッケージで、LaTeX文書をMarkdown形式で作成できます。
