# 全体設定したい（`_quarto.yml`）

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

Quartoのプロジェクト全体の設定は、プロジェクトルートに配置した`_quarto.yml`に記述します。
このファイルには、プロジェクトのメタデータや、出力形式ごとの設定を記述できます。

上記のサンプルでは
HTML出力に対してCosmoテーマを使用し、目次を有効にし、`Noto Sans JP`フォントを指定しています。
また、Typst出力に対しては`Hiragino Sans`フォントを指定し、
さらにTypstの設定を別ファイル`templates/preamble.typ`から読み込んでいます。
