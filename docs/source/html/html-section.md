# セクションしたい（`section`）

```html
<article>
    <h1>記事のタイトル</h1>

    <section>
        <h2>はじめに</h2>
        <p>本文...</p>
    </section>

    <section>
        <h2>使い方</h2>
        <p>本文...</p>
    </section>
</article>
```

`section`タグは、見出しを持つ内容のまとまり（章・節）を表すタグです。
長い文書を意味のあるかたまりに区切るときに使います。

`section`タグには、必ず見出し（`h1`〜`h6`）を付けます。
見出しを付けられないなら、それは`section`ではなく`div`が適切です。

`section`タグは`article`の中だけでなく、`body`直下や`main`、`aside`の中でも使えます。
以下に、`article`以外でよく使うパターンを紹介します。

## ランディングページを区分したい

```html
<body>
    <header>...</header>

    <main>
        <section id="features">
            <h2>特徴</h2>
            <p>...</p>
        </section>

        <section id="pricing">
            <h2>料金プラン</h2>
            <p>...</p>
        </section>

        <section id="faq">
            <h2>よくある質問</h2>
            <p>...</p>
        </section>
    </main>

    <footer>...</footer>
</body>
```

サービス紹介ページのように、1ページを「特徴」「料金」「FAQ」などのブロックに分ける場合、
それぞれを`section`タグで囲みます。

`id`を付けておくと、ページ内リンク（`<a href="#pricing">`）のジャンプ先にもなります。

## 一覧ページをカテゴリで分けたい

```html
<main>
    <h1>お知らせ</h1>

    <section>
        <h2>プレスリリース</h2>
        <ul>
            <li><a href="#">...</a></li>
        </ul>
    </section>

    <section>
        <h2>イベント情報</h2>
        <ul>
            <li><a href="#">...</a></li>
        </ul>
    </section>
</main>
```

記事一覧やお知らせページを種類ごとに分けるときにも使います。
`section`の中に`article`を並べる形になることもあります。

## サイドバーのブロックを分けたい

```html
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
```

ブログのサイドバーのように、複数の小さなブロックが並ぶ場所でも、
それぞれに見出しがあるなら`section`で囲めます。

## div との違い

`section`と`div`はどちらも要素をまとめる箱ですが、意味が違います。

- `section` … 見出しを持つ、意味のあるひとかたまり
- `div` … 意味を持たない。CSSやJavaScriptのために囲むだけ

「ここは1つの節だ」と説明できるなら`section`、
単にスタイルを当てるためにまとめたいだけなら`div`を使います。

## article との違い

`section`と`article`はどちらも内容のまとまりですが、独立性が違います。

- `article` … それ単体で完結し、切り出しても意味が通じる
- `section` … 文書の一部で、単体では完結しない

ニュースサイトのトップページで「スポーツ」「経済」などのジャンルごとに区切るなら`section`、
その中の1本1本のニュースは`article`です。

## リファレンス

- [section](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/section)
