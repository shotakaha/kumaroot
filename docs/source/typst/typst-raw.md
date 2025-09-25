# コードブロックしたい（`#raw`）

```typst
#raw(
    lang: "python",
    theme: "halcyon.tmTheme",
    block: true,
)[
    コードブロック
]
```

[raw要素](https://typst.app/docs/reference/text/raw/)でコードブロックを表示できます。

## テーマを設定したい（`theme`）

```typ
#set raw(theme: auto)    // デフォルトテーマ
#set raw(theme: none)    // シンタックスハイライトをOFF
```

`theme`オプションで、コードブロック表示の見た目を変更できます。
ドキュメント全体に設定したいので`#set raw`を使います。

```typ
#set raw(theme: "halcyon.tmTheme")
```

テーマは`TextMate`で利用されているフォーマットが使えます。
その形式にしたがって自作することもできます。

:::{note}

公式ドキュメントに`halcyon.tmTheme`を使ったサンプルが載っていますが、
ファイルが見つからずコンパイルエラーになります。

:::

## カスタマイズしたい

```typst
// 全体的な設定
#set raw(font: "Moralerspace Kryption")
#set raw(size: 12pt)

// コードブロック表示
#show raw.where(block: true): it => block(
    fill: rgb("#1d2433"),    // 背景色
    inset: 2em,
    radius: 1em,
    width: 100%,
    text(fill: rgb("#a2aabc"), it)    // 文字色
)

// インライン表示
#show raw.where(block: false): it => box(
    fill: rgb("#afafaf"),
    text(fill: rgb("#1f1f1f"), it)
)
```

素のままだと、コードブロックであることが視認しづらいため
`#show`ルールと`block要素`を使って、背景を追加しています。

:::{seealso}

- [](../latex/latex-minted.md)

:::
