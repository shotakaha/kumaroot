# テンプレートしたい（`show...with`）

```typ
// Filename: settings.typ

// Define config function (as usual Typst function)
#let config(
    title: none,
    author: none,
    date: none,
    body
) = {

  // Set Japanese fonts
  set text(
    font: ("Hiragino Kaku Gothic Pro", "Hiragino Sans"),
    lang: "ja",
    size: 10pt,
  )

  // Set page layout
  set page(
    paper: "a4",
    numbering: none,
  )

  // Set paragraph spacing
  set par(
    justify: false,
    first-line-indent: 0pt,
    leading: 0.65em,
    spacing: 1em,
  )

}
```

```typ
// Import file and functions
#import "settings.typ": config

// Setup using "show ... with" statement
#show config.with()
```

関数の`with`メソッドと`#show`構文を使って、関数を**テンプレート**として利用できます。
ドキュメント全体に関する設定は、簡単に肥大化します。

最初から設定用のTypstファイルを作成し、本文ファイルでインポートして使うようにするとよいです。
ドキュメントの規模にかかわらず、同じフォーマットにするのがよいと思います。
