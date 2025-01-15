# ドキュメントクラスを設定したい（``latex_docclass``）

```python
# デフォルト（欧文）
latex_docclass = {
    "howto": "article",
    "manual": "report"
    }

# デフォルト（和文）
latex_docclass = {
    "howto": "jsreport",
    "manual": "jsbook"
    }
```

`latex_docclass` でドキュメントクラスへのマッピングを変更できます。
`howto`は`article`や`report`に相当する短めの文書
`manual`は`book`に相当する長めの文書に設定する値です。

日本語の場合、`howto`は`jsreport`クラス、`manual`は`jsbook`クラスになっています。

```python
latex_docclass = {
    "howto": "ltjsreport",
    "manual": "ltjsbook",
}
```

LuaLaTeXで日本語を扱う場合は、このマッピングを
`ltjsreport`クラスと`ltjsbook`クラスへ変更するか、
`luatexja`パッケージを読み込むとよいです。

:::{note}

和文クラスに`jlreq`があります。
しかし、[Sphinxの内部テンプレート](https://github.com/sphinx-doc/sphinx/blob/master/sphinx/templates/latex/latex.tex_t)に`papersize`と`pointsize`のオプションがハードコードされているため、`jlreq`のオプションが設定できません。

:::
