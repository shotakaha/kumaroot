```{eval-rst}
.. index::
    pair: レイアウトしたい; Typst
    pair: ヘッダーしたい; Typst
```

# ページ設定したい（`#page`）

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

[pageキー](https://typst.app/docs/reference/layout/page/)で用紙サイズや余白の大きさ、ヘッダーやフッターの内容、ノンブルの表示方法など、ページ全体を設定できます。

:::{seealso}

LaTeXの`geometry`や`fancyhdr`などの機能に相当します。

- [](../latex/latex-geometry.md)
- [](../latex/latex-fancyhdr.md)

:::

## 用紙サイズしたい（`paper`）

```typst
#set page(paper: "a4")  // w210.0 mm x h297.0 mm
#set page(paper: "a0")  // w841.0 mm x h1189.0 mm
```

[page要素のpaperオプション](https://typst.app/docs/reference/layout/page/#parameters-paper)で用紙サイズを変更できます。
デフォルトは`"a4"`です。

```typst
#set page(paper: "jis-b5")  // w182.0 mm x h257.0 mm
```

ISO規格のほかにもJIS規格（日本）、DIN規格（ドイツ）、ANSI規格（アメリカ）など多様な規格の用紙サイズが定義されています。

:::{note}

用紙サイズ名は[page.rs](https://github.com/typst/typst/blob/main/crates/typst-library/src/layout/page.rs)にハードコードされていました。

:::

```typst
#set page(paper: "presentation-16-9")  // w297.0 mm x h167.0625 mm
#set page(paper: "presentation-4-3")  // w280.0 mm x h210.0 mm
```

発表スライド用のサイズもありました。

```typst
#set page(paper: "jp-business-card")  // w91.0 mm x h55.0 mm
#set page(paper: "jp-shiroku-ban-4")  // w264.0 mm x h379.0 mm
```

日本の名刺サイズもありました。

## 余白したい（`margin`）

```typst
#set page(margin: 30mm)  // 上下左右: 30 mm
```

`margin`オプションで、余白の大きさを変更できます。
デフォルトは`auto`になっていて、短辺の2.5/21倍に相当します。A4の場合は`25 mm`です。

```typst
#set page(
    margin: (x: 8pt, y: 4pt),  // 左右: 8pt、上下: 4pt
)
```

上下左右を一括、左右（`x`）と上下（`y`）、
すべて別々（`top` / `bottom` / `left` / `right`）など柔軟に設定できます。

## ノンブルしたい（`numbering`）

```typst
// 表示内容: "現在のページ数／総ページ数"
// 表示位置：各ページの下中央
#set page(
    numbering: "1 / 1"
    number-align: center + bottom,
    )

// 表示内容: "現在のページ数"
// 表示位置：各ページの右下
#set page(
    numbering: "1",
    number-align: right,
)
```

`numbering`オプションでノンブル（＝ページ番号）を表示できます。
また、`number-align`オプションでノンブルの表示位置を変更できます。

:::{note}

ノンブルはデフォルトで非表示です。
ユーザーが`numbering`オプションを明示する必要があります。

:::

```typst
#show page(where: page(where: page.where(not page.first))): it => align(center + bottom)[#numbering("1 / 1")]
```

表紙だけノンブルを非表示にしたい場合は`#show`ルールで設定します。

## ヘッダー／フッターしたい（`header` / `footer`）

```typst
#set page(
    header: [
        #set text(8pt)
        ヘッダー
    ],
    footer: [
        #set text(8pt)
        フッター
    ]
)
```

`header`オプションと`footer`オプションで、
ドキュメント全体に共通のヘッダーやフッターを表示できます。
デフォルトは`auto`になっていて、`numbering`オプションが有効な場合は、ノンブル（ページ番号）がフッターとして表示されます。

```typst
header-ascent(30% + 0pt)
footer-descent(30% + 0pt)
```

ヘッダーとフッターの表示位置は、それぞれ
天（上の余白）、地（下の余白）からの相対位置で調整できます。
`%`は余白に対する割合、`pt`はオフセット量です。

## 段組したい（`columns`）

```typst
// 2段組
#set page(
    columns: 2,
    gutter: 1.5em  // 段間の間隔
)

// 3段組
#set page(
    columns: 3,
    gutter: 5mm
)
```

`columns`オプションで段組を変更できます。
デフォルトは1段組（`columns: 1`）です。

```typst
// 本文中
#columns(2)[
このコンテンツブロックは2段組
]

そのあとの本文はページ設定の段組に戻る
```

`#columns(段数)`で、本文中に部分的に段組を適用できます。



## 縦置きしたい（``flipped``）

```typst
#set page(
    paper: "jp-business-card",  // 91.0 mm x 55.0 mm
    flipped: true
)
```

[page要素のflippedオプション](https://typst.app/docs/reference/layout/page/#parameters-flipped)で、用紙の短辺と長辺のサイズを入れ替えできます。
上のサンプルでは、名刺を縦置きする場合を想定してみました。

## リファレンス

- [page - Element](https://typst.app/docs/reference/layout/page/)
