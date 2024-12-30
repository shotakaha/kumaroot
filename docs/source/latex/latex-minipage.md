# ページ分割したい（`minipage`）

```latex
\begin{minipage}[揃える方向]{幅}
\end{minipage}
```

`minipage`環境で、1つのページを複数の領域に分割できます。
コンテンツを揃える方向をオプションで指定します。
一段の幅は`\textwidth`を基準に指定するとよいです。

```latex
\noindent  % インデントを削除
\begin{minipage}[t]{0.45\textwidth}
左側の内容
\end{minipage}
\hfill  % ミニページ間のスペースを自動調整
\begin{minipage}[t]{0.45\textwidth}
右側の内容
\end{minipage}
```

`\noindent`を使うと、左段の余白を揃えることができます。
`\hfill`で段の間の余白を自動調整できます。
