# 参考文献したい（`biblatex`）

```latex
\usepackage[style=authoryear]{biblatex}
\addbibresource{文献リスト.bib}

\begin{document}

\printbibliography

\end{document}
```

`biblatex`は参考文献を出力するパッケージです。
`Biber`と組み合わせて使うことが推奨されています。

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
