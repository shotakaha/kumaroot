# フッターしたい（`footer`）

```html
<body>
    <main>...</main>

    <footer>
        <p>&copy; 2024 - KumaROOT</p>
    </footer>
</body>
```

`footer`タグは、そのまとまりの末尾に置く補足情報を表すタグです。
`body`直下に置けばサイト全体のフッター、`article`の中に置けばその記事のフッターになります。

`footer`の中に`header`タグや`footer`タグを入れることはできません。

:::{seealso}

- [](./html-header.md)
- [](./html-nav.md)
- [](./html-article.md)

:::

## サイトフッターしたい

```html
<body>
    <main>...</main>

    <footer>
        <p>&copy; 2024 - KumaROOT</p>
    </footer>
</body>
```

`body`直下に置く`footer`タグは、サイト全体のフッターです。
ページ末尾に表示するので`main`タグの後に配置します。

コピーライト情報やサイト全体のナビゲーション、SNSリンクなどを掲載することが多いです。

すべてのページで共通するパーツなので、
SSGやCMSを利用している場合は部分テンプレートとして作成しておくとよいです。

## メガフッターしたい

```html
<footer>
    <div class="footer-logo">ロゴ</div>
    <nav class="footer-nav">
        <!-- リンク集 -->
    </nav>
    <div class="footer-copyright">コピーライト</div>
</footer>
```

メガフッターとは、サイト全体のナビゲーションやリンク集を並べた大きめのフッターのことです。

`footer`の中にはロゴやコピーライトなど複数の区画を配置しますが、
`header`や`footer`は使えないので`div`にクラス名をつけて区分けします。
`nav`にも、グローバルナビなど他の`nav`と見分けられるよう`footer-nav`のようなクラス名をつけておくとよいです。

```css
footer {
    display: block flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    padding: 2rem;
}

.footer-logo {
    font-weight: bold;
}

.footer-nav ul {
    display: block flex;
    gap: 1.5rem;
    list-style: none;
    padding: 0;
}

.footer-copyright {
    font-size: 0.875rem;
    color: #666;
}
```

`display: block flex`と`justify-content: space-between`で、
ロゴを左、コピーライトを右に寄せつつ、`nav`を間に配置できます。
`flex-wrap: wrap`を指定しておくと、画面幅が狭いときに自動で縦積みに折り返ります。

## 記事フッターしたい

```html
<article>
    コンテンツ本体

    <footer>
        <p>
            <img src="著者アイコンのパス" alt="著者名">
            著者名です。著者のプロフィールです。
        </p>
        <p>公開日: <time datetime="2026-08-23">2026年8月23日</time></p>
        <p>
            タグ:
            <a href="/tags/html">HTML</a>
            <a href="/tags/css">CSS</a>
        </p>
    </footer>
</article>
```

`article`タグの中に置く`footer`タグは、その記事のフッターです。
著者プロフィールや公開日、タグなど、記事本体に付随する情報をまとめて掲載します。

`article`の中に置くことで、サイト全体ではなくこの記事のフッターだと明示できます。

```css
article > footer {
    margin-top: 2rem;
    padding-top: 1rem;
    border-top: 1px solid #ddd;
    font-size: 0.875rem;
    color: #666;
}

article > footer img {
    width: 2.5rem;
    height: 2.5rem;
    border-radius: 50%;
    vertical-align: middle;
}

article > footer p:first-child {
    display: block flex;
    align-items: center;
    gap: 0.5rem;
}

article > footer a {
    display: inline flow-root;
    padding: 0.25rem 0.75rem;
    background: #f0f0f0;
    border-radius: 999px;
    text-decoration: none;
}
```

`border-top`で本文との区切り線を入れ、フォントを小さめ・グレー系にすることで、補足情報であることを視覚的に分かりやすくしています。
著者アイコンは`border-radius: 50%`で丸くし、`display: block flex`でテキストと横並びにしています。
タグのリンクは`border-radius: 999px`で丸みの強い「ピル型」のバッジとして表現しています。

## リファレンス

- [footer](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/footer)
- [address](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/address)
- [time](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/time)
- [ARIA: contentinfo ロール](https://developer.mozilla.org/ja/docs/Web/Accessibility/ARIA/Reference/Roles/contentinfo_role)
