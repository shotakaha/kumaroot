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
latex-build
latex-documentclass
latex-usepackage
latex-fonts
latex-page
latex-par
latex-heading
latex-tableofcontents
latex-enumitem
latex-emph
latex-figure
latex-amsmath
latex-bibliography
latex-hyperref
```

## 物理したい

```{toctree}
---
maxdepth: 1
---
latex-hepparticles
latex-physics
latex-siunitx
```

## その他

```{toctree}
---
maxdepth: 1
---
latex-masterthesis
latex-primer
latex-ide
latex-online
latex-document
```



## リファレンス

- [改定第8版・LaTeX2e美文書作成入門（技術評論社）](https://gihyo.jp/book/2020/978-4-297-11712-2)
- [日本語TeX Wiki](https://texwiki.texjp.org)
- [CTAN - Comprehensive TeX Archive Network](https://ctan.org/)
- [MacTeX - TeX Users Group](https://tug.org/mactex/)
- [A first set of LaTeX packages](https://tug.org/TUGboat/tb41-2/tb128heff-packages.pdf)
- [Overleaf Documentation](https://www.overleaf.com/learn)
