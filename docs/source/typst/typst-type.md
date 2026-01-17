# 型情報したい（`#type`）

```typst
#let value = 42
#type(value)  // => int
```

`#type`関数で変数の型を取得できます。
自作の関数を作っていてうまくいかないときに、確認すべきデバッグ手順のひとつです。

## 型確認したい

```typst
// 型情報を確認するための関数
#let get_type(value) = {
  block(
    width: 100%,
    stroke: 1pt,
    inset: 1em,
  )[
  - input: #value
  - repr: #repr(value)
  - type: #type(value)
  ]
}
```

型情報を簡単に確認するために
`get_type`という関数を作りました。

```typst
#get_type(42)  // int
#get_type(3.14)  // float
#get_type((...))  // array
#get_type((key: value))  // dictionary
#get_type(true)  // bool
#get_type([...])  // content
#get_type(<...>)  // label
#get_type(x => x + 1)  // function
#get_type(none)   // none
#get_type(auto)   // auto
```

## リファレンス

- [Type - Typst](https://typst.app/docs/reference/foundations/type/)
