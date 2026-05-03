# コードブロックしたい（`#raw`）

`````typst
// 簡易マークアップ

これは `inline code` です。

```python
# これはコードブロックです。
def hello():
    print("hello")
```

// 関数マークアップ
これは #raw[inline code]です。

#raw(
  lang: "python",
  block: true,
)[
# これはコードブロックです。
def hello():
    print("hello")
]
`````

`raw`要素で、コードブロックを表示できます。
`lang`オプションでシンタックスハイライトする言語を設定できます。
`block`オプションで、インライン表示とブロック表示を変更できます。

backtickを使った簡易マークアップの場合、
1つの場合はインライン表示、
3つの場合はブロック表示、となります。

## ブロック表示したい（`#raw.block`）

```typst
#raw(
  "コードサンプル",
  block: true
)
```

`block`オプションで、
インライン表示とブロック表示を変更できます。

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
#show raw: set text(font: ("Moralerspace Krypton", "HackGen35Console NF"))
```

コードブロックを表示するときは、等幅フォント（モノフォント）を設定するとよいです。
上記のサンプルでは、コード用フォントとして
`Moralerspace Krypton`と
`HackGen35Console NF`を指定しています。

## コードブロックを設定したい（`raw.where(block: true)`）

```typst
// フォント設定
#show raw: set text(font: "Noto Sans Mono")
// ブロックの設定
#show raw.where(block: true): set block(
  fill: luma(95%),
  inset: 1em,
  radius: 1em
)

#raw(
  lang: "python",
  block: true,
)[
def hello():
    print("hello")
]
```

`raw.where(block: true)`で、ブロック表示のコードブロックを選択できます。
上記のサンプルでは、すべてのコードブロックを対象に、
背景色（`fill: luma(95%)`）、
パディング（`inset: 1em`）を追加し、
角を丸く（`radius: 1em`）しています。

:::{seealso}

- [](../latex/latex-minted.md)

:::

## インラインコードを設定したい（`raw.where(block: false)`）

```typst
#show raw.where(block: false): set text(fill: olive)
```

`raw.where(block: false)`で、インライン表示のコードブロックを選択できます。
上記のサンプルでは、すべてのインラインコードを対象に、文字色をオリーブ（`fill: olive`）にしています。

## 言語名を表示したい

```typst
#show raw.where(block: true): it => {
  block(
    stroke: luma(90%),
  )[
    // 言語名を表示するブロック
    block[
      #align(right)[
        #it.lang
      ]
    ]
    // コードをそのまま表示するブロック
    block(
      stroke: luma(80%),
    )[
      #it
    ]
  ]
}
```

コードブロックの言語名を表示することもできます。
デフォルトでは表示されていないため、`#show raw.where(block: true): it => {...}`の形で、コードブロック全体をクロージャーして装飾する必要があります。

上記のサンプルでは、コードブロック全体を`block`要素に変換して、言語名を表示するブロックとコードを表示するブロックの2つを組み合わせています。
