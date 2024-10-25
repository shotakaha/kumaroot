# ページ割り設定したい（`[pagination]` / `pagination.toml`）

```toml
# hugo.toml
[pagination]
pageSize = 10
path = "page"
```

`[pagination]`セクションでページ割りを設定できます。
デフォルトのページ割りは10ページ／記事ごとになっています。

:::{note}

これまでは以下のように`paginate`キーで設定していました。

```toml
# hugo.toml
paginate = 10
paginatePath = "page"
```

`v0.128.0`からdeprecatedになり、将来的に削除される予定だそうです。

:::

## 記事一覧に追加したい

```html
<!-- /layouts/_default/list.html -->
{{ template "_internal/pagination.html" . }}
{{ range .Paginator.Pages }}
    {{ .Title }}
{{ end }}
```

## 前後の記事を追加したい

```html
<head>
    <link rel="prev" href="前の記事のパーマリンク">
    <link rel="next" href="次の記事のパーマリンク">
</head>
```

```html
<nav>
    <ul>
        <li><a rel="prev" href="前の記事のパーマリンク">前の記事</li>
        <li><a rel="next" href="次の記事のパーマリンク">次の記事</li>
    </ul>
</nav>
```

## リファレンス

- [Pagination - Templates - gohugo.io](https://gohugo.io/templates/pagination/)
