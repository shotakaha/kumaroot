# 見出しと副題したい（`hgroup`）

```html
<hgroup>
    <h1>フランケンシュタイン</h1>
    <p>あるいは現代のプロメテウス</p>
</hgroup>
```

`hgroup`タグは、見出しと、その副題やキャッチコピーを1つのまとまりとして囲むタグです。

中に入れられるのは、見出し（`h1`〜`h6`）1つと、その前後に置く`p`タグだけです。
`p`タグは本文の段落ではなく、見出しに添える副題として扱われます。

:::{note}

`hgroup`は"heading group"の略ですが、いまの仕様では見出しは1つしか入りません。
名前と中身がずれているので、「見出しに`p`の副題をくっつける箱」と覚えるとよいです。

:::

## 副題をつけたい

```html
<hgroup>
    <h1>くまブログ</h1>
    <p>HTMLとCSSの学習記録</p>
</hgroup>
```

サイト名やページタイトルの下にキャッチコピーを置きたいときに使います。

`hgroup`で囲むと、その`p`が「タイトルに付随する副題」だと明示できます。
文書のアウトラインには見出し（`h1`）だけが反映され、副題の`p`はアウトラインに影響しません。

## 記事のヘッダーで使いたい

```html
<article>
    <header>
        <hgroup>
            <h1>記事のタイトル</h1>
            <p>3分で読める入門記事</p>
        </hgroup>
        <p>公開日: <time datetime="2026-08-30">2026年8月30日</time></p>
    </header>

    <p>本文...</p>
</article>
```

`header`タグの中に`hgroup`を置く形が典型です。

`hgroup`が「タイトルと副題」だけをまとめ、
公開日や著者など冒頭のその他の情報は`header`の直下に並べます。

## hgroup を使わない書き方

```html
<h1>くまブログ</h1>
<p class="subtitle">HTMLとCSSの学習記録</p>
```

副題を表示したいだけなら、`hgroup`を使わず見出しの下に`p`を置くだけでもかまいません。
`hgroup`の利点は「この`p`は本文ではなく副題」と意味づけできる点だけなので、使う機会は多くありません。

## リファレンス

- [hgroup](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/hgroup)
- [見出し要素 h1〜h6](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/Heading_Elements)
