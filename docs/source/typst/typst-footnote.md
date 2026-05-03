# 脚注したい（`#footnote`）

```typst
脚注を参照してください。
#footnote[これは脚注です]
```

`#footnote`要素で脚注を作成できます。

## 脚注を装飾したい

```typst
#show footnote.entry: set text(
  size: 0.8em,
  fill: luma(50%),
)
```

`footnote.entry`要素に対して`#show`ルールを定義することで、脚注のスタイルを変更できます。
上記のサンプルでは、脚注の文字サイズを小さくし、文字色を薄くしています。

また、本文中の脚注番号は`#super`要素でマークアップされるため、`#super`に対して`show`ルールを適用すればよいそうです。

## リファレンス

- [footnote | Element | Typst](https://typst.app/docs/reference/model/footnote/)
