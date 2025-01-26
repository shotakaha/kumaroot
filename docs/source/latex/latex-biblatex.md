# 参考文献したい（`biblatex`）

```latex
% プリアンブル
\usepackage[style=authoryear]{biblatex}
% 文献リストを読み込む
\addbibresource{文献リスト1.bib}
\addbibresource{文献リスト2.bib}

\begin{document}

本文中で文献を参照する\cite{参照キー}。

% 本文の末尾
\printbibliography[title={参考文献}]

\end{document}
```

`biblatex`は参考文献を出力するパッケージです。
`Biber`と組み合わせて使うことが推奨されています。

`\addbibresource`コマンドで、文献リストのファイルを読み込みます。
文献リストは複数指定できます。

`\cite`コマンドで、本文中で文献を参照し、`\printbibliography`で出力します。
`title`オプションで、見出しを変更できます。
デフォルトは「Bibliography」になっています。

:::{note}

`Biber`は、従来のBibTeXの代替として設計されたツールです。
`BibTeX`形式のファイルをそのまま読み込んだり、
ソートやフィルタリング機能が利用できたり、
Unicodeが完全サポートされていたりと
より簡単＆柔軟な利用が可能になっています。

:::

## 参照スタイルしたい

```latex
\usepackage[style=numeric]{biblatex}  % デフォルト
\usepackage[style=authoryear]{biblatex}
```

`style`オプションで、参照スタイルを変更できます。
利用可能な設定値は`$ texdoc biblatex`でドキュメントを確認してください。

## BibTeXしたい

```latex
\usepackage[backend=biber]{biblatex}  % デフォルト
\usepackage[backend=bibtex]{biblatex}
```

`backend=bibtex`オプションで、従来のBibTeXを利用できます。
