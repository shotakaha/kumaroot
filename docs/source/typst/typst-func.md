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

`#let`コマンドを使って、関数を定義できます。
定義した関数は、同じファイル内の任意の箇所で呼び出すことができます。
この値は再代入できない定数的な値です。

上記のサンプルでは`#cover`関数を定義しています。
この関数は、レポートの表紙を出力するための関数で、
タイトル（`title`）、
著者（`author`）、
日付（`date`）を引数として受け取ります。
関数の中では、それぞれの引数をブロック要素（`block`）で囲んで表示しています。

## 位置引数したい

```typst
#let cover(
  title,
  author,
  date
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

#cover(
  "レポートのタイトル",
  "著者名",
  "日付"
)
```

位置引数（positional arguments）は、位置で識別される引数です。
初期値がない引数は、位置引数になります。
関数を呼び出すときは、引数の位置に対応する値を指定します。

## 名前付き引数したい

```typst
#let cover(
  title: none,
  author: none,
  date: none
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

#cover(title: "レポートのタイトル", author: "著者", date: "日付")
#cover("レポートのタイトル", "著者名", "日付")  // => エラー
```

名前付き引数（named arguments）は、引数名で識別される引数です。
初期値がある引数は、名前付き引数になります。
関数を呼び出すときは、引数名と値を`引数名: 値`の形式で指定します。
位置引数と名前付き引数は混在できますが、位置引数を先に定義する必要があります。

## 可変長引数したい

```typst
#let cover(
  title,
  ..authors,
  date: datetime.today().display()
) = {
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

可変長引数（variadic arguments）は、引数の数が不定な場合に使用します。
スプレッド演算子（`..`）を使って定義します。
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

Typstのコンテンツブロックは、とても柔軟な機能です。
引数の内容をユーザーに任せることができるため、関数の再利用性が高まります。

:::{note}

引数の自由度と制限の設計は毎回の悩みです。
自由度を高くしすぎると、Typstの標準機能の薄いラッパーになってしまう可能性があります。
制限を強くしすぎると、ユーザーが関数を使いにくくなってしまう可能性があります。
関数の目的や利用シーンに応じて、適切な自由度と制限のバランスを見つけることが重要です。

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

## 無名関数したい

```typst
#let custom-heading = it => [
  #upper(it.body)
]

#show heading: custom-heading
```

無名関数（unnamed functions）は、関数定義の一種で、名前を持たない関数です。
`=>`を使って定義します。
引数は1つだけで、関数の本体は`[...]`で囲まれたコンテンツブロックになります。
このサンプルでは、`custom-heading`という変数に、引数`it`を大文字に変換する無名関数を代入しています。

この関数は、`#show heading`ルールで使用され、見出しのテキストを大文字に変換します。

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
