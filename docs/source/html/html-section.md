# 章・節したい（`section`）

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
