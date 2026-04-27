# テンプレートしたい（`#show:` + `with`）

```typst
// 関数をインポート: template(title, author, ..., body)
#import "settings.typ": template

// 全体にtemplate関数を適用
#show: template.with(
  title: "すばらしいタイトル",
  author: "すばらしい著者",
  // その他の引数
)

// ここから本文
= 文書のタイトル

本文がここに入ります。
フォント、ページサイズ、段落スタイルが自動的に適用されます。
```

`#show`ルールと`with`メソッドを組み合わせて、ドキュメント全体に共通の設定（フォント、ページレイアウト、段落スタイルなど）を簡単に適用できます。

上記のサンプルでは設定ファイル（`settings.typ`）から`template`関数をインポートしたあと、
`template.with(...)`で初期値を設定して、
`#show: template.with(...)`でページ全体に適用しています。

:::{note}

テンプレート設計のポイントは、ドキュメント全体の設定をまとめた関数を定義することです。
そのためには、「何が設定で」「何が装飾か」を明確に分けることが重要です。
また、ドキュメントの本文を受け取ることができるように、関数の最後の引数を`content`型にする必要があります。
慣習で`body`という変数名を使うことが多いようですが、`content`型であれば何でもいいと思います。

:::

:::{seealso}

```typst
// ある関数を定義
#let f(title, body) = {...}

// bodyを引数に設定
f(title: "タイトル", [本文])

// bodyは関数の外に配置できる
f(title: "タイトル")[
  本文
]

// withでtitleを固定した新しい関数を作成
#show: f.with(title: "タイトル")

本文（ここに書いた文章が、マークアップも含めてすべてf関数のbody引数に渡される）


// （おそらく）以下と同じ意味
#let g = f.with(title: "タイトル")

g[本文（ここに書いた文章が以下略）]
```

:::

## `with`メソッド

```typst
// 基本的な関数定義: xとyを足す関数
#let f(x, y) = x + y

// xを10に固定した新しい関数を作成
#let add10 = f.with(x: 10)
add10(5)  // 15
add10(20) // 30
```

Typstのすべての関数は`with`メソッドを持っています。
`with`メソッドは、関数の引数を事前に設定した新しい関数を返します。

```typst
#let add20 = add10.with(x: 20)
add20(5)  // 25
add20(20) // 40
```

`with`で設定した引数は、さらに上書きできるため、
メソッドチェーンのように利用できます。

## 設定ファイルしたい

```typ
// Filename: settings.typ

#let config(
    title: none,
    author: none,
    date: none,
    body
) = {
  // フォント設定
  set text(
    font: ("Hiragino Kaku Gothic Pro", "Hiragino Sans"),
    lang: "ja",
    size: 10pt,
  )

  // ページレイアウト
  set page(
    paper: "a4",
    numbering: none,
  )

  // 段落スタイル
  set par(
    justify: false,
    first-line-indent: 0pt,
    leading: 0.65em,
    spacing: 1em,
  )

  // 本文を表示
  body
}
```

まず、ドキュメント全体の設定をまとめたファイル（`settings.typ`）を作成し、設定用の関数（`config`）を定義します。

設定ファイルとして分離することで、
ドキュメント設定の管理・保守が簡単になります。

また、複数のドキュメントで同じテンプレートを再利用できるため、ドキュメントの規模が増えても、一貫したフォーマットが保てます。
