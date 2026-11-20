# 参考文献したい（`thebibliography`）

```latex

% 本文
〜については〇〇である\cite{文献キー}。

% 本文の末尾
% 「参考文献」という見出しは自動で挿入される
\begin{thebibliography}{99}
\bibitem{文献キー} 著者名, 『タイトル』, 出版社, 出版年
\bibitem{fukagawa2021} 深川峻太郎, 『アインシュタイン方程式を読んだら「宇宙」がみえた - ガチンコ相対性理論』, 講談社, 2021年5月21日
\end{thebibliography}
```

`thebibliography`環境で、参考文献リストを作成できます。
`\begin{thebibliography}{99}`の引数は、文献番号の表示幅を示す文字列です。
例えば`99`は、文献番号が2桁までであることを表します。
`\bibitem`で参考文献ごとにキーを設定し、文献情報を入力します。
文献キーは、文書中で一意になるようにします。
手動で作成する場合は「著者名＋出版年」（例：`fukagawa2021`）のような形にするとよいです。

このキーを`\cite`コマンドで参照すると、
文献リストを生成するときに自動で採番してくれます。
ただし、`\cite`の番号は2回コンパイルしないと確定しません。

詳細は[Bibliography management in LaTeX - Overleaf](https://www.overleaf.com/learn/latex/Bibliography_management_in_LaTeX)が参考になります。
`bibtex`、`natbib`、`biblatex`を使う方法がそれぞれ説明されています。

:::{hint}

この方法は、参考文献の数が少ないときに有効です。
文献数が増えてきたら[bib形式ファイル](./latex-bib.md)で管理するほうが確実です。
文献キーも一意のものを生成してくれます。

:::
