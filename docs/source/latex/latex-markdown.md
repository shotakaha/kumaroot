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

`markdown`は、Markdown記法を使えるようにするパッケージです。
`CommonMark`に対応しています。
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

```latex
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

## Markdownのフレーバー

| 年 | フレーバー | 概要 | 拡張機能 |
|---|---|---|---|
| 2004 | Markdown | Markdownのオジリナル版 | |
| 2005 | MultiMarkdown | Markdownの拡張版 | 脚注、表、引用、メタデータ、LaTeXのサポート |
| 2006 | Pandoc Markdown | Pandocツール用 | 数式、脚注、スライド作成 |
| 2008 | kramdown | Ruby用 | 表、数式、カスタム要素 |
| 2009 | GitHub Flavored Markdown | GitHub用 | 表、チェックボックス、コードブロック、URLの自動リンク |
| 2014 | CommonMark | Markdownの標準化 | 一貫性と互換性のあるパーサー、多言語対応 |

Markdownから派生／拡張した記法のことを**フレーバー**と呼びます。
フレーバーを年表にしてみましたが、多種多様なことがわかります。

よく知られているのはGitHub Flavored Markdown（GFM）だと思います。
GFMのリリースでMarkdown記法が普及しました。
また、このように多様化したフレーバーの標準化を目指しているのが`CommonMark`です。
近年の拡張はこの`CommonMark`がベースになっています。

:::{seealso}

Markdownのオリジナル作者たちと、
標準化を目指したコミュニティはバチバチのようです。
なので、そのままMarkdownを名乗ることが許されず、
`CommonMark`という別の名前になっているらしいです。

:::
