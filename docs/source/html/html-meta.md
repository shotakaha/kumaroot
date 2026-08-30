# メタ情報したい（`meta`）

```html
<head>
    <meta charset="utf-8">
    <meta name="description" content="サイトの説明">
    <meta name="viewport" content="width=device-width">

    <!-- name属性は自由なキーを設定できる -->
    <meta name="キー" content="値">
</head>
```

メタ情報は`head`タグの中に記述します。
`meta`タグを使ってkey-valueペアで設定します。

:::{seealso}

- [](./html-head.md)
- [](./html-meta-ogp.md)

:::

## 文字エンコーディングしたい（`charset`）

```html
<meta charset="utf-8">
```

`charset`キーで、文書の文字エンコーディングを設定できます。
HTML標準で使えるのは`utf-8`のみです。

この宣言は省略不可で、`head`の最初の方（`title`より前）に書いておく必要があります。

## サイト説明したい（`description`）

```html
<meta name="description" content="サイトの説明">
```

`description`キーで、ページの内容を要約する説明文を設定できます。
`content`に設定できる値は任意の文字列です。
省略すると、検索エンジンが本文から抜粋してスニペットを作ります。

検索結果のスニペットとして表示されることがあるため、ページごとに簡潔で具体的な説明を書いておくとよいです。

## クロール制御したい（`robots`）

```html
<meta name="robots" content="index,follow">
```

`robots`キーで、検索エンジンのクローラーへの指示を設定できます。
`content`に設定できる値は
`index`/`noindex`（インデックスするか）と
`follow`/`nofollow`（リンクを辿るか）の
組み合わせです。
デフォルトは`index,follow`です。

下書きページや検索結果に出したくないページには`noindex`を明示しておくとよいです。

## ビューポートしたい（`viewport`）

```html
<meta name="viewport" content="width=device-width">
```

`viewport`キーで、
[ビューポート](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/meta/name/viewport)
のサイズを設定できます。
`content`に設定できる値は
`width`（表示幅）や
`initial-scale`（初期表示倍率）などのカンマ区切りです。
省略するとブラウザ標準のレイアウト幅で表示されます。

画面の幅はデバイスによって異なるため、`width=device-width`を設定しておきましょう。
よく`initial-scale=1`を書いているサンプルがありますが、`initial-scale`のデフォルトは1倍なので省略してよいと思います。

## リダイレクトしたい

```html
<meta http-equiv="refresh" content="秒数;url=リダイレクト先のURL">
```

`http-equiv="refresh"`キーで、ページのリダイレクトを設定できます。
`content`に設定できる値は「待機秒数」と「リダイレクト先URL」をセミコロンでつないだ文字列です。

:::{warning}

`meta`によるリダイレクトは、利用者の予告なくページが切り替わるためアクセシビリティ上の問題があります。
サーバー側で301／302リダイレクトを設定できる場合は、そちらを使うほうがよいです。

:::

## リファレンス

- [meta](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/meta)
- [meta name="viewport"](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/meta/name/viewport)
- [Robots \<meta\> tag](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)
