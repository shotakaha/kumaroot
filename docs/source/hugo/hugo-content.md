# コンテンツしたい（`/content/`）

```{toctree}
---
maxdepth: 1
---
hugo-content-links
hugo-content-figure
hugo-content-shortcodes
hugo-content-youtube
```

## フロントマターしたい

```{toctree}
---
maxdepth: 1
---
hugo-frontmatter
hugo-frontmatter-title
hugo-frontmatter-date
hugo-frontmatter-images
hugo-frontmatter-taxonomies
```

## 設定ファイルしたい（`contentDir`）

```toml
# hugo.toml
contentDir = "content"
defaultContentLanguage = "ja"
defaultContentLanguageInSubdir = false
hasCJKLanguage = true
summaryLength = 50
enableEmoji = true
```

コンテンツに関連しそうな設定を選んでみました。

## リファレンス

- [Content Management](https://gohugo.io/content-management/)
