# upLaTeXの設定

```{code-block} python
---
caption: conf.py
---
latex_engine = "uplatex"

latex_docclass = {"howto": "jsreport", "manual": "jsbook"}

latex_elements = {
    "papersize": "a4paper",
    "pointsize": "12pt",
    # "extraclassoptions": "tombow",
    "preamble": "",    # あとで追加するので定義だけしておく
}
```
