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

## タイトルを太字にしたい

```typst
#show title: set text(size: 1.5em, weight: "black")

#title[太字にしたタイトル]
```

`#show title`ルールで、タイトルを装飾できます。

## タイトルを中央寄せにしたい

```typst
#show title: set text(size: 1.5em, weight: "black")
#show title: set align(center)
```

`set align`でタイトルの表示位置を変更できます。
`#show`ルールは順番に重ね書きできるため、太字にする設定と、中央寄せする設定を、分けて定義しればOKです。

## タイトルに枠線をつけたい

```typst
#show title: set text(size: 1.5em, weight: "black")
#show title: block(
  width: 100%,
  stroke: luma(50%) + 2pt,
  fill: luma(90%),
  inset: 1em,
)
```

`set block`を使って、タイトルに枠線や背景を追加できます。
デフォルトだと文字数の幅なので`width: 100%`で行幅いっぱいに広げるのがオススメです。

## 外部パッケージしたい

Typstには、いい感じのタイトルページを作成する機能がまだありません。
Typst Universeにある
`pubmatter`や
`beautitled`などの外部パッケージを利用するとよいかもしれません。

:::{seealso}

- [pubmatter - Typst Universe](https://typst.app/universe/package/pubmatter)
- [beautitled - Typst Universe](https://typst.app/universe/package/beautitled)

:::

## リファレンス

- [title - Typst](https://typst.app/docs/reference/model/title/)
