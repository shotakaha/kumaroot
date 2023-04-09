# ドキュメントを設定したい（``latex_documents``）

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
