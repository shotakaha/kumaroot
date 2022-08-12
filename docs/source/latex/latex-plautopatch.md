# plautopatch

日本語でLaTeXする場合は、ファイルの先頭で必ず読み込んでおくとよいパッケージです。
pLaTeXやupLaTeXと非互換性があるパッケージを読み込んでしまった場合に、
その衝突を解消できるパッケージを自動で読み込んでくれます。
衝突したパッケージ名の一覧は、実行結果の中で確認できます。

```latex
%\RequirePackage{plautopatch}
\documentclass{jsarticle}

% プリアンブル

% コンテンツ
\begin{document}

\end{document}
```
