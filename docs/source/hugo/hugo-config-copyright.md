# 著作権表示したい（`copyright`）

```toml
# hugo.toml
copyright = "©️サイト名 年"
```

ウェブサイトのフッターに著作権を表示するサンプルです。
もっともシンプルなものは上記の通りだと、僕は考えます。

## テンプレートしたい（`.Site.Copyright`）

```html
<p>{{ .Site.Copyright }}</p>
```

`{{ .Site.Copyright }}`でサイト全体の著作権を表示できます。

## カスタマイズしたい（`.params.copyright`）

```toml
# hugo.toml
title = "サイト全体のタイトル"
copyright = "サイト名 年"

[params]
copyright = "サイト名 年"
since = "プロジェクト開始年"
license = "MIT"
cc = "CC-BY"
```

著作権表示をよりカスタマイズしたい場合は、
`[params]`セクションに作成します。

```html
&copy; {{ with .Site.Copyright | default .Site.Title }} {{ . | safeHTML }} {{ with .Site.Params.since }}{{ . }} -- {{ end }} {{ now.Format "2006" }} {{ end }}
```
