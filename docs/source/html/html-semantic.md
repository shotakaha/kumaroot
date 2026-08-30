# セマンティクスしたい（semantics）

```html
<!-- div だけで組み立てた例 -->
<div class="header">
    <div class="nav">...</div>
</div>
<div class="main">
    <div class="article">...</div>
    <div class="related">...</div>
</div>
<div class="sidebar">...</div>
<div class="footer">...</div>
```

```html
<!-- セマンティクスを意識した例 -->
<header>
    <nav>...</nav>
</header>
<main>
    <article>...</article>
    <aside class="related">...</aside>
</main>
<aside class="sidebar">...</aside>
<footer>...</footer>
```

[セマンティクス](https://developer.mozilla.org/ja/docs/Glossary/Semantics)とは、もともと言語学で「意味」を指す言葉です。
HTML／CSSでは、「そのタグやクラスが何を表すか」を考えてマークアップする手法です。

HTML4までは、`<div>`や`<span>`のようなタグを使って「見た目を第一」にレイアウトを組むのが一般的でした。
HTML5で、`<header>`、`<nav>`、`<main>`、`<article>`、`<section>`、`<aside>`、`<footer>`など、「セマンティクス」に基づいたタグが追加されました。

ウェブサイトは人間だけでなく、ブラウザ・検索エンジン・スクリーンリーダーといった機械も読みます。
こうした機械は見た目（CSS）を理解しないため、意味に合ったHTMLタグを使うことで、構造を認識させる必要があります。

:::{seealso}

- [](./html-a11y.md)

:::

:::{note}

セマンティクスに唯一の正解はありません。
[コンテンツカテゴリー](https://developer.mozilla.org/ja/docs/Web/HTML/Guides/Content_categories)を参考にしつつ、作成者が文書構造をどう捉えるかで決まります。
LaTeXやWordのアウトライン機能で見出しを組むのと同じ感覚です。

:::

## ヘッダーしたい（`header`）

```html
<!-- セマンティクス -->
<header>
    <a href="/" class="logo">サイト名</a>
    <nav>...</nav>
</header>
```

`header`タグで、サイトのロゴやナビゲーションなど、ページの先頭にまとまる情報を記述できます。

```html
<!-- div -->
<div class="header">
    <div class="logo">サイト名</div>
    <div class="nav">...</div>
</div>
```

これまでは`.header`クラスを作るのが一般的でした。

:::{seealso}

- [](./html-header.md)

:::

## ナビゲーションしたい（`nav`）

```html
<!-- セマンティクス -->
<nav aria-label="メインメニュー">
    <ul>
        <li><a href="/">ホーム</a></li>
        <li><a href="/blog">ブログ</a></li>
    </ul>
</nav>
```

`nav`タグで、主要なリンク集を記述できます。リンクは`ul`と`li`で並べます。

```html
<!-- div -->
<div class="nav">
    <div class="nav-item"><a href="/">ホーム</a></div>
    <div class="nav-item"><a href="/blog">ブログ</a></div>
</div>
```

これまでは`.nav`クラスを作るのが一般的でした。

:::{seealso}

- [](./html-nav.md)

:::

## メインコンテンツしたい（`main`）

```html
<!-- セマンティクス -->
<main>
    ...
</main>
```

`main`タグで、そのページの中心的な内容を記述できます。表示される`main`は1ページに1つです。

```html
<!-- div -->
<div id="content">
    ...
</div>
```

これまでは`#content`や`#main`のIDを付けるのが一般的でした。

:::{seealso}

- [](./html-main.md)

:::

## 記事したい（`article`）

```html
<!-- セマンティクス -->
<article>
    <h1>記事のタイトル</h1>
    <p>本文...</p>
</article>
```

`article`タグで、それ単体で完結するまとまり（記事、投稿、商品カード）を記述できます。
タイトルは`div`ではなく見出しタグ（`h1`〜`h6`）を使います。

```html
<!-- div -->
<div class="article">
    <div class="title">記事のタイトル</div>
    <div class="body">本文...</div>
</div>
```

これまでは`.article`クラスを作るのが一般的でした。

:::{seealso}

- [](./html-article.md)

:::

## 章・節したい（`section`）

```html
<!-- セマンティクス -->
<section>
    <h2>機能一覧</h2>
    <p>...</p>
</section>
```

`section`タグで、見出しを持つ意味のあるかたまりを記述できます。
見出しを付けられないなら`section`ではなく`div`のままでかまいません。

```html
<!-- div -->
<div class="section">
    <div class="heading">機能一覧</div>
    <p>...</p>
</div>
```

これまでは`.section`クラスを作るのが一般的でした。

:::{seealso}

- [](./html-section.md)

:::

## 補足したい（`aside`）

```html
<!-- セマンティクス -->
<aside class="sidebar">
    <section>
        <h2>カテゴリ</h2>
        <ul>...</ul>
    </section>
</aside>
```

`aside`タグで、本筋から外れた補足（サイドバー、関連記事、余談）を記述できます。

```html
<!-- div -->
<div class="sidebar">
    <div class="widget">カテゴリ一覧</div>
</div>
```

これまでは`.sidebar`クラスを作るのが一般的でした。

:::{seealso}

- [](./html-aside.md)

:::

## フッターしたい（`footer`）

```html
<!-- セマンティクス -->
<footer>
    <p>&copy; 2024</p>
</footer>
```

`footer`タグで、まとまりの末尾に置く補足情報（コピーライト、フッターナビ）を記述できます。

```html
<!-- div -->
<div class="footer">
    <div class="copyright">&copy; 2024</div>
</div>
```

これまでは`.footer`クラスを作るのが一般的でした。

:::{seealso}

- [](./html-footer.md)

:::

## div のまま残すもの

```html
<div class="grid">
    <article>...</article>
    <article>...</article>
</div>
```

意味を持たず、単にCSSのグリッドやFlexboxのためにまとめたいだけなら`div`が正解です。
すべてを意味のあるタグに置き換える必要はありません。

## リファレンス

- [セマンティクス](https://developer.mozilla.org/ja/docs/Glossary/Semantics)
- [コンテンツカテゴリー](https://developer.mozilla.org/ja/docs/Web/HTML/Guides/Content_categories)
- [HTML 要素リファレンス](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements)
- [HTML によるコンテンツの構造化](https://developer.mozilla.org/ja/docs/Learn_web_development/Core/Structuring_content)
