# 関数したい（`#let`）

```typst
#let greet(name) = {
    let greeting = "Hello, " + name
    greeting + "!"
}

#greet("World")
```

`#let`キーワードで関数を定義できます。
定義した関数は`#関数名`で、本文の任意の箇所で呼び出すことができます。

## 位置引数したい

```typst
#let greet(first, last) = {
    let greeting = "Hello, " + first
    greeting + " " + last + "!"
}

#greet("First", "Second")
```

位置引数（positional arguments）は、
位置で識別される引数です。
関数が呼び出された時に、最初から順番に処理されます。

## 名前付き引数したい

```typst
#let greet(first: none, last: none) = {
    let greeting = "Hello, " + first
    greeting + " " + last + "!"
}

#greet(first: "First", last: "Second")
#greet(last: "First", first: "Second")
#greet("First", "Second")  // => エラー
```

名前付き引数（named arguments）は
`変数名: 値`の形式で指定する引数です。
関数を定義するときにデフォルト値を指定すると、名前付き引数にできます。

:::{note}

```typst
#let greet(name, hello: "Hello") = {
    let greeting = hello + ", " + name
    greeting + "!"
}

#greet("World")  // => Hello, World!
#greet("World", hello: "Good morning")  // => Good morning, World!
```

位置引数と名前付き引数は混在できます。
Pythonなど多くのプログラミング言語と同じで、
位置引数を先に定義する必要があります。

:::

## コンテンツブロックしたい

```typst
#greet(hello: [*Hello*])  // => 太字のHello
#greet(hello: "*Hello*")  // => そのまま *Hello*
```

角括弧（`[...]`）で囲んだ内容は「コンテンツブロック」と認識され、マークアップしたコンテンツをそのまま渡すことができます。

### 可変長引数（任意の数の引数）

`..` 演算子で任意の数の引数を受け取れます：

```typst
#let list(title, ..items) = {
  let item-text = items
    .pos()
    .map(item => [- #item])
    .join()

  [
    == #title
    #item-text
  ]
}

#list("Shopping", "Apples", "Bread", "Milk")
```

可変長引数には以下のメソッドがあります：

- `.pos()`: 位置引数を配列として取得
- `.named()`: 名前付き引数を辞書として取得

## 制御フローを含む関数

### 条件分岐（if-else）

```typst
#let status(value) = {
  if value > 0 [
    Positive
  ] else if value == 0 [
    Zero
  ] else [
    Negative
  ]
}

Result: #status(-5)
```

### ループ処理（for）

```typst
#let enumerate-items(..items) = {
  let index = 1
  for item in items.pos() {
    [#index. #item]
    index = index + 1
  }
}

#enumerate-items("First", "Second", "Third")
```

複数の値をループで処理する：

```typst
#let pair-list(..values) = {
  let pairs = values.pos()
  for (key, value) in pairs.zip() {
    [#key → #value]
  }
}
```

### ループ制御したい（`break` / `continue`）

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

      `#code`
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
    [*#severity.upper():* #title]
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
    .filter(x => type(x) == "integer" and x > 0)
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

## 無名関数と矢印構文

### 矢印構文での関数定義

`=>` 演算子を使って、その場で無名関数を定義できます。これは `#let` を使わない別の関数定義方法です：

```typst
// 単一パラメータ（括弧は省略可能）
#let double(x) = (x => x * 2)(5)
// 結果: 10

// 複数パラメータ
#let add = (a, b) => a + b
#add(3, 5)
// 結果: 8
```

### show ruleでの矢印関数

show ruleでは矢印関数がよく使われます：

```typst
#show "hello": it => [#it THERE]

hello world
// 結果: hello THERE world
```

見出しを装飾する例：

```typst
#show heading: it => {
  set align(center)
  set text(font: "Inria Serif")
  ~ #emph(it.body) ~
}

= Welcome
```

### 配列操作での矢印関数

`.map()` や `.filter()` などの高階関数に矢印関数を渡す：

```typst
#let numbers = (1, 2, 3, 4, 5)

// map: 各要素を2倍にする
#numbers.map(x => x * 2)
// 結果: (2, 4, 6, 8, 10)

// filter: 3より大きい値のみ
#numbers.filter(x => x > 3)
// 結果: (4, 5)
```

### `#let` vs 矢印構文の使い分け

**`#let func(...) = ...` を使う場合：**

- 関数を複数回呼び出す
- 複雑なロジックを含む
- 他のファイルからインポートする必要がある

```typst
#let alert(body, fill: red) = {
  rect(
    fill: fill,
    inset: 8pt,
    radius: 4pt,
    [*Warning:* #body]
  )
}

#alert[Danger!]
#alert(fill: blue)[Caution]
```

**矢印構文 `(...) => ...` を使う場合：**

- show ruleで一度きりの処理
- 配列操作のコールバック
- シンプルな計算式

```typst
#show heading.where(level: 2): it => [📌 #it.body]

#let filtered = data.filter(item => item.active)
```

### 矢印構文の制限事項

矢印関数には以下の制限があります：

1. **インポート不可** - 他のファイルからインポートできない
2. **再帰呼び出し困難** - 関数が自身を参照する名前がない
3. **複雑なロジック向けでない** - シンプルな処理に適している

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
