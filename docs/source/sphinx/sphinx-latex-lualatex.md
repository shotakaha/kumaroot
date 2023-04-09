# LuaLaTeXしたい

```{code-block} python
---
caption: conf.py
---
root_doc = "index"

latex_engine = "lualatex"

latex_docclass = {
    "howto": "ltjsreport",
    "manual": "ltjsbook",
}

latex_documents = {
    root_doc,
    "出力ファイル名.tex",
    "タイトル",
    "著者名",
    "howto"
    True,
}

latex_elements = {
    # ドキュメントクラスオプションの設定
    "papersize": "a4paper",
    "pointsize": "12pt",
    "extraclassoptions": "tombow",

    # フォントの設定
    "fontpkg": "",

    # 追加パッケージはあとで設定できるようにする
    "extrapackages": "",
    "preamble": "",

    # Polyglossiaを無効にする
    "polyglossia": "",

    # ヘッダーを装飾する
    "fncychap": r"\usepackage[Bjornstrup]{fncychap}",
}

# hyperrefの前に読み込むパッケージを追加する
latex_elements["extrapackages"] = r"""
\usepackage{physics}
"""

# hyperrefの後に読み込むパッケージを追加する
latex_elements["preamble"] = r"""
\setlength{\footskip}{3\zw}
\hypersetup{bookmarksnumbered=true}
\hypersetup{bookmarksopen=true}
"""

latex_show_pagerefs = True
latex_show_urls = "footnote"
```

```{note}
本当は``jlreq``クラスを使いたくていろいろ調べてみました。
しかし、いまのSphinx（v5.1）では、用紙サイズとフォントサイズのオプションが省略できない形で
ハードコードされていて、使うのが難しそうなことがわかりました。
なので``ltjs``系のクラスを使っています。
```
