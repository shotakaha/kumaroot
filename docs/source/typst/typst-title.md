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
#show title: it => {
  set text(size: 1.5em, weight: "black")
  [#it]
}
```

```typst
#show title: text.with(size: 1.5em, weight: "black")
```

## タイトルを中央寄せしたい

```typst
#show title: it => {
  set align(center)
  [#it]
}
```

```typst
#show title: align.with(center)
```

## 太字にして中央寄せしたい

```typst
#show title: it => {
  set text(size: 1.5em, weight: "black")
  set align(center)
  [#it]
}
```

```typst
#show title: text.with(size: 1.5em, weight: "black")
#show title: align.with(center)
```

## リファレンス

- [title - Typst](https://typst.app/docs/reference/model/title/)
