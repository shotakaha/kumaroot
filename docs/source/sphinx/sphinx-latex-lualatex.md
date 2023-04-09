# LuaLaTeXしたい

```{code-block} python
---
caption: conf.py
---
latex_engine = "lualatex"

latex_docclass = {
    "howto": "ltjsreport",
    "manual": "ltjsbook",
}

latex_documents = {
    "index", # root_doc
    "出力ファイル名.tex",
    "タイトル",
    "著者名",
    "テーマを選択", # "manual"(default) or "howto",
    "toctree_only", # True or False
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
    # 無効にする
    "polyglossia": "",
    # ヘッダーを装飾する
    "fncychap": r"\usepackage[Bjornstrup]{fncychap}",
}
```

## latex_engine

日本語文書のLaTeXエンジンは``lualatex``を使うのがよいと思います。

## latex_docclass

``LuaLaTeX``の場合、``ltjs``クラスを使います。
``latex_documents["theme"]``のデフォルトは``manual``なので、そこを追加するだけでもOKだと思います。
ここではついでに``howto``も設定していますが、どこにも使っていません。

``latex_elements["extraclassoptions"]``で用紙サイズ（``papersize``）とフォントサイズ（``pointsize``）以外のドキュメントクラスオプションを追加できます。

その他のパッケージは


``polyglossia``関係のwarningが多数表示されたため、無効にしています。


```{note}
本当は``jlreq``クラスを使いたくていろいろ調べてみました。
しかし、いまのSphinx（v5.1）では、用紙サイズとフォントサイズのオプションが省略できない形で
ハードコードされていて、使うのが難しそうなことがわかりました。
なので``ltjs``系のクラスを使っています。
```
