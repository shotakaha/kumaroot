# 引用したい（`#cite`）

```typst
// 簡易マークアップ
〜は〜である @key1。

// 関数マークアップ
〜は〜である #cite("key1")。
```

`#cite`要素で、文献を引用できます。
引数に文献キーを指定します。

文献キーは、`#bibliography`要素で定義した文献キーを指定します。
複数の文献を引用する場合は、キーをカンマで区切って指定できます。

引用スタイルは、`#bibliography`要素で指定したスタイルが適用されます。

## リファレンス

- [cite | Element | Typst](https://typst.app/docs/reference/model/cite/)
