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

## 用紙サイズしたい（``paper``）

```typst
#set page(paper: "a4")  // w210.0 mm x h297.0 mm
#set page(paper: "a0")  // w841.0 mm x h1189.0 mm
#set page(paper: "jis-b5")  // w182.0 mm x h257.0 mm

#set page(paper: "presentation-16-9")  // w297.0 mm x h167.0625 mm
#set page(paper: "presentation-4-3")  // w280.0 mm x h210.0 mm

#set page(paper: "jp-business-card")  // w91.0 mm x h55.0 mm
#set page(paper: "jp-shiroku-ban-4")  // w264.0 mm x h379.0 mm
```

[page要素のpaperオプション](https://typst.app/docs/reference/layout/page/#parameters-paper)で用紙サイズを変更できます。
デフォルトは``"a4"``です。
ISO規格のほかにもJIS規格（日本）、DIN規格（ドイツ）、ANSI規格（アメリカ）など多様な規格の用紙サイズが定義されています。それぞれの用紙サイズは[page.rs](https://github.com/typst/typst/blob/main/crates/typst/src/layout/page.rs)で確認できます。
よく使いそうな設定や、こんな設定もあった、というのを上に書いてみました。

## 余白したい（``margin``）

```typst
#set page(margin: 30mm)  // 上下左右: 30 mm
#set page(
    margin: (x: 8pt, y: 4pt ),  // 左右: 8pt、上下: 4pt
)
```

[page要素のmarginオプション](https://typst.app/docs/reference/layout/page/#parameters-margin)で余白サイズを変更できます。
デフォルトは``auto（短辺の2.5/21倍）``です。
A4の場合は``25 mm``です。

## 段組したい（``columns``）

```typst
#set page(columns: 2)  // 2段組
#set page(columns: 3)  // 3段組
```

[page要素のcolumnsオプション](https://typst.app/docs/reference/layout/page/#parameters-columns)で、段組を変更できます。
デフォルトは``1``です。

## 縦置きしたい（``flipped``）

```typst
#set page(
    paper: "jp-business-card",  // 91.0 mm x 55.0 mm
    flipped: true
)
```

[page要素のflippedオプション](https://typst.app/docs/reference/layout/page/#parameters-flipped)で、用紙の短辺と長辺のサイズを入れ替えできます。
上のサンプルでは、名刺を縦置きする場合を想定してみました。
