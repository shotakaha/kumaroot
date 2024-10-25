# 日付フォーマットしたい（`params.date_format`）

```toml
# hugo.toml
[params]
date_format = "2006-01-02"
```

`[params]`セクションで日付フォーマットを設定します。

## テンプレートしたい（`.Date.Format`）

```html
{{ .Date.Format .Site.Params.date_format }}
```

[.Date.Format](https://gohugo.io/methods/time/format/)関数を使って日付フォーマットできます。
フォーマット文字列は設定ファイルで定義します。

/content/記事/index.md
:   ```toml
    date = "2024-04-30T15:30:34+09:00"
    ```

## ISO8601形式にしたい

```html
{{- $iso8601 := "2006-01-02T15:04:05-07:00" -}}
{{ with .PublishDate }}{{ .Format $iso8601 | printf "%q" | safeHTMLAttr }}{{ end }}
```

[Schema用](https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/schema.html)の内部テンプレートからISO8601形式に変換している箇所を抜粋しました。
ウェブ標準などで日付フォーマットが定まっている場合は、このようにテンプレート内で固定するとよさそうです。

## コピーライト表示したい

/config/_default/params.toml
:   ```html
    [footer]
    showCopyright = true
    ```

/layouts/partials/copyright.html
:   ```html
    {{ if .Site.Params.footer.showCopyright | defaut true }}
    <div class="copyright">
        <span>&copy; {{ now.Format "2006" }}</span>
    </div>
    {{ end }}
    ```

フッター領域のコピーライト表示に「年」を併記したい場合を想定したサンプルです。
複数のテンプレートで利用したいので、部分テンプレートとして作成しました。
また、設定ファイルで非表示に設定できるようにしてあります。

## リファレンス

- [Date - gohugo.io](https://gohugo.io/methods/page/date/)
- [Format - gohugo.io](https://gohugo.io/methods/time/format/)
