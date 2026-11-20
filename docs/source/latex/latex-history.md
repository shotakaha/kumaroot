# TeXの系譜

:::{caution}

ウェブに落ちていた情報を、表面的に拾い集めたものです。
リリース年などは、だいたいこれくらい、と思って眺めてください。

:::

| エンジン名 | リリース年 | ベースのエンジン | フォーマット | できごと |
|---|---|---|---|---|
| TeX78 | 1978 | - | - | D. Knuthが組版システムを開発 |
| TeX82 | 1982 | TeX78 | PlainTeX | TeX78を改良 |
| LaTeX | 1984 | - | LaTeX | L. LamportがTeX82のマクロパッケージを開発 |
| BibTeX | 1985 | - | - | O. Patashnikが文献生成ツールを開発 |
| LaTeX2.09 | 1985 | - | LaTeX2.09 | LaTeXを改良したフォーマットを公開 |
| MakeIndex | 1986 | - | - | 索引生成ツールを開発 |
| pTeX | 1991 | TeX82 | pLaTeX | TeX82を拡張したエンジン。日本語組版（縦書き、禁則処理、和文フォントなど）に対応 |
| eTeX | 1994 | TeX82 | - | TeX82を拡張したエンジン。レジスタを増加。プリミティブを追加。 |
| LaTeX2e | 1994 | - | LaTeX2e | LaTeX2eをリリース。LaTeX2.09の後継バージョン |
| dvipdfm | 1997 | - | - | DVIをPDFに変換するツール。PostScriptを介さずに直接PDFを生成 |
| pdfTeX | 1997 | TeX82 + e-TeX | pdfLaTeX | Han The ThanhがpdfTeXをリリース。PostScriptを介さずにPDFを直接生成できるようになる。 |
| dvipdfmx | 2002 | - | - | CJK対応したdvipdfm |
| xindy | 2004 | - | - | MakeIndexの後継となる索引生成ツール。Unicodeに対応 |
| XeTeX | 2005 | eTeX | XeLaTeX | XeTeXのリリース。eTeXを拡張したエンジン。Unicode対応。OpenTypeフォント対応。|
| LuaTeX | 2007 | pdfTeX | LuaLaTeX | LuaLaTeXのリリース。pdfTeXを拡張したエンジン。Unicode対応。Lua対応。 |
| ConTeXt MkIV | 2007 | LuaTeX | ConTeXt | |
| Biber | 2009 | - | - | 文献生成ツール。BibTeXの代替ツール。BibLaTeXパッケージと一緒に利用する。|
| LuaHBTeX | 2015 | LuaTeX | LuaLaTeX | LuaTeXを拡張したエンジン。|

TeXの系譜を整理してみました。
美文書LaTeXに書かれていたTeXエンジンの変遷や、
ウェブ上で拾った情報、Wikipediaに記載されていた年などを元に並べたものです。
きちんと裏どりしたものではないことはご留意ください。

開発史を眺めると、
欧文の文書作成でスタートしたツールが、
日本語（やCJK）対応、Unicode対応、OpenTypeフォント対応、と
時代のニーズに合わせて進歩してきたことが感じられます。

また、いちエンドユーザーとしては、これらの偉業をリスペクトしつつ、
XeLaTeXやLuaLaTeXといったいわゆる**モダンLaTeX**を
ありがたく利用させてもらうのがよいのかなと思います。

:::{mermaid}

graph TD
    subgraph Legacy["Legacy TeX"]
        O[TeX] -->|マクロパッケージ| B[LaTeX]
        O -->|レジスタ拡張| A[e-TeX]
        O -->|日本語化| D[pTeX]
        B -->|日本語化| C[pLaTeX]
        D --> C
        D -->|Unicode対応| E[upTeX]
        C -->|Unicode対応| F[upLaTeX]
        E --> F
    end
    subgraph Modern["Modern TeX"]
        G[pdfTeX] --> J[pdfLaTeX]
        G --> LT[LuaTeX]
        LT --> H[LuaLaTeX]
        LT -->|HarfBuzz| K[LuaHBTeX]
        X[XeTeX] --> I[XeLaTeX]
    end
    A --> G
    A --> X

:::
