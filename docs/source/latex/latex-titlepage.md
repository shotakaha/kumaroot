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

`titlepage`環境で表紙をカスタマイズできます。
`\begin{document}`よりあとに記述します。
文字サイズや改行位置など、すべて自分で設定します。
また、`vspace`や`vfill`などを使って縦方向の間隔もすべて設定が必要です。

## 水平線したい（`\rule`）

```latex
\begin{titlepage}
  \centering
  \vspace*{3cm}  % 上部のアキを調整
  %
  \rule{\textwidth}{5pt} \\[1cm]
  {\Huge ドキュメントのタイトル} \\[1cm]
  {\LARGE サブタイトル} \\[1cm]
  \rule{\textwidth}{5pt} \\[2cm]
  % ロゴを挿入
  \includegraphics[width=0.4\textwidth]{画像ファイル.jpg} \\[2cm]
  {\Large 名前} \\[1cm]
  {\large 日付} \\[3cm]
  \vfill  % ページ末尾までのアキを自動調整
  {\large 所属名／プロジェクト名}
\end{titlepage}
```

タイトルとサブタイトルが目立つように
`\rule`コマンドで上下に水平線を追加してみました。

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

`background`パッケージと`titlepage`環境を組み合わせて、
表紙の背景に画像を設定できます。
