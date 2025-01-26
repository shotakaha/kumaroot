# 参考文献したい（`bibtex`）

:::{note}

このページは従来のBibTeXを使った方法です。
新しく文書作成する場合は
[biblatex](./latex-biblatex.md)の利用をオススメします。

:::

```latex
% 参考文献の表示形式を設定
\bibliographystyle{plain}

% 参考文献.bibを読み込む
\bibliography{参考文献}

% 本文の末尾
\printbibliography
```

`BibTeX`を使って参考文献を生成する方法です。
表示形式は`.bst`ファイルで定義されています。

## 表示形式したい（`\bibliographystyle`）

```latex
\bibliographystyle{plain}
```

`\bibliographystyle`コマンドで、表示形式を変更できます。
表示形式は`スタイル名.bst`で定義されています。

```console
$ kpsewhich plain.bst
/usr/local/texlive/2024/texmf-dist/bibtex/bst/base/plain.bst

$ cat /usr/local/texlive/2024/texmf-dist/bibtex/bst/base/plain.bst
```

[kpsewhich](./latex-kpsewhich.md)で`スタイル名.bst`を検索してパスを確認できます。
このファイルの内容を直接確認すると、表示される内容が（なんとなく）分かります。

:::{caution}

```latex
! Package biblatex Error:
 '\bibliographystyle' invalid
 for 'biblatex'.
```

`\bibliographystyle`コマンドは
[biblatexパッケージ](./latex-biblatex.md)と一緒には使えませんでした。


:::
