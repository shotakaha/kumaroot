# タイトル／著者を設定したい（``latex_documents``）

```python
root_doc = "index"

latex_documents = {
    root_doc, # デフォルトは"index"
    "ファイル名.tex",
    "タイトル",
    "著者",
    "manual", # or "howto"
    False, # or True
}
```

[latex_documents](https://www.sphinx-doc.org/ja/master/usage/configuration.html#confval-latex_documents)を使って設定します。
タイトルや著者だけを設定する変数はないみたいです。
