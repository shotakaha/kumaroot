# 箇条書きしたい（``enumitem``）

箇条書きするために``itemize``、``enumerate``、``description``の3つの環境があります。
それらを使いやすくする``enumitem``パッケージがあります。

## リストしたい（``itemize``）

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

順序のない箇条書きは``itemize``環境を使います。
``itemize``環境はレベル4まで入れ子にできます。

## リストの見出し記号を変更したい

```latex
\begin{itemize}
    \item レベル1 - リスト1
    \item レベル1 - リスト2
    \item[★] レベル1 - リスト3
\end{itemize}
```

箇条書きの記号は``\item``のオプションで一時的に変更できます。

## リストの見出し記号をまとめて変更したい（``\labelitemi``）

```latex
\renewcommand{\labelitemi}{・}    % レベル1
\renewcommand{\labelitemii}{・}   % レベル2
\renewcommand{\labelitemiii}{・}  % レベル3
\renewcommand{\labelitemiv}{・}   % レベル4
```

リストの見出し記号は``\labelitemi``を再定義することでまとめて変更できます。
レベルごとに記号を設定でき、
レベル1は``\labelitemi``、
レベル2は``\labelitemii``、
レベル3は``\labelitemiii``、
レベル4は``\labelitemiv``、
を使って変更できます。

## 順序リストしたい（``enumerate``）

```latex
\begin{enumerate}
    \item 順序ありリスト1
    \item 順序ありリスト2
    \item 順序ありリスト3
\end{enumerate}
```

順序がある箇条書きは``enumerate``環境を使います。
``enumerate``環境はレベル4まで入れ子にできます。

## 順序リストの記号をまとめて変更したい（``\labelenumi``）

```latex
\renewcommand{\labelenumi}{（\arabic{\theenumi}）}      % レベル1: 1. -> （1）
\renewcommand{\labelenumi}{（\roman{\theenumii}）}     % レベル2: (a) -> （i）
\renewcommand{\labelenumiii}{（\roman{\theenumiii}）}  % レベル3: i. -> （i）
\renewcommand{\labelenumiv}{（\roman{\theenumiv}）}    % レベル4: A. -> （i）
```

順序リストの見出しは``\labelenumi``を再定義することでまとめて変更できます。
順序の数値は``\theenumi``に入っています。
レベルごとに記号を設定でき、
レベル1は``\labelenumi``と``\theenumi``、
レベル2は``\labelenumii``と``\theenumii``、
レベル3は``\labelenumiii``と``\theenumiii``、
レベル4は``\labelenumiv``と``\theenumiv``、
を使って変更できます。

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