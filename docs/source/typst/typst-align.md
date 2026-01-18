# 配置したい（`#align`）

```typst
// 左右の位置指定
#align(left)[左寄せのコンテンツ]
#align(center)[中央寄せのコンテンツ]
#align(right)[左寄せのコンテンツ]

// 言語による位置指定（RTLで判別）
#align(start)[左寄せのコンテンツ]
#align(end)[右寄せのコンテンツ]
```

`#align`要素でコンテンツの配置を変更できます。
コンテンツブロックごとに
`left | center | right`を指定できます。

言語によっては右から読む場合もあります。
`start | end`はそれに対応できる設定値です。

また、ページの上下方向を指指定す場合は
`top | horizon | bottom`を使用します。

:::{note}

`middle`ではなく`horizon`になっていて、覚えにくいです。

:::

## リファレンス

- [align | Element | Typst](https://typst.app/docs/reference/layout/align/)
- [alignment | Typst](https://typst.app/docs/reference/layout/alignment/)
