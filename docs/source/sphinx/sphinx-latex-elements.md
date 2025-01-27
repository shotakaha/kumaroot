# ドキュメントクラスオプションを設定する（``latex_elements``）

ドキュメントクラス（``\documentclass``）のオプションを設定する部分です。
プリアンブルの設定は、ここで書くと長くなって読みにくくなるため、
ここでは変数の定義だけして、中身はあとで書くことにします。

```python
latex_elements = {
    "papersize" = "a4paper",
    "pointsize" = "12pt",
    "preamble": "",    # あとで追加するので定義だけしておく
    "figure_align": "htbp",
#   "fontpkg": "\\usepackage{times}",
    "polyglossia": "",
    "fncychap": r"\usepackage[Bjornstrup]{fncychap}",
}
```

``LaTeX`` 文書の出力は以下のようになります。

```latex
\documentclass[a4paper, 12pt, dvipdfmx]{sphinxmanual}
```

## パッケージを追加したい

LaTeXのパッケージはプリアンブルに追加しますが、その順序が重要なときがあります。
とくに``hyperref``パッケージは最後に読み込むのがよいとされています。
Sphinxはこれに対応していて、``hyperref``パッケージの前に読み込む場合は``latex_elements["extrapackages"]``、後に読み込む場合は``latex_elements["preamble"]``を使います。

``latex_elements``の``extrapackages``や``preamble``に複数のパッケージを追加すると読みにくくなります。
なので、僕は次のように``latex_elements``の中でキーだけ確保しておき、後からパッケージを追加するように書いています。
LaTeXの変数には``\``を使うものが多いため、raw文字列を使っています。

```python
latex_elements = {
    ...,
    "extrapackages": "",
    "preamble": "",
}

latex_elements["extrapackages"] = r"""
\usepackage{physics}
"""

latex_elements["preamble"] = r"""
\hypersetup{bookmarksnumbered=true}
"""
```

``LaTeX`` 文書の出力は以下のようになります。

```latex
\usepackage{physics}

% Include hyperref last.
\usepackage{hyperref}
% Fix anchor placement for figures with captions.
\usepackage{hypcap}% it must be loaded after hyperref.
% Set up styles of URL: it should be placed after hyperref.
\urlstyle{same}
\usepackage{sphinxmessages}
\setcounter{tocdepth}{0}

\hypersetup{bookmarksnumbered=true}
```

## Polyglossiaパッケージを無効にしたい

```python
latex_elements = {
    ...,
    "polyglossia": "",
    ...,
}
```

LaTeXエンジンに``lualatex``を指定すると、自動で``Polyglossia``パッケージが読み込まれるようになっています。
このままビルドすると、多数の``Package polyglossia Warning: Asking to add empty feature to latin font(Script="CJK" to scripttag "")``が表示されます。
多言語対応したドキュメントであれば、無効にしてしまいましょう。

## fncychapパッケージのテーマを変更したい

```python
latex_elements = {
    ...,
    "fncychap": r"\usepackage[Bjornstrup]{fncychap}",
    ...,
}
```

Sphinxのデフォルトは``Bjarne``ですが、``Bjornstrup``に変更するとよいと思います。
選択できるテーマは[fncychapパッケージ](../latex/latex-fncychap.md)を参照してください。
