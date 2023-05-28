# PDFしたい（``make latexpdf``）

```console
$ make latex
$ make latexpdf
```

PDFを生成するときは``make latexpdf``を実行します。
生成したファイルは{file}`build/latex/`に出力されます。

## LaTeXファイルを生成したい（``make latex``）

```console
$ make latex
$ less build/latex/kumaroot.tex
```

``make latex``でコンパイルせずにLaTeXファイルだけを生成できます。
新しいLaTeXパッケージを追加したあとなどに、PDFファイルの生成がうまくいかない場合は、まずLaTeXファイルを生成し、その内容を直接確認したほうが原因が早く見つかる場合があります。

```{note}
PDFファイルを生成する場合、ビルドするパソコンでLaTeX環境を整えておく必要があります。
詳しくは[](../latex/latex-usage.md)を参照してください。
```

## リファレンス

- [LaTeX出力のオプション](https://www.sphinx-doc.org/ja/master/usage/configuration.html#options-for-latex-output)
- [LaTeXのカスタマイズ](https://www.sphinx-doc.org/ja/master/latex.html)
