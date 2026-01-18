# スタイリングしたい

```typst
// ページ設定
#set page(
  paper: "a4",
  numbering: "1 / 1",
)

// フォント設定
#set text(
  lang: "ja",
  font: ("Noto Sans CJK JP"),
)

// 見出しの設定
#set heading(
  numbering: "1.1",
)

// 見出しの表示設定
#show heading: it => {
  block(
    fill: luma(90%),
    width: 100%,
    inset: 1em,
  )[
    #it
  ]
}
```

ドキュメントをカスタマイズする方法に
`set`ルールと
`show`ルールの2つがあります。

`set`ルールは、要素のもつパラメーターを使って文書全体のデフォルト設定を変更したいとき、
`show`ルールは文書の要素（の一部）の「表示方法」を変更したいときに使います。

:::{note}

2つのルールの使い分けの基準はまだ体得できていません。

現時点では、
変更したい要素がもつパラメーターで対応できるときは`set`ルール、
できないときは`show`ルールを考えてみる、という基準で使い分けています。

:::

:::{seealso}

- [](./typst-set.md)
- [](./typst-show.md)

:::

## リファレンス

- [Styling - Typst](https://typst.app/docs/reference/styling/)
