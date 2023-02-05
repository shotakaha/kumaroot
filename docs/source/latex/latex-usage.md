# LaTeXの使い方

理系学生の多くは卒論／修論の時にLaTeXをがしがし使うことになると思います。
その時に「インストールできないー」などと焦っていては時既に時間切れ[^bronto]
なので、その手助けになればと思い、簡単にまとめておきます。

[^bronto]: ブロント語

LaTeXの基本的な事項については「LaTeX2e美文書作成入門（技術評論社）」を
手に取ることをオススメします。
ここにまとめてあることも、そのソースのほとんどは美文書作成入門です。

僕がはじめて手に取ったのは、改訂第3版（2004年1月30日発売）だったと思います。
研究室の本棚に置かれていたもので、少し版が古いものでした。
数年に一度改訂されていて、現在の最新版は第8版（2020年11月14日発売）です。

いろいろと変わっている方法もあるので、ぜひ最新版を購入しましょう。
（とくに第7版→第8版では``(u)pLaTeX``→``LuaLaTeX``へと移り変わった様子が分かります。）

```{toctree}
---
maxdepth: 1
---
latex-install
latex-online
latex-document
latex-build
latex-documentclass
latex-usepackage
latex-maketitle
latex-tableofcontents
latex-flushright
latex-section
latex-graphicx
latex-figure

latex-fonts
latex-fonts-more
latex-amsmath
latex-bibliography

latex-ide
latex-include
latex-index
latex-japanese
latex-linebreak
latex-luatexja-ruby
latex-masterthesis
latex-newcommand
latex-primer
latex-ref

```

## 追加パッケージ

```{toctree}
---
maxdepth: 1
---
latex-booktabs
latex-bxjalipsum
latex-enumitem
latex-fancyhdr
latex-fncychap

latex-hepparticles
latex-hyperref
latex-inputenc
latex-microtype
latex-minted
latex-physics
latex-siunitx
latex-xcolor
```

## リファレンス

- [改定第8版・LaTeX2e美文書作成入門（技術評論社）](https://gihyo.jp/book/2020/978-4-297-11712-2)
- [日本語TeX Wiki](https://texwiki.texjp.org)
- [CTAN - Comprehensive TeX Archive Network](https://ctan.org/)
- [MacTeX - TeX Users Group](https://tug.org/mactex/)
- [A first set of LaTeX packages](https://tug.org/TUGboat/tb41-2/tb128heff-packages.pdf)
