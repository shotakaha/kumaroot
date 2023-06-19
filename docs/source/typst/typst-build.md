```{eval-rst}
.. index::
    pair: ビルドしたい; Typst
```

# タイプセットしたい

```console
$ typst compile 入力ファイル名.typ
$ typst compile 入力ファイル名.typ 出力ファイル名.pdf
```

``compile``コマンドを使ってPDFファイルを生成できます。

:::{seealso}

- [](../latex/latex-latexmk.md)
- [](../sphinx/sphinx-build.md)

:::

```{eval-rst}
.. index::
    pair: プレビューしたい; Typst
```

## ライブプレビューしたい

```console
$ typst watch 入力ファイル名.typ
$ typst watch 入力ファイル名.typ 出力ファイル名.pdf
```

``watch``コマンドを使ってライブプレビューできます。

:::{seealso}

- [](../latex/latex-latexmk.md)
- [](../sphinx/sphinx-autobuild.md)

:::
