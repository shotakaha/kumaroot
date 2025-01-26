# ページ分割したい（`minipage`）

```latex
\begin{minipage}[揃える方向]{段幅}
\end{minipage}
```

`minipage`環境で、1つのページを複数の領域に分割できます。
コンテンツを揃える方向と段幅の指定が必要です。
一段の幅は`\textwidth`を基準に指定するとよいです。

`minipage`を使うと
左右に図版を並べたり、
左に図、右に説明テキストを配置したり、
左にソースコード、右に出力結果を配置したり、
などがお手軽に実現できます。

```latex
\noindent  % 文頭のインデントを削除
\begin{minipage}[t]{0.45\textwidth}
左段の内容
\end{minipage}
\hfill  % 段間（ミニページ間の間隔）を自動調整
\begin{minipage}[t]{0.45\textwidth}
右段の内容
\end{minipage}
```

`\noindent`で文頭のインデントを削除して左段の余白に揃えることができます。
`\hfill`で段間を自動調整できます。

:::{note}

より多くの段を作る場合は`multicol`パッケージや`paracol`パッケージを使う方がよいかもしれません。

:::
