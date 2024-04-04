# 本文したい（``#text``）

```typst
#text(オプション)[コンテキスト]
```

```typst
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

[text要素](https://typst.app/docs/reference/text/text/)で、本文の設定を変更できます。
ドキュメントのはじめに``#set text``することで一括設定できます。
上記のサンプルは日本語のドキュメント作成のときにコピペで使い回している設定です。
LaTeXに比べて和文フォントがとても簡単に設定できます。

:::{seealso}

- [](../latex/latex-luatexja.md)
- [](../latex/latex-luatexja-preset.md)
- [](../latex/latex-luatexja-fontspec.md)
:::

## フォントしたい（``font``）

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

## ウェイトしたい（``weight``）

```typst
#set text(weight: "thin")       // 100
#set text(weight: "extralight") // 200
#set text(weight: "light")      // 300
#set text(weight: "regular")    // 400
#set text(weight: "medium")     // 500
#set text(weight: "semibold")   // 600
#set text(weight: "bold")       // 700
#set text(weight: "extrabold")  // 800
#set text(weight: "black")      // 900
```

``weight``オプションで、フォントのウェイト（＝太さ）を変更できます。
デフォルトは``"regular"``です。

フォントの書体を選ぶときは、ウェイトがたくさんある書体がオススメです。
見出しと本文でウェイトを変えるだけで、よみやすいドキュメントが作成できます。

## フォントサイズしたい（``size``）

```typst
#set heading: set text(size: 1.5em)
```

``size``オプションで、フォントサイズを変更できます。
デフォルトは``11pt``です。
上記のサンプルでは見出しのフォントサイズを、本文の1.5倍にしています。

## 文字色したい（``fill``）

```typst
#set text(fill: luma(80%))
```

``fill``オプションで、フォントの色を変更できます。
デフォルトは``luma(0%)``です。

Typstにはさまざまな[色の設定方法](https://typst.app/docs/reference/visualize/color/)があります。

基本的には[RGB関数](https://typst.app/docs/reference/visualize/color/#definitions-rgb)でRGB値とA値を設定すればよいです。
グレイスケールを使う場合は[luma関数](https://typst.app/docs/reference/visualize/color/#definitions-luma)があります。
印刷物を作成する場合は[cymk関数](https://typst.app/docs/reference/visualize/color/#definitions-cmyk)を使うのがよいかもしれません。

## 言語したい（``lang``）

```typst
#set text(lang: "ja")
```

``lang``オプションで、本文の言語を変更できます。
言語コードは``ISO639-1/2/3``から選択します。
デフォルトは``"en"``です。
