# メニュー設定したい（`[menu]`）

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

`[menu]`セクションで、サイトのメニューやナビゲーションを作成できます。
内部ページは`pageRef`プロパティ、外部ページは`url`プロパティを使います。
`identifier`と`parent`プロパティを使って、メニューを階層化できます。

設定の概要は[Menusのドキュメント](https://gohugo.io/content-management/menus/)、設定可能な項目は[Menusメソッド](https://gohugo.io/methods/site/menus/)を参照してください。

## メニューを入れ子にしたい

```toml
[menu]
[[menu.main]]
identifier = "parent"
name = "親ページ"
pageRef = "/parent"

[[menu.main]]
parent = "parent"
name = "子ページ1"
pageRef = "/parent/child1"

[[menu.main]]
parent = "parent"
name = "子ページ2"
pageRef = "/parent/child2"
```

`identifier`と`parent`プロパティを使って、メニューを階層化できます。
まず、親ページの`identifier`プロパティを設定します。
そして、子ページに`parent`プロパティを追加し、親ページの`identifier`名を設定します。

:::{caution}

同じメニュー名（`main`）に複数のエントリーを追加する場合は、
`[menu.main]`ではなく`[[menu.main]]`（配列テーブル）を使います。
`[menu.main]`を繰り返すとTOMLの構文エラー（`table main already exists`）になります。

:::

## 複数のメニューを設定したい

```toml
# frontmatter
menu = ["main", "footer", "docs"]
title = "問い合わせ"
```

用途別に複数のメニュー変数を作成できます。
そして、どのメニュー用に表示するか、ページごとのfrontmatterで選択できます。

上記サンプルでは「問い合わせ」ページを**メイン用**（`site.Menus.main`）、**フッター用**（`site.Menus.footer`）、**ドキュメント用**（`site.Menus.docs`）の3種類に設定しています。

## メニューのアイコンをつけたい

```toml
[menu]
[[menu.main]]
identifier = "about"
name = "about"
url = "/about/"
pre = '<i class="fas fa-info-circle"></i>'
```

`pre`変数を、メニュー名の先頭にアイコンを追加できます。
アイコンはFontAwesomeなどのウェブフォントを利用するのがよいです。
メニュー名の末尾に追加する場合は`post`要素を使います。

## 言語ごとにメニューしたい（`menus.ja.toml` / `menus.en.toml`）

```toml
# /config/_default/menus.ja.toml
[[main]]
name = "ホーム"
pageRef = "/"
weight = 10

[[main]]
name = "概要"
pageRef = "/about"
weight = 20
```

```toml
# /config/_default/menus.en.toml
[[main]]
name = "Home"
pageRef = "/"
weight = 10

[[main]]
name = "About"
pageRef = "/about"
weight = 20
```

[多言語サイト](./hugo-config-languages.md)の場合、`/config/_default/`に`menus.{言語コード}.toml`を配置すると、言語ごとに別のメニュー内容を設定できます。
`hugo.toml`側の`[menu]`セクションとは違い、ファイル名の時点で対象言語が決まるため、
ファイルの中身では`[menu.main]`ではなく`[[main]]`のように`menu.`を省略して書きます。

同じ`identifier`のページでもメニュー名を言語ごとに変えたい場合や、
言語によってメニュー項目自体を増減させたい場合に使います。

## リファレンス

- [Menus - gohugo.io](https://gohugo.io/content-management/menus/)
- [Menus method - gohugo.io](https://gohugo.io/methods/site/menus/)
- [Language configuration - gohugo.io](https://gohugo.io/configuration/languages/)
