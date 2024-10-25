# ページ設定したい（``frontmatter``）

```toml
title = "タイトル"
date = "日付"
images = ["画像パス", "画像パス"]
tags = ["hugo", "frontmatter"]
draft = true
```

ファイルの先頭に記述する[フロントマター](https://gohugo.io/content-management/front-matter/)で
ページごとの設定を記述できます。
フロントマターで設定した変数は、テンプレートで使うことができます。
また、ユーザー定義の変数も設定できます。

HugoではTOML、YAML、JSON、ORGの4つの形式でフロントマターを記述できます。
このドキュメントのサンプルはTOML形式で記述しています。

## 日本語したい

```toml
isCJKLanguage = true
```

日本語などを使う場合は設定しましょう。
マルチバイト文字に対して、``.WordCount`` や``.Count``が正確になるらしいです。
