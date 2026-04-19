# Quartoの使い方

`Quarto`は、`qmd`形式の拡張Markdownファイルを使って、
ドキュメントやスライドを作成できるツールです。

```yaml
# /._quarto.yml
project:
  type: website
  output-dir: _site
  render:
    - "docs/**/*.qmd"

website:
  title: "Quartoの使い方"
  description: "Quartoの基本的な使い方"
  navbar:
    left:
      - href: docs/index.qmd
        text: Home
      - href: docs/about.qmd
        text: About

format:
  html:
    theme: cosmo
    toc: true
    mainfont: "Noto Sans JP"
    include-in-header: |
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP&display=swap">
  typst:
    mainfont: "Hiragino Sans"
    include-before-body: templates/preamble.typ  ## Typstの設定を別ファイルに分離
```

```{toctree}
---
maxdepth: 1
---
quarto-install
quarto-frontmatter
quarto-preview
quarto-render
```
