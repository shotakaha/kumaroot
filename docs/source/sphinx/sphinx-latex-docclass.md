# ドキュメントクラスを設定する（``latex_docclass``）

``latex_documents`` はデフォルトのままにしておき``latex_docclass`` を変更します。

```python
latex_docclass = {"howto": "article", "manual": "report"}  # デフォルト
latex_docclass = {"howto": "jreport", "manual": "jsbook"}  # 日本語文書のデフォルト
```

``LuaLaTeX``を使う場合に``jlreq``クラスを使うことができないか
いろいろテストしてみたのですが、いまのSphinx（v5.1）の仕様では
``ltjs``系のクラスを使うのがよさそうなことだと判断しました。

```python
latex_docclass = {"howto": "ltjsreport", "manual": "ltjsbook"}
```
