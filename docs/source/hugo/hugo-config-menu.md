# メニューを作成したい（``[menu]``）

```toml
[menu]
[[menu.main]]
identifier = "about"
name = "About"
url = "about"
pre = ""
weight = 1
```

``[menu]``セクションを使って、ウェブサイトのメニューやナビゲーションと呼ばれる部分を作成できます。
メニューは階層化できます。

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
```

メニューのカテゴリーを複数設定したい場合、``menu``変数に配列で定義します。
上記では**メイン用**、**フッター用**、**ドキュメント用**のメニューを定義しています。

## メニューのアイコンをつけたい

```toml
[menu]
[[menu.main]]
identifier = "about"
name = "about"
url = "/about/"
pre = '<i class="fas fa-info-circle"></i>'
```

メニューのアイコンはFontAwesomeなどのウェブフォントを利用するのがよいです。
``pre``要素を使って、メニュー名の先頭にアイコンを追加できます。
メニュー名の末尾に追加する場合は``post``要素を使います。

## リファレンス

- [Menus](https://gohugo.io/content-management/menus/)
