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

- [PAGE.Title](https://gohugo.io/methods/page/title/)
- [PAGE.LinkTitle](https://gohugo.io/methods/page/linktitle/)
- [PAGE.Permalink](https://gohugo.io/methods/page/permalink/)
- [PAGE.RelPermalink](https://gohugo.io/methods/page/relpermalink/)
