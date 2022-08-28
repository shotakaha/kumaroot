# LaTeXの使い方

ほとんどの人は修論の時にLaTeXをがしがし使うことになると思います。
その時に「インストールできないー」などと焦っていては時既に時間切れ[^bronto]
なので、その手助けになればと思い、簡単にまとめておきます。

[^bronto]: ヒント：ブロント語

日本語でLaTeXするときのエンジンとドキュメントクラスのメインの組み合わせは以下の3通りがあります。
個人的な感想を一緒に書いておきました。

``LuaLaTeX + jlreq``
:   新しくLaTeXに入門する場合は、ここからはじめればOKだと思います。
    これから作成する文書はこれ一択でいいと思います。

``LuaLaTeX + ltjsarticle``
:   LaTeX経験者で、これまでの知識を活かしながらLuaLaTeXを使い方は、
    この組み合わせがよいと思います。
    過去のファイルを書き換えることはオススメしません。

``upLaTeX + jsarticle``
:   これまでに作成したLaTeX文書を再コンパイルする際に必要な組み合わせです。
    また、ウェブの情報を読み解くときに知っておいたほう情報です。
    ``fontenc``や``otf``など追加必須のパッケージが多数あります。

LaTeXの基本的な事項については「LaTeX2e美文書作成入門（技術評論社）」を
手に取ることをオススメします。
ここにまとめていることも、そのソースのほとんどは美文書作成入門です。

数年に一度改訂されていて、現在の最新版は第8版（2020年11月14日発売）です。
もしかしたら研究室の本棚に古い版が置かれているかもしれませんが、
いろいろと変わっている方法もあるので、ぜひ最新版[^update]を購入しましょう。

[^update]: 第7版→第8版では``(u)pLaTeX``→``LuaLaTeX``へと移り変わっていく様子が分かります

```{toctree}
---
maxdepth: 1
---
latex-install
latex-japanese
latex-yatex
latex-document
latex-documentclass
latex-fonts
latex-usepackage
latex-build
latex-maketitle
latex-linebreak
latex-include
latex-ref
latex-toc
latex-index
latex-primer
```

## リファレンス

- [改定第8版・LaTeX2e美文書作成入門（技術評論社）](https://gihyo.jp/book/2020/978-4-297-11712-2)
- [日本語TeX Wiki](https://texwiki.texjp.org)
- [CTAN - Comprehensive TeX Archive Network](https://ctan.org/)
- [MacTeX - TeX Users Group](https://tug.org/mactex/)
- [A first set of LaTeX packages](https://tug.org/TUGboat/tb41-2/tb128heff-packages.pdf)
