# 変数したい（`#let`）

```typst
#let name = value
```

`#let`コマンドを使って、変数を定義できます。
一度定義した変数名は、同じファイルで後から再利用できます。
この値は再代入できない定数的な値です。

## 配列したい（`(...)`）

```typst
#let authors = ("著者1", "著者2")

このドキュメントは
#authors.at(0)さんと
#authors.at(1)さんが執筆しました。
```

## 辞書したい（`(key: value)`）

```typst
#let config = (
  font: "Noto Serif",
  size: 12pt,
)

フォント: #config.font
サイズ: #config.size
```
