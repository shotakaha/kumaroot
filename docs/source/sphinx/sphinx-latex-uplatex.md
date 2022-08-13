# upLaTeXの設定

```python
root_doc = "index"

latex_engine = "uplatex"

latex_documents = [(
    root_doc,
    "KumaROOT.tex",      # 出力するLaTeXファイル名
    "KumaROOT",          # LaTeX文書のタイトル
    "Shota Takahashi",   # 著者
    "manual",            # "manual" / "howto"
    False,               # toctree_only
)]

latex_docclass = {"manual": "jsbook"}

latex_elements = {
    'papersize' = 'a4paper',
    'pointsize' = '12pt',
    'preamble': '',    # あとで追加するので定義だけしておく
    'figure_align': 'htbp',
#   'fontpkg': '\\usepackage{times}',
}

latex_elements['preamble'] += '\\usepackage{pxjahyper}\n'
latex_elements['preamble'] += '\\usepackage{graphics}\n'
latex_elements['preamble'] += '\\hypersetup{bookmarksnumbered=true}\n'
latex_elements['preamble'] += '\\hypersetup{bookmarksopen=true}\n'
latex_elements['preamble'] += '\\hypersetup{bookmarksopenlevel=2}\n'
latex_elements['preamble'] += '\\hypersetup{colorlinks=true}\n'
latex_elements['preamble'] += '\\hypersetup{pdfpagemode=UseOutlines}\n'
```
