# 関数したい（`#let`）

```typst
// レポートの表紙を出力する関数を定義
#let cover(
    title,
    author,
    date: datetime.today().display()
) = {
  block()[
    #title
  ]

  block()[
    #author
  ]

  block()[
    #date
  ]
}

// 表紙を出力
#cover("レポートのタイトル", "著者名", date: "2026/01/01")
```

`#let`キーワードで関数を定義できます。
ここではレポートの表紙を出力する関数を作ってみました。
定義した関数は`#関数名`で、本文の任意の箇所で呼び出すことができます。

## 位置引数したい

```typst
#let cover(title, author, date) = {
  block()[
    #title
  ]
  block()[
    #author
  ]
  block()[
    #date
  ]
}

#cover("レポートのタイトル", "著者名", "日付")
```

位置引数（positional arguments）は、
位置で識別される引数です。
関数が呼び出された時に、最初から順番に処理されます。

## 名前付き引数したい

```typst
#let cover(title: none, author: none, date: none) = {
  block()[
    #title
  ]
  block()[
    #author
  ]
  block()[
    #date
  ]
}

#cover(title: "レポートのタイトル", author: "著者", date: "日付")
#cover("レポートのタイトル", "著者名", "日付")  // => エラー
```

名前付き引数（named arguments）は
`変数名: 値`の形式で指定する引数です。
関数を定義するときにデフォルト値を指定すると、名前付き引数にできます。

:::{note}

```typst
#let cover(
    title,
    author,
    date: datetime.today().display()
) = {...}

#cover("レポートのタイトル", "著者名")  // => 日付は自動取得
#cover("レポートのタイトル", "著者名", date: "2026/01/16")  // => 日付を固定
```

位置引数と名前付き引数は混在できます。
Pythonなど多くのプログラミング言語と同じで、
位置引数を先に定義する必要があります。

:::

## 可変長引数したい

```typst
#let cover(title, ..authors, date: datetime.today().display()) = {
  block()[
    #title
  ]
  block()[
    #authors.pos().join(", ")
  ]
  block()[
    #date
  ]
}

#cover(
  "タイトル",
  "著者1", "著者2", "著者3",
  date: "2026/01/16",
)
```

スプレッド演算子（`..`）で可変長引数を定義できます。
位置引数を配列にする場合は`.pos()`、
名前付き引数を辞書型にする場合は`.named()`で変換できます。

:::{note}

複数の著者を指定する場合はよくあるため、可変長引数のサンプルとしてみましたが、わざわざ可変長引数にするより、そのまま配列として渡せるようにしたほうが可読性がよさそうです。

```typst
#cover(
    title,
    authors: (),
    date: datetime.today().display()) = {
  block()[
    #title
    ]
  block()[
    // authorsは配列なので pos() は不要
    #authors.join(",")
  ]
  block()[
    #date
  ]
}

#cover(
  "タイトル",
  authors: ("著者1", "著者2", "著者3"),
  date: "2026/01/16")
```

:::

## コンテンツブロックしたい

```typst
#cover(
  [*レポートのタイトル*],
  authors: ("著者1", "著者2", "著者3"),
  date: "2026/01/16",
)
```

角括弧（`[...]`）で囲んだ内容は「コンテンツブロック」と認識され、マークアップしたコンテンツをそのまま渡すことができます。
関数の引数にコンテンツブロックをそのまま渡すことができます。

:::{note}

コンテンツブロックを渡すサンプルとして、**太字にしたレポートタイトル**を引数として渡しましたが、このようなタイトル装飾は関数で定義するほうが実用的です。

:::

## 条件分岐したい（`if-else`）

```typst
#let cover(
  title: none,
  authors: (),
  date: datetime.today().display(),
) = {
  if title != none {
    block()[
      #title
    ]
  }

  if authors.len() > 0 {
    block() [
      #authors.jon(", ")
    ]
  }

  if date == none {
    // 日付を非表示
  } else {
    block()[
      #date
    ]
  }
}

#cover(
  title: [*レポートのタイトル*],
  authors: ("著者1", "著者2"),
  date: none,  // 非表示
)
```

`if-else`構文で条件分岐できます。
`#cover`関数のすべての引数を名前付きにして、
デフォルト動作で表示／非表示を分けてみました。

