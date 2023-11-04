# レスポンシブしたい

さまざまな端末や機器のサイズに対応するデザイン手法を「[レスポンシブ・ウェブ・デザイン](https://developer.mozilla.org/ja/docs/Learn/CSS/CSS_layout/Responsive_Design)」と呼びます。
タブレット、携帯電話、テレビなどのどれで表示しても、自動的に画面に合わせることができるものです。

## ビューポートしたい

```html
<meta name="viewport" content="width=device-width initial-scale=1">
```

## メディアクエリしたい

```css
@media print {
    .container {
        font-size: 10pt;
    }

}

@media screen {
    .container {
        font-size: 12pt;
    }
}
```

[@media](https://developer.mozilla.org/ja/docs/Web/CSS/@media)を使って、メディア種別を指定できます。
メディア種別は``all``、``print``、``screen``、``speech``から選択できます。
ブラウザで表示する設定の場合は``screen``を指定します。

メディアクエリは複数設定できるため、印刷時とブラウザ表示時で文字サイズを変えることもできます。

## ブレークポイントしたい

```css
@media (max-width: 575.98px) { /* スマホ縦持ち */ };
@media (max-width: 767.98px) { /* スマホ横持ち */ };
@media (max-width: 991.98px) { /* タブレット */ };
@media (max-width: 1199.98px) { /* デスクトップ */ };
@media (max-width: 1399.98px) { /* でかいデスクトップ */ };
```

メディア特性（の画面幅）を使って、ブレークポイントを設定します。
``min-width``もしくは``max-width``を使ってデバイス幅によって場合分します。
上記サンプルはBootstrap5の設定を参考にしたものです。
指定する幅の大きさは、デバイスの普及状況によって変化します。

:::{note}

以下のようにメディア種別（``@media screen``）と一緒に書く場合もありますが、いまはメディア特性だけでOKのようです。

```css
@media screen and (max-width: 575.98px ) { /* スマホ縦持ち */};
```

:::
