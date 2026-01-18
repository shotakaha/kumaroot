# テンプレートしたい（`#show: ...with`）

```typst
#import "settings.typ": config

// 全体にconfig関数を適用
#show: config.with(
    title: "すばらしいタイトル",
    author: "すばらしい著者",
    // その他の引数
)

// ここから本文
= 文書のタイトル

本文がここに入ります。
フォント、ページサイズ、段落スタイルが自動的に適用されます。
```

ドキュメント全体に共通の設定（フォント、ページレイアウト、段落スタイルなど）を簡単に適用したいときは、`#show...with`構文を使ってテンプレート化します。

上記のサンプルでは設定ファイル（`settings.typ`）から`config`関数をインポートして、`#show...with`で全体に適用しています。

:::{note}

## `with`メソッド

Typstのすべての関数は`with`メソッドを持っています。このメソッドは、指定した引数を事前に設定した新しい関数を返します。

テンプレート設計では、`config.with(title: "...", author: "...")` のように必要なパラメーターを事前設定し、その結果を `#show:` で適用することで、ドキュメント全体にスタイルを反映させます。

:::

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
