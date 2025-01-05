# ローカルスコープしたい（`\begingroup` / `\endgroup`）

```latex
\begingroup
%局所的な設定
\endgroup
```

`\begingroup`、`\endgroup`でローカルスコープを定義できます。
ドキュメント内で行間やフォントを局所的に設定したり、
自作したコマンド／環境内に変更を留めたりできます。

```latex
\begin{document}

通常のテキスト。通常のテキスト。通常のテキスト。通常のテキスト。通常のテキスト。

\begingroup
\Large
一時的に大きなフォントサイズのテキスト。一時的に大きなフォントサイズのテキスト。一時的に大きなフォントサイズのテキスト。
\endgroup

通常のテキスト。通常のテキスト。通常のテキスト。通常のテキスト。通常のテキスト。

\end{document}
```

`\Large`のような閉じ括弧のないコマンドは、閉じるのを忘れてしまいがちです。
`\begingroup`と`\endgroup`で囲むことで回避できます。

```latex
%% プリアンブル
\usepackage{xcolor}

\newcommand{\colorcommand}[2]{%
  % Usage: \colorcommand{#1}{#2}
  %    #1: テキストの色
  %    #2: テキスト
  \begingroup
  \color{#1}
  #2
  \endgroup
}

%% 本文
\begin{document}

通常の文字色のテキスト。通常の文字色のテキスト。通常の文字色のテキスト。

\colorcommand{red}{ここだけ赤色のテキスト。}

通常の文字色のテキスト。通常の文字色のテキスト。通常の文字色のテキスト。

\end{document}
```

ローカルスコープは`\newcommand`の中でも利用できます。
