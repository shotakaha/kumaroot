# フロントマターしたい

````md
---
icon: lucide/braces
title: Zensicalのフロントマター
description: Zensicalのフロントマターについての説明
status: new # deprecated
---
````

ページのタイトルや説明文などのメタデータは、フロントマターとしてMarkdownファイルの先頭に記述します。

## タイトルしたい（`title`）

```md
---
title: ページのタイトル
---

# ページのタイトル
```

`title`で、ページのタイトルを指定できます。

## 概要したい（`description`）

```md
---
description: ページの概要
---

# ページのタイトル
```

`description`で、ページの概要を指定できます。

## アイコンしたい（`icon`）

```md
---
icon: lucide/braces
---

# ページのタイトル
```

`icon`で、ページのアイコンを指定できます。
アイコンはナビゲーションバーやページのヘッダーに表示されます。
アイコンは `Lucide`、`Material Design`、`Font Awesome`、`Octicons`、`Simple Icons`のアイコンセットから選択できます。

## ステータスしたい（`status`）

```md
---
status: new
status: deprecated
---
```

`status`で、ページのステータスを指定できます。

```toml
[project.extra.status]
# <identifier> = "<description>"
new = "Recently added"
```

表示するためには、`project.extra.status`にステータスの識別子と説明を追加する必要があります。

## リファレンス

- [Front Matter - Zensical](https://zensical.org/docs/authoring/frontmatter/)
