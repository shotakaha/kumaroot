# 表示スタイルしたい（`display`）

```css
display: 外部の表示型 内部の表示型;
```

`display`プロパティで要素の表示スタイル（`block` / `inline`）を変更できます。

`display`プロパティは2値構文になっていて、
1番目の引数は「外部の表示型」で``block``、``inline``から選択します。
その要素の親要素に対する表示スタイルを設定します。

2番目の引数は「内部の表示型」で``flow``、``flow-root``、``flex``、``grid``から選択します。
その要素の子要素に対する表示型を設定します。

## これまで（1値型）とこれから（2値型）

```css
display: block;       /* これまでの書き方 */
display: block flow;  /* 現在の書き方 */

display: inline-block;
display: inline flow-root;
```

`display`プロパティはこれまで1値型構文でした。
後方互換性のため、従来の記述も使うことができます。
ただし、いつまで使えるかは分からないので、これからウェブサイトを作る場合は、
2値構文で定義するとよいです。

:::{note}

[CSS Display Module Level3](https://drafts.csswg.org/css-display/)では、[displayプロパティは2値構文](https://developer.mozilla.org/ja/docs/Web/CSS/display/multi-keyword_syntax_of_display)で記述することになっています。

:::

## ブロック表示にしたい（``display: block flow``）

```css
code {
    display: block flex;
    width: 100vw;
    height: 100vw;
}
```

デフォルトでインライン要素である`code`タグをブロック要素に変更し、
子要素をフレックスにしたサンプルです。
ブロック表示要素は`width`や`height`を設定できるようになります。
また、要素の前後で改行されます。

### デフォルトでブロック表示のタグ

- `div`: 汎用的なブロック要素タグ
- `h1 ... h6`: 見出し
- `section`: セクション
- `p`: 段落
- `blockquote`: 引用
- `hr`: 区切り線
- `figure` / `figcaption`: 図
- `nav` / `main` / `footer` / `aside` / `header`

## インライン表示したい（``display: inline flow``）

```css
h1 {
    display: inline flow;
}
```

デフォルトでブロック要素である`h1`タグをインライン要素に変更し、
子要素をフローコンテンツにしたサンプルです。

### デフォルトでインライン表示のタグ

- `span`: 汎用的なインライン要素タグ
- `img`: 画像
- `a`: ハイパーリンク
- `strong`: 重要なテキスト
- `q`: 短い引用
- `sub` / `sup`: 下付き文字 / 上付き文字
- `br`: 改行
- `code` / `kbd`: コード / キーボード入力
- `em` / `b` / `i` / `u`: 強調系

## リファレンス

- [display](https://developer.mozilla.org/ja/docs/Web/CSS/display)プロパティを使って、HTMLタグの表示方法を設定できます。
