# 表紙したい（`titlepage`）

```latex
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
```

`titlepage`環境で、`\maketitle`より自由に表紙を設定できます。
