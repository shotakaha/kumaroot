# 表示スタイルしたい（`display`）

```css
display: 外部の表示型 内部の表示型;
```

`display`プロパティで要素の表示スタイルを変更できます。
1番目の引数で「外部の表示型」でその要素自体の並び方（`block`か`inline`か）を、
2番目の引数「内部の表示型」で子要素の並び方（`flow`、`flow-root`、`flex`、`grid`など）を指定します。

## ブロック要素にしたい（`block flow`）

```css
div {
    display: block flow;
}
```

`block flow`は、ブロック要素の表示型です。
横幅いっぱいに広がり、縦に積み重なるように表示されます。
`div`や`section`、`p`などのブロック要素は、デフォルトでこの表示型を持っています。

### デフォルトでブロック表示のタグ

- `div`: 汎用的なブロック要素タグ
- `h1 ... h6`: 見出し
- `section`: セクション
- `p`: 段落
- `blockquote`: 引用
- `hr`: 区切り線
- `figure` / `figcaption`: 図
- `nav` / `main` / `footer` / `aside` / `header`

## インライン要素にしたい（`inline flow`）

```css
span {
    display: inline flow;
}
```

`inline flow`は、インライン要素の表示型です。
横に並び、内容に応じて高さが調整されます。
`span`や`img`、`a`などのインライン要素は、デフォルトでこの表示型を持っています。

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

## フロート要素を内包したい（`block flow-root`）

```css
.container {
    display: block flow-root;
}
```

```html
<div class="container">
    <img style="float: left;" src="画像のパス">
    <p>floatした画像の隣に回り込む文章。</p>
</div>
```

子要素に`float`を使うと、親要素の高さがつぶれてしまうことがあります。
`block flow-root`を親要素に指定しておくと、floatした子要素も含めて高さを計算し直してくれます。
昔ながらの`clearfix`テクニックの代わりに使える、現在の標準的な書き方です。

## 横並びでサイズ指定したい（`inline flow-root`）

```css
.badge {
    display: inline flow-root;
    width: 4rem;
    height: 2rem;
}
```

インライン要素はデフォルトでは`width`や`height`、上下の`margin`が効きません。
`inline flow-root`を指定すると、前後の要素と横並びのまま、サイズや余白を指定できるようになります。
ボタンやバッジ、アイコン付きラベルなど、テキストの流れの中でサイズを揃えたい部品によく使います。

## 横並びカードにしたい（`block flex`）

```css
.cards {
    display: block flex;
    gap: 1rem;
}
```

`block flex`は、子要素をFlexboxで並べるためのコンテナーを作ります。
カード一覧やヘッダー内のロゴ・ナビゲーションの横並びなど、現在のレイアウトでもっともよく使う組み合わせです。

揃え方や折り返し、伸び縮みの指定は [フレックスボックスしたい（`display: flex`）](css-flexbox.md) を参照してください。

## グリッドレイアウトにしたい（`block grid`）

```css
.gallery {
    display: block grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
}
```

`block grid`は、子要素を2次元のグリッドで並べるためのコンテナーを作ります。
ページ全体のレイアウトや、画像ギャラリーのような格子状の表示に向いています。

:::{note}

`inline flex`や`inline grid`もありますが、
コンテナー自体をテキストの流れに埋め込む機会は少なく、実務ではあまり使いません。

:::

## 1値構文で書きたい（後方互換）

```css
display: block;       /* 1値構文（従来の書き方） */
display: block flow;  /* 2値構文（現在の書き方） */

display: inline-block;
display: inline flow-root;
```

`display`プロパティはこれまで1値型構文でした。
後方互換性のため、従来の記述も使うことができます。
ただし、いつまで使えるかは分からないので、これからウェブサイトを作る場合は、
2値構文で定義するとよいです。

`inline-block`は1値構文における書き方で、2値構文では`inline flow-root`に相当します。
どちらも同じ表示になりますが、これから書く場合は2値構文のほうがよいです。

## リファレンス

- [display](https://developer.mozilla.org/ja/docs/Web/CSS/display)
- [displayプロパティの2値構文](https://developer.mozilla.org/ja/docs/Web/CSS/display/multi-keyword_syntax_of_display)
- [CSS Display Module Level 3](https://drafts.csswg.org/css-display/)
