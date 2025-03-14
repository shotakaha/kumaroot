# 参考文献したい（`thebibliography`）

```latex

% 本文
〜については〇〇である\cite{文献キー}。

% 本文の末尾
% 「参考文献」という見出しは自動で挿入される（はず）
\begin{thebibliography}{文献数の最大値}
\bibitem{文献キー} 著者名, "タイトル", 出版社, 出版年
\bibitem{fukagawa2021} 深川峻太郎『アインシュタイン方程式を読んだら「宇宙」がみえた - ガチンコ相対性理論』講談社（2021年5月21日）
\end{thebibliography}
```

`thebibliography`環境で、参考文献リストを作成できます。
`\bibitem`で参考文献ごとにキーを設定し、文献情報を入力します。
文献キーは、文書中で一意になるようにします。
手動で作成する場合は「著者名／実験名_出版年」のような形にするとよいです。

このキーを`\cite`コマンドで参照すると、
文献リストを生成するときに自動で採番してくれます。

詳細は[Bibliography management in LaTeX - Overleaf](https://www.overleaf.com/learn/latex/Bibliography_management_in_LaTeX)が参考になります。
``bibtex``、``natbib``、``biblatex``を使う方法がそれぞれ説明されていて、その中で``biblatex``がオススメされています。

:::{hint}

この方法は、参考文献の数が少ないときに有効です。
文献数が増えてきたら[bib形式ファイル](./latex-bib.md)で管理するほうが確実です。
文献キーも一意のものを生成してくれます。

:::
