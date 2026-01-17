# タイトルしたい（`#title`）

```typst
#set document(
  title: [すごいタイトル]
)

#title()
```

`#title()`関数でドキュメントのメインタイトルを表示できます。
Typst v0.14.0で追加されました。

```typst
#title[カスタムタイトル]
```

デフォルトは`document.title`で指定したコンテンツになっています。
コンテンツ引数を使って、任意のタイトルに変更できます。

:::{note}

`#title`は、ドキュメント全体のタイトルを表示する関数です。
ドキュメントの任意の箇所で複数回呼び出すことができますが、
ドキュメントの冒頭で1度だけ呼び出すのがセマンティック的に正しいと思います。

:::

## タイトルを大きくしたい

```typst
#show title: it => {
  set text(size: 20pt)
  it.body
}
```

## 中央寄せしたい

```typst
#show title: it => {
  align(center)[
    #it.body
  ]
}
```

## リファレンス

- [title - Typst](https://typst.app/docs/reference/model/title/)
