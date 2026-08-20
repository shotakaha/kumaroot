# タイトルしたい（`.Title`）

```toml
# /content/記事/index.md
title = "記事のタイトル"
```

```go
<h1>{{ .Title }}</h1>
```

```html
<h1>記事のタイトル</h1>
```

フロントマターの`title`で指定した値は、`.Title`ページ変数でテンプレートから取得できます。

## Emojiしたい（`emojify`）

```toml
# /content/記事/index.md
title = "記事のタイトル :heart:"
```

```go
<h1>{{ .Title | emojify }}</h1>
```

```html
<h1>記事のタイトル ❤️</h1>
```

`emojify`関数にパイプすると、`:heart:`のようなGitHub風の絵文字コードを実際の絵文字に変換できます。
`hugo.toml`で`enableEmoji = true`を設定しておく必要があります。

## 短いタイトルしたい（`.LinkTitle`）

```toml
# /content/記事/index.md
title = "記事のとても長いタイトル"
linkTitle = "短いタイトル"
```

```go
<a href="{{ .RelPermalink }}">{{ .LinkTitle }}</a>
```

```html
<a href="/記事/">短いタイトル</a>
```

一覧ページやナビゲーションなど、`.Title`をそのまま使うと長すぎる場合に、`.LinkTitle`で別のタイトルを指定できます。
`linkTitle`を指定しなかった場合は`.Title`の値がそのまま使われます。

## 単語の頭文字を大文字にしたい（`strings.Title`）

```go
{{ strings.Title "hello world" }}
```

```html
Hello World
```

`strings.Title`関数で、文字列中の各単語の頭文字を大文字にできます。
`.Title`ページ変数とは別物（Go言語の`strings`パッケージに由来する文字列操作関数）なので、名前が紛らわしい点に注意してください。

## リファレンス

- [Title - gohugo.io](https://gohugo.io/methods/resource/title/)
- [LinkTitle - gohugo.io](https://gohugo.io/methods/page/linktitle/)
- [strings.Title - gohugo.io](https://gohugo.io/functions/strings/title/)
- [transform.Emojify - gohugo.io](https://gohugo.io/functions/transform/emojify/)
- [Single page templates - gohugo.io](https://gohugo.io/templates/single-page-templates/)
