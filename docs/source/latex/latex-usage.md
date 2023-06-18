# LaTeXの使い方

理系学生の多くは卒論／修論のときにLaTeXをがしがし使うことになると思います。
その時になって「インストールできないー」などと焦っていては 時既に時間切れ[^bronto] です。
少しでもその手助けになればと思い、僕の経験をまとめておきます。

[^bronto]: ブロント語

LaTeXの基本は「LaTeX2e美文書作成入門（技術評論社）」を読むことをオススメします。
ここに整理したことも、ソースのほとんどが美文書作成入門です。

僕がはじめて手に取ったのは、改訂第3版（2004年1月30日発売）だったと思います。
研究室の本棚に置かれていたもので、少し版が古いものでした。
数年に一度改訂されていて、現在の最新版は第8版（2020年11月14日発売）です。

LaTeXの開発も進んでいて、以前とは変わっている方法もあります。
ぜひ最新版を購入しましょう。
（とくに第7版→第8版では``(u)pLaTeX``→``LuaLaTeX``へと主エンジンが移り変わった様子が分かります。）

また、クラウドLaTeXのOverleafのドキュメントもとても充実しています。
どのパッケージを使うとよさげかの参考にするとよいです。

```{toctree}
---
maxdepth: 1
---
latex-install
latex-ide
latex-online
latex-document
latex-latexmk
latex-documentclass
latex-maketitle
latex-tableofcontents
latex-flushright
latex-section
latex-linebreak
latex-enumitem
latex-graphicx
latex-figure
latex-booktabs
latex-amsmath
latex-index
latex-bibliography
latex-ref
latex-hyperref
latex-include
latex-setlength
```

## 追加パッケージ

```{toctree}
---
maxdepth: 1
---
latex-graphicx
latex-usepackage
latex-geometry
latex-layout
latex-inputenc
latex-plautopatch
latex-luatexja-ruby
latex-bxjalipsum
latex-fancyhdr
latex-fncychap
latex-inputenc
latex-microtype
latex-minted
latex-xcolor
latex-masterthesis
latex-primer
```

## 物理したい

```{toctree}
---
maxdepth: 1
---
latex-newcommand
latex-hepparticles
latex-physics
latex-siunitx
```

## フォントしたい

```{toctree}
---
maxdepth: 1
---
latex-fonts
latex-font-family
latex-font-series
latex-font-shape
latex-font-size
latex-fonts-more
latex-fontenc
latex-lmodern

latex-kanji-config-udpmap-sys
latex-fontspec
latex-luatexja
latex-luatexja-preset
latex-luatexja-fontspec
latex-otf
latex-luatexja-otf
latex-japanese
```

## リファレンス

- [改定第8版・LaTeX2e美文書作成入門（技術評論社）](https://gihyo.jp/book/2020/978-4-297-11712-2)
- [日本語TeX Wiki](https://texwiki.texjp.org)
- [CTAN - Comprehensive TeX Archive Network](https://ctan.org/)
- [MacTeX - TeX Users Group](https://tug.org/mactex/)
- [A first set of LaTeX packages](https://tug.org/TUGboat/tb41-2/tb128heff-packages.pdf)
- [Overleaf Documentation](https://www.overleaf.com/learn)
