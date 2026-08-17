# テーマ独自の設定をしたい（`[params]` / `params.toml`）

```toml
# /config/_default/params.toml
colorScheme = "neon"
defaultAppearance = "light"
autoSwitchAppearance = true
enableSearch = true
mainSections = ["posts"]

[header]
layout = "basic"

[footer]
showMenu = true
showCopyright = true

[homepage]
layout = "card"
showRecent = true
showRecentItems = 6

[article]
showDate = false
showAuthor = true
showReadingTime = true
showTableOfContents = true
```

Hugo本体が知らない、テーマ固有の設定値は``[params]``セクション（もしくは``params.toml``）に書きます。
どんなキーが使えるかはテーマのドキュメントに依存するので、利用するテーマの設定リファレンスを確認してください。

上記サンプルは[Blowfishテーマ](https://blowfish.page/docs/configuration/)の例です。
Blowfishでは``[header]`` / ``[footer]`` / ``[homepage]`` / ``[article]`` / ``[list]`` / ``[taxonomy]`` / ``[term]``のように、
ページの種類ごとにサブセクションを分けて表示・非表示を切り替えられるようになっています。

## テンプレートしたい（`.Site.Params` / `.Params`）

```html
{{ .Site.Params.colorScheme }}
{{ .Site.Params.article.showAuthor }}
```

サイト全体の``[params]``は``.Site.Params``（もしくは``site.Params``）でテンプレートから参照できます。
ネストしたセクション（``[article]``など）は``.Site.Params.article.showAuthor``のようにドットでたどります。

ページ単位のfrontmatterで``params``を上書きした場合は``.Params``で取得できます。

## 未使用の項目はコメントアウトしておきたい

```toml
[article]
showDate = false
# showViews = false
# showLikes = false
showAuthor = true
```

テーマによっては設定可能な項目がとても多く、
デフォルト値のまま使う項目まですべて書き出すと見通しが悪くなります。

変更した項目だけを有効にして、将来使うかもしれない項目は``#``でコメントアウトしたまま残しておくと、
「その項目が存在すること」と「デフォルトのままであること」の両方が一目でわかります。

## リファレンス

- [Configure Params - gohugo.io](https://gohugo.io/getting-started/configuration/#configure-params)
- [Blowfish Configuration](https://blowfish.page/docs/configuration/)
