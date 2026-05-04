```{eval-rst}
.. index::
    pair: ビルドしたい; Typst
```

# タイプセットしたい（``typst compile``）

```console
$ typst compile 入力ファイル名.typ  // -> 入力ファイル名.pdf
$ typst compile 入力ファイル名.typ 出力ファイル名.pdf

// プロジェクトルートを指定
$ typst compile --root .. 入力ファイル名.typ 出力ファイル名.pdf
```

`typst compile`コマンドでTypstファイル（`.type`）をPDFファイル（`*.pdf`）にコンパイルします。
`--root`オプションでプロジェクトルートを指定できます。
カレントディレクトリにないファイルを`#import`していたり、`#include`していたりする場合は、プロジェクトルートの指定が必要です。

```console
$ mkdir -p /tmp/typst-PROJECT/
$ typst compile --root .. 入力ファイル名.pdf /tmp/typst-PROJECT/出力ファイル名.pdf
```

Git管理しているリポジトリにPDFファイルが散らかるのを避けるため、
`/tmp/typst-PROJECT/`に一時ディレクトリを作成して、
出力するようにしています。

:::{note}

組版システムではコンパイルのことをタイプセットと呼びます。

:::

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
