# コードブロックしたい（`#raw`）

```typst
#show raw: text.with(font: "Noto Sans Mono")
#show raw.where(block: true): block.with(fill: luma(95%), inset: 1em, radius: 1em)
#show raw.where(block: false): text.with(fill: olive)

#raw(
  lang: "python",
  block: true,
)[
def hello():
    print("hello")
]
```

[raw要素](https://typst.app/docs/reference/text/raw/)で、コードブロックを表示できます。

:::{seealso}

- [](../latex/latex-minted.md)

:::

## マークアップしたい

`````typst

インラインで`code`をマークアップ表示できます。

ブロックで

```python
def hello():
    print("hello")
```

を表示できます。

`````

コードブロックは、Markdown記法と同じように
`` `（back-tick） ``
でマークアップできます

## ブロック表示したい（`#raw.block`）

```typst
#raw(
  "コードサンプル",
  block: true
)
```

`block`オプションで、
インライン表示とブロック表示を変更できます。

backtickを使ったマークアップの場合、
1つの場合はインライン表示、
3つの場合はブロック表示、となります。

## シンタックスしたい（`#raw.lang`）

```typst
#raw(
  "コードサンプル",
  lang: "python",
)
```

`lang`オプションでシンタックスハイライトする言語を設定できます。
Markdown記法でサポートされている言語名の他に、Typst固有の
`typ`（Typst markup）、
`typc`（Typst code）、
`typm`（Typst math）
がサポートされているそうです。

## 等幅フォントしたい

```typst
#show raw: text.with(font: "Noto Sans Mono")
```

コードブロックは表示するときは、等幅フォント（モノフォント）を設定するとよいです。

## 文字色したい

```typst
#show raw.where(block: false): text.with(fill: olive)
```

インライン表示するときの文字色を変更するサンプルです。
`raw.where(block: false)`でインライン表示を選択しています。

## 背景色したい

```typst
#show raw.where(block: true): block.with(fill: luma(95%), inset: 1em, radius: 1em)
```

ブロック表示するときの背景色を追加するサンプルです。
`raw.where(block: true)`でブロック表示を選択しています。
