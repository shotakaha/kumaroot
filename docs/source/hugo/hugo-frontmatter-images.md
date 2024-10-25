# 関連画像したい（`images`）

```toml
images = [
    "画像のパス",
    "画像のパス",
    "画像のパス",
    ]
```

`images`キーでページに関連する画像を設定できます。
`images`はリスト型で設定できます。

この変数は、
[OGP用](https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/opengraph.html)や
[Twitter Cards用](https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/twitter_cards.html)、
[Schema用](https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/schema.html)
の内部テンプレートでも使われています。

:::{note}

これらの内部テンプレートの中では、``images``が明示的に設定されていない場合には、リソース（=``$.Resources``）にある**feature**や**cover**、**thumbnail**がファイル名に含まれる画像ファイルを探すようになっています。

:::
