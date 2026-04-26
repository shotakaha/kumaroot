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

:::{note}

[TypstApp](https://typst.app/)のウェブアプリのデフォルトが、
よく分からない明朝フォントになっているため、
日本語フォントへの変更は必須です。

:::

```typst
ここはデフォルトのフォントで表示
#text(fill: luma(80%))[
  ここは薄いグレーの文字で表示
]
ここもデフォルトのフォントで表示
```

`#text`で本文中のテキストを部分的に装飾できます。

## フォント書体したい（`font`）

```typst
// 全体設定
#set text(
  font: "Harano Aji Gothic"
)

// 個別設定
ここは原ノ味ゴシックで表示
#text(font: "Harano Aji Mincho")[ここだけ原の味明朝で表示]
ここは原ノ味ゴシックで表示
```

`font`オプションで、フォント（の書体）を変更できます。
LaTeXと比べると和文フォントがとても簡単に利用できます。

:::{seealso}

- [](../latex/latex-luatexja.md)
- [](../latex/latex-luatexja-preset.md)
- [](../latex/latex-luatexja-fontspec.md)

:::

```console
// 利用できるフォントを確認
$ typst fonts

// フォント名で検索
$ typst fonts | rg "Harano"
Harano Aji Gothic
Harano Aji Mincho

// サンセリフ体・ゴシック体
$ typst fonts | rg "Sans"
$ typst fonts | rg "Gothic"

// セリフ体・明朝体
$ typst fonts | rg "Serif"
$ typst fonts | rg "Mincho"

// 等幅フォント
$ typst fonts | rg "Mono"
$ typst fonts | rg "Console"

// CJKフォント
$ typst fonts | rg "CJK"
```

`typst fonts`コマンドで、利用可能なフォントの一覧を確認できます。
フォント名がずらーっと表示されるだけなので、`rg`（`ripgrep`）などの検索コマンドと組み合わせて探してください。

## フォントウェイトしたい（`weight`）

```typst
#text(weight: "regular")    // デフォルト

// 全体設定
#set text(weight: "thin")       // 100
#set text(weight: "extralight") // 200
#set text(weight: "light")      // 300
#set text(weight: "regular")    // 400
#set text(weight: "medium")     // 500
#set text(weight: "semibold")   // 600
#set text(weight: "bold")       // 700
#set text(weight: "extrabold")  // 800
#set text(weight: "black")      // 900

// 個別設定
#text(weight: "bold")[ここだけ太字で表示]
```

`weight`オプションで、フォントのウェイト（＝太さ）を変更できます。
デフォルトは`"regular"`です。
選択できるウェイトは、利用するフォントによって異なります。

:::{hint}

フォント書体を選ぶときに、ウェイトが豊富かどうかも判断材料に加えることをオススメします。
見出しと本文でウェイトを変えるだけで、統一感があるドキュメントが作成できます。

:::

## フォントサイズしたい（`size`）

```typst
#text(size: 11pt)    // デフォルト

// 全体設定
#set text(size: 12pt)

// 個別設定
#text(size: 18pt)[ここだけ大きい文字で表示]
```

`size`オプションで、フォントサイズを変更できます。
デフォルトは`11pt`です。
タイトルや見出しなど、部分的にサイズを変更したいときに使用します。

## 文字色したい（`fill`）

```typst
#text(fill: luma(0%))    // デフォルト（黒）

// 全体設定
#set text(
  fill: luma(80%)
)

// 個別設定
#text(fill: rgb(blue))[ここだけ青い文字で表示]
```

`fill`オプションで、フォントの色を変更できます。
デフォルトは`luma(0%)`（黒）です。

:::{seealso}

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

:::

## 言語設定したい（`lang`）

```typst
#text(lang: "en")    // デフォルト

// 全体設定
#set text(
  lang: "ja"
)

// 個別設定
#text(lang: "en")[ここだけ英語で表示]
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

## 和文フォントあれこれ

僕が利用することのある和文フォントの一部を紹介します。
どれを選べばよいか分からないときの参考にしてください。

:::{note}

フォントは`Homebrew`経由もしくは、
直接ダウンロードして`Font Book.app`でインストールしています。
Typstでは、フォントパスを追加設定することなく、利用できています。

:::

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

ヒラギノフォントは、macOSに標準搭載されている日本語フォント書体です。
macOSユーザーは、とりあえずヒラギノフォントを利用しておけば間違いないと思います。

この中でも`Hiragino Sans`がオススメです。
この書体は、2015年ころに追加されたサンセリフ体（＝ゴシック体）で、ウェイトも豊富です。
簡単に統一感のあるドキュメントを作りたいときに便利です。

古くからのmacOSユーザーには
角ゴシック体（`Hiragino Kaku Gothic`）、
丸ゴシック体（`Hiragino Maru Gothic`）、
明朝体（`Hiragino Mincho`）
のほうが馴染みがあるかもしれません。
利用できる文字種により`Std`、`StdN`、`Pro`、`ProN`の区分があります。
とりあえず`ProN`を使えばよいと思います。

### Notoフォント／Source Hanフォント

```console
$ typst fonts | rg "CJK JP"
Noto Sans CJK JP
Noto Serif CJK JP
```

NotoフォントはGoogleが開発したオープンソースの書体です。
文字化けすると現れる「□」（＝豆腐）をなくそうというコンセプトで、「No Tofu」ことを目的に開発されました。

そのCJKセットである`Noto Sans CJK JP`と`Noto Serif CJK JP`は、日本語を含む東アジアの言語に対応したフォントです。
ウェブ媒体でも広く利用されています。
日英混植のドキュメントで活躍します。

Typstのウェブアプリでもデフォルトで利用できるフォントのひとつです。

:::{note}

GoogleとAdobeが共同開発したフォントで、
Google側のフォント名が`Noto`で、
Adobe側のフォント名が`Source Han`（源ノ角）です。
基本的に同じフォントです。

:::

### 原ノ味フォント

```console
$ typst fonts | rg "Harano Aji"
Harano Aji Gothic
Harano Aji Mincho
```

[原ノ味フォント](https://github.com/trueroad/HaranoAjiFonts)は、源ノフォント（源ノ明朝・源ノ角ゴシック）をAdobe-Japan1フォントになるように組み替えたフォントです。
LuaLaTeX-jaのプリセットで利用されているフォントなので、LuaLaTeXユーザーには馴染みがあるかもしれません。

Adobe-Japan1フォントは、JIS X 0213で定義されている文字をすべて収録しているフォントで、漢字の字形がJIS X 0213に準拠しています。
日本語のドキュメントを作成する場合は、原ノ味フォントもオススメです。

### 游ゴシック／游明朝フォント

```console
$ typst fonts | rg "Yu[Gothic,Mincho]"
YuGothic
YuMincho
YuMincho +36p Kana
```

游ゴシック／游明朝フォントは、字游工房が開発した日本語フォントです。
WindowsやmacOSに標準搭載されています。

### BIZ UDフォント

```console
$ typst fonts | rg "BIZ UD"
BIZ UDGothic
BIZ UDMincho
BIZ UDPGothic
BIZ UDPMincho
```

BIZ UDフォントは、モリサワが開発した日本語フォントです。
ビジネス用途に最適化されたユニバーサルデザイン（UD）フォントで、読みやすさと視認性に優れています。

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

[HackGen（白源）フォント](https://github.com/yuru7/HackGen)は、プログラミン向けに設計された日本語対応の等幅フォントです。
日本語のコメントが入ったコードブロックのフォント設定に向いています。

`HackGen`は半角1:全角2の純粋な等幅フォント、
`HackGen35`は可読性を優先させるために半角3:全角5としたフォントです。
`NF`は`Nerd Font`のことで、絵文字やFontAwesomeなどに対応しています。
日常のターミナル操作などにも向いています。

:::{note}

[tawara (yuru7)さん](https://github.com/yuru7/) が個人開発しているフォントです。
他にも`PlemolJP`、`moralerspace`、`UDEV Gothic`などのさまざまなフォントを開発されています。
すべて日本語に対応しているのでありがたく使わせていただいております。

:::

:::{seealso}

[UDEV Gothicフォント](https://github.com/yuru7/udev-gothic)

- BIZ UDフォントとJetBrains Monoをベースにした日本語対応のプログラミングフォント

[PlemolJPフォント](https://github.com/yuru7/PlemolJP)

- IBM Plex MonoとIBM Plex Sans JPを合成した日本語対応のプログラミングフォント
- 名前が秀逸🍻

[Moralerspaceフォント](https://github.com/yuru7/moralerspace)

- GitHubが開発したMonaspaceフォントとIBM Plex Sans JPなどを合成した日本語対応のプログラミングフォント
- `Monaspace Krypton`を日本語でも使えるようになってとても嬉しい
- ターミナル表示にも設定して常用している

:::

### FontWorksフォント

```console
$ typst fonts | rg One
Aoboshi One
Cherry Bomb One
Darumadrop One
Dela Gothic One
Klee One
Mochiy Pop One
Monomaniac One
Potta One
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
