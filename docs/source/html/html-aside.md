# 余談したい（`aside`）

```html
<main>
    <article>
        <p>本文...</p>
    </article>

    <aside class="related">
        <h2>関連記事</h2>
        <ul>
            <li><a href="#">関連する記事1</a></li>
            <li><a href="#">関連する記事2</a></li>
        </ul>
    </aside>
</main>
```

`aside`タグは、本筋から少し外れた補足的な内容を表すタグです。
その部分を読み飛ばしても、本文の理解に支障がないものを入れます。

サイドバー、関連記事、用語の補足、広告などが該当します。

## サイドバーにしたい

```html
<body>
    <main>...</main>

    <aside class="sidebar">
        <section>
            <h2>カテゴリ</h2>
            <ul>...</ul>
        </section>
        <section>
            <h2>月別アーカイブ</h2>
            <ul>...</ul>
        </section>
    </aside>

    <footer>...</footer>
</body>
```

`body`直下に置く`aside`タグは、ページ全体に対する補足です。
ブログのサイドバーのように、カテゴリ一覧やアーカイブ、プロフィールなどをまとめる区画に使います。

1つのページに`aside`タグは複数あってかまいません。
本文中の補足と、ページ全体のサイドバーが同時に存在する形もよくあります。

:::{note}

`aside`タグは「補足」を表すので、ページの中心的な内容には使いません。
中心的な内容は`main`タグや`article`タグで囲みます。

:::

## リファレンス

- [aside](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/aside)
