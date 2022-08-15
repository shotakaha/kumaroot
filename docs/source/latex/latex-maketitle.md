# 表紙を作成したい（``maketitle``）

タイトル（``\title``）、著者（``\author``）、日付（``\date``）は``\maketitle``の前に書きます。
3つの順番も適当で構いません。

```latex

\title{すごい文書}
\author{すごい著者}
\date{2022年8月1日}

\begin{document}
\maketitle
\end{document}
```

## タイトルを2行にしたい

区切りたい箇所に``\\``を使います。


```latex
\title{すごい長いタイトル \\ 本当に長いタイトルなのです}
```

## 複数の著者名を表示したい

著者名の間に``\and``を使います。

```latex
\author{すごい著者 \and これまたすごい著者}
```

## 作成日を表示したい

LaTeXファイルをコンパイルした日を自動挿入したい場合は``\today``を使います。

```latex
\date{\today}
```
