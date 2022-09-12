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
```

```{toctree}
---
maxdepth: 1
caption: 設定例
---
sphinx-latex-lualatex
sphinx-latex-uplatex
```
