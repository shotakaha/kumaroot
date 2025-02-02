# 見出ししたい（`titlesec`）

```latex
% プリアンブル
\usepackage[オプション]{titlesec}
\titleformat{コマンド名}[shape]{フォーマット}{番号ラベル}{区切り}{before-code}[after-code]

```

`titlesec`パッケージで見出しをカスタマイズできます。
`\titleformat{}`を使って、それぞれの見出しコマンドをカスタマイズできます。

コマンド名には
`\part`（article）、
`\chapter`（reportとbook）、
`\section`、`\subsection`、`\subsubsection`、
`\paragraph`、`\subparagraph`を指定できます。

`shape`は`titlesec`で定義されている表示スタイルです。

番号ラベルは`\thesection`などを設定します。
区切りは`1em`などの長さで指定します
`before-code`、`after-code`は必要であれば設定します。

## 章ごとに改ページしたい

```latex
\titleformat{\section}{\newpage\ebseries\Large}{\thesection}{0.1em}
% コマンド名: \section
% フォーマット: \newpage（改ページ） \ebseries（極太） \Large（大きく）
% 番号ラベル : \thesection
% ラベルとタイトルのアキ: 1em
% before-script: なし
```

フォーマットに`\newpage`を追加することで、
`\section{}`ごとに改ページできます。
