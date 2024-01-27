# TeXエンジンの変遷

美文書LaTeXに書かれていたTeXエンジンの変遷を、整理してみました。
日本語に対応するのがとても大変な作業であったことが分かりました。

**モダンLaTeX**であるXeLaTeXとLuaLaTeXはデフォルトでUTF8に対応しています。
現在では、特段の理由がないかぎり、このどちらかを使うのがよいのだと思います。

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
    J -->|Lua| H
    G --> I[XeLaTeX]

:::
