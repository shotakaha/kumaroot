# ヘッドしたい（``/layouts/partials/head.html``）

```html
{{ $title := "" }}
{{ $description := "" }}

{{- if .IsHome -}}
    {{- $title = .Site.Title -}}
{{- else -}}
    {{- $title = printf "%s | %s" .Title .Site.Title -}}
{{- end -}}

{{- if .Description - }}
    {{- $description = .Description -}}
{{- else .IsPage - }}
    {{- $description = .Summary -}}
{{- else -}}
    {{- $description = .Site.Params.description -}}
{{- end -}}

<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{ $title }}</title>
<meta name="description" content="{{ $description }}">

{{ hugo.Generator }}

<link rel="canonical" href="{{ .Permalink }}">

{{- block "robots" . -}}
    <meta name="robots" content="index,follow">
    <meta name="googlebot" content="index,follow">
{{- end -}}

<!-- Googleフォントを読み込む（あとで追加する）-->
<!-- CSSを読み込む（あとで追加する）-->
<!-- JSを読み込む（あとで追加する）-->

{{ template "_internal/google_analytics.html" . }}
```

``<head>``タグで読み込む部分テンプレートです。
