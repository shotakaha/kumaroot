# タクソノミーしたい（``.Site.Taxonomies``）

/config/_default/hugo.toml
:   ```toml
    [taxonomies]
    category = "categories"
    tag = "tags"
    author = "authors"  # 追加したタクソノミー
    group = "groups"    # 追加したタクソノミー
    ```

/content/記事/index.md
:   ```toml
    title = "記事のタイトル"
    authors = ["名前1", "名前2"]
    groups = ["グループ1", "グループ2"]
    ```

/layouts/partials/taxonomy.html
:   ```go
    {{ range $taxonomy, $terms := .Site.Taxonomies }}
    {{ end }}
    ```

## リファレンス

- [Taxonomies - gohugo.io](https://gohugo.io/content-management/taxonomies/)
- [Taxonomy templates - gohugo.io](https://gohugo.io/templates/taxonomy-templates/)
- [Taxonomies - gohugo.io](https://gohugo.io/methods/site/taxonomies/)
