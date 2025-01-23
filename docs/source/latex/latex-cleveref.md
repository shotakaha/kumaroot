# 相互参照したい（`cleveref`）

```latex
% プリアンブル
\usepackage{cleveref}
% \crefname{環境名}{単数}{複数形}
\crefname{section}{セクション}{セクション}
\crefname{figure}{図}{図}
\crefname{table}{表}{表}

\begin{figure}
  \centering
  \includegraphics[オプション]{ファイル名}
  \caption{キャプション}
  \label{キー}
\end{figure}

図\ref{sec:キー} に示しました。
\cref{sec:label} に示しました。
```

`cleveref`は相互参照の機能を拡張するパッケージです。
標準の[ref](./latex-ref.md)コマンドでは、
ユーザーが「図」「表」など、参照先の環境に合わせて本文中に入力する必要がありました。
`\ref`を`\cref`や`\Cref`コマンドに変えるだけで、その煩わしさから解放されます。

```latex
% プリアンブル
\usepackage{hyperref}
\usepackage{cleveref}
```

[hyperrefパッケージ](./latex-hyperref.md)と一緒に使う場合は、
`hyperref`のあとに読み込みます。

:::{note}

```latex
\usepackage{cleveref}
\usepackage{hyperref}
```

`hyperref`より前に読み込むと、タイプセット時にエラーになります。

:::

## 相互参照カウンター
