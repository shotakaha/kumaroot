# ページタイトルしたい（`title` / `linkTitle`）

```toml
title = "ページのタイトル"
linkTitle = "リンク用のタイトル"
```

ページのタイトルはfront matterの`title`で設定します。
`linkTitle`でリンク用の（短い）タイトルを設定できます。

## テンプレートしたい（`.Title` / `.LinkTitle`）

```html
<h1>{{- .Title -}}</h1>
```

`{{ .Title }}`でページにタイトルを表示できます。

```html
<a href="{{ .RelPermalink }}">{{- .LinkTitle -}}</a>
```

`{{ .LinkTitle }}`でリンク用のタイトルを表示できます。
`.LinkTitle`が設定されてない場合は`.Title`が適用されます。

## リファレンス

- [Title - Page Methods - gohugo.io](https://gohugo.io/methods/page/title/)
- [LinkTitle - Page Methods - gohugo.io](https://gohugo.io/methods/page/linktitle/)
