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
`article`の中だけでなく、`body`直下や`main`、`aside`の中でも使えます。

長い文書を意味のあるかたまりに区切るときに使います。
見出し（`h1`〜`h6`）が付けられるなら`section`、
付けられないなら`div`を使うのがセマンティクス的に適切です。

## ランディングページしたい

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

サービス紹介ページのように、1ページを「特徴」「料金」「FAQ」などのブロックに分ける場合は、それぞれを`section`タグで囲みます。

`id`を付けて、ページ内リンク（`<a href="#pricing">`）のジャンプ先にできます。

## 一覧ページをカテゴリ分類したい

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

記事一覧やお知らせページをカテゴリごとに分けるときにも`section`が使えます。
`section`の中に`article`を並べることもできます。

## サイドバーを分類したい

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

ブログのサイドバーでは、「カテゴリ別」「月別アーカイブ」などの小さなブロックに分類するときにも`section`が使えます。

## 使い分けたい（`div` / `section` / `article`）

::::{mermaid}

graph TD
    A[要素をまとめたい] --> B{見出しがある}
    B -->|いいえ| DIV[div]
    B -->|はい| C{単体で完結できる}
    C -->|いいえ| SEC[section]
    C -->|はい| ART[article]

::::

`div`は意味を持たないブロック要素です。
ただの装飾やスクリプトのために要素をまとめるときに使います。

`section`は、ある程度の意味のあるまとまりを表すブロック要素です。
それぞれのセクションには必ず見出し（`h1`〜`h6`）を付ける必要があります。

`article`は、単体で完結する内容のまとまりを表すブロック要素です。

:::{hint}

見出しは付くけれど「章」と呼ぶには弱い程度のまとまりなら、`section`にせず`div`のままでかまいません。

:::

## リファレンス

- [section](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/section)
