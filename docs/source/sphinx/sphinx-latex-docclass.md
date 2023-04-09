# ドキュメントクラスを設定したい（``latex_docclass``）

```python
# latex_docclass = {"howto": "article", "manual": "report"}  # デフォルト
latex_docclass = {"howto": "jreport", "manual": "jsbook"}  # 日本語文書のデフォルト
```

``latex_docclass`` でドキュメントクラスへのマッピングを変更できます。
日本語文書の場合、``howto``は``jsreport``クラス、``manual``は``jsbook``クラスになっています。
