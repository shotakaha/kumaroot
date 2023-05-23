# メタ情報したい（``meta``）

```html
<head>
    <meta name="キー" content="値">
</head>
```

``meta``タグや``head``タグの中に配置します。
基本的にkey-valueペアで設定します。

## 文字エンコードしたい（``charset``）

```html
<meta charset="utf-8">
```

## ビューポートしたい（``viewport``）

```html
<meta name="viewport" content="width=device-width">
```

[ビューポート](https://developer.mozilla.org/ja/docs/Web/HTML/Viewport_meta_tag)のサイズを設定できます。
画面の幅はデバイスによって異なるため、``width=device-width``を設定しておきましょう。
また、``initial-scale``で読み込んだときの表示倍率を設定できます。
よく``initial-scale=1``を書いているサンプルがありますが、デフォルトで1倍なので省略してよいと思います。


## サイトを説明したい（``description``）

```html
<meta name="description" content="サイトの説明">
```
