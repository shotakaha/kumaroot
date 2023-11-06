# フォントしたい（``font``）

```css
body {
    font: サイズ 書体;
}
```

[font](https://developer.mozilla.org/ja/docs/Web/CSS/font)を使って、フォント表示に関するプロパティを一括指定できます。

## 書体したい（``font-family``）

```css
body {
    font-family:
}
```

[font-familyプロパティ](https://developer.mozilla.org/ja/docs/Web/CSS/font-family)を使って、ウェブ表示に使う書体を指定できます。
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

[font-sizeプロパティ](https://developer.mozilla.org/ja/docs/Web/CSS/font-size)を使って、フォントの大きさを変更できます。
ルート要素のフォントサイズを基準にする``rem``を使うと、ウェブサイト全体で統一感が出せると思います。

上記サンプルでは、ルート要素（``body``）のサイズを``20px``に設定し、それぞれの見出しのサイズを``x倍``に変更しています。
``h4``から``h6``は、このほうが使いやすいかなと思ってフォントサイズを同じにしてあります。
