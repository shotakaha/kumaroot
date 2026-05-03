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
用紙サイズや余白の大きさ、ヘッダーやフッターの内容、ノンブルの表示方法、ページ背景など、ページ全体を設定できます。
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
```

`paper`オプションで用紙サイズを変更できます。
デフォルトは`"a4"`です。
ISO規格のほかにもJIS規格（日本）、DIN規格（ドイツ）、ANSI規格（アメリカ）など多様な規格の用紙サイズが定義されています。

:::{note}

用紙サイズ名は[page.rs](https://github.com/typst/typst/blob/main/crates/typst-library/src/layout/page.rs)にハードコードされていました。
:::

```typst
// 20cm四方の印刷物
#set page(
  width: 20.0cm,
  height: 20.0cm
)
```

`width`と`height`オプションで長さを直接指定できます。

```typst
// A0サイズ: w841.0 mm x h1189.0 mm
#set page(paper: "a0")
// 直接指定
#set page(width: 841.0mm, height: 1189.0mm)
```

ポスター発表する場合は、A0サイズが一般的です。
`paper: "a0"`を指定するか、`width`と`height`を直接指定します。

```typst
// アスペクト比16:9（w297.0 mm x h167.0625 mm）
#set page(paper: "presentation-16-9")

// アスペクト比4:3（w280.0 mm x h210.0 mm）
#set page(paper: "presentation-4-3")
```

発表スライド用の選択肢もあります。
少し前は4:3でしたが、現在は16:9が主流です。

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
)

#set page(
  margin: (
    top: 1cm,
    bottom: 2cm,
    left: 3cm,
    right: 4cm,
  )
)
```

上下左右を一括、左右（`x`）と上下（`y`）、
すべて別々（`top` / `bottom` / `left` / `right`）など柔軟に設定できます。

## ノンブルしたい（`numbering` / `number-align`）

```typst
#set page(numbering: "1")    // 1, 2, 3, ... で表示
#set page(numbering: "1 / 1")  // 現在のページ数 / 総ページ数

#set page(numbering: none)   // 非表示（デフォルト）
#set page(numbering: "i")    // i, ii, iii, ... で表示
#set page(numbering: "1 of 1")  // 現在のページ数 of 総ページ数
```

`numbering`オプションででノンブル（＝ページ番号）を設定できます。
デフォルトは`none`（＝非表示）です。
`numbering: "1"`で単純にページ数を表示できます。
`numbering: "1 / 1"`で、現在のページ数と総ページ数を表示できます。
`numbering: "i"`でローマ数字で表示できます。

```typst
// 右上に「現在のページ / 総ページ数」を表示
#set page(
  numbering: "1 / 1",
  number-align: right + top,
)
```

`number-align`オプションでノンブルの表示位置を変更できます。
デフォルトは`center + bottom`（＝中央下）です。
`left | center | right` + `top | bottom` の組み合わせで指定します。
上のサンプルでは、右上にノンブルを表示する設定になっています。

```typst
// 1ページ目（表紙）はノンブル非表示
// 2ページ目以降は「現在のページ / 総ページ数」を表示
#let footer-content = context {
  if counter(page).get().first() > 1 [
    #align(center)[
      #counter(page).display() / #counter(page).final().at(0)
    ]
  ]
}

#set page(
  footer: footer-content
)
```

表紙をノンブル非表示にしたい場合は、自分で条件を設定する必要があります。
上のサンプルでは、`counter(page).get().first()`で現在のページ数を取得し、1ページ目はノンブル非表示、2ページ目以降は「現在のページ / 総ページ数」を表示するようにしています。

:::{note}

`counter`は`context`内で使用する必要があります。
`counter(page).get()`の戻り値は配列になっているので、`.first()`で現在のページ数を取得し、`.final().at(0)`で総ページ数を取得しています。

:::

:::{warning}

ノンブルはデフォルトでページの中央下に表示されますが、
`footer`オプションを設定すると無視されます。

`footer`オプション（や`header`オプション）を設定する場合は、ノンブル表示も自分で再定義する必要があります。

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

```typst
#let custom-header = {
  set text(size: 9pt)
  grid(
    inset: 1em,
    // stroke: 0.5pt,
    columns: (1fr, auto, 1fr),
    gutter: 1em,
    align: (left, center, right),
    [左寄せのヘッダー],   // ここを編集
    [中央のヘッダー],     // ここを編集
    [右寄せのヘッダー],   // ここを編集
  )
}

// ページ設定に追加
#set page(
  header: custom-header,
)
```

`grid`関数を使って、ヘッダーを3分割し、左寄せ・中央・右寄せのヘッダーを作成できます。

:::{seealso}

- [](../latex/latex-fancyhdr.md)

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
)

// 3段組
#set page(
  columns: 3,
)
```

`columns`オプションで段組の数を変更できます。
デフォルトは1段（`columns: 1`）です。

:::{seealso}

`#page`のオプションでは段間を設定できないようです。
段間を調整したい場合は、
[#columns要素](https://typst.app/docs/reference/layout/columns/)
で本文中で段組するほうがよさそうです。

:::

:::{caution}

`set page(columns: n)`で段組すると、タイトルも段組に含まれます。
通常、タイトルは段組の外に配置したいと思うので、
タイトルを表示したあとに`#page(columns: n)`を呼ぶとよいです。

```typst
#set page(paper: "a4", margin: 25mm)

#title[ここにタイトルを表示]

#page(columns: 2)  // タイトルのあとに段組を設定
```

:::

## 縦置きしたい（`flipped`）

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
// 透かし文字の設定
// 斜めに回転させて、薄いグレーで表示
#let watermark = {
  rotate(-45deg)[
    #text(size: 2em, fill: luma(90%))[
      *preliminary*
    ]
  ]
}

#set page(background: watermark)
```

`background`オプションで、ドキュメントのすべてのページの背景にコンテンツを設定できます。
「preliminary」や「confidential」などの透かしを入れたい場合に利用できます。

```typst
#let header-band = {
    place(top, rect(width: 100%, height: 20mm, fill: luma(90%)))  // ページ上部に背景を配置
}
#let footer-band = {
    place(bottom, rect(width: 100%, height: 20mm, fill: luma(90%)))  // ページ上部に背景を配置
}

#set page(
  background: {
    header-band
    footer-band
  }
)
```

`background`オプションで、ページの上下に帯を配置できます。
`place`関数でそれぞれの配置（`top` / `bottom`）を指定して、
`rect`関数でページ幅いっぱい（`width: 100%`）の帯を作成して、背景色を薄いグレーにしています。

:::{caution}

`header`や`footer`オプションで指定すると、本文の幅に制限されます。

:::

:::{note}

最前面にコンテンツを表示できる
`foreground`オプションもあります。

:::

## リファレンス

- [page - Element](https://typst.app/docs/reference/layout/page/)
