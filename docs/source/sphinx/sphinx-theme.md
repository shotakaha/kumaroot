# 各種ビルダーを設定したい

```bash
$ make help
```

{command}`make help`コマンドで、利用可能なビルダーを確認できます。
それぞれのビルダーの基本設定はすべて{file}`conf.py`にまとめて記述します。

## ウェブの設定

```bash
$ make html
$ make dirhtml
$ make singlehtml
```

HTMLを生成するには、テーマの設定が必要です。
デフォルトは``alabaster``に設定されています。
僕は``sphinx_rtd_theme``をよく使っています。

テーマごとに設定オプションが異なるので、詳細はテーマの公式ドキュメントを参照してください。

```{note}
Sphinxのテーマなので、Sphinxドキュメントで生成されています。
ソースコードを読むだけでもとても参考になります。
```

```{toctree}
---
maxdepth: 1
---
sphinx-html-rtd
sphinx-html-bootstrap
```

## LaTeXの設定

```bash
$ make latex
$ make latexpdf
$ make latexpdfja
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
