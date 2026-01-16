```{eval-rst}
.. index::
    pair: レイアウトしたい; Typst
    pair: ヘッダーしたい; Typst
```

# ページ設定したい（`#page`）

```typst
// #set page(..options)
#set page(
    paper: "a4",
    margin: (x: 25mm, y: 25mm),
    columns: 1,
    //fill: luma(99%),  // 全ページの背景色,
    numbering: "1 / 1",
    number-align: center,
    header: [ヘッダー],
)
```

[page要素](https://typst.app/docs/reference/layout/page/)で
用紙サイズや余白の大きさ、ヘッダーやフッターの内容、ノンブルの表示方法など、
ページ全体を設定できます。
`#set page(..options)`の形式で、ファイルの頭に記述します。

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
// 日本の名刺サイズ
#set page(paper: "jp-business-card")  // w91.0 mm x h55.0 mm
#set page(paper: "jp-shiroku-ban-4")  // w264.0 mm x h379.0 mm
```

日本の名刺サイズ（`jp-business-card`など）もありました。

```typst
// 横（width）と縦（height）で指定
#set page(width: 91.0mm, height: 55.0mm)
```

`width`と`height`オプションで長さを直接指定できます。

## 余白したい（`margin`）

```typst
#set page(margin: 30mm)  // 上下左右: 30 mm
```

`margin`オプションで、余白の大きさを変更できます。
デフォルトは`auto`になっていて、短辺の2.5/21倍に相当します。A4の場合は`25 mm`です。

```typst
#set page(
  margin: (
    x: 2cm,    // 左右の余白
    y: 1cm,    // 上下の余白
)
```

上下左右を一括、左右（`x`）と上下（`y`）、
すべて別々（`top` / `bottom` / `left` / `right`）など柔軟に設定できます。

## ノンブルしたい（`numbering`）

```typst
#set page(numbering: none)   // 非表示（デフォルト）
#set page(numbering: "1")    // 1, 2, 3, ... で表示
#set page(numbering: "i")    // i, ii, iii, ... で表示

// カスタム表示
#set page(numbering: "1 of 1")   // 現在のページ数 of 総ページ数
#set page(numbering: "1 / 1")    // 現在のページ数 / 総ページ数
```

`numbering`オプションでノンブル（＝ページ番号）を表示できます。
ノンブルはデフォルトで非表示です。
ユーザーが`numbering`オプションを明示する必要があります。

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

`number-align`オプションでノンブルの表示位置を変更できます。

```typst
#set page(
  footer: context {
    if counter(page).get().first() > 1 [
      #align(center)[
        #counter(page).display() / #counter(page).final().at(0)
      ]
    ]
  }
)
```

表紙だけノンブルを非表示にしたい場合の設定です。

:::{note}

`counter.final`は`context`内でのみ使用できるメソッドです。
戻り値は配列になっているので`.at(0)`で総ページ数を取得する必要がありました。

:::

## ヘッダー／フッターしたい（`header` / `footer`）

```typst
// 非表示
#set page(
    header: none,
    footer: none,
)

// auto（ページ番号を表示）
#set page(
    numbering: "1"
    footer: auto,
    // or
    // number-align: top,
    // header: auto,
)

// カスタム設定
#set page(
    header: [ヘッダー],
    footer: [フッター],
)
```

`header`オプションと`footer`オプションで、
ドキュメント全体に共通のヘッダーやフッターを表示できます。
デフォルトは`auto`になっていて、`numbering`オプションが有効な場合は、ノンブル（ページ番号）がフッターに表示されます。
`number-align: top`を指定するとヘッダーに表示できます。

```typst
header-ascent(30% + 0pt)
footer-descent(30% + 0pt)
```

ヘッダーとフッターの表示位置は、それぞれ
天（上の余白）、地（下の余白）からの相対位置で調整できます。
`%`は余白に対する割合、`pt`はオフセット量です。

```typst
// レポート用ヘッダーを定義
#let report-header = {
    // フォントサイズを変更
    set text(size: 8pt)
    // ヘッダーエリアを2分割
    // 左寄せ: 授業名
    // 右寄せ: 学籍番号
    grid(
        columns: (1fr, 1fr),
        align: (left, right),
        [授業名],    // ここを編集
        [学籍番号],  // ここを編集
    )
    // ヘッダーエリアと本文の区切り線
    line(length: 100%, stroke: 0.5pt)
}

// レポート用フッターを定義
#let report-footer = {
    set text(size: 9pt)
    set align(center)
    // "--- ページ番号 ---" と表示
    // counter は context内で使う必要がある
    context { "--- " + counter(page).display() + " ---"}
}

#set page(
  header: report-header,
  footer: report-footer,
)
```

講義のレポートなどで使うことを想定したシンプルなヘッダーとフッターのサンプルです。
`report-header`と`report-footer`を変数として定義しておくとよいと思います。

:::{note}

```typst
#set page(
  header: [#report-header],
  footer: [#report-footer],
)
```

`page`要素の`header`と`footer`オプションには、コンテンツブロックを明示的に指定してもOKです。

:::

### 章ごとに変更したい

```typst
#let current-chapter = state("chapter", "")

#set page(
  header: context [
    #set text(size: 9pt)
    #let page-num = counter(page).get().first()
    #if page-num > 1[
      #grid(
        columns: (1fr, 1fr),
        align: (left, right),
        [第#counter(heading).display()章: #current-chapter.get()],
        [全体の文書タイトル]
      )
      #line(length: 100%, stroke: 0.5pt),
    ]
  ],
  footer: context [
    #set text(size: 9pt)
    #set align(center)
    #if counter(page).get().first() > 1[
      - #counter(page).display() -
    ]
  ]
)

// 見出し（レベル1）が呼ばれるたびに `current-chapter`を更新
#show heading.where(level: 1): it => {
    current-chapter.update(it.body)  // 状態を更新
    it  // 見出しをそのまま表示
}
```

状態管理機能（`state`）を使って`current-chapter`を定義し、
レベル1の見出しが呼ばれる更新されるにしています。

`context`内で`current-chapter.get()`することで、
各ページでの章タイトルを取得できます。

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
