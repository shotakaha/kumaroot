# LaTeXの設定

PDFを生成するために``LaTeX``の設定をします。

```{toctree}
---
maxdepth: 1
---
sphinx-latex-engine
sphinx-latex-docclass
sphinx-latex-elements
sphinx-latex-preamble
sphinx-latex-sectioning
```

## 表紙の設定（ ``latex_logo`` ）

表紙にロゴを挿入することもできます。
必要ないなら``None``（デフォルト値）のままで問題ありません。

```python
# The name of an image file (relative to this directory)
# to place at the top of the title page.
latex_logo = './images/toumin_kuma.png'
```

## 設定例

```{toctree}
sphinx-latex-lualatex
sphinx-latex-uplatex
```
