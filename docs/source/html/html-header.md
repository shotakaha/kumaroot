# ヘッダーしたい（`header`）

```html
<body>
    <header>
        <a href="/" class="logo">サイト名</a>
        <nav>
            <ul>
                <li><a href="/about">このサイトについて</a></li>
                <li><a href="/blog">ブログ</a></li>
            </ul>
        </nav>
    </header>
    <main>...</main>
    <footer>...</footer>
</body>
```

`header`タグは、ページや記事の冒頭に置く導入部分を表すタグです。
サイト名やロゴ、グローバルナビゲーション、検索フォームなどをまとめます。

`body`直下に置くとページ全体のヘッダーになり、
表示位置の都合で`main`タグの前に配置します。

ウェブサイト全体で共通するパーツなので、
SSGやCMSを利用している場合は
部分テンプレートとして作成しておくとよいです。

## 記事のヘッダーにしたい

```html
<article>
    <header>
        <h1>記事のタイトル</h1>
        <p>公開日: <time datetime="2026-08-30">2026年8月30日</time></p>
    </header>

    <p>記事の本文...</p>
</article>
```

`header`タグは`article`や`section`の中にも置けます。
その場合は、その記事や節の見出し・公開日・著者など、冒頭にまとまる情報を囲みます。

1つのページに`header`タグは複数あってかまいません。
ページ全体のヘッダーと、各記事のヘッダーが同時に存在する形はよくあります。

:::{note}

`header`タグの中に、別の`header`タグや`footer`タグを入れることはできません。

:::

## リファレンス

- [header](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/header)
