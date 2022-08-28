# 分割したファイルを読み込みたい

```latex
\begin{document}

\include{cover}       % cover.tex を読み込む
\include{chapter/01}  % chapter/01.tex を読み込む
\include{chapter/02}  % chapter/02.tex を読み込む

\end{document}
```

修論や博論を作成する場合、章ごとにファイルを分割しておくと修正作業が捗ります。
分割したファイルはドキュメントクラスやプリアンブルの設定は不要です。
