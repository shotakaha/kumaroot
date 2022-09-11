# ドキュメントクラスを設定する（``latex_docclass``）

``latex_documents`` はデフォルトのままにしておき``latex_docclass`` を変更します。

```python
latex_docclass = {"howto": "article", "manual": "report"}  # デフォルト
latex_docclass = {"howto": "jreport", "manual": "jsbook"}  # 日本語文書のデフォルト
```

``LuaLaTeX``を使う場合は``ltjs``クラスを使うのがよさそうです。


```python
latex_docclass = {"howto": "ltjsreport", "manual": "ltjsbook"}
```

```{note}
``jlreq``クラスを使いたくていろいろ調べてみたのですが、
用紙サイズとフォントサイズのオプションが省略できない形で
ハードコードされていたりして、
いまのSphinx（v5.1）の仕様では難しそうなことがわかりました。
```
