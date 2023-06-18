# 和文テキストしたい（``text``）

```rust
#set text(
    font: (
        "HackGen",
        "Noto Sans CJK JP",
    ),
    size: 12pt,
    weight: "regular",
    lang: "ja"

)
```

[text要素のfontパラメーター](https://typst.app/docs/reference/text/text/#parameters-font)を使って、和文フォントに変更できます。
複数のフォントを設定でき、利用可能なフォントが見つかるまで探してくれます。

## こまかく和文フォントしたい

```rust
#[
#set text(font: "Noto Serif CJK JP")
- Noto Serif CJK JP
#set text(font: "Noto Sans CJK JP")
- Noto Sans CJK JP
#set text(font: "Futura")
- Futura; フツラ
#set text(font: "Yusei Magic")
- Yusei Magic; たぬき油性マジック
#set text(font: "HackGen")
- HackGen; 白源
#set text(font: "HackGen Console")
- HackGen Console; 白源コンソール
#set text(font: "HackGen35")
- HackGen35; 白源35
]
```

フォントはいつでも切り替えできます。
