```{eval-rst}
.. index::
    pair: ビルドしたい; Typst
```

# タイプセットしたい（``typst compile``）

```console
$ typst compile 入力ファイル名.typ
$ typst compile 入力ファイル名.typ 出力ファイル名.pdf
```

``typst compile``コマンドを使ってTypstファイル（``.type``）をPDFファイル（``*.pdf``）にコンパイルします。
組版システムではコンパイルのことをタイプセットと呼びます。

:::{seealso}

- [](../latex/latex-latexmk.md)
- [](../sphinx/sphinx-build.md)

:::

```{eval-rst}
.. index::
    pair: Preview; Typst
```

## ライブプレビューしたい（``typst watch``）

```console
$ typst watch 入力ファイル名.typ
$ typst watch 入力ファイル名.typ 出力ファイル名.pdf
```

``watch``コマンドを使ってライブプレビューできます。

:::{seealso}

- [](../latex/latex-latexmk.md)
- [](../sphinx/sphinx-autobuild.md)

:::
