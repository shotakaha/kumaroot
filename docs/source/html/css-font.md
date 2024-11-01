# フォントしたい（``font``）

```css
body {
    font: サイズ 書体;
}
```

`font`プロパティでフォント表示を設定できます。

## 書体したい（``font-family``）

```css
body {
    font-family:
}
```

`font-family`で書体を変更できます。
複数の書体を、優先度をつけて設定できます。

## サイズしたい（``font-size``）

```css
body { font-size: 20px; }
h1 { font-size: 3rem; }    /* 3倍 */
h2 { font-size: 2.5rem; }  /* 2.5倍 */
h3 { font-size: 2rem; }    /* 2倍 */
h4 { font-size: 1.5rem; }  /* 1.5倍 */
h5 { font-size: 1.5rem; }  /* 1.5倍 */
h6 { font-size: 1.5rem; }  /* 1.5倍 */
```

`font-size`でフォントの大きさを変更できます。
サイズに`rem`を使うとウェブサイト全体の文字の統一感を出しやすくなると思います。

上記サンプルでは、
ルート要素（``body``）のサイズを``20px``に設定し、
それぞれの見出しのサイズを``x倍``に変更しています。

:::{note}

実際に使ってみると`h4`から`h6`は見出しとしての出番が少ないタグです。
フォントサイズは同じにして、別の装飾で見分けられるようにしています。

:::

## リファレンス

- [fontプロパティ](https://developer.mozilla.org/ja/docs/Web/CSS/font)
- [font-familyプロパティ](https://developer.mozilla.org/ja/docs/Web/CSS/font-family)
- [font-sizeプロパティ](https://developer.mozilla.org/ja/docs/Web/CSS/font-size)
