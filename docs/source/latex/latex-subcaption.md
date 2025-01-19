# 複数画像したい（`subcaption`）

```latex
% プリアンブル
\usepakcage{subcaption}
\subcaptionsetup{%オプション
  % デフォルト値
  margin=0pt,
  font+=smaller,
  labelformat=parens,
  labelsep=space,
  skip=6pt,
  list=false,
  hypcap=false,
}

% 本文
\begin{figure}
  \begin{minipage}{0.45\textwidth}
    \centering
    \includegraphics{example-image.pdf}
    \subcaption{図1のキャプション}
    \label{fig:sub1}
  \end{minipage}
  \hfill
  \begin{minipage}
    \centering
  \end{minipage}
\end{figure}
```

複数の画像を並べたい場合は``subcaption``を使います。

:::{note}

``subfigure``はメンテされていないらしく、
いまは``subcaption``を使うほうがよいみたいです。

:::

## 環境ごとに設定したい

```latex
\subcaptionsetup[環境名]{オプション}

\subcaptionsetup[table]{オプション}
\subcaptionsetup[figure]{オプション}
```
