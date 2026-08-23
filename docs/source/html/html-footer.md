# フッターしたい（`footer`）

```html
<body>
    <main>...</main>
    <footer>
        <p>&copy; 2024 - KumaROOT</p>
    </footer>
</body>
```

`footer`タグは、ウェブサイトのフッター情報を表示するタグです。
ページ末尾に表示するため`main`タグの後に配置します。
`footer`要素は`header`や`footer`を子孫に持つことはできません。

フッターにはウェブサイトのコピーライト情報や、
サイト全体のナビゲーションを掲載することが多いです。

ウェブサイト全体で共通するパーツなので、
SSGやCMSを利用している場合は
部分テンプレートとして作成しておくとよいです。

## メガフッターしたい

```html
<footer>
    <div class="footer-logo">ロゴ</div>
    <nav class="footer-nav">
        <!-- メガフッター -->
    </nav>
    <div class="footer-copyright">コピーライト</div>
</footer>
```

メガフッターとは、サイト全体のナビゲーションやリンク集を並べた大きめのフッターのことです。
`footer`の中にはロゴやコピーライトなど複数の区画を配置することが多いですが、
`header`や`footer`は使えないので`div`にクラス名をつけて区分けします。
`nav`にもグローバルナビなど他の`nav`と見分けられるよう、`footer-logo`や`footer-copyright`と揃えたクラス名をつけておくとよいです。

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

## コンテンツ情報したい

```html
<body>
    <main>
        <article>
            コンテンツ本体
            <footer>
                コンテンツのメタ情報（作成日、著者名、など）
            </footer>
        </article>
    </main>
    <footer>...</footer>
</body>
```

`footer`要素はほとんどのフローコンテンツ要素の子要素として配置できます。
作成したページのメタ情報を表示したい場合は、
`article`の子要素として配置するとよいです。

## リファレンス

- [footer](https://developer.mozilla.org/ja/docs/Web/HTML/Element/footer)
