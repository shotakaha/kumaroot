```{eval-rst}
.. index::
    single: Sphinx Extensions; OGP
```

# OGPしたい（``sphinxext-opengraph``）

```console
$ pip3 install sphinxext-opengraph
```

```python
# conf.py
extensions = [
    ...,
    "sphinxext.opengraph",
    ...
]
```

SphinxJPハッカソンに参加して教えてもらった拡張パッケージです。
[sphinxext-opengraph](https://pypi.org/project/sphinxext-opengraph/)を使うと、ウェブサイトにOGP情報を追記できます。
{file}`conf.py`の``extensions``にパッケージ名を追記するだけで、HTML中に最低限のOGP情報が追加されるので、とりあえず使っておくとよいと思います。

OGPは{file}`conf.py`で全体、フロントマターでページごとに設定できます。

このページは以下のOGP情報が追加されました。

```html
<meta content="ROOT, Python" name="keywords" />
<meta property="og:title" content="OGPしたい（sphinxext-opengraph）" />
<meta property="og:type" content="website" />
<meta property="og:url" content="sphinx/sphinx-extensions-opengraph.html" />
<meta property="og:site_name" content="KumaROOT" />
<meta property="og:description" content="SphinxJPハッカソンに参加して教えてもらった拡張パッケージです。 sphinxext-opengraph を使うと、ウェブサイトにOGP情報を追記できます。 conf.py で全体のOGPを設定でき、フロントマターでページごとのOGPを設定できます。 conf.py の extensions にパッケージ名を追記するだけで、HTML中に最低限のOGP情報が追加されるので、とりあえず使っ..." />
```

## サイト全体のOGPを設定したい

```python
# conf.py

## Options for OGP (sphinxext-opengraph)

ogp_site_url = "サイトの公開URL"
ogp_description_length = 200
ogp_site_name = "サイト名" # デフォルトは project で設定した文字列
ogp_social_cards = # あとで調べる
ogp_image = "サイトOGP画像のパス" # ogp_site_urlからの相対パス
ogp_image_alt = "サイトOGP画像の代替テキスト" # デフォルトは ogp_site_name で設定した文字列
ogp_use_first_image = True
ogp_type = "website"
ogp_custom_meta_tags = [
    '<meta property="og:ignore_canonical" content="true" />',
]
ogp_enable_meta_description = True
```

デフォルトの設定でも十分ですが、サイト全体のOGP情報を設定できます。
``ogp_use_first_image``と``ogp_enable_meta_description``は有効にするとよいでしょう。

## ページごとのOGPを設定したい

```yaml
---
ogp_description_length: 150
og:description: "ページの説明"
description : "ページの説明"
og:title: "ページのタイトルを上書き"
og:type: "article"
og:image: "OGP画像の絶対パス"
og:image:alt: "OGP画像の代替テキスト"
---

# タイトル

本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文
本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文本文
```

## リファレンス

- [sphinxext-opengraph - Read the Docs](https://sphinxext-opengraph.readthedocs.io/en/latest/)
- [sphinxext-opengraph - GitHub](https://github.com/wpilibsuite/sphinxext-opengraph)
- [The Open Graph Protocol](https://ogp.me/)
