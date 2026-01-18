# フォントしたい（`#text`）

```typst
#set text(
  lang: "ja",
  font: "Harano Aji Gothic",
  size: 12pt,
  weight: "regular",
)
```

[text要素](https://typst.app/docs/reference/text/text/)で、本文のフォント設定などを変更できます。
ドキュメント全体の設定は`set`ルールで一括設定します。

上記のサンプルは日本語のドキュメント作成のときにコピペで使い回している設定です。
LaTeXと比べると和文フォントがとても簡単に設定できます。

:::{note}

[TypstApp](https://typst.app/)の場合、
デフォルトが、よく分からない明朝フォントになっているため、日本語フォントへの変更は必須です。

:::

:::{seealso}

- [](../latex/latex-luatexja.md)
- [](../latex/latex-luatexja-preset.md)
- [](../latex/latex-luatexja-fontspec.md)

:::

## フォントサイズしたい（`size`）

```typst
#set text(
  size: 11pt
)
```

`size`オプションで、フォントサイズを変更できます。
デフォルトは`11pt`です。

```typst
#show heading.where(level: 1): set text(size: 18pt, weight: "bold")
#show heading.where(level: 2): set text(size: 16pt, weight: "semibold")
#show heading.where(level: 3): set text(size: 14pt, weight: "medium")
#show heading.where(level: 4): set text(size: 12pt, weight: "medium", style: "italic")
```

上記のサンプルのように、見出しレベルごとにフォントサイズを変更できます。

## 文字色したい（`fill`）

```typst
#set text(
  fill: luma(80%)
)
```

`fill`オプションで、フォントの色を変更できます。
デフォルトは`luma(0%)`です。

Typstにはさまざまな
[色の設定方法](https://typst.app/docs/reference/visualize/color/)
があります。

基本的には
[RGB関数](https://typst.app/docs/reference/visualize/color/#definitions-rgb)
でRGB値とA値を設定すればよいです。
グレイスケールを使う場合は
[luma関数](https://typst.app/docs/reference/visualize/color/#definitions-luma)
があります。
印刷物を作成する場合は
[cymk関数](https://typst.app/docs/reference/visualize/color/#definitions-cmyk)
を使うのがよいかもしれません。

## 言語設定したい（`lang`）

```typst
#set text(
  lang: "ja"
)
```

`lang`オプションで、ドキュメントの言語を変更できます。
言語コードは`ISO639-1/2/3`から選択します。
デフォルトは`"en"`です。
日本語の場合は`"ja"`にします。

:::{note}

ウェブアプリ限定かもしれませんが、
`lang: "ja"`に設定することで、
スペルチェックによるエラーを抑制できました。

:::

## フォントしたい（`font`）

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

## 利用できるフォントを確認したい（``typst fonts``）

```console
$ typst fonts
$ typst fonts --variants
```

`typst fonts`コマンドで、利用可能なフォントの一覧を確認できます。
`--variants`オプションでより詳細な情報を確認できます。

フォント名を指定して表示する機能はないようなので、`ripgrep`など検索コマンドと組み合わせて探します。

:::{hint}

僕はフォントを`Homebrew`経由でインストールしています。
Typstでは、フォントパスを追加設定することなく、使うことができています。

:::

以下に、困ったときにオススメの日本語フォントを紹介します。

### ヒラギノフォント

```console
$ typst fonts | rg Hiragino
Hiragino Kaku Gothic Interface
Hiragino Kaku Gothic Pro
Hiragino Kaku Gothic ProN
Hiragino Kaku Gothic Std
Hiragino Kaku Gothic StdN
Hiragino Maru Gothic Pro
Hiragino Maru Gothic ProN
Hiragino Mincho Pro
Hiragino Mincho ProN
Hiragino Sans
Hiragino Sans CNS
Hiragino Sans GB
Hiragino Sans GB Interface
```

ヒラギノフォントは、macOSに標準搭載されている日本語フォントファミリーです。
角ゴシック体、丸ゴシック体、明朝体には、
利用できる文字種により`Std`、`StdN`、`Pro`、`ProN`の区分があります。
とりあえずProNを使えばよいと思います。

また、2015年ころに、多言語対応のサンセリフ体が追加されました。
ウェイトも豊富なので、簡単に統一感のあるドキュメントを作りたいときに便利です。

### Notoフォント

```console
$ typst fonts | rg "Noto" |
 rg "CJK"
Noto Sans CJK JP
Noto Serif CJK JP
```

NotoフォントはGoogleとAdobeが共同開発したフォントです。
`Noto Sans CJK JP`はサンセリフ体（＝ゴシック体）、
`Noto Serif CJK JP`はセリフ体（＝明朝体）です。
日英混植のドキュメントで活躍します。

:::{note}

Google側のフォント名が`Noto`で、
Adobe側のフォント名が`Source Han`（源ノ角）です。
基本的に同じフォントです。

:::

### 游ゴシック／游明朝フォント

```console
$ typst fonts |
 rg "Yu[Gothic,Mincho]"
YuGothic
YuMincho
YuMincho +36p Kana
```

游ゴシック／游明朝フォントは、字游工房が開発した日本語フォントです。
WindowsやmacOSに標準搭載されています。

### HackGenフォント

```console
$ typst fonts | rg HackGen
HackGen
HackGen Console
HackGen Console NF
HackGen35
HackGen35 Console
HackGen35 Console NF
```

HackGen（白源）は、プログラミン向けに設計された日本語対応の等幅フォントです。
日本語のコメントが入ったコードブロックのフォント設定に向いています。

`HackGen`は半角1:全角2の純粋な等幅フォント、
`HackGen35`は可読性を優先させるために半角3:全角5としたフォントです。
`NF`は`Nerd Font`のことで、絵文字やFontAwesomeなどに対応しています。
日常のターミナル操作などにも向いています。

:::{note}

[tawara (yuru7)さん](https://github.com/yuru7/) が個人開発しているフォントです。
他にも`PlemolJP`、`moralerspace`などのさまざまなフォントを開発している方です。
すべて日本語に対応しているのでありがたく使わせていただいております。

:::

### ポップなフォント

```console
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

`* One`フォントはFontWorksが開発したフォントです。
Google Fontsとして提供されているので無料で利用できます。
ポップなフォントなので、カジュアルさを出したいときに利用できます。

## リファレンス

- [text | element | Typst](https://typst.app/docs/reference/text/text)
