# 日付フォーマットしたい（``.Format``）

```html
{{ now.Format "2006" }}
```

[.Format](https://gohugo.io/methods/time/format/)関数を使って日付フォーマットできます。
フォーマット文字列は設定ファイルで定義できます。

```html
{{ now.Format .Site.Params.date_format }}
```

```toml
[params]
date_format = "2006-01-02"
```

## ISO8601形式にしたい

```html
{{- $iso8601 := "2006-01-02T15:04:05-07:00" -}}
{{ with .PublishDate }}{{ .Format $iso8601 | printf "%q" | safeHTMLAttr }}{{ end }}
```

[Schema用](https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/schema.html)の内部テンプレートからISO8601形式に変換している箇所を抜粋しました。
ウェブ標準などで日付フォーマットが定まっている場合は、このようにテンプレート内で固定するとよさそうです。
