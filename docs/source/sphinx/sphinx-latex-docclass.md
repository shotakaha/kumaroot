# ドキュメントクラスを設定したい（``latex_docclass``）

```python
# latex_docclass = {"howto": "article", "manual": "report"}  # デフォルト
latex_docclass = {"howto": "jreport", "manual": "jsbook"}  # 日本語文書のデフォルト
```

``latex_docclass`` でドキュメントクラスへのマッピングを変更できます。
日本語文書の場合、``howto``は``jsreport``クラス、``manual``は``jsbook``クラスになっています。

LaTeXエンジンにLuaLaTeXを使う場合は、``ltjsreport``と``ltjsbook``に変更するとよいと思います。

```python
latex_docclass = {
    "howto": "ltjsreport",
    "manual": "ltjsbook",
}
```

:::{note}

最近の日本語文書のドキュメントクラスに``jlreq``があります。
しかし、Sphinxでは``papersize``と``pointsize``のオプションが[テンプレートにハードコード](https://github.com/sphinx-doc/sphinx/blob/master/sphinx/templates/latex/latex.tex_t)されているため、``jlreq``のオプションが設定できません。

:::
