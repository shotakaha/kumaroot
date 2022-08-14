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

```{toctree}
sphinx-latex-engine
sphinx-latex-elements
```

## 表紙の設定（ ``latex_logo`` ）

表紙にロゴを挿入することもできます。
必要ないなら ``None`` （デフォルト値）のままで問題ありません。

```python
# The name of an image file (relative to this directory)
# to place at the top of the title page.
latex_logo = './images/toumin_kuma.png'
```
