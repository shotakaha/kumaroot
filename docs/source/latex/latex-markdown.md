# Markdownしたい（`markdown`）

```latex
% プリアンブル
\usepackage[hybrid]{markdown}

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
`hybrid`オプションを有効にすると、`markdown`環境の中でLaTeXコマンドが使えるようになります。
ひとつの文書の中で、LaTeX記法とMarkdown記法のいいとこどりができるように
使い分けると執筆の効率があがりそうです。

## インライン数式したい（`texMathDollars`）

```latex
\begin{markdown}
アインシュタインは$E=mc^{2}$のひとです。
\end{markdown}
```

`$...$`で挟むことでインライン数式できます。
また`$$...$$`で挟むことでディスプレイ数式できます。

複雑な数式は、`markdown`環境に入れずに、素直に`align`環境などを使いましょう。

:::{note}

もし`$...$`記法が効かない場合、`texMathDollars`オプションを明示してください。

```{latex}
\usepackage[hybrid,texMathDollors]{markdown}
```

:::

## LaTeXコマンドしたい（`hybrid`）

```latex
% プリアンブル
\usepackage[hybrid]{markdown}
\usepackage{siunitx}

% 本文
\section{SuperKEKB加速器}

\begin{markdown}
SuperKEKB加速器は周長\qty{3}{\km}の円型加速器です。
\end{markdown}

\section{Belle II 測定器}

\begin{markdown}
Belle II 測定器は\qtyproduct{8x8x8}{\m}の大きな測定器です。
\end{markdown}
```

`hybrid`オプションを有効にすると`markdown`環境の中で
LaTeXコマンドが使えるようになります。
`markdown`環境の中は、Markdown記法で閉じていたほうがよいと思います。
ただ、単位表示の[siunitxパッケージ](./latex-siunitx.md)は便利すぎる。
