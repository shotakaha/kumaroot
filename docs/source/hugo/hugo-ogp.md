# OGPを設定したい（``/layouts/partials/head.html``）

```go
{{ template "_internal/opengraph.html" . }}
```

Hgoの[内部テンプレート](https://gohugo.io/templates/internal/)を使ってOGPを設定できます。
[_internal/opengraph.html](https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/opengraph.html)を``head``用の部分テンプレートに書いておけばOKです。

OGP画像などの設定は、サイト全体の設定ファイル（{file}`config.toml`）
もしくは各コンテンツのフロントマターで設定します。
設定できる項目は、ドキュメントでは網羅されていないため、内部テンプレート（``opengraph.html``）のソースを直接確認したほうがよいです。

## サイト全体のOGP

```toml
[params]
description = "サイトの説明"
images = ["画像1", "画像2"]
title = "サイトのタイトル"

[taxonomies]
series = "series"
```

サイト全体のOGPは``config.toml``に整理します。

## ``og:title``したい

```html
<meta property="og:title" content="{{ .Title }}" />
```

``og:title``は``config.toml``やフロントマターの``title``で設定します。

## ``og::description``したい

```html
<meta property="og:description" content="{{ with .Description }}{{ . }}{{ else }}{if .IsPage}}{{ .Summary }}{{ else }}{{ with .Site.Params.description }}{{ . }}{{ end }}{{ end }}{{ end }}" />
```

``og:description``はフロントマターの``description``で設定します。
``description``が設定されていない場合、個別ページの場合は``summary``、それ以外（＝一覧ページなど）は``config.toml``に設定した``params.description``が適用されます。

## ``og:type``したい

```html
<meta property="og:type" content="{{ if .IsPage }}article{{ else }}website{{ end }}" />
```

``og:type``は自分で設定する必要はありません。
ページのタイプに応じて自動で適用されます。

## ``og:url``したい

```html
<meta property="og:url" content="{{ .Permalink }}" />
```

``og:url``は自分で設定する必要はありません。
ページのパーマリンク（＝絶対URL）が自動で適用されます。

## ``og:image``したい

```html
{{- with $.Params.images -}}
{{- range first 6 . }}<meta property="og:image" content="{{ . | absURL }}" />{{ end -}}
{{- else -}}
{{- $images := $.Resources.ByType "image" -}}
{{- $featured := $images.GetMatch "*feature*" -}}
{{- if not $featured }}{{ $featured = $images.GetMatch "{*cover*,*thumbnail*}" }}{{ end -}}
{{- with $featured -}}
<meta property="og:image" content="{{ $featured.Permalink }}"/>
{{- else -}}
{{- with $.Site.Params.images }}<meta property="og:image" content="{{ index . 0 | absURL }}"/>{{ end -}}
{{- end -}}
{{- end -}}
```

フロントマターの``images``で画像を設定できます。
ソースコードを確認すると、最大6枚の画像を適用できます。

また、コンテンツファイルと同じディレクトリにある画像ファイルがある場合、
ファイル名に``*feature*``、``*cover*``、``*thumbnail*``を含む画像ファイルが自動で適用されます。

上記が設定されていない場合は、``config.toml``の``params.images``の画像が適用されます。
``params.images``は複数枚設定できますが、``og:image``として利用できるのは最初の1枚だけです。

## リファレンス



- [The Open Graph Protocol](https://ogp.me/)
