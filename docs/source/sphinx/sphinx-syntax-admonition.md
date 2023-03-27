# 注釈したい（``admonition``）

````md
```{hint}
これは``hint（ヒント）``型の注釈です。
```
````

```{hint}
これは``hint（ヒント）``型の注釈です。
```

文章中に注釈を挿入するディレクティブです。
注釈の種類として、``attention（注意）`` / ``caution（注意）`` / ``danger（危険）`` / ``error（エラー）`` / ``hint（ヒント）`` / ``important（重要）`` / ``note（注釈）`` / ``seealso（参考）`` / ``tip（Tip）`` / ``warning（警告）``がプリセットされています。
HTMLだと背景色のついたボックス、PDF（＝LaTeX）だと、枠に囲まれたボックスで表示されます。

これらのディレクティブは引数を取りませんが、``:class:``と``:name:``のオプションが使えます。



:::{seealso}
注釈（``admonition``）を使う場合、設定で``colon_fence``と``html_admonition``を有効にしておくとよいです。

```python
myst_enable_extensions = [
    "colon_fence",
    "html_admonition",
]
```

とくに``colon_fence``を有効にすると、` ``` `を``:::``で置き換えられるので、
上記のように注釈ディレクティブ（この場合は``seealso``）の中でも、いつも通りのMarkdown記法でコードブロックを載せることができます。
:::



## リファレンス

- [Admonitions - MyST Parser](https://myst-parser.readthedocs.io/en/stable/syntax/admonitions.html)
- [HTML Admonitions - MyST Parser](https://myst-parser.readthedocs.io/en/stable/syntax/optional.html#syntax-html-admonition)
