# メタデータしたい（``/layouts/partials/head.html``）

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

{{ template "_internal/opengraph.html" . }}
{{ template "_internal/google_analytics.html" . }}
```

[head](https://developer.mozilla.org/ja/docs/Web/HTML/Element/head)タグで読み込む部分テンプレートです。

## 文字エンコーディングを宣言したい

```html
<meta charset="utf-8">
```

文字エンコーディングは``UTF-8``にします。
これはハードコードしておいてよいでしょう。

## ビューポートを設定したい

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

ビューポートの初期値を設定します。
モバイル端末で表示するための設定です。

## タイトルを設定したい

```html
<title>{{ .Title }}</title>
```

[title](https://developer.mozilla.org/ja/docs/Web/HTML/Global_attributes/title)でドキュメントのタイトルを設定します。

シンプルに``{{ .Title }}``を呼ぶだけでもOKですが、検索結果などに使われるため、サイト名も併記している場合が多いです。
トップページでは``サイト名``、その他のページでは``ページのタイトル | サイト名``などとする場合は、条件分岐させます。
