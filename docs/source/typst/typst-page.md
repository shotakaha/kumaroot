```{eval-rst}
.. index::
    pair: レイアウトしたい; Typst
    pair: ヘッダーしたい; Typst
```

# レイアウトしたい（``#page``）

```typst
#set page(
    paper: "a4",
    margin: (x: 25mm, y: 25mm),
    columns: 1,
    //fill: 背景色,
    numbering: "1 / 1",
    number-align: center,
    header: [
        #set text(8pt)[ヘッダー・左]
    ]
)
```

[page要素](https://typst.app/docs/reference/layout/page/)でページ全体の設定ができます。
用紙のサイズや余白の大きさ、ヘッダーやフッターの内容、ノンブルの表示方法など設定できます。

:::{seealso}

- [](../latex/latex-usepackage-geometry.md)
- [](../latex/latex-usepackage-fancyhdr.md)

:::

## 用紙サイズしたい

```typst
#set page(paper: "a4")  // 210.0 mm x 297.0 mm
#set page(paper: "a0")  // 841.0 mm x 1189.0 mm
#set page(paper: "jis-b5")  // 182.0 mm x 257.0 mm

#set page(paper: "presentation-16-9")  // 297.0 mm x 167.0625 mm
#set page(paper: "presentation-4-3")  // 280.0 mm x 210.0 mm

#set page(paper: "jp-business-card")  // 91.0 mm x 55.0 mm
#set page(paper: "jp-shiroku-ban-4")  // 264.0 mm x 379.0 mm
```

[page要素のpaperオプション](https://typst.app/docs/reference/layout/page/#parameters-paper)で用紙サイズを変更できます。
デフォルトは``"a4"``です。
ISO規格のほかにもJIS規格（日本）、DIN規格（ドイツ）、ANSI規格（アメリカ）など多様な規格の用紙サイズが定義されています。それぞれの用紙サイズは[page.rs](https://github.com/typst/typst/blob/main/crates/typst/src/layout/page.rs)で確認できます。
よく使いそうな設定や、こんな設定もあった、というのを上に書いてみました。
