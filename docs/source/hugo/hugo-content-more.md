# リード文したい（`<!--more-->`）

```markdown
リード文。リード文。リード文。リード文。リード文。
リード文。リード文。リード文。リード文。リード文。

<!--more-->

本文。本文。本文。本文。本文。本文。本文。本文。
本文。本文。本文。本文。本文。本文。本文。本文。
本文。本文。本文。本文。本文。本文。本文。本文。
```

`<!--more-->`で本文を区切ることで、リード文を定義できます。

## テンプレートしたい（`.Summary`）

```html
{{ range .Pages }}
  <h2><a href="{{ .RelPermalink }}">{{ .LinkTitle }}</a></h2>
  {{ .Summary }}
  {{ if .Truncated }}
    <a href="{{ .RelPermalink }}">続きを読む...</a>
  {{ end }}
{{ end }}
```

`.Summary`でリード文を表示できます。
上のサンプルはページのタイトルとリード文の一覧を表示できます。
実用としては、これにグリッド形式やカード形式のタグ／クラス属性を追加して整列させるとよいです。

## リファレンス

- [Content summaries](https://gohugo.io/content-management/summaries/)
- [PAGE.Summary](https://gohugo.io/methods/page/summary/)
