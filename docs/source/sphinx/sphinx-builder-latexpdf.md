# PDFを生成したい（``make latexpdf``）

```bash
$ make latex
$ make latexpdf
$ make latexpdfja
```

PDFを生成するときは{command}`make latexpdf`を実行します。
生成したファイルは{file}`build/latex/`以下に出力されます。

```bash
$ cd $KUMAROOT
$ make latexpdf
$ open build/latex/kumaroot.pdf
```

新しくパッケージを追加したあとに、PDF生成がうまくいかない場合は、LaTeX文書を直接確認したほうが原因が早く見つかる場合があります。
{command}`make latex`でコンパイルせずにLaTeX文書を作成できます。

```bash
$ cd $KUMAROOT
$ make latex
$ less build/latex/kumaroot.tex
```



```{note}
PDFを生成する場合、ビルドするパソコンでLaTeX環境を整えておく必要があります。
詳しくは[](../latex/latex-usage.md)を参照してください。
```

```{toctree}
---
maxdepth: 1
---
sphinx-latex-engine
sphinx-latex-docclass
sphinx-latex-elements
sphinx-latex-preamble
sphinx-latex-logo
sphinx-latex-section
sphinx-latex-thesection
```

```{toctree}
---
maxdepth: 1
caption: 設定例
---
sphinx-latex-lualatex
sphinx-latex-uplatex
```

## リファレンス

- [LaTeX出力のオプション](https://www.sphinx-doc.org/ja/master/usage/configuration.html#options-for-latex-output)
- [LaTeXのカスタマイズ](https://www.sphinx-doc.org/ja/master/latex.html)
