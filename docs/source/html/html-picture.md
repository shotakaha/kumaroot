# 画像したい（`picture`）

```html
<picture>
    <source srcset="image.webp" type="image/webp">
    <source srcset="image.jpg" type="image/jpeg">
    <img src="image.jpg" alt="画像の説明">
</picture>
```

`<picture>`要素は、複数の画像を切り替えて表示するための要素です。
`<source>`で指定した画像のうち、ブラウザが対応している形式のものが表示されます。

上記のサンプルでは、
WebP形式に対応しているブラウザでは`image.webp`が、
対応していないブラウザでは`image.jpg`が表示されます。

## アートディレクションしたい（`media`）

```html
<picture>
    <source media="(max-width: 480px)" srcset="image-mobile.webp" type="image/webp">
    <source media="(min-width: 481px)" srcset="image-desktop.webp" type="image/webp">
    <img src="image-desktop.jpg" alt="画像の説明">
</picture>
```

`media`属性で、画面サイズに応じて表示する画像を切り替えることができます。
表示条件は[](./css-media.md)を参照してください。

## リファレンス

- [picture](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/picture)
- [source](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/source)
- [img](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/img)
