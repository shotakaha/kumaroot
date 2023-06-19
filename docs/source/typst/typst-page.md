```{eval-rst}
.. index::
    pair: レイアウトしたい; Typst
    pair: ヘッダーしたい; Typst
```

# レイアウトしたい（``page``）

```rust
#set page(
    paper: "a4",
    margin: (x: 25mm, y: 25mm),
    columns: 1,
    //fill: 背景色,
    numbering: "1 / 1",
    number-align: center,
    header: [
        #set text(8pt)[ヘッダー・左]
    ]
)
```

[page要素](https://typst.app/docs/reference/layout/page/)でページ全体の設定ができます。
用紙のサイズや余白の大きさ、ヘッダーやフッターの内容、ノンブルの表示方法など設定できます。

:::{seealso}

- [](../latex/latex-geometry.md)
- [](../latex/latex-fancyhdr.md)

:::
