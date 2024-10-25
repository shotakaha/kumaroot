# タクソノミー設定したい（`[taxonomies]` / `taxonomies.toml`）

```toml
# /config/_default/hugo.toml
[taxonomies]
category = "categories"
tag = "tags"
author = "authors"  # 追加したタクソノミー
group = "groups"    # 追加したタクソノミー
```

`[taxonomies]`セクションでタクソノミーを設定します。
デフォルトで`category`と`tag`が有効です。

## テンプレートしたい（`.Site.Taxonomies`）

```go
// /layouts/partials/taxonomy.html
{{ range $taxonomy, $terms := .Site.Taxonomies }}
{{ end }}
```

`.Site.Taxonomies`でタクソノミーのアクセスできます。
タクソノミーは**分類**（taxonomy）と**項目**（terms）のマップ型になっています。

## ページ設定したい

```toml
title = "記事のタイトル"
authors = ["名前1", "名前2"]
groups = ["グループ1", "グループ2"]
```

タクソノミーはページのfront matterで設定できます。
`authors`や`groups`が分類で、その配列の要素が項目です。

## リファレンス

- [Taxonomies - gohugo.io](https://gohugo.io/content-management/taxonomies/)
- [Taxonomy templates - gohugo.io](https://gohugo.io/templates/taxonomy-templates/)
- [Taxonomies - gohugo.io](https://gohugo.io/methods/site/taxonomies/)
