# ドキュメントクラスを設定する（``latex_docclass``）

``latex_documents`` はデフォルトのままにしておき、``latex_docclass`` を変更します。

```python
latex_docclass = {"howto": "article", "manual": "report"}  # デフォルト
latex_docclass = {"howto": "jreport", "manual": "jsbook"}  # 日本語文書のデフォルト
latex_docclass = {"manual": "jlreq"}
```
