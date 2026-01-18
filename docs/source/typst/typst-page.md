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
// A4サイズ: w210.0 mm x h297.0 mm
#set page(paper: "a4")

// B5サイズ: w182.0 mm x h257.0 mm
#set page(paper: "jis-b5")

// 20cm四方の印刷物
#set page(
  width: 20.0cm,
  height: 20.0cm
)
```

[page要素のpaperオプション](https://typst.app/docs/reference/layout/page/#parameters-paper)で用紙サイズを変更できます。
デフォルトは`"a4"`です。
ISO規格のほかにもJIS規格（日本）、DIN規格（ドイツ）、ANSI規格（アメリカ）など多様な規格の用紙サイズが定義されています。

`width`と`height`オプションで長さを直接指定できます。

:::{note}

用紙サイズ名は[page.rs](https://github.com/typst/typst/blob/main/crates/typst-library/src/layout/page.rs)にハードコードされていました。

:::

### ポスター発表したい

```typst
// A0サイズ: w841.0 mm x h1189.0 mm
#set page(paper: "a0")
// 直接指定
#set page(width: 841.0mm, height: 1189.0mm)
```

### プレゼンテーションしたい

```typst
// アスペクト比16:9（w297.0 mm x h167.0625 mm）
#set page(paper: "presentation-16-9")

// アスペクト比4:3（w280.0 mm x h210.0 mm）
#set page(paper: "presentation-4-3")
```

### 名刺したい

```typst
// 日本の名刺サイズ
#set page(paper: "jp-business-card")  // w91.0 mm x h55.0 mm
#set page(paper: "jp-shiroku-ban-4")  // w264.0 mm x h379.0 mm
// 直接指定
#set page(width: 91.0mm, height: 55.0mm)
```

日本の名刺サイズ（`jp-business-card`など）もありました。

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

## ノンブルしたい（`numbering` / `number-align`）

```typst
// 右上に「現在のページ / 総ページ数」を表示
#set page(
  numbering: "1 / 1",
  number-align: right + top,
)
```

`numbering`オプションでノンブル（＝ページ番号）の表示形式を変更できます。
デフォルトは`none`（＝非表示）です。
`number-align`で表示位置を変更できます。
`left | center | right` + `top | bottom` の組み合わせで指定します。
デフォルトは`center + bottom`です。

```typst
#set page(numbering: none)   // 非表示（デフォルト）
#set page(numbering: "1")    // 1, 2, 3, ... で表示
#set page(numbering: "i")    // i, ii, iii, ... で表示

// カスタム表示
#set page(numbering: "1 of 1")   // 現在のページ数 of 総ページ数
#set page(numbering: "1 / 1")    // 現在のページ数 / 総ページ数
```

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

:::{warning}

`header`オプションや`footer`オプションを設定すると、
ノンブル（`numbering`オプション）の設定は無視されます。
ノンブルしたい場合は、それぞれのコンテンツとして自分で再定義する必要があります。

:::

## ヘッダーしたい（`header`）

```typst
#set page(
  header: [ヘッダー],
  header-ascent: 1em,
)
```

`header`オプションで、文書のすべてのページにヘッダーを表示できます。
デフォルトは`auto`です。
`numbering`オプションが有効になっている場合は、ノンブルが表示されます。
`header-ascent`で、本文エリアとヘッダーのアキを調整できます。

:::{note}

`ascent`なので、正の長さにすると上方向に移動します。
負の長さも設定できます。

:::

## フッターしたい（`footer`）

```typst
#set page(
  footer: [フッター],
  footer-descent: 1em,
)
```

`footer`オプションで、文書のすべてのページにフッターを表示できます。
デフォルトは`auto`です。
`numbering`オプションが有効になっている場合は、ノンブルが表示されます。
`footer-descent`で、本文エリアとフッターのアキを調整できます。

:::{note}

`descent`なので、正の長さにすると下方向に移動します。
負の長さ設定できます。

:::

### レポート用ヘッダーとフッター

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

### 章タイトルとヘッダー

```typst
#let current-chapter = state("chapter", "")

#let custom-header = context {
  set text(size: 9pt)
  let page-num = counter(page).get().first()
  if page-num > 1 {
    grid(
      columns: (1fr, 1fr),
      align: (left, right),
      [第#counter(heading).display()章: #current-chapter.get()],
      [全体の文書タイトル]
    )
    line(length: 100%, stroke: 0.5pt),
  }
}

#let custom-footer context {
  set text(size: 9pt)
  set align(center)
  let page-num = counter(page).get().first()
  if page-num > 1 {
    "--- " + counter(page).display() + " ---"
  }
}

#set page(
  header: custom-header,
  footer: custom-footer,
)

// 見出し（レベル1）が呼ばれるたびに `current-chapter`を更新
#show heading.where(level: 1): it => {
    current-chapter.update(it.body)  // 状態を更新
    it  // 見出しをそのまま表示
}
```

状態管理機能（`state`）を使って、ヘッダーに章タイトルを出力できます。

状態管理用の変数`current-chapter`を定義します。
レベル1の見出しが呼ばれるたびに、この変数を更新し、新しい章タイトルを保存します。

`context`内で`current-chapter.get()`を呼ぶと、各ページでの章タイトルを取得できます。

:::{caution}

このサンプルはうまくいっていそうで、うまくいってないです。
章が切り替わるページでは、前のページのタイトルがヘッダーに表示されてしまいます。
修正方法が分からずそのままにしてあります。
`state`関数による状態管理を、なんとなく理解する参考にしてください。

:::

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

## 背景色したい（`fill`）

```typst
#set page(fill: rgb(blue))
```

`fill`オプションで文書全体の背景色を変更できます。

## 透かししたい（`background`）

```typst
#set page(background: [
  #rotate(-45deg)[
    #text(size: 2em, fill: luma(90%))[
      *preliminary*
    ]
  ]
])
```

`background`オプションで、ドキュメントのすべてのページの背景にコンテンツを設定できます。
「preliminary」や「confidential」などの透かしを入れたい場合に利用できます。

:::{note}

最前面にコンテンツを表示できる
`foreground`オプションもあります。

:::

## リファレンス

- [page - Element](https://typst.app/docs/reference/layout/page/)
