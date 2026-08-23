# 余白したい（`margin`）

```css
.box {
  margin: 1em 2em 1em 2em;  /* 上 右 下 左 */
}
```

`margin`プロパティで要素の**外側**の余白を設定できます。
単位は`em`や`rem`、`px`や`%`が使えます。

値の指定方法は、値の個数によって意味が変わります。

- 1個: `margin: すべて;`
- 2個: `margin: 上下 左右;`
- 3個: `margin: 上 左右 下;`
- 4個: `margin: 上 右 下 左;`

`margin`は一括指定プロパティ（shorthand property）なので、上下左右のマージンを一括で指定できるのですが、
引数の順番が覚えにくいです。
以下のように個別に設定したほうが、分かりやすくてよいかもしれません。

## 中央寄せしたい（`margin: auto`）

```css
.box {
  width: 40rem;
  margin: 0 auto;
}
```

`margin: auto`は、要素の余白を自動で計算してくれる値です。
`margin: 0 auto`を指定すると、上下の余白は0、左右の余白は自動で計算され、コンテンツが中央に配置されます。

この設定は、`width`など、幅が決まっている要素に対してのみ有効です。
また、上下の`margin`に`auto`を指定しても中央寄せにはなりません。

## 一括マージンしたい（`margin`）

```css
.box {
    margin: 1em;  /* 上 下 左 右 */
}
```

## 上下マージンしたい（`margin-top` / `margin-bottom`）

```css
.box {
  margin-top: 1em;
  margin-bottom: 1em;
}
```

`margin-top`と`margin-bottom`で、上下の余白を個別に指定できます。

```css
.box {
  margin: 1em 0;  /* 上下 左右 */
}
```

## 左右マージンしたい（`margin-left` / `margin-right`）

```css
.box {
  margin-left: 1em;
  margin-right: 1em;
}
```

`margin-left`と`margin-right`で、左右の余白を個別に指定できます。

```css
.box {
    margin: 0 1em;
}
```

## 個別マージンしたい

```css
.box {
  margin-top: 1em;
  margin-bottom: 2em;
  margin-left: 3em;
  margin-right: 4em;
}
```

すべてのマージンを個別に指定することもできます。

```css
.box {
    margin: 1em 4em 2em 3em;
}
```


ブロック要素同士の隙間が詰め詰めになっていると窮屈に感じることがあります。
適切なマージンをつけると見やすくなると思います。

インライン要素（`display: inline flow`）には、上下の`margin`が効きません。
左右の`margin`は効くので、上下の余白も指定したい場合は
[表示スタイルしたい（`display`）](./css-display.md)で紹介した`inline flow-root`に変更する必要があります。

:::{hint}

CSSを編集できない場合は、改行（`<br>`タグ）で対応するケースもありますが、
本来であれば適切なマージン設定をすべきだと思います。

:::

## リファレンス

- [margin](https://developer.mozilla.org/ja/docs/Web/CSS/margin)
