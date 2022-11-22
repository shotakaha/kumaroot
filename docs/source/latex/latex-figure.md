# 画像を配置したい（``figure``）

```latex
\begin{figure}[配置オプション]
\includegraphics[図のオプション]{画像ファイル名}
\caption{画像のキャプション}
\end{figure}
```

``\includegraphics``コマンドで挿入した画像を、``figure``環境を使ってページ内に配置します。
``\caption``コマンドで画像のキャプションを追加できます。

## 画像を指定した場所に置きたい

```latex
\begin{figure}{h} % here
...
\end{figure}
```

配置オプションのは``h / t / b / p``から選択できます。
デフォルトは``[tbp]``になっています。
