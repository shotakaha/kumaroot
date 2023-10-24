# メタ情報したい（``/layouts/partials/meta.html``）

```html
{{ block "meta" . }}
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="ページの説明">
<meta name="author" content="ページの著者名">
<meta name="keywords" content="関連する単語, 関連する単語">
<meta name="theme-color" content="">
<meta name="color-scheme" content="light dark">
{{ end }}
```

[標準メタデータ名](https://developer.mozilla.org/ja/docs/Web/HTML/Element/meta/name)の部分テンプレートです。
