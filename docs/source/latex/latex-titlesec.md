# 見出ししたい（`titlesec`）

```latex
% プリアンブル
\usepackage[オプション]{titlesec}

\titleformat{コマンド名}[shape]{フォーマット}{番号ラベル}{区切り}{before-code}[after-code]
```

`titlesec`パッケージで見出しをカスタマイズできます。
`\titleformat{}`を使って、それぞれの見出しコマンドをカスタマイズできます。
パッケージのドキュメントの補遺にサンプルが載っています（`$ texdoc titlesec`）
そこを読むと使い方がよくわかると思います。

## 枠付きにしたい（`frame`）

```latex
\titleformat{\section}[frame]
    % 全体：デフォルトフォント
    {\normalfont}
    % 番号ラベル：左寄せ
    {\filright \footnotesize \enspace 第 \thesection 章 \enspace}
    {1em}
    % 見出し：中央寄せ
    {\Large\bfseries\filcenter}
```

`frame`スタイルを使って見出しに枠を追加できます。

## 線付きにしたい（`\titlerule`）

```latex
\titleformat{\section}
    {\titlerule
        \vspace{0.5em}%
        \normalfont
        \vspace{0.5em}%
      \titlerule}
    {第 \thesection 章}
    {1em}
    {\Large}
```

`\titlerule`で水平線を追加できます。
見出しの上下に水平線を追加しました。

## 見出しラベルしたい（`\titlelabel`）

```latex
% プリアンブル
% デフォルト（ラベル タイトル）
\titlelabel{\thetitle\quad}

% ラベル. タイトル
\titlelabel{\thetitle.\quad}
```

`\titlelabel{}`で見出しラベルを一括で変更できます。
`\thetitle`は、
節番号（`\thesection`）、
項番号（`\thesubsection`）など、
見出しのレベルに応じたコマンドです。

## 改ページしたい（`\sectionbreak`）

```latex
\titleformat{\section}
    {\newpage\ebseries\Large}
    {\thesection}
    {0.1em}
% コマンド名: \section
% フォーマット: \newpage（改ページ） \ebseries（極太） \Large（大きく）
% 番号ラベル : \thesection
% ラベルとタイトルのアキ: 1em
% before-script: なし
```

フォーマットに`\newpage`を追加することで、
`\section{}`ごとに改ページできます。

```latex
\newcommand{\sectionbreak}{\clearpage}
```

`\sectionbreak`コマンドを定義し、
`\clearpage`などの改行コマンドを割り当てても、
同様のことができます。

## 標準タイトルしたい（`\chapter`）

```latex
\titleformat{\chapter}[display]
    {\normalfont\huge\bfseries}
    {\chaptertitlename\ \thechapter}
    {20pt}
    {\Huge}

\titlespacing*{\chapter}
    {0pt}
    {50pt}
    {40pt}
```

## 標準タイトルしたい（`\section`）

```latex
\titleformat{\section}
    {\normalfont\Large\bfseries}
    {\thesection}
    {1em}
    {}

\titlespacing*{\section}
    {0pt}
    {3.5ex plus 1ex minux .2ex}
    {2.3ex plus .2ex}
```

## 標準タイトルしたい（`\subsection`）

```latex
\titleformat{\subsectoin}
    {\normalfont\large\bfseries}
    {\thesubsection}
    {1em}
    {}

\titlespacing*{\subsection}
    {0pt}
    {3.25ex plus 1ex minus .2ex}
    {1.5ex plus .2ex}
```

## 標準タイトルしたい（`\subsubsection`）

```latex
\titleformat{\subsubsection}
    {\normalfont\normalsize\bfseries}
    {\thesubsubsection}
    {1em}
    {}

\titlespacing*{\subsubsection}
    {0pt}
    {3.25ex plus 1ex minus .2ex}
    {1.5ex plus .2ex}
```

## 標準タイトル（`\paragraph`）

```latex
\titleformat{\paragraph}[runin]
    {\normalfont\normalsize\bfseries}
    {\theparagraph}
    {1em}
    {}

\titlespacing*{\paragraph}
    {0pt}
    {3.25ex plus 1ex minus .2ex}
    {1em}
```

## 標準タイトルしたい（`\subparagraph`）

```latex
\titleformat{\subparagraph}[runin]
    {\normalfont\normalsize\bfseries}
    {\thesubparagraph}
    {1em}
    {}

\titlespacing*{\subparagraph}
    {\parindent}
    {3.25ex plus 1ex minus .2ex}
    {1em}
```
