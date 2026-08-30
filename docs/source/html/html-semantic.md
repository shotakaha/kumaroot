# セマンティクスしたい（semantics）

```html
<!-- div だけで組み立てた例 -->
<div class="header">
    <div class="nav">...</div>
</div>
<div class="main">
    <div class="article">...</div>
    <div class="sidebar">...</div>
</div>
<div class="footer">...</div>
```

```html
<!-- セマンティクスを意識した例 -->
<header>
    <nav>...</nav>
</header>
<main>
    <article>...</article>
    <aside class="sidebar">...</aside>
</main>
<footer>...</footer>
```

[セマンティクス](https://developer.mozilla.org/ja/docs/Glossary/Semantics)とは、「その部分が何なのか」に合ったHTMLタグを選ぶことです。

上の2つは、CSSを当てれば同じ見た目になります。
ですが`<div class="nav">`はブラウザにとって「ただの箱」で、
`<nav>`は「ここはナビゲーション」という意味が伝わります。

## なぜセマンティクスを意識するのか

意味の通ったタグを使うと、次の効果があります。

- スクリーンリーダーが、ランドマークや見出しを頼りにページ内を移動できる
- 検索エンジンがページの構造を理解しやすくなる
- CSSやJavaScriptから要素を指すとき、見た目用のクラス名に依存せず安定する
- HTMLを読むだけで文書構造を追える（未来の自分や他の人が助かる）

`<div>`をたくさん並べたHTMLは、見た目は作れても、これらの情報が失われます。

## どう判断するのか

タグを選ぶときは、次の順番で考えます。

1. そのまとまりが何かを言葉にする（ナビゲーション、補足、記事、章…）
2. 対応するタグがあれば使う（`nav`、`aside`、`article`、`header`、`footer`…）
3. 対応するタグがなく、見出しを付けられるなら`section`、付けられないなら`div`
4. タグだけで伝えきれない部分は`aria-*`属性で補う（[アクセシビリティしたい](html-a11y.md)）

:::{note}

セマンティクスに「唯一の正解」はありません。
[コンテンツカテゴリー](https://developer.mozilla.org/ja/docs/Web/HTML/Guides/Content_categories)を参考にしつつ、作成者が文書構造をどう捉えるかで決まります。
LaTeXの文書構造や、Wordのアウトライン・スタイル機能で見出しを組むのと同じ感覚です。

:::

## ヘッダーしたい

```html
<!-- div -->
<div class="header">
    <div class="logo">サイト名</div>
    <div class="nav">...</div>
</div>
```

```html
<!-- セマンティクス -->
<header>
    <a href="/" class="logo">サイト名</a>
    <nav>...</nav>
</header>
```

ページ冒頭のロゴやナビゲーションのまとまりは`header`にします。
詳しくは [ヘッダーしたい（`header`）](html-header.md) を参照してください。

## ナビゲーションしたい

```html
<!-- div -->
<div class="nav">
    <div class="nav-item"><a href="/">ホーム</a></div>
    <div class="nav-item"><a href="/blog">ブログ</a></div>
</div>
```

```html
<!-- セマンティクス -->
<nav aria-label="メインメニュー">
    <ul>
        <li><a href="/">ホーム</a></li>
        <li><a href="/blog">ブログ</a></li>
    </ul>
</nav>
```

主要なリンク集は`nav`で囲み、リンクは`ul`と`li`で並べます。
詳しくは [ナビゲーションしたい（`nav`）](html-nav.md) を参照してください。

## メインコンテンツしたい

```html
<!-- div -->
<div id="content">
    ...
</div>
```

```html
<!-- セマンティクス -->
<main>
    ...
</main>
```

そのページの中心的な内容は`main`で囲みます。表示される`main`は1ページに1つです。
詳しくは [メインコンテンツしたい（`main`）](html-main.md) を参照してください。

## 記事したい

```html
<!-- div -->
<div class="article">
    <div class="title">記事のタイトル</div>
    <div class="body">本文...</div>
</div>
```

```html
<!-- セマンティクス -->
<article>
    <h1>記事のタイトル</h1>
    <p>本文...</p>
</article>
```

それ単体で完結するまとまり（記事、投稿、商品カード）は`article`にします。
タイトルは`div`ではなく見出しタグ（`h1`〜`h6`）を使います。
詳しくは [記事したい（`article`）](html-article.md) を参照してください。

## 章・節したい

```html
<!-- div -->
<div class="section">
    <div class="heading">機能一覧</div>
    <p>...</p>
</div>
```

```html
<!-- セマンティクス -->
<section>
    <h2>機能一覧</h2>
    <p>...</p>
</section>
```

見出しを持つ意味のあるかたまりは`section`にします。
見出しを付けられないなら`section`ではなく`div`のままでかまいません。
詳しくは [章・節したい（`section`）](html-section.md) を参照してください。

## 補足したい

```html
<!-- div -->
<div class="sidebar">
    <div class="widget">カテゴリ一覧</div>
</div>
```

```html
<!-- セマンティクス -->
<aside class="sidebar">
    <section>
        <h2>カテゴリ</h2>
        <ul>...</ul>
    </section>
</aside>
```

本筋から外れた補足（サイドバー、関連記事、余談）は`aside`にします。
詳しくは [補足したい（`aside`）](html-aside.md) を参照してください。

## フッターしたい

```html
<!-- div -->
<div class="footer">
    <div class="copyright">&copy; 2024</div>
</div>
```

```html
<!-- セマンティクス -->
<footer>
    <p>&copy; 2024</p>
</footer>
```

まとまりの末尾に置く補足情報（コピーライト、フッターナビ）は`footer`にします。
詳しくは [フッターしたい（`footer`）](html-footer.md) を参照してください。

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
