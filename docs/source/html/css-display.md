# 要素の表示レベルを変更したい（``display``）

```css
display: 外部の表示型 内部の表示型;
```

[display](https://developer.mozilla.org/ja/docs/Web/CSS/display)プロパティを使って、HTMLタグの表示方法を設定できます。

1番目の引数（＝外部の表示型）は``block``と``inline``から選択します。
その要素の外部（＝親要素）に対する表示型を設定します。

2番目の引数（＝内部の表示型）は``flow``、``flow-root``、``flex``、``grid``から選択します。
その要素の内部（＝子要素）に対する表示型を設定します。

:::{note}

[CSS Display Module Level3](https://drafts.csswg.org/css-display/)では、[displayプロパティは2値構文](https://developer.mozilla.org/ja/docs/Web/CSS/display/multi-keyword_syntax_of_display)で記述することになっています。
後方互換性のため、これまでの記述も使うことができます。
いつまで使えるかは分かりません。

:::

```css
display: block flow;  /* 現在の書き方 */
display: block;       /* これまでの書き方 */

display: inline flow-root;
display: inline-block;
```

## ブロックレベルにしたい（``display: block flow``）

```css
span {
    display: block flex;
    width: 100vw;
    height: 100vw;
}
```

``span``タグをブロックレベルに変更し、子要素をフレックスにしたサンプルです。
ブロックレベルは``width``や``height``を設定できるようになります。
また、要素の前後で改行されます。

## インライン要素したい（``display: inline flow``）

```css
h1 {
    display: inline flow;
}
```

``h1``タグをインラインレベルに変更し、子要素をフローコンテンツにしたサンプルです。
見出しの文字数に合わせた幅になります。
