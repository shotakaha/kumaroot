# キャプションしたい（``caption``）

```latex
%% プリアンブル
\usepackage{caption}
\captionsetup{
    format = hang,
    font = small,  %% footnotesize / scriptsize
    labelfont = bf,
    singlelinecheck=false,
    width=0.95\linewidth,
}

%% 本文
\begin{figure}
  \centering
  \includegraphics[width=0.8\linewidth]{ファイル名}
  \caption{図のキャプション。デフォルトだと行幅いっぱいに表示される。}
\end{figure}
```

``caption``パッケージを使って画像キャプションの表示を変更できます。
``\captionsetup``で、本文中のキャプションを一括設定できます。
キャプションのフォントのサイズを、本文より小さくしたり、図番号からキャプションを字下げしたり、図番号のみ太字にしたりできます。
詳しくは``$ texdoc caption``して設定オプションを確認してください。

:::{hint}

LaTeXで幅を設定する場合``\textwidth``もしくは``\linewidth``を基準にすることが多いです。
個人的に図のキャプションは、画像の幅よりも狭くしたい派なので、``\linewidth``を基準にしています。

:::

## 個別設定したい

```latex
\usepackage{caption}

\begin{figure}
    \centering
    \captionsetup{width=0.8\linewidth}
    \includegraphics[width=0.9\linewidth]{ファイル名}
    \caption{図のキャプション}
\end{figure}
```

``figure``環境の中で``\captionsetup``して、個別で設定できます。
