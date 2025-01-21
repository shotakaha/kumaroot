# コードブロックしたい（``#raw``）

```typst
#show raw: set block(fill: luma(235), inset: 2em, radius: 1em, width: 100%)
#show raw: set text(font: ("Roboto Mono", "Noto Sans CJK JP"))
```

[raw要素](https://typst.app/docs/reference/text/raw/)でコードブロックを表示できます。
素のままだと、コードブロックであることが視認しづらいため
``#show``ルールと``block要素``を使って、背景を追加しています。

:::{seealso}

- [](../latex/latex-minted.md)

:::
