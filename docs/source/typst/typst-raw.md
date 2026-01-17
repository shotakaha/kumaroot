# コードブロックしたい（`#raw`）

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

## コードブロックしたい

```typst
#raw(
    lang: "python",
    theme: "halcyon.tmTheme",
    block: true,
)[
    コードブロック
]
```

[raw要素](https://typst.app/docs/reference/text/raw/)のオプションで、
コードブロック表示を細かく変更できます。

:::{seealso}

- [](../latex/latex-minted.md)

:::

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

## カスタマイズしたい

```typst
// 全体的な設定
//#set raw(font: "Moralerspace Kryption")
//#set raw(size: 12pt)

// コードブロック表示
#show raw.where(block: true): it => {
  // 文字色を変更
  set text(fill: rgb("#a2aabc"))
  // 背景を変更
  block(
    fill: rgb("#1d2433"),    // 背景色
    inset: 2em,
    radius: 1em,
    width: 100%,
  )
}

// インライン表示
#show raw.where(block: false): it => {
  // 文字色を変更
  set text(fill: rgb("#1f1f1f"))
  // 背景を変更
  box(
    fill: rgb("#afafaf")
  )[
    #it
  ]
}
```

デフォルトのままだと、
コードブロックであることが視認しづらいため
`#show`ルールで表示スタイルを変更してみました。

`where`セレクターを使って、
ブロック表示とインライン表示で
異なるスタイルを適用しています。