## ループ処理したい（`for`）

```typst
#cover(
  title: none,
  authors: (),
  date: datetime.today().display()
) = {
  // title表示は省略
  if authors.len() > 0 {
    for author in authors {
      block()[
        #author
      ]
    }
  }
}
```

`for`で配列に対してループ処理できます。
このサンプルでは、著者を別行（別ブロック）で表示するようにしました。

## ループ制御したい（`break` / `continue`）

```typst
#let count-to-limit(limit) = {
  for i in range(100) {
    if i == limit { break }
    if calc.rem(i, 2) == 0 { continue }
    [#i ]
  }
}

#count-to-limit(10)
```

`break` / `continue`でループ処理を制御できます。

## 実践的な関数パターン

### パターン1: スタイル設定の再利用

```typst
#let heading-style = (
  size: 16pt,
  weight: "bold",
  fill: navy
)

#let custom-heading(body) = {
  text(..heading-style, body)
}

#custom-heading[Chapter 1]
```

### パターン2: 複数の処理を組み合わせる

```typst
#let code-box(code, lang: "typst") = {
  block(
    fill: luma(240),
    inset: 10pt,
    radius: 4pt,
    [
      *#lang*

      #raw(code)
    ]
  )
}

#code-box("let x = 5", lang: "rust")
```

### パターン3: 条件に応じた異なる出力

```typst
#let note(title, severity: "info") = {
  let color = if severity == "warning" {
    orange
  } else if severity == "error" {
    red
  } else {
    blue
  }

  rect(
    fill: color.lighten(80%),
    stroke: 1pt + color,
    inset: 8pt,
    [*#upper(severity):* #title]
  )
}

#note("All is well", severity: "info")
#note("Watch out!", severity: "warning")
```

### パターン4: データの変換と集約

```typst
#let filter-and-format(..data) = {
  data
    .pos()
    .filter(x => type(x) == int and x > 0)
    .map(x => [Item: #x])
    .join(", ")
}

#filter-and-format(1, -2, 3, "text", 5)
// 結果: Item: 1, Item: 3, Item: 5
```

## show-setルールで関数を使う

`.where` セレクターと組み合わせて、特定の要素に関数を適用：

```typst
// 見出しにカスタム装飾を適用
#let decorated-heading(it) = {
  [✦ #it.body ✦]
}

#show heading.where(level: 2): it => decorated-heading(it)

== Section Title
```

## 無名関数したい

```typst
#let custom-heading = it => [
  #upper(it.body)
]

#show heading: custom-heading
```

`=>`を使って無名関数（unnamed functions）を定義できます。
Show rulesと合わせて使うことが多いです。

:::{note}

上記サンプルでは`custom-heading`という変数に無名関数を代入していますが、通常は
`#show`ルールに直接指定します。

```typst
#show heading: it => [
  #upper(it.body)
]
```

:::

:::{note}

無名関数を使うときには、慣習で`it`という変数名を使うようです。
`it`が持つデータは`fields()`メソッドで確認できます。

```typst
#show heading: it => [
  #it.fields()
]
```

:::

## 関数内での変数スコープ

変数は定義されたブロック内でのみアクセス可能です：

```typst
#let process() = {
  let temp = "temporary value"
  [#temp]
}

#process()
// #temp  ← エラー: scope外

#temp = "これは外側の変数"
#temp  ← OK
```

## ベストプラクティス

1. **デフォルト引数を活用する** - 柔軟で使いやすい関数を作成
2. **名前付き引数を使う** - 引数が3つ以上の場合は名前付きにする
3. **コンテンツ型を活用する** - マークアップを関数で装飾・加工
4. **引数の展開を使う** - 設定を再利用可能な辞書として管理
5. **単一責任** - 1つの関数は1つのことに集中させる
6. **わかりやすい名前** - 関数の役割が名前から明確にわかるように

## 関連ドキュメント

関数の応用例については、以下も参照してください：

- [テンプレートしたい（`#show...with`）](typst-with.md) - `.with` メソッドで引数を事前設定
- [セレクターしたい（`.where`）](typst-where.md) - `.where` メソッドで特定の要素を選択
