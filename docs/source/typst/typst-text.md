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

## フォントを確認したい（``typst fonts``）

```console
$ typst fonts
$ typst fonts --variants
Hiragino Sans
- Style: Normal, Weight: 100, Stretch: 100%
- Style: Normal, Weight: 200, Stretch: 100%
- Style: Normal, Weight: 250, Stretch: 100%
- Style: Normal, Weight: 300, Stretch: 100%
- Style: Normal, Weight: 400, Stretch: 100%
- Style: Normal, Weight: 500, Stretch: 100%
- Style: Normal, Weight: 600, Stretch: 100%
- Style: Normal, Weight: 700, Stretch: 100%
- Style: Normal, Weight: 800, Stretch: 100%
- Style: Normal, Weight: 900, Stretch: 100%
```

ターミナルで``typst fonts``すると、利用できるフォントの一覧を表示できます。
``--variants``オプションでより詳細に表示できます。

```console
$ typst fonts | rg HackGen
HackGen
HackGen Console
HackGen Console NF
HackGen35
HackGen35 Console
HackGen35 Console NF

$ typst fonts | rg One
Cherry Bomb One
Darumadrop One
Klee One
Merienda One
Monomaniac One
Rampart One
Reggae One
RocknRoll One
Train One
```

フォント名を指定して表示する機能はないみたいなので、検索コマンド（ここでは``ripgrep``）と組み合わせて探しています。

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
