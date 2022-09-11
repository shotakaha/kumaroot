# LuaLaTeXの設定

```{code-block} python
---
caption: conf.py
---
latex_engine = "lualatex"

latex_docclass = {
    "howto": "ltjsreport",
    "manual": "ltjsbook",
}

latex_elements = {
    "papersize": "a4paper",
    "pointsize": "12pt",
    "extraclassoptions": "tombow",
    "preamble": "",    # あとで追加するので定義だけしておく
    "polyglossia": "",
}
```

``polyglossia``関係のwarningが多数表示されたため、無効にしています。
