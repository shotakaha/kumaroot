# 参考文献したい（``thebibliography``）

```latex
\begin{thebibliography}{文献番号の最大値}
\bibitem{参照キー} 深川峻太郎『アインシュタイン方程式を読んだら「宇宙」がみえた - ガチンコ相対性理論』講談社（2021年5月21日）
\end{thebibliography}
```

参考文献をリストする場合は``thebibliography``環境を使います。
``\item``の代わりに``\bibitem``を使うことで、参照番号の採番をパソコンにまかせて自動化できます。

詳細は[Bibliography management in LaTeX - Overleaf](https://www.overleaf.com/learn/latex/Bibliography_management_in_LaTeX)が参考になります。
``bibtex``、``natbib``、``biblatex``を使う方法がそれぞれ説明されていて、その中で``biblatex``がオススメされています。



## 文献リストしたい

```bib
@文献の種類{参照キー,
    キー = {値},
}
```

文献リストが多い場合、LaTeX文書内に手入力するのはなかなか大変です。
そのような時は``.bib``ファイルを作成してまとめておくのがよいです。

### 書籍を参照したい（``@book``）

```bibtex
@book{参照キー1,
    author = {},
    publisher = {},
    title =  {},
    year = {},
    address = {},
    edition = {},
    month = {},
    note = {}
    number = {},
    series = {},
    month = {},
    volume = {},
}
```

書籍を参照する場合``@book``を使います。
必要な項目は``author``、``title``、``publisher``、``year``です。
オプションで``volume``、``number``、``series``、``address``、``edition``、``month``、``note``を設定できます。
