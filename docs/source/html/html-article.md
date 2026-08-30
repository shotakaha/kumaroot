# 記事したい（`article`）

```html
<article>
    <header>
        <h1>記事のタイトル</h1>
        <p>公開日: <time datetime="2026-08-30">2026年8月30日</time></p>
    </header>

    <p>記事の本文...</p>

    <footer>
        <p>著者: くま</p>
    </footer>
</article>
```

`article`タグは、それ単体で完結するひとまとまりの内容を表すタグです。
「その部分だけを切り出して、他の場所に置いても意味が通じるか」が目安です。

ブログ記事、ニュース記事、フォーラムの投稿、商品カード、コメント1件などが該当します。

## 一覧の中で使いたい

```html
<main>
    <h1>ブログ記事一覧</h1>

    <article>
        <h2><a href="/blog/1">1本目の記事</a></h2>
        <p>記事の要約...</p>
    </article>

    <article>
        <h2><a href="/blog/2">2本目の記事</a></h2>
        <p>記事の要約...</p>
    </article>
</main>
```

`article`タグは1つのページに複数置けます。
記事一覧のように、同じ形のまとまりが並ぶ場合は、それぞれを`article`タグで囲みます。

各`article`には見出し（`h1`〜`h6`）を付けます。
見出しがないと、そのまとまりが何なのかが伝わらず、
スクリーンリーダーの見出し一覧やページのアウトラインにも表示されません。
見出しを付けられないなら、`article`ではなく`div`を使います。

## section との違い

`article`と`section`はどちらも内容のまとまりを表しますが、使い分けの目安があります。

- `article` … それ単体で完結し、切り出して再配布できるもの
- `section` … 文書の中の章・節。単体では完結しない見出し付きのかたまり

記事の本文を章ごとに区切るなら、`article`の中に`section`を並べます。

## リファレンス

- [article](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/article)
