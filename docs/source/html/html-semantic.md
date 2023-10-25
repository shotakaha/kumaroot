# セマンティクスしたい（semantics）

```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>ページのタイトル | サイト名</title>
    </head>

    <body>
        <header>
            <nav>
                <!-- グローバルナビゲーション -->
            </nav>
        </header>

        <main>
            <article>
                <header>
                    <h1>ページのタイトル</h1>
                    <time>公開日</time>
                </header>

                <figure>
                    <img src="#">
                    <figcaption>図のキャプション／クレジット</figcaption>
                </figure>

                <section>
                    <h2>章見出し1</h2>
                    <p>本文本文本文本文本文</p>

                    <h3>節見出し2</h3>
                    <p>本文本文本文本文本文</p>
                    <blockquote>引用引用引用引用引用引用</blockquote>
                </section>

                <section>
                    <h2>賞見出し2</h2>
                    <p>本文</p>
                </section>

                <footer>
                    <!-- 執筆者の情報 -->
                </footer>
            </article>

            <aside>
                <h2>関連記事</h2>
                <article>
                    <h3>関連記事のタイトル</h3>
                    <time>公開日</time>
                </article>
                <article>
                    <h3>関連記事のタイトル</h3>
                    <time>公開日</time>
                </article>
                <article>
                    <h3>関連記事のタイトル</h3>
                    <time>公開日</time>
                </article>
            </aside>

        </main>

        <aside>
            <!-- サイドバー -->
        </aside>

        <footer>
            <header>ロゴ</header>
            <nav>
                <!-- メガフッター -->
            </nav>
            <footer>コピーライト</footer>
        </footer>

    </body>
</html>
```

HTMLの[セマンティクス](https://developer.mozilla.org/ja/docs/Glossary/Semantics)は、文書構造を基に、適切なタグを割り当てることです。
タグ割り当ては具体的に定義されておらず、作成者やユースケースに依存しています。
[コンテンツカテゴリー](https://developer.mozilla.org/ja/docs/Web/HTML/Content_categories)の区分を参考にするとよいと思います。

上記のサンプルも、僕の解釈で作成したものです。
以下のような対応で、よくあるHTMLマークアップの変換を考えています。

| よくあるHTMLタグ | セマンティクスを意識したタグ |
|---|---|
| ``<div id="main">`` | ``<main>`` |
| ``<div class="sidebar">`` | ``<aside class="related">`` |
| ``<div class="related_pages">`` | ``<aside class="related_pages">`` |
| ``<div class="nav">`` | ``<nav>`` |
| ``<div class="footer">`` | ``<footer>`` |
| ``<span class="published">`` | ``<time class="published">`` |

:::{note}

LaTeXで文書を作成したり、WordやGoogleドキュメントのアウトライン機能やスタイル機能を使ったりするのと、作業工程の感覚が同じだなぁと思っています。

:::

## メタデータ・コンテンツ

``<head>``タグ内に記述するタグです。
文書の文字エンコーディングやページのタイトル、読み込むスタイルシートなどを設定できます。

- [title](https://developer.mozilla.org/ja/docs/Web/HTML/Element/title)
- [meta](https://developer.mozilla.org/ja/docs/Web/HTML/Element/meta)
- [link](https://developer.mozilla.org/ja/docs/Web/HTML/Element/link)
- [script](https://developer.mozilla.org/ja/docs/Web/HTML/Element/script)

## フロー・コンテンツ

``<body>``タグ内に記述できるタグです。
いろいろあります。

## 区分（sectioning）・コンテンツ

``<body>``タグ内に記述するタグです。
文書のアウトライン（やセクション）を構成するタグです。

- [nav](https://developer.mozilla.org/ja/docs/Web/HTML/Element/nav)
- [article](https://developer.mozilla.org/ja/docs/Web/HTML/Element/article)
- [section](https://developer.mozilla.org/ja/docs/Web/HTML/Element/section)
- [aside](https://developer.mozilla.org/ja/docs/Web/HTML/Element/aside)

## 見出し（heading）・コンテンツ

セクションの見出しのためのタグです。
``hgroup``は

- [h1 - h6](https://developer.mozilla.org/ja/docs/Web/HTML/Element/Heading_Elements)
- [hgroup](https://developer.mozilla.org/ja/docs/Web/HTML/Element/hgroup)（非推奨みたい）

## 記述（phrasing）・コンテンツ

本文を記述するためのタグです。
記述コンテンツが集まって段落を構成します。

## 埋め込み（embedded）・コンテンツ

文書に画像や動画などを埋め込むためのタグです。

- [img](https://developer.mozilla.org/ja/docs/Web/HTML/Element/img)
- [embed](https://developer.mozilla.org/ja/docs/Web/HTML/Element/embed)
- [audio](https://developer.mozilla.org/ja/docs/Web/HTML/Element/audio)
- [video](https://developer.mozilla.org/ja/docs/Web/HTML/Element/video)
- [iframe](https://developer.mozilla.org/ja/docs/Web/HTML/Element/iframe)
