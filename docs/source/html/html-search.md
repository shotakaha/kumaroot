# 検索したい（`search`）

```html
<header>
    <a href="/" class="logo">サイト名</a>

    <search>
        <form action="/search">
            <label for="q">サイト内検索</label>
            <input type="search" id="q" name="q">
            <button type="submit">検索</button>
        </form>
    </search>
</header>
```

`search`タグは、検索や絞り込みのためのフォームをまとめるタグです。
中に`form`タグや`input`タグを入れて使います。

サイト内検索、ページ内の絞り込み、検索候補の表示などに使います。

## 検索結果には使わない

```html
<search>
    <!-- 検索フォームはここ -->
    <form action="/search">...</form>
</search>

<main>
    <!-- 検索結果はメインコンテンツとして表示する -->
    <h1>「HTML」の検索結果</h1>
    <ul>...</ul>
</main>
```

`search`タグが表すのは「検索するための場所」であって、検索した結果ではありません。
検索結果の一覧は、そのページの中心的な内容なので`main`タグの中に置きます。

:::{note}

`search`タグは、支援技術に「ここは検索の区画」と伝える`search`ランドマークになります。
以前は`<form role="search">`のように`role`属性で指定していましたが、
`search`タグを使えば`role`属性は不要です。

すべてのブラウザで2023年10月から使えるようになった、比較的新しいタグです。

:::

## リファレンス

- [search](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/search)
