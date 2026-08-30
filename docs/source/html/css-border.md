# 枠線したい（`border`）

```css
.box {
    border: 1px solid #cccccc;
    border-radius: 8px;
}
```

`border`プロパティで、要素のまわりに枠線を引けます。
枠線は「太さ・線の種類・色」の3つをまとめて指定します。

枠線は、ボックスモデルの4層（内容・パディング・枠線・マージン）のうち、パディングとマージンのあいだの層です。
`border-radius`で角を丸めたり、`outline`でレイアウトに影響しない線を引いたりもできます。

:::{seealso}

- [](./css-box.md)

:::

## 枠線を引きたい（`border`）

```css
.box {
    border: 1px solid #cccccc;
}
```

`border`プロパティで、要素の枠線を「太さ・線の種類・色」の順にまとめて指定できます。

線の種類には次のようなものがあります。

- `solid` … 実線
- `dashed` … 破線
- `dotted` … 点線
- `double` … 二重線
- `none` … 枠線なし（初期値）

太さは`1px`のような数値のほか、`thin` / `medium` / `thick`のキーワードも使えます。

## 一辺だけ枠線を引きたい（`border-top` など）

```css
.quote {
    border-left: 4px solid #0066cc;
    padding-left: 1rem;
}

.table-row {
    border-bottom: 1px solid #dddddd;
}
```

`border-top`、`border-right`、`border-bottom`、`border-left`で、特定の一辺だけに枠線を引けます。

引用ブロックの左に太い線を入れる、表の行の下に区切り線を入れる、といった装飾によく使います。

## 太さ・種類・色を個別に指定したい

```css
.box {
    border-width: 2px;
    border-style: dashed;
    border-color: #0066cc;
}
```

`border-width`、`border-style`、`border-color`で、枠線の3要素を別々に指定できます。

`border-style`は初期値が`none`なので、`border-width`や`border-color`だけ指定しても枠線は表示されません。
枠線を出すには`border-style`が必須です。

## 角を丸くしたい（`border-radius`）

```css
.card {
    border-radius: 8px;
}

.avatar {
    border-radius: 50%;
}
```

`border-radius`プロパティで、要素の角を丸くできます。

値が大きいほど丸みが強くなります。
`50%`を指定すると、正方形は円、長方形は楕円になります。

枠線がなくても、背景色や画像がある要素なら角丸が見た目に効きます。

```css
.tab {
    border-radius: 8px 8px 0 0;  /* 左上 右上 右下 左下 */
}
```

値を4つ並べると、角ごとに丸みを変えられます。
順番は左上から時計回りです。

## 枠線の外に線を引きたい（`outline`）

```css
button:focus {
    outline: 2px solid #0066cc;
    outline-offset: 2px;
}
```

`outline`プロパティは`border`によく似ていますが、ボックスモデルの層に含まれず、レイアウトの幅や高さに影響しません。

キーボード操作でフォーカスした要素を目立たせる用途が中心です。
`outline`を消すとキーボードで操作している人が現在位置を見失うため、消すなら代わりの見た目を必ず用意します。

## リファレンス

- [border](https://developer.mozilla.org/ja/docs/Web/CSS/border)
- [border-style](https://developer.mozilla.org/ja/docs/Web/CSS/border-style)
- [border-radius](https://developer.mozilla.org/ja/docs/Web/CSS/border-radius)
- [outline](https://developer.mozilla.org/ja/docs/Web/CSS/outline)
