# 変数したい（`#let`）

```typst
#let 変数名 = 値
```

`#let`コマンドを使って、変数を定義できます。
一度定義した変数名は、同じファイルで後から再利用できます。
この値は再代入できない定数的な値です。

## 配列したい

```typst
#let authors = ["著者1", "著者2"]

このドキュメントは
#authors[0]さんと
#authors[1]さんが執筆しました。
```

## 辞書したい

```typst
#let config = (
    font: "Noto Serif",
    size: 12pt,
)

フォント: #config.font
サイズ: #config.size
```

## 関数したい（`func`）

```typst
#let 関数名(引数1, 引数2, ...) => 式

#let 関数名 = func(引数1, 引数2, ...) => 式

#let square(x) = x * x
#let add(x, y) = x + y

#square(3)  // => 9
#add(2, 5)  // 7
```

`#let 関数名`で関数を定義できます。
定義した関数は `#関数名` のように呼び出します。

:::{note}

公式ドキュメントには記載がありませんが、
`func(...) => ...`でも関数を定義できるようです。

:::

```typst
#let factorial(n) = {
    if n <=1 {
        1
    } else {
        n * factorial(n - 1)
    }
}

#factorial(5)  // 120
```

複雑な処理を定義する場合は`=>`の代わりに`{}`ブロックを作成します。
