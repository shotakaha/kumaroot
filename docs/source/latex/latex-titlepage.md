# 表紙したい（`titlepage`）

```latex
\begin{document}

\begin{titlepage}
  \centering
  \vspace*{3cm}  % 上部のアキを調整
  {\Huge ドキュメントのタイトル} \\[1cm]
  {\LARGE サブタイトル} \\[2cm]
  % ロゴを挿入
  \includegraphics[width=0.4\textwidth]{画像ファイル.jpg} \\[2cm]
  {\Large 名前} \\[1cm]
  {\large 日付} \\[3cm]
  \vfill  % ページ末尾までのアキを自動調整
  {\large 所属名／プロジェクト名}
\end{titlepage}

\end{document}
```

`titlepage`環境でより自由に表紙を設定できます。
`\begin{document}`よりあとに記述します。
文字サイズや改行位置など、すべて自分で設定します。
また、各要素間の間隔もすべて設定が必要です。

## 背景画像したい（`background`）

```latex
\usepackage{background}
\backgroundsetup{
    % 背景画像の設定
    scale=1,
    color=black,
    opacity=0.5,
    angle=0,
    position=current page.south,
    vshift=3cm,
    hsift=3cm,
    contents={\includegraphics[width=\paperwidth]{画像ファイル.jpg}}
}

\begin{document}

\begin{titlepage}
  \centering
  {\Huge 表紙のタイトル}
\end{titlepage}

\end{document}
```

`background`パッケージと`titlepage`環境を組み合わせて、表紙の背景に画像を設定できます。
