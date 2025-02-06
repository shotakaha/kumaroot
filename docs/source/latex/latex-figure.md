# 画像を配置したい（`figure`）

```latex
% プリアンブル
\usepackage{graphicx}
\usepackage{float}
\usepackage{caption}

\begin{figure}[H]
  \centering
  \includegraphics[オプション]{ファイル名}
  \caption[短いキャプション]{図の説明}
\end{figure}
```

`figure`環境で画像を自動配置できます。
画像は[graphicxパッケージ](./latex-graphicx.md)で挿入します。
[floatパッケージ](./latex-float.md)で場所を指定して出力できます。
[captionパッケージ](./latex-caption.md)でキャプションをカスタマイズできます。

その他画像に関係するパッケージを以下に整理しました。

```{toctree}
latex-graphicx
latex-caption
latex-subcaption
latex-mwe
```
