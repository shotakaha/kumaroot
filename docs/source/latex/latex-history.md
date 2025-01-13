# TeXの系譜

:::{caution}

ウェブに落ちていた情報を、表面的に拾い集めたものです。
リリース年などは、だいたいこれくらい、と思って眺めてください。

:::

| | リリース年 | エンジン名 | ベースのエンジン | フォーマット | できごと |
|---|---|---|---|---|---|
| TeX | | 1978 | TeX78 | - | - | D. Knuthが組版システムを開発 |
| TeX改良版 | 1982 | TeX82 | TeX78 | PlainTeX | TeX78を改良 |
| LaTeX | 1984 | TeX82 | - | LaTeX | L. LamportがTeXのマクロパッケージを開発 |
| BibTeX | 1985 | - | - | - | O. Patashnikが文献生成ツールを開発 |
| LaTeX2.09 | 1985 | TeX82 | - | LaTeX2.09 | LaTeXを改良したフォーマットを公開 |
| MakeIndex | 1986 | - | - | - | 索引生成ツールを開発 |
| pTeX | 1991 | pTeX | TeX82 | pLaTeX | TeX82を拡張したエンジン。日本語組版（縦書き、禁則処理、和文フォントなど）に対応 |
| eTeX | 1994 | eTeX | TeX82 | - | TeX82を拡張したエンジン。レジスタを増加。プリミティブを追加。 |
| LaTeX2e | 1994 | TeX82 | - | LaTeX2e | LaTeX2eをリリース。LaTeX2.09の後継バージョン |
| dvipdfm | 1997 | - | - | - | DVIをPDFに変換するツール。PostScriptを介さずに直接PDFを生成 |
| pdfTeX | 1997 | pdfTeX | TeX82 | pdfLaTeX | Han The ThanhがpdfTeXをリリース。PostScriptを介さずにPDFを直接生成できるようになる。 |
| dvipdfmx | 2002 | - | - | - | CJK対応したdvipdfm |
| xindy | 2004 | - | - | - | MakeIndexの後継となる索引生成ツール。Unicodeに対応 |
| XeTeX | 2005 | XeTeX | eTeX | XeLaTeX | XeTeXのリリース。eTeXを拡張したエンジン。Unicode対応。OpenTypeフォント対応。|
| LuaTeX | 2007 | LuaTeX | pdfTeX | LuaLaTeX | LuaLaTeXのリリース。pdfTeXを拡張したエンジン。Unicode対応。Lua対応。 |
| ConTeXt | 2008 | ConTeXt | LuaTeX | ConTeXt | |
| Biber | 2009 | - | - | - | 文献生成ツール。BibTeXの代替ツール。BibLaTeXパッケージと一緒に利用する。|
| LuaHBTeX | 2015 | LuaHBTeX | LuaTeX | LuaLaTeX | LuaTeXを拡張したエンジン。|

TeXの系譜を整理してみました。
美文書LaTeXに書かれていたTeXエンジンの変遷や、
ウェブ上で拾った情報、Wikipediaに記載されていた年などを元に並べたものです。
きちんと裏どりしたものではないことはご留意ください。

開発史を眺めると、
欧文の文書作成でスタートしたツールが、
日本語（やCJK）対応、Unicode対応、OpenTypeフォント対応、と
時代のニーズに合わせて進歩してきたんことが感じられます。

また、いちエンドユーザーとしては、これらの偉業をリスペクトしつつ、
XeLaTeXやLuaLaTeXといったいわゆる**モダンLaTeX**を
ありがたく利用させてもらうのがよいのかなと思います。

:::{mermaid}

graph TD
    O[TeX] -->|レジスタ拡張| A[e-TeX]
    O --> |機能強化| B[LaTeX]
    A --> B
    A -->|日本語化| D[pTeX]
    B -->|日本語化| C[pLaTeX]
    D --> C
    D -->|Unicode対応| E[upTeX]
    C -->|Unicode対応| F[upLaTeX]
    E --> F
    A --> G[モダンLaTeX]
    G --> H[LuaLaTeX]
    G --> J[pdfLaTeX]
    G --> I[XeLaTeX]
    J --> |Lua| H
    H --> |HarfBuzz| K[LuaHBTeX]

:::
