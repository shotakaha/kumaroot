# 日付フォーマットしたい（``.Format``）

```html
{{ now.Format "2006" }}
```

[.Format](https://gohugo.io/functions/format/)関数を使って日付フォーマットできます。
フォーマット文字列は設定ファイルで定義できます。

```html
{{ now.Format .Site.Params.date_format }}
```

```toml
[params]
date_format = "2006-01-02"
```
