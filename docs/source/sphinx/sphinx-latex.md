# LaTeXの設定

PDFを生成するために``LaTeX``の設定をします。

## LaTeXエンジンを設定する（``latex_engine``）

```python
latex_engine = "lualatex"    # LuaLaTeXを使う
latex_engine = "uplatex"     # upLaTeXを使う（日本語ドキュメントのデフォルト値）
```

## ドキュメントクラスを設定する（``latex_docclass``）

``latex_documents`` はデフォルトのままにしておき、``latex_docclass`` を変更します。

```python
root_doc = "index"
latex_documents = [(
    root_doc,
    "KumaROOT.tex",      # 出力するLaTeXファイル名
    "KumaROOT",          # LaTeX文書のタイトル
    "Shota Takahashi",   # 著者
    "manual",            # "manual" / "howto"
    False,               # toctree_only
)]

latex_docclass = {"howto": "article", "manual": "report"}  # デフォルト
latex_docclass = {"howto": "jreport", "manual": "jsbook"}  # 日本語文書のデフォルト
latex_docclass = {"manual": "jlreq"}
```

```{TODO}
- LuaLaTeXを使いたい（sphinx-latex-lualatex.md）
- upLaTeXの設定（sphinx-latex-ptex2pdf.md）
```

## ドキュメントクラスオプションの設定（ ``latex_elements`` ）

ドキュメントクラス（ ``\documentclass`` ）のオプションを設定する部分です。
プリアンブルの設定は、ここで書くと長くなって読みにくくなるため、
ここでは変数の定義だけして、中身はあとで書くことにします。

```python
latex_elements = {
    'papersize' = 'a4paper',
    'pointsize' = '12pt',
    'preamble': '',    # あとで追加するので定義だけしておく
    'figure_align': 'htbp',
#   'fontpkg': '\\usepackage{times}',
}
```

``LaTeX`` 文書の出力は以下のようになります。

```latex
\documentclass[a4paper, 12pt, dvipdfmx]{sphinxmanual}
```



## プリアンブルの追加（ ``latex_elements['preamble']`` ）

``latex_elements`` の``preamble``に複数のパッケージを書くと可読性が下がるため、
以下のように``latex_elements['preamble']``にパッケージ単位で追加して書くことにしています。

単なる文字列として追加するため、パッケージ名の終わりには改行コード（``\n``）が必要です。

```python
latex_elements['preamble'] += '\\usepackage{pxjahyper}\n'
latex_elements['preamble'] += '\\usepackage{graphics}\n'
latex_elements['preamble'] += '\\hypersetup{bookmarksnumbered=true}\n'
latex_elements['preamble'] += '\\hypersetup{bookmarksopen=true}\n'
latex_elements['preamble'] += '\\hypersetup{bookmarksopenlevel=2}\n'
latex_elements['preamble'] += '\\hypersetup{colorlinks=true}\n'
latex_elements['preamble'] += '\\hypersetup{pdfpagemode=UseOutlines}\n'
```

``LaTeX`` 文書の出力は以下のようになります。

```latex
\usepackage{pxjahyper}
\usepackage{graphics}
\hypersetup{bookmarksopen=true}
\hypersetup{bookmarksopenlevel=2}
\hypersetup{colorlinks=true}
\hypersetup{pdfpagemode=UseOutlines}
```

## トップレベルのセクション名を設定する

ドキュメントのトップレベルを「部（part）」「章（chapter）」「節（section）」から選択する。
デフォルトは``None``になっている。



```python
latex_toplevel_sectioning = None
latex_toplevel_sectioning = "part"
latex_toplevel_sectioning = "chapter"
latex_toplevel_sectioning = "section"
```

```{toctree}
sphinx-latex-preambles
sphinx-latex-logo
```
