# フレックスボックスしたい（`display: flex`）

```css
.cards {
    display: flex;
    gap: 1rem;
}
```

```html
<div class="cards">
    <div class="card">1枚目</div>
    <div class="card">2枚目</div>
    <div class="card">3枚目</div>
</div>
```

Flexbox（フレックスボックス）は、子要素を1方向（横または縦）に並べるためのレイアウトのしくみです。
親要素に`display: flex`を指定すると、その直下の子要素が自動的に横並びになります。

`display: flex`を指定した親要素を「フレックスコンテナー」、
並べられる子要素を「フレックスアイテム」と呼びます。
アイテム同士の間隔は`gap`で指定します。

## 中央に置きたい（`justify-content` / `align-items`）

```css
.box {
    display: flex;
    justify-content: center;  /* 横方向の位置 */
    align-items: center;      /* 縦方向の位置 */
    height: 200px;
}
```

`justify-content`は並んでいる方向（主軸）の位置、
`align-items`はそれと直角の方向（交差軸）の位置をそろえます。

`display: flex`の初期状態では主軸が横なので、
`justify-content: center`で左右中央、`align-items: center`で上下中央になります。
両方に`center`を指定すると、要素をコンテナーのど真ん中に置けます。

## 均等に並べたい（`justify-content`）

```css
.nav {
    display: flex;
    justify-content: space-between;
}
```

`justify-content`には、アイテムのあいだに余白を配る値もあります。

- `space-between` … 両端をコンテナーの端にそろえ、あいだを均等にあける
- `space-around` … 各アイテムの左右に同じ余白をつける
- `space-evenly` … アイテムのあいだと両端の余白をすべて同じにする

ヘッダーで「左にロゴ、右にナビゲーション」を作るときは`space-between`をよく使います。

## 折り返したい（`flex-wrap`）

```css
.cards {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
}

.card {
    width: 200px;
}
```

初期状態では、フレックスアイテムは折り返さず、幅が足りないと縮んで1行に収まろうとします。

`flex-wrap: wrap`を指定すると、入りきらないアイテムが次の行に折り返されます。
カード一覧のように「画面が広ければ横に並べ、狭ければ折り返したい」ときに使います。

## 幅の伸び縮みを決めたい（`flex`）

```css
.sidebar {
    flex: 0 0 240px;  /* 伸びない・縮まない・基準幅240px */
}

.main {
    flex: 1;  /* 余ったスペースを埋めるように伸びる */
}
```

`flex`プロパティは、フレックスアイテム側に指定します。
「伸びやすさ・縮みやすさ・基準の幅」を1行でまとめて指定できます。

- `flex: 1` … 余白を分け合って伸びる。複数のアイテムに指定すると等幅になる
- `flex: 0 0 240px` … 伸び縮みせず、常に240pxを保つ

サイドバーを固定幅、本文を残り全部、というレイアウトは`flex: 0 0 <幅>`と`flex: 1`の組み合わせで作れます。

## 縦に並べたい（`flex-direction: column`）

```css
.stack {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}
```

`flex-direction`で、アイテムを並べる方向を変えられます。
初期値は`row`（横）で、`column`にすると縦並びになります。

`flex-direction: column`にすると主軸と交差軸が入れ替わるので、
`justify-content`が縦方向の位置、`align-items`が横方向の位置になります。

## 並び順を変えたい（`order`）

```css
.item-a { order: 2; }
.item-b { order: 1; }
```

`order`プロパティで、HTMLの記述順を変えずに、表示上の並び順だけを入れ替えられます。
数値が小さいアイテムほど先に表示されます。初期値は`0`です。

画面が狭いときだけ特定の要素を先頭に出す、といった調整に使います。
ただし読み上げ順やキーボード操作の順序はHTMLのままなので、多用は避けます。

## リファレンス

- [フレックスボックスの基本概念](https://developer.mozilla.org/ja/docs/Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox)
- [display](https://developer.mozilla.org/ja/docs/Web/CSS/display)
- [justify-content](https://developer.mozilla.org/ja/docs/Web/CSS/justify-content)
- [align-items](https://developer.mozilla.org/ja/docs/Web/CSS/align-items)
- [flex](https://developer.mozilla.org/ja/docs/Web/CSS/flex)
