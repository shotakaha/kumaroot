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

`markdown`パッケージで、LaTeX文書をMarkdown記法で作成できます。
ひとつの文書の中で、LaTeX記法とMarkdown記法の
いいとこどりをするように使い分けると執筆の効率があがりそうです。

## インライン数式したい（`texMathDollars`）

```latex
% プリアンブル
\usepackage[texMathDollars]{markdown}


% 本文
\begin{markdown}
アインシュタインは$E=mc^{2}$のひとです。
\end{markdown}
```

`texMathDollars`オプションを有効にすると、
`markdown`環境内でもインライン数式できます。

:::{hint}

複雑な数式などは、素直に`align`環境などを使いましょう。

:::
