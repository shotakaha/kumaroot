# LaTeXの使い方

LaTeXの基本的な事項については「LaTeX2e美文書作成入門（技術評論社）」を
手に取ることをオススメします。
ここにまとめてあることも、そのソースのほとんどは美文書作成入門です。

僕がはじめて手に取ったのは、改訂第3版（2004年1月30日発売）だったと思います。
研究室の本棚に置かれていたもので、少し版が古いものでした。
数年に一度改訂されていて、現在の最新版は第8版（2020年11月14日発売）です。
いろいろと変わっている方法もあるので、ぜひ最新版を購入しましょう。
（第7版→第8版では``(u)pLaTeX``→``LuaLaTeX``へと移り変わっていく様子が分かります。）

そのころと比べると、LaTeXは簡単に使えるようになっています。

理系学生の多くは卒論／修論の時にLaTeXをがしがし使うことになると思います。
その時に「インストールできないー」などと焦っていては時既に時間切れ[^bronto]
なので、その手助けになればと思い、簡単にまとめておきます。

[^bronto]: ブロント語



日本語でLaTeXするときのエンジンとドキュメントクラスの組み合わせは以下の3通りがあります。
用途にあった組み合わせを選んでください。
参考となるように僕の感想を添えておきました。

``LuaLaTeX + jlreq``
:   新しくLaTeXに入門する場合は、この組み合わせでOKだと思います。
    これから作成する文書はこれ一択でいいと思います。

``LuaLaTeX + ltjsarticle``
:   LaTeX経験者で、これまでの知識を活かしながらLuaLaTeXを使い方は、
    この組み合わせがよいと思います。
    過去のファイルを書き換えることはオススメしません。

``upLaTeX + jsarticle``
:   これまでに作成したLaTeX文書を再コンパイルする際に必要な組み合わせです。
    また、ウェブの情報を読むときに知っておくとよい情報です。
    日本語の設定に[fontenc](./latex-fontenc.md)や[otf](./latex-otf.md)など追加必須のパッケージが多数あります。



```{toctree}
---
maxdepth: 1
---
latex-install
latex-online
latex-document
latex-documentclass
latex-build
latex-usepackage
latex-fonts
latex-maketitle
latex-linebreak
latex-include
latex-ref
latex-toc
latex-index
latex-amsmath
latex-fancyhdr
latex-microtype
latex-physics
latex-siunitx
latex-hepparticles
latex-primer
latex-japanese
latex-ide
```

## リファレンス

- [改定第8版・LaTeX2e美文書作成入門（技術評論社）](https://gihyo.jp/book/2020/978-4-297-11712-2)
- [日本語TeX Wiki](https://texwiki.texjp.org)
- [CTAN - Comprehensive TeX Archive Network](https://ctan.org/)
- [MacTeX - TeX Users Group](https://tug.org/mactex/)
- [A first set of LaTeX packages](https://tug.org/TUGboat/tb41-2/tb128heff-packages.pdf)
