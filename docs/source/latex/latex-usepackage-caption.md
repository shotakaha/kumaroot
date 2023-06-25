# キャプションしたい（``caption``）

```latex
%% プリアンブル
\usepackage{caption}
\captionsetup{
    format = hang,
    font = small,  %% footnotesize / scriptsize
    labelfont = bf,
    singlelinecheck=false,
    width=0.8\linewidth,
}

%% 本文
\begin{figure}
  \centering
  \includegraphics[width=0.8\linewidth]{ファイル名}
  \caption{図のキャプション。デフォルトだと行幅いっぱいに表示される。}
\end{figure}
```

``caption``パッケージを使って画像キャプションの表示を変更できます。
キャプションのフォントのサイズを、本文より小さくしたり、図番号からキャプションを字下げしたり、図番号のみ太字にしたりできます。

パッケージオプションでも設定できますが、``\captionsetup``を使ったほうが設定が読みやすいと思います。
詳しくは``$ texdoc caption``して設定オプションを確認してください。
