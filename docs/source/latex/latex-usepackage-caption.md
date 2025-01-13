# キャプションしたい（`caption`）

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

`caption`パッケージで図（figure）や表（table）などのキャプション表示をカスタマイズできます。
このパッケージを使うことで、キャプションの外観や配置、スタイルを細かく制御できます。

ページ全体の設定は`\captionsetup`コマンドを利用します。
詳しい使い方はパッケージのドキュメントを参照してください（`$ texdoc caption`）

## フォントしたい（`font`）

```latex
\captionsetup{
    font = small,
    labelfont = bf,
    % textfont = it,
}
```

`font`オプションでフォントサイズを変更できます。
`labelfont`で図ラベル、
`textfont`でキャプション本体の書体を変更できます。

欧文ではキャプションを斜体（イタリック）にする場合もあるようですが、
和文の場合は斜体にしないほうがよいと思います。

## 余白したい（`skip`）

```latex
\captionsetup{
    width = 0.95\linewidth,
    skip = 10pt,
}
```

`width`オプションでキャプションの横幅を変更できます。
`skip`オプションで、図表とキャプションの間隔を変更できます。

:::{hint}

LaTeXで幅を設定する場合、
ページ幅（`\textwidth`）もしくは、
親環境の幅（`\linewidth`）などを基準にできます。

図表のキャプションは、`figure`や`tabular`などの親環境の幅を基準にしたいため、
このサンプルでは`\linewidth`を使っています。

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

図表のキャプションを個別にカスタマイズしたい場合は、
環境の中で`\captionsetup`します。
