# カスタム404したい（`/layouts/404.html`）

```html
{{- define "robots" -}}
    <meta name="robots" content="noindex,nofollow">
    <meta name="googlebot" content="noindex,nofollow">
{{- end -}}

{{ define "main" }}
<section>
    <!-- Not Found 時の案内 -->
</section>
{{ end }}
```

404ページをカスタマイズできます。
クローラーに収集されないように設定してあります。

:::{caution}

`{{ define "robots" }}`が実際に出力されるには、
[ベーステンプレート](./hugo-layouts-baseof.md)側に対応する`{{ block "robots" . }}{{ end }}`を`<head>`内に追加しておく必要があります。
`block`がない場合、`define`側の内容はエラーにならずに黙って無視されるので注意してください。

:::

## リファレンス

- [block](https://gohugo.io/functions/go-template/block/)
- [define](https://gohugo.io/functions/go-template/define/)
- [Base templates](https://gohugo.io/templates/base/)
