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
latex-fonts-more
```

文字のフォント選びは文書の印象を大きく左右します。
LuaLaTeXでは、[fontspec](./latex-fontspec.md)や[luatex-fontspec](./latex-luatexja-fontspec.md)を使うことで、
かなり簡単かつ自由にフォント設定を変更できるようになっています。

:::{hint}

最近のTeXディストリビューションは、
欧文フォントは**Latin Modern**、
和文フォントは**原の味（HaranoAji）**
がデフォルトのフォントになっています。

はじめてLaTeXを使う場合は、フォントを変更せずに使っても問題はありません。

:::

## フォント設定のサンプル

```{toctree}
latex-lmodern
latex-font-dotgothic16
latex-font-kiwi-maru
latex-font-hiragino
latex-font-zen-maru-gothic
```
