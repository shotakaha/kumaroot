# カスタム404したい（``/layouts/404.html``）

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
