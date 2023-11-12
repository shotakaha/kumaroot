# 画像したい（``/layouts/shortcodes/figure.html``）

```go
{{< figure src="サムネイル画像の相対パス" link="オリジナル画像の相対パス" loading="lazy" >}}
```

本文中に画像を挿入する場合は、ビルトインされている[figure](https://gohugo.io/content-management/shortcodes/#figure)ショートコードを使います。
上記サンプルのは、次のHTMLに変換されます。

```html
<figure>
    <a href="オリジナル画像の相対パス">
        <img src="サムネイル画像の相対パス" loading="lazy">
    </a>
</figure>
```

``figure``ショートコードは引数を取ることができます。
詳細は[figure.html](https://github.com/gohugoio/hugo/blob/master/tpl/tplimpl/embedded/templates/shortcodes/figure.html)のソースを読むのが一番です。

## サイズしたい

```go
{{< figure
    src="画像の相対パス"
    width="80%"
    loading="lazy"
>}}
```

```html
<figure>
    <img src="画像の相対パス" width="80%" loading="lazy">
</figure>
```

``width``、``height``、``loading``を使って``img``要素の属性を指定できます。
画像のサイズは幅か高さのどちらか片方を指定するのがよいです。
大きな画像を使う場合は、遅延ローディングを有効にするとよいと思います。

## キャプションしたい

```go
{{< figure
  src="サムネイル画像の相対パス"
  link="オリジナル画像の相対パス"
  loading="lazy"
  title="画像のタイトル"
  caption="画像のキャプション（Markdown記法OK）"
  attr="関連リンク（Markdown記法OK）"
  attrlink="関連URL"
>}}
```

``title``、``caption``、``attr``、``attrlink``の引数を追加して、画像キャプション（``figcaption``）を表示できます。
上記のサンプルは次のHTMLに変換されます。

```html
<figure>
    <a href="オリジナル画像の相対パス">
        <img src="サムネイル画像の相対パス" loading="lazy">
    </a>
    <figcaption>
        <h4>画像のタイトル</h4>
        画像のキャプション
        <a href="関連URL">関連リンクの説明</a>
    </figcaption>
</figure>
```

## 別ウィンドウしたい

```go
{{<figure
    src="画像の相対パス"
    link="外部URL"
    target="_blank"
    rel="noopener"
>}}
```

``target``、``rel``を使って``link``を開く動作を指定できます。
外部URLを開く場合は``target="_blank" rel="noopener"``をセットで指定し、別ウィンドウ（タブ）で開くようにするとよいです。
``link``がない場合はHTMLに変換されません。

```html
<figure>
    <a href="外部URL" target="_blank" rel="noopener">
        <img src="画像の相対パス">
    </a>
</figure>
```
