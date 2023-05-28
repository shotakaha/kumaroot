```{eval-rst}
.. index::
    pair: Sphinx; index
```

# 索引したい（``index``）

````md
:::{index} キーワード
:::
````

索引（インデックス）にページを登録したい場合は、[indexディレクティブ](https://www.sphinx-doc.org/ja/master/usage/restructuredtext/directives.html#index-generating-markup)でマークアップします。
結果は[索引ページ](genindex)で確認できます。

## 複数の索引したい

````md
```{eval-rst}
.. index::
    pair: キーワード1; キーワード2
```
````

``pair``オプションを使って、1つのページを複数の索引に登録できます。

:::{hint}

``MyST-Parser``では``pair``オプションをうまくパースできないみたいです。
なので、``{eval-rst}``の中で使っています。

具体的な使い方は、このページの``.md``ソースも確認してください。
ページの先頭で次のように記述しています。

````md
```{eval-rst}
.. index::
    pair: sphinx; index
```
````

:::
