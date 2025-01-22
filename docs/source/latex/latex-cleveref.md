# 相互参照したい（`cleveref`）

```latex
\usepackage{cleveref}

\section{見出しを参照}
\label{sec:label1}

相互参照を \ref{sec:label}章 に整理しました。
相互参照を \cref{sec:label} に整理しました。
```

標準の[ref](./latex-ref.md)コマンドでは、
ユーザーが「図」「表」など、参照先に合わせて本文中に入力する必要がありました。

`cleveref`パッケージに含まれる、`\cref`、`\Cref`コマンドを使うと、
自動で判別してくれます。
