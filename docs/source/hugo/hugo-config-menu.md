# メニューしたい（``[menu]``）

```toml
[menu]
[[menu.main]]
identifier = "about"
name = "About"
url = "about"
pre = ""
weight = 1
```

``[menu]``セクションで、サイトのメニューやナビゲーションを作成できます。
メニューは階層化できます。

設定の概要は[Menusのドキュメント](https://gohugo.io/content-management/menus/)、設定可能な項目は[menu variables](https://gohugo.io/variables/menus/)を参照してください。

## メニューを入れ子にしたい

```toml
[menu]
[menu.main]
identifier = "parent"
name = "Parent"
url = "parent"

[menu.main]
parent = "parent"
identifier = "child"
name = "Child"
url = "child"
```

``parent``に親メニューの``identifier``を指定することで、メニューを階層化できます。

## 複数のメニューを設定したい

```toml
menu = ["main", "footer", "docs"]
title = "問い合わせ"
```

ページのfrontmatterでも``menu``変数でメニューを設定できます。
複数設定することができ、上記サンプルでは**メイン用**（``site.Menus.main``）、**フッター用**（``site.Menus.footer``）、**ドキュメント用**（``site.Menus.docs``）としてテンプレートで呼び出すことができます。

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
