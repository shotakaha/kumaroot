# コードブロックしたい（``raw``）

```typst
`raw`インライン要素
```

````typst
```言語名 raw```インライン要素
````

````typst
```typst
#raw(lang: 言語名)[ブロック要素]
```
````

[raw要素](https://typst.app/docs/reference/text/raw/)でコードブロックを表現できます。

Markdownの用に「`（backtick）」を使った表記もあります。

:::{seealso}

- [](../latex/latex-usepackage-minted.md)

:::

## 背景色したい

```typst
#show raw: set block(fill: luma(235), inset: 2em, radius: 1em, width: 100%)
#show raw: set text(font: ("Roboto Mono", "Noto Sans CJK JP"))
```

素のコードブロックはブロックであることが視認しづらいです。
``#show``ルールと``block要素``を使って、背景を追加するとよいです。
