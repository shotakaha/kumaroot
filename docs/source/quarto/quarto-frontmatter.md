# フロントマターしたい

```yaml
---
title: ""
description: ""
author: ""
date: 2026-04-19
date-modified: last-modified
format:
  html:
    toc: true
    number-sections: true
  typst:
    toc: true
    number-sections: true
---

## 見出し

本文
```

`.qmd`ファイルの先頭に、YAML形式のフロントマターを記述できます。
フロントマターは、ドキュメントのメタデータを定義するための特殊なエリアです。
記事のタイトル（`title`）の他に、
簡単な説明（`description`）や著者（`author`）、
公開日（`date`）、更新日（`date-modified`）などの情報を追加できます。

:::{note}

記事やページにメタデータを付与することで、その内容を構造化できます。
ドキュメントビルダーの多くでは、この仕組みを「フロントマター」と呼びます。
ドキュメントの先頭に区切り文字で配置し、
YAML形式（`---`）や
TOML形式（`+++`）、
JSON形式（`{}`）で記述します。

:::

## ディレクトリ一覧したい（`listing`）

```yaml
---
title: "ディレクトリ一覧"
listing:
  contents: "*.qmd"
  type: default
  sort: "title asc"
  fields: [title, description, date]
---
```

`listing`フィールドで、指定したファイルを一覧表示できます。
カテゴリ用ディレクトリに`index.qmd`を配置し、上記のようにフロントマターを設定することで、そのディレクトリ内の`.qmd`ファイルの一覧を自動的に生成できます。

`contents`フィールドで対象のファイルを指定し、
`fields`フィールドで表示するメタデータを選択できます。
