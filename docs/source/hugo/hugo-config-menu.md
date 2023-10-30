# メニューしたい（``[menu]``）

```toml
[menu]
[[menu.main]]
name = "Home"
pageRef = "/"
weight = 10

[[menu.main]]
name = "About"
pageRef = "/about"
weight = 20

[[menu.main]]
name = "Related Page"
url = "外部ページ"
weight = 90
```

``[menu]``セクションで、サイトのメニューやナビゲーションを作成できます。
内部ページは``pageRef``プロパティ、外部ページは``url``プロパティを使います。
``identifier``と``parent``プロパティを使って、メニューを階層化できます。

設定の概要は[Menusのドキュメント](https://gohugo.io/content-management/menus/)、設定可能な項目は[menu variables](https://gohugo.io/variables/menus/)を参照してください。

## メニューを入れ子にしたい

```toml
[menu]
[menu.main]
identifier = "parent"
name = "親ページ"
pageRef = "/parent"

[menu.main]
parent = "parent"
name = "子ページ1"
pageRef = "/parent/child1"

[menu.main]
parent = "parent"
name = "子ページ2"
pageRef = "/parent/child2"
```

``identifier``と``parent``プロパティを使って、メニューを階層化できます。
まず、親ページの``identifier``プロパティを設定します。
そして、子ページに``parent``プロパティを追加し、親ページの``identifier``名を設定します。

## 複数のメニューを設定したい

```toml
menu = ["main", "footer", "docs"]
title = "問い合わせ"
```

用途別に複数のメニュー変数を作成できます。
そして、どのメニュー用に表示するか、ページごとのfrontmatterで選択できます。

上記サンプルでは「問い合わせ」ページを**メイン用**（``site.Menus.main``）、**フッター用**（``site.Menus.footer``）、**ドキュメント用**（``site.Menus.docs``）の3種類に設定しています。

## メニューのアイコンをつけたい

```toml
[menu]
[[menu.main]]
identifier = "about"
name = "about"
url = "/about/"
pre = '<i class="fas fa-info-circle"></i>'
```

``pre``変数を、メニュー名の先頭にアイコンを追加できます。
アイコンはFontAwesomeなどのウェブフォントを利用するのがよいです。
メニュー名の末尾に追加する場合は``post``要素を使います。
