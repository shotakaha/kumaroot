# 参考文献したい（`#bibliography`）

```typst
// 参考文献を読み込む
#bibliography("papers.bib")

このことが知られている。 #cite(<key1>)
それは複数の文献にも書いてある。 @key2 @key3
```

`#bibliography`要素で参考文献ファイルを読み込ませると、
`#cite`要素で文献キー（`<ラベル型>`）を指定して引用できるようになります。

参考文献は
[Hayagriva](https://github.com/typst/hayagriva)形式（`.yaml`）もしくは
BibLaTeX形式（`.bib`）がサポートされています。

:::{note}

Hayagrivaは、Typst用に開発された参考文献パッケージのようです。

:::

:::{seealso}

- [](./typst-ref.md)
- [](./typst-cite.md)

:::

## リファレンス

- [bibliography | Element | Typst](https://typst.app/docs/reference/model/bibliography/)
