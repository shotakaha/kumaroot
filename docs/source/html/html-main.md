# メインコンテンツしたい（`main`）

```html
<header>...</header>
<nav class="breadcrumbs">...</nav>

<main>
    <article>...</article>
    <aside class="related_pages">...</aside>
</main>

<aside class="sidebar">...</aside>
<footer>...</footer>
```

`main`タグでメインコンテンツを囲みます。
そのページの中心的な内容を表すタグなので、1ページに1つだけ使います。

`main`タグの子要素には、
たとえば`article`タグ（本文のまとまり）や`aside`タグ（関連ページなどの補足）を使って
文書構造をより適切にマークアップできます。
入れる中身はページによって変わるので、`article`や`aside`とは限りません。

:::{note}

厳密には「`hidden`属性の付いていない`main`タグは文書内に1つだけ」というルールです。
画面を出し分けるような特殊な構成では、`hidden`を付けた`main`タグを複数置くこともあります。

:::

## リファレンス

- [main](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/main)
