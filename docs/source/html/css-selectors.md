# セレクターしたい

```css
セレクター名 {
    プロパティ名: 値;
}
```

CSSでは、要素やクラス名などの``セレクター``に対して``プロパティ名: 値;``を追加して設定します。
そのため、基本的なセレクターの使い方について整理してみます。
詳細はMdNの[CSSセレクター](https://developer.mozilla.org/ja/docs/Web/CSS/CSS_Selectors)を参照してください。

## グループ化したい（``,``）

```css
h1,
h2,
h3 {
    padding: 1rem,
}
```

``,（カンマ）``を使ってセレクターをグループ化できます。
複数の要素（やクラス）に同じCSSを設定する場合に使います。

## 子孫結合子したい

```css
main p {
    padding: 1rem;
    line-height: 1.5;
}
```

``（空白）``を使って子孫要素を一括して設定できます。

## 子結合子したい（``>``）

```css
nav.breadcrumb > ul {
    padding: 2rem;
}
```

```html
<nav class="breadcrumb">
    <ul>
        <li><a href="URL">HOME</a></li>
        <li><a href="URL">カテゴリ名</a></li>
        <li>ページタイトル</li>
    </ul>
</nav>
```

``>``を使って子セレクターの設定ができます。
