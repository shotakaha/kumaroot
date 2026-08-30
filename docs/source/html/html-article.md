# 記事したい（`article`）

```html
<main>
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
</main>
```

`article`タグは、それ単体で完結するひとまとまりの内容を表すタグです。
「その部分だけを切り出して、他の場所に置いても意味が通じるか」が使い分けの目安です。

ブログ記事、ニュース記事、フォーラムの投稿、商品カード、コメント1件などが該当します。
各`article`には見出し（`h1`〜`h6`）を付けます。
見出しがないと、そのまとまりが何なのかが伝わらず、
スクリーンリーダーの見出し一覧やページのアウトラインにも表示されません。
見出しを付けられないなら、`article`ではなく`div`を使います。

## 記事一覧したい

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
記事一覧のように同じ形のまとまりが並ぶ場合は、それぞれを`article`タグで囲みます。

一覧では本文の代わりに要約だけを入れますが、
その1件が「その記事を表すまとまり」なので`article`が適切です。

## コメント・レビューしたい

```html
<article class="post">
    <h2>記事のタイトル</h2>
    <p>記事の本文...</p>
</article>

<section class="comments">
    <h2>コメント</h2>

    <article class="comment">
        <h3>ユーザーA</h3>
        <p>コメントの本文...</p>
        <footer><time datetime="2026-08-30">2026年8月30日</time></footer>

        <article class="comment">
            <h4>ユーザーB</h4>
            <p>返信の本文...</p>
        </article>
    </article>
</section>
```

記事へのコメントや商品レビューは、1件ずつが独立した投稿なので`article`で囲みます。

返信は親コメントに属しつつ、それ自体も1件の投稿です。
このように`article`の中に`article`を入れられる、数少ないパターンです。

## カードしたい

```html
<section>
    <h2>おすすめ商品</h2>

    <article class="card">
        <img src="product-a.jpg" alt="">
        <h3>商品A</h3>
        <p>¥1,980</p>
        <a href="/products/a">詳細を見る</a>
    </article>

    <article class="card">
        <img src="product-b.jpg" alt="">
        <h3>商品B</h3>
        <p>¥2,480</p>
        <a href="/products/b">詳細を見る</a>
    </article>
</section>
```

商品カードやユーザーカードのように、
どこに置いても「その1件を表すまとまり」として成り立つものは`article`です。

カードを並べる親には、見出しを持つ`section`を使うとまとまりが明確になります。

## タイムラインしたい

```html
<main>
    <h1>タイムライン</h1>

    <article class="post">
        <h2>投稿者名</h2>
        <p>投稿の本文...</p>
        <footer><time datetime="2026-08-30T12:00">12:00</time></footer>
    </article>

    <article class="post">
        <h2>投稿者名</h2>
        <p>投稿の本文...</p>
        <footer><time datetime="2026-08-30T12:05">12:05</time></footer>
    </article>
</main>
```

SNSのタイムラインのように、投稿が時系列で並ぶ画面でも、
1投稿ずつを`article`で囲みます。

投稿単体を別の画面（投稿の詳細ページなど）に表示しても意味が通じるので、`article`が適切です。

## リファレンス

- [article](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/article)
