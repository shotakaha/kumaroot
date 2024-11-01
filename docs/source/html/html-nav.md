# ナビゲーションしたい（`nav`）

```html
<body>
    <nav>
        <ul>
            <li><a href="#">トップページ</a></li>
            <li><a href="about">このページについて</a></li>
            <li><a href="project">プロジェクト</a></li>
        </ul>
    </nav>
    <main>...</main>
    <footer>...</footer>
</body>
```

`nav`タグでナビゲーションを囲います。
サイト全体のナビゲーションはページ先頭に表示するため`main`タグの前に配置します。

`nav`タグの子要素には`ul`タグを使ってそれぞれのページへの内部リンクを列挙します。
表示デザインはCSSを定義します。
ウェブ検索して好みのCSSソースコードを探してみるとよいです。

ウェブサイト全体で共通するパーツなので、
SSGやCMSを利用している場合は
部分テンプレートとして作成しておくとよいです。

## リファレンス

- [nav](https://developer.mozilla.org/ja/docs/Web/HTML/Element/nav)
