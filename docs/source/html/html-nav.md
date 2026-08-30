# ナビゲーションしたい（`nav`）

```html
<body>
    <header>
        <a href="/" class="logo">サイト名</a>
        <nav aria-label="メインメニュー">
            <ul>
                <li><a href="/">トップページ</a></li>
                <li><a href="/about">このサイトについて</a></li>
                <li><a href="/blog">ブログ</a></li>
            </ul>
        </nav>
    </header>

    <main>...</main>
    <footer>...</footer>
</body>
```

`nav`タグは、主要なナビゲーションのまとまりを表すタグです。
中には`ul`タグでリンクを並べます。

`nav`で囲むのは、メインメニューやパンくず、ページ送りなど「そのページを移動するための主要なリンク集」です。
本文中のリンクや、フッターの細かいリンクまで`nav`で囲む必要はありません。

:::{seealso}

- [](./html-header.md)
- [](./html-footer.md)
- [](./html-aside.md)

:::

## 複数のnavを見分けたい（`aria-label`）

```html
<nav aria-label="メインメニュー">...</nav>
<nav aria-label="パンくずリスト">...</nav>
<nav aria-label="ページ送り">...</nav>
```

1つのページに`nav`タグは複数置けます。

複数ある場合は、それぞれに`aria-label`で名前を付けます。
スクリーンリーダーは`nav`を「ナビゲーション」というまとまりとして読み上げるので、
名前がないとどれがどれか区別できなくなるためです。

CSSでの見分け用にはクラス名（`class="breadcrumb"`など）を別に付けます。

## グローバルナビしたい

```html
<header>
    <a href="/" class="logo">サイト名</a>

    <nav aria-label="メインメニュー">
        <ul>
            <li><a href="/">トップページ</a></li>
            <li><a href="/products">製品</a></li>
            <li><a href="/support">サポート</a></li>
        </ul>
    </nav>
</header>
```

サイトのどのページからも使うメインメニューです。
`header`タグの中に置くことが多く、全ページで共通するので、
SSGやCMSを利用している場合は部分テンプレートとして作成しておくとよいです。

```css
header nav ul {
    display: block flex;
    gap: 1.5rem;
    list-style: none;
    margin: 0;
    padding: 0;
}
```

`display: block flex`でリンクを横並びにし、`list-style: none`でリストの黒点を消します。

## パンくずしたい

```html
<nav aria-label="パンくずリスト">
    <ol>
        <li><a href="/">ホーム</a></li>
        <li><a href="/blog">ブログ</a></li>
        <li>この記事のタイトル</li>
    </ol>
</nav>
```

いまページが階層のどこにいるかを示すのがパンくずです。

上下関係のある並びなので、`ul`ではなく順序リストの`ol`を使います。
現在ページ（最後の項目）はリンクにせず、テキストのままにします。

```css
nav[aria-label="パンくずリスト"] ol {
    display: block flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    list-style: none;
    padding: 0;
}

nav[aria-label="パンくずリスト"] li + li::before {
    content: "›";
    margin-right: 0.5rem;
}
```

`li + li::before`で、2つ目以降の項目の前に区切り記号（`›`）を入れています。

## ページ送りしたい

```html
<nav aria-label="ページ送り">
    <a href="/blog/3" rel="prev">← 前の記事</a>
    <a href="/blog/5" rel="next">次の記事 →</a>
</nav>
```

記事の前後へ移動するリンクです。
`rel="prev"` / `rel="next"`を付けると、前後の関係をブラウザや検索エンジンに伝えられます。

## 目次したい

```html
<nav aria-label="目次">
    <ul>
        <li><a href="#intro">はじめに</a></li>
        <li><a href="#install">インストール</a></li>
        <li><a href="#usage">使い方</a></li>
    </ul>
</nav>
```

長い記事の中で、各見出しへジャンプするリンク集です。

リンク先は`#見出しのid`にします。
リンクしたい見出しに`id`属性（`<h2 id="install">`）を付けておく必要があります。

## リファレンス

- [nav](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/nav)
- [ARIA: navigation ロール](https://developer.mozilla.org/ja/docs/Web/Accessibility/ARIA/Reference/Roles/navigation_role)
- [aria-label](https://developer.mozilla.org/ja/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-label)
