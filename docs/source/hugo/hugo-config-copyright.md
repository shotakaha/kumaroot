# 著作権表示したい（``.Site.Copyright``）

```html
©️サイト名 年
```

ウェブサイトのフッターには著作権を表示することが多いです。
もっともシンプルなものは上記の通りだと、僕は考えます。

```html
&copy; {{ with .Site.Copyright | default .Site.Title }} {{ . | safeHTML }} {{ now.Format "2006" }} {{ end }}
```

```html
&copy; {{ with .Site.Copyright | default .Site.Title }} {{ . | safeHTML }} {{ with .Site.Params.since }}{{ . }} -- {{ end }} {{ now.Format "2006" }} {{ end }}
```


```toml
# hugo.toml
title = "ウェブサイト名"
copyright = "著作権表示"

[params]
since = "プロジェクト開始日"
```
