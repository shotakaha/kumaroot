# 脚注したい（`#footnote`）

```typst
脚注を参照してください。
#footnote[これは脚注です]
```

`#footnote`要素で脚注を作成できます。

## 文字色したい

```typst
#show footnote.entry: set text(red)
```

脚注のスタイルを変更する場合は
`#footnote.entry`に`show`ルールを適用します。

また、本文中の脚注番号は`#super`要素でマークアップされるため、`#super`に対して`show`ルールを適用すればよいそうです。

## リファレンス

- [footnote | Element | Typst](https://typst.app/docs/reference/model/footnote/)
