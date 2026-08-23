# 画像したい（`figure`）

```html
<figure>
    <img src="画像のパス" alt="画像の説明">
    <figcaption>画像のキャプション</figcaption>
</figure>
```

`figure`タグは、画像や図表など、本文から独立して参照できるコンテンツをまとめて表示するタグです。
`img`だけでなく`table`や`pre`、`blockquote`なども子要素に持てる汎用的なタグです。

:::{note}

`img`専用のタグと思われがちですが、画像以外のコンテンツもまとめて表示できます。

:::

`figcaption`タグでキャプションを追加できます。
`figure`の最初か最後の子要素として置く必要があり、途中に挟むことはできません。
`figcaption`は省略可能で、画像だけを`figure`で囲むこともできます。

## リファレンス

- [figure](https://developer.mozilla.org/ja/docs/Web/HTML/Element/figure)
- [figcaption](https://developer.mozilla.org/ja/docs/Web/HTML/Element/figcaption)
