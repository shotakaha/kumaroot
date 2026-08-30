# ヘッド情報したい（`head`）

```html
<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>ページタイトル | サイト名</title>
        <link rel="stylesheet" href="/style.css">
    </head>
    <body>
        ...
    </body>
</html>
```

`head`タグは、そのページの情報（メタデータ）をまとめて書く場所です。
`html`タグの直下、`body`タグの前に1つだけ置きます。

`head`の中身は画面に表示されません。
ページのタイトル、文字コード、読み込むCSSやJavaScript、検索エンジン向けの説明などを書きます。

このうち`meta`タグで指定するもの（文字コード、ページの説明、OGPなど）は [メタ情報したい（`meta`）](html-meta.md) にまとめています。

## タイトルを指定したい（`title`）

```html
<head>
    <title>記事のタイトル | サイト名</title>
</head>
```

`title`タグで、ページのタイトルを指定します。

タイトルはブラウザのタブ、ブックマーク名、検索結果の見出しに使われます。
「ページ固有の名前 | サイト名」の形にすると、どのページを見ているか分かりやすくなります。

## CSSを読み込みたい（`link`）

```html
<head>
    <link rel="stylesheet" href="/style.css">
</head>
```

`link`タグで、外部のCSSファイルを読み込みます。
`rel="stylesheet"`でスタイルシートだと伝え、`href`にファイルのパスを指定します。

ファビコン（タブのアイコン）も`link`タグで指定します。

```html
<link rel="icon" href="/favicon.ico">
```

## JavaScriptを読み込みたい（`script`）

```html
<head>
    <script src="/main.js" defer></script>
</head>
```

`script`タグで、外部のJavaScriptファイルを読み込みます。

`head`の中に書く場合は`defer`を付けます。
`defer`があると、HTMLの読み込みを止めずにダウンロードし、HTMLを読み終えてから実行します。

:::{seealso}

- [](./html-html.md)
- [](./html-body.md)
- [](./html-meta.md)

:::

## リファレンス

- [head](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/head)
- [title](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/title)
- [link](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/link)
- [script](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/script)
