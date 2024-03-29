# 画像したい（``img``）

```html
<img src="画像のパス" alt="画像の説明">
```

[img](https://developer.mozilla.org/ja/docs/Web/HTML/Element/img)タグで画像を挿入できます。
``src``属性は必須で、挿入したい画像のパスを指定します。
ローカルにある画像を使う場合は相対パスで指定するとよいです。
外部URLを指定することもできます。

``alt``属性には代替テキストを記述します。
いわゆる画像のキャプションを書いておけばよいのですが、ページには表示されません。
この属性は任意ですが、アクセシビリティ向上のために指定したほうがよいものです。

## 遅延読み込みしたい

```html
<img src="画像のパス" loading="lazy">
```

``loading``属性を``lazy``にして遅延読み込みできます。
ファイルサイズの大きな画像を使った場合、ページ全体を読み込むまでに時間がかかってしまいます。
``loading="lazy"``を指定すると、ビューポートの範囲外のときに読み込みを後回しにできます。
