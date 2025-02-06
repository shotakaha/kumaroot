# 表を配置したい（`table`）

```latex
% プリアンブル
\usepackage{tabularray}
\usepackage{caption}

\begin{table}
  \centering
  \caption[短いキャプション][キャプション]
  \begin{tblr}{
    colspec={Q[l]Q[c]Q[r]},
    }
    \toprule
    Alpha & Beta & Gamma\\
    \midrule
    1 & 2 & 3\\
    \bottomrule
    \end{tblr}
\end{table}
```

`table`環境で表を自動配置できます。
表は[tabularrayパッケージ](./latex-tabularray.md)を利用します。
[画像の配置](./latex-figure.md)と同じように[captionパッケージ](./latex-caption.md)が利用できます。

```{toctree}
latex-tabularray
latex-booktabs
```
