# フォントしたい（``#text(font: フォント名)``）

```typst
#text(font: "HackGen")[HackGen; 白源]
#text(font: "HackGen Console")[HackGen Console; 白源コンソール]
#text(font: "HackGen35")[HackGen35; 白源35]

#text(font: "Noto Serif CJK JP")[Noto Serif CJK JP]
#text(font: "Noto Sans CJK JP")[Noto Sans CJK JP]

#text(font: "Futura")[Futura; フツラ]
#text(font: "Yusei Magic")[Yusei Magic; たぬき油性マジック]
```

[text要素のfontオプション](https://typst.app/docs/reference/text/text/#parameters-font)でフォントを変更できます。
``#text(font: フォント名)[本文]``で、部分的にフォントを変更できます。

## 利用できるフォントを確認したい（``typst fonts``）

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

``typst fonts``コマンドで、利用できるフォントの一覧を確認できます。
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

:::{note}

僕はフォントを``Homebrew``でインストールしていますが、
フォントパスを追加設定などを必要とせずに使うことができています。

:::
