# フォントしたい

フォントを操作する方法を整理しました。

```{toctree}
---
maxdepth: 1
---
latex-usefont
latex-font-family
latex-font-series
latex-font-shape
latex-font-size
latex-fontspec
latex-fontsetup
latex-unicode-math
latex-luatexja
latex-luatexja-fontspec
latex-luatexja-preset
latex-luatexja-otf
latex-luatexja-ruby
latex-polyglossia
latex-fonts-more
```

文字のフォント選びは文書の印象を大きく左右します。
LuaLaTeXでは、[fontspec](./latex-fontspec.md)や[luatex-fontspec](./latex-luatexja-fontspec.md)を使うことで、
かなり簡単かつ自由にフォント設定を変更できるようになっています。

## フォント設定を確認したい（`tlmgr conf updmap`）

```console
$ tlmgr conf updmap
updmap configuration values (from /usr/local/texlive/2024/texmf-dist/web2c/updmap.cfg):
dvipdfmDownloadBase14 = true
dvipsDownloadBase35 = true
dvipsPreferOutline = true
pdftexDownloadBase14 = true

LW35 = URWkb
KanjiMap = uptex-tc-@tcEmbed@.map
jaEmbed = haranoaji
jaVariant = -04
koEmbed = baekmuk
scEmbed = arphic
tcEmbed = arphic
```

`tlmgr conf updmap`でフォント設定（とくに`updmap.cfg`）を確認できます。

最近のTeXディストリビューションは、
欧文フォントは**Latin Modern**、
和文フォントは**原の味（HaranoAji）**
がデフォルトのフォントになっています。
はじめてLaTeXを使う場合は、フォントを変更せずに使っても問題はありません。

:::{note}
韓国語（korean）、簡体字（simplified chinese）、繁体字（traditional chinese）に
設定されているフォントはやや古めのようです。

韓国語はNanum系、
簡体字はSource Han CN系、
繁体字はSource Han TW系にすると
日本語フォント（原ノ味）ともマッチするみたいです。

```console
koEmbed = nanumtype1
scEmbed = sourcehan
tcEmbed = sourcehan
```

:::

## フォント設定のサンプル

```{toctree}
latex-lmodern
latex-font-dotgothic16
latex-font-kiwi-maru
latex-font-hiragino
latex-font-zen-maru-gothic
```
