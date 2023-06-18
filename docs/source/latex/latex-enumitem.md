# 箇条書きしたい（``enumitem``）

```latex
%% プリアンブル
\usepackage{enumitem}

%% 本文
\begin{itemize}[labelsep=1\zw]
    \item 項目1
    \item 項目2
\end{itemize}
```

箇条書きするためのデフォルト環境は``itemize``、``enumerate``、``description``の3つあります。
それらをカスタマイズできる``enumitem``パッケージを使います。

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

**順序のない**箇条書きは``itemize``環境を使います。
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

**順序がある**箇条書きは``enumerate``環境を使います。
``enumerate``環境はレベル4まで入れ子にできます。

## 順序リストの記号をまとめて変更したい（``\labelenumi``）

```latex
\renewcommand{\labelenumi}{\arabic{enumi}.}    % レベル1: 1. -> 1.
\renewcommand{\labelenumii}{\arabic{enumi}.\arabic{enumii}.}     % レベル2: (a) -> 1.1.
\renewcommand{\labelenumiii}{\arabic{enumi}.\arabic{enumii}.\arabic{enumiii}.}  % レベル3: i. -> 1.1.1.
\renewcommand{\labelenumiv}{\arabic{enumi}.\arabic{enumii}.\arabic{enumiii}.\arabic{enumiv}.}    % レベル4: A. -> 1.1.1.1.
```

順序リストの見出しは``\labelenumi``を再定義することでまとめて変更できます。
順序の数字のカウンターは``enumi``に入っています。
レベルごとに記号を設定でき、
レベル1は``\labelenumi``と``enumi``、
レベル2は``\labelenumii``と``enumii``、
レベル3は``\labelenumiii``と``enumiii``、
レベル4は``\labelenumiv``と``enumiv``、
を使って変更できます。

## 説明書きしたい（``description``）

```latex
\begin{description}
    \item[ラベル1] 説明1
    \item[ラベル2] 説明2
    \item[ラベル3] 説明3
\end{enumerate}
```
