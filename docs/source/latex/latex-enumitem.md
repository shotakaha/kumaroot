# 箇条書きしたい（``enumitem``）

箇条書きするための環境は``itemize``、``enumerate``、``description``の3つの環境があります。
また、それらをさらに使いやすく拡張する``enumitem``パッケージがあります。

## 箇条書きしたい（``itemize``）

```latex
\begin{itemize}
    \item レベル1 - リスト1
    \begin{itemize}
        \item レベル2 - リスト1
        \item レベル2 - リスト2
        \item レベル2 - リスト3
    \end{itemize}
    \item レベル1 - リスト2
    \item レベル1 - リスト3
\end{itemize}
```

箇条書きは``itemize``環境を使います。
``itemize``環境は（レベル4まで）入れ子にできます。

## ラベルを部分的に変更したい

```latex
\begin{itemize}
    \item レベル1 - リスト1
    \item レベル1 - リスト2
    \item[★] レベル1 - リスト3
\end{itemize}
```

箇条書きのラベルは``\item``のオプションで部分的に変更できます。

## ラベルをまとめて変更したい（``\labelitemi``）

```latex
\renewcommand{\labelitemi}{・}
\renewcommand{\labelitemii}{・}
\renewcommand{\labelitemiii}{・}
\renewcommand{\labelitemiv}{・}
```

箇条書きのラベルは``\labelitemi``を再定義することでまとめて変更できます。
レベル1は``\labelitemi``、
レベル2は``\labelitemii``、
レベル3は``\labelitemiii``、
レベル4は``\labelitemiv``、
で変更できます。

## 順序あり箇条書きしたい（``enumerate``）

```latex
\begin{enumerate}
    \item 順序ありリスト1
    \item 順序ありリスト2
    \item 順序ありリスト3
\end{enumerate}
```

順序をつけた箇条書きは``enumerate``環境を追加います。

## 説明書きしたい（``description``）

```latex
\begin{description}
    \item[ラベル1] 説明1
    \item[ラベル2] 説明2
    \item[ラベル3] 説明3
\end{enumerate}
```

## 箇条書きしたい（``enumitem``）

```latex
\usepackage{enumitem}
```
