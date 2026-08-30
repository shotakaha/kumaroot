# 補足したい（`aside`）

```html
<article>
    <h1>記事のタイトル</h1>
    <p>本文...</p>

    <aside class="note">
        <!-- この記事への補足 -->
    </aside>
</article>

<aside class="sidebar">
    <!-- ページ全体への補足 -->
</aside>
```

`aside`タグは、本筋から少し外れた補足的な内容を表すタグです。
その部分を読み飛ばしても、本文の理解に支障がないものを入れます。

サイドバー、関連記事、用語の補足、広告などが該当します。

`aside`を置く場所によって、何に対する補足かが変わります。
`article`の中に置くとその記事への補足、`article`の外（`main`直下や`body`直下）に置くとページやサイト全体への補足になります。

## 関連記事したい

```html
<main>
    <article>
        <h1>記事のタイトル</h1>
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

記事の下に置く「関連記事」や「あわせて読みたい」のリストは`aside`で囲みます。
本文を読み終えた人向けの案内であって、記事そのものではないためです。

上記のように`article`の外に置くと、そのページ全体に対する関連記事という意味になります。

## 用語説明したい

```html
<article>
    <h1>記事のタイトル</h1>

    <p>本文の中で<b>専門用語</b>が出てきます...</p>

    <aside class="note">
        <h2>専門用語とは</h2>
        <p>ここで用語のかんたんな説明をします。</p>
    </aside>

    <p>本文の続き...</p>
</article>
```

本文の途中に差し込む用語説明や余談も`aside`で囲みます。
読み飛ばしても本文の流れが追えるものが対象です。

`article`の中に置いているので、この記事の中でだけ意味を持つ補足になります。

## サイドバーしたい

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
