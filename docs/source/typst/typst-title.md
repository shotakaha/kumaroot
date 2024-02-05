# タイトルしたい

```typst
#let title = "すごいタイトル"
#show title: set align(center)
#show title: set text(weight: "black", size: 2em)

#title
```

タイトルを「タイトル」っぽく表示するコマンドはないので、``#show``ルールを使って設定します。

タイトルっぽい見た目にするために、

1. 中央揃え
2. ウェイトの変更
3. フォントサイズの変更

にしてみました。

## 長いタイトルしたい

```typst
#let title(content) = {
    set align(center)
    set text(weight: "black", size: 2em)
    [#content]
}

#title[改行が必要なくらい \ すごく長いタイトル]
```

改行が必要なタイトルの場合、関数にします。
``[]``の中はTypst記法が使えるため、改行（`\`）も利用できます。
