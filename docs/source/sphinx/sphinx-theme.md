# 各種ビルダーを設定する

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
sphinx-latex
sphinx-latex-lualatex
sphinx-latex-uplatex
```
