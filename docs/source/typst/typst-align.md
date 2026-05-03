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

`#align`要素でコンテンツの表示位置を変更できます。
コンテンツブロックごとに
横方向の位置（`left | center | right | start | end`）と
縦方向の位置（`top | horizon | bottom`）を
組み合わせて指定します。
デフォルトは`start + top`です。

:::{note}

`start | end`は、言語の方向に応じて、左寄せまたは右寄せになります。
たとえば、英語などの左から右に読む言語では、`start`は左寄せ、`end`は右寄せになります。
一方で、アラビア語などの右から左に読む言語では、`start`は右寄せ、`end`は左寄せになります。
このように、`start | end`を使用することで、言語の方向に応じた配置が可能になります。

:::

:::{note}

縦方向の位置指定は、`top | horizon | bottom`の3種類があります。
中央寄せが`middle`ではなく`horizon`になっていて、間違えやすいので注意が必要です。

:::

## リファレンス

- [align | Element | Typst](https://typst.app/docs/reference/layout/align/)
- [alignment | Typst](https://typst.app/docs/reference/layout/alignment/)
