# LaTeXの使い方

理系学生の多くは卒論や修論のときにLaTeXを本格的に使うようになるのではないでしょうか？
その時になって「インストールできないー」などと焦っていては 時既に時間切れ[^bronto] です。
また、論文の内容より、ツールの使い方に時間を取られてしまっては本末転倒です。
少しでもその手助けになればと思い、僕の経験をまとめておきます。

とくに「[](./latex-masterthesis.md)」では、
いまならどのようなLaTeX構成がベストなのか、
自分の修論ファイルを10年振りくらいに開き、
実際に手を動かしながら考えてみました。

[^bronto]: ブロント語

LaTeXを体得するために、まずは
「LaTeX2e美文書作成入門（技術評論社）」を読むことをオススメします。
僕がはじめて手に取ったのは2008年ころだったと思います。
研究室の本棚に置かれていたもので、改訂第3版（2004年1月30日発売）と少し版が古いものでした。
当時はまったく気にしていませんでしたが、
近年は3年に一度改訂されているので、ぜひ最新版を購入しましょう。
ウェブ上も情報が落ちていますが、かなり断片的で、
ものによっては古すぎるものもあります。

現在の最新版は第8版（2020年11月14日発売）です。
（とくに第7版→第8版では``(u)pLaTeX``→``LuaLaTeX``へと主エンジンが移り変わった様子が分かります。）

LaTeXは現在も開発が進んでいおり、
この10年でも大きく変わったことを改めて実感しました。
とくに環境構築の敷居が下がっていて、かなり快適にはじめられるようになっています。
また、OverleafやCloudLaTeXといったクラウドサービスも普及し、
共同編集なども簡単にできるようになっています。
Overleafのドキュメントもとても充実しています。
どのパッケージを使うとよさげかの参考にするとよいです。

## 環境構築したい

```{toctree}
---
maxdepth: 2
---
latex-setup
```

## タイプセットしたい

```{toctree}
---
maxdepth: 2
---
latex-build
```

## ドキュメントクラスしたい

```{toctree}
---
maxdepth: 2
---
latex-documentclass
```

## プリアンブルしたい

```{toctree}
---
maxdepth: 2
---
latex-preamble
```


## フォントしたい

```{toctree}
---
maxdepth: 2
---
latex-fonts
latex-luatexja
latex-lmodern
latex-fontspec
latex-japanese
```

## ページ設定したい

```{toctree}
---
maxdepth: 2
---
latex-page
```

## 見出ししたい

```{toctree}
---
maxdepth: 2
---
latex-heading
latex-maketitle
latex-titlepage
latex-tableofcontents
```

## 段落したい

```{toctree}
---
maxdepth: 2
---
latex-par
latex-hyperref
latex-emph
latex-minted
latex-xcolor
latex-bxjalipsum
```

## 図版したい

```{toctree}
---
maxdepth: 2
---
latex-figure
latex-booktabs
```

## 数式したい

```{toctree}
---
maxdepth: 2
---
latex-amsmath
```

## 箇条書きしたい

```{toctree}
---
maxdepth: 2
---
latex-list
```

## 参考文献したい

```{toctree}
---
maxdepth: 2
---
latex-bibliography
latex-biblatex
```

## 物理したい

```{toctree}
---
maxdepth: 1
---
latex-pmatrix
latex-hepparticles
latex-physics
latex-siunitx
latex-feynman
```

## その他

```{toctree}
---
maxdepth: 1
---
latex-masterthesis
latex-a0poster
latex-primer
latex-ide
latex-online
latex-document
latex-history
latex-microtype
latex-minipage
latex-showframe
```

## リファレンス

- [改定第8版・LaTeX2e美文書作成入門（技術評論社）](https://gihyo.jp/book/2020/978-4-297-11712-2)
- [日本語TeX Wiki](https://texwiki.texjp.org)
- [CTAN - Comprehensive TeX Archive Network](https://ctan.org/)
- [MacTeX - TeX Users Group](https://tug.org/mactex/)
- [A first set of LaTeX packages](https://tug.org/TUGboat/tb41-2/tb128heff-packages.pdf)
- [Overleaf Documentation](https://www.overleaf.com/learn)
