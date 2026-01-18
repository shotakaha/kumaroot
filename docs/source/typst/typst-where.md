# セレクターしたい（`#show` + `.where`）

```typst
#show heading.where(level: 1): it => {...}
#show heading.where(level: 2): it => {...}
```

`.where`は、
要素のプロパティに基づいて**条件付きで要素を選択・抽出**するメソッドです。
抽出された要素に対して、`show`ルールでスタイリングを適用できます。

## 見出しレベルしたい（`#heading.level`）

```typst
#show heading.where(level: 1): it => {
  set align(center)[
    #it
  ]
}

// レベル2の見出しを赤色
#show heading.where(level: 2): it => {
  set text(red)[
    #it
  ]
}
```

## コードブロックしたい（`#raw.block`）

```typst
// インラインコードのスタイル
#show raw.where(block: false): box.with(
  fill: luma(240),
  inset: (x: 3pt, y: 0pt),
  radius: 2pt,
)

// ブロックコードのスタイル
#show raw.where(block: true): block.with(
  fill: luma(240),
  inset: 10pt,
  radius: 4pt,
)
```

## 図表リストしたい

```typst
// 画像のリストだけを作成
#outline(
  title: [図一覧],
  target: figure.where(kind: image),
)

// 表のリストだけを作成
#outline(
  title: [表一覧],
  target: figure.where(kind: table),
)
```

## ヘッダーに見出しを表示したい

```typst
#set page(
    header: context {
  // 現在位置より前のレベル1見出しを取得
  let headings = query(
    heading.where(level: 1).before(here())
  )
  if headings.len() > 0 {
    let current = headings.last()
    emph(current.body)
  }
})
```
