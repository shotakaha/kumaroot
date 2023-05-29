```{eval-rst}
.. index::
    pair: Sphinx; index
```

# 索引したい（``index``）

````md
```{eval-rst}
.. index::
    single: 索引1
    single: 索引2; 索引3
    pair: 索引4; 索引5
    triple: 索引6; 索引7; 索引8
```
````

[index](https://www.sphinx-doc.org/ja/master/usage/restructuredtext/directives.html#index-generating-markup)を使って、ページを索引（インデックス）に登録できます。
``;``で区切って複数の索引を設定できます。
ドキュメント全体から集めた索引は{file}``getindex``に書き出され、[索引ページ](genindex)で確認できます。

:::{hint}

ロールを使うと**単語単位**で索引に登録できます。
このドキュメントでは、各ページの先頭でディレクティブを使って**ページ単位**で索引に登録することにしています。
具体的な使い方は、このページの``.md``ソースも確認してください。

:::

## 複数索引したい（``pair``）

````md
```{eval-rst}
.. index::
    single: 目的; ツール名
```
````

``pair``オプションを使うと、1つのページを複数の索引に登録できます。

:::{note}

このページは``pair: Sphinx; index``としてあり、``Sphinx -> index``と``index -> Sphinx``で検索できるようにしてあります。
索引は、1ページだけに設定しても（当たり前ですが）旨みはありません。
複数ページに設定することで、より適切な登録の仕方が見えてきます。

:::
