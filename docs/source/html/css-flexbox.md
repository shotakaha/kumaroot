# フレックスボックスしたい（`display: block flex`）

```css
.cards {
    display: block flex;  /* 1値構文では display: flex; */
    gap: 1rem;
}
```

```html
<div class="cards">
    <div>1枚目</div>
    <div>2枚目</div>
    <div>3枚目</div>
</div>
```

フレックスボックス（flexbox）は、1次元（横方向または縦方向）に並べるレイアウト方式です。
親要素に`display: block flex`を指定すると、その直下の子要素が自動的に1次元に並びます。
デフォルトは横方向（左から右）に並びます。

親要素を「フレックスコンテナー」、
子要素を「フレックスアイテム」と呼びます。
フレックスコンテナーの子要素は、ブロック要素（`<div>`や`<p>`など）だけでなく、インライン要素（`<span>`や`<a>`など）も自動的にフレックスアイテムになります。
フレックスアイテムの間隔は`gap`で指定します。

:::{hint}

フレックスアイテムとなるのは、フレックスコンテナーの**直下の子要素**だけです。
孫要素はフレックスアイテムになりません。

:::

:::{note}

```css
/* 2値構文 */
display: block flex;

/* 1値構文（従来の書き方） */
display: flex;
```

CSS Display Module Level 3の仕様変更により、2値構文で書くことが推奨されているので、このドキュメントでは2値構文（`display: block flex`）で書いています。

これまでの1値構文（`display: flex`）でも同じように解釈されるので、適宜読み替えながら使ってください。

:::

:::{seealso}

フレックスボックスが登場する前は、`float`や`inline-block`を使って横並びを作っていました。

```css
.card {
    float: left;
    display: inline-block;
    margin-right: 1rem;
}
```

:::

## 縦並びにしたい（`flex-direction`）

```css
.stack {
    display: block flex;
    flex-direction: column;
    gap: 0.5rem;
}
```

`flex-direction`で、アイテムを並べる向きを変更できます。
デフォルトは`row`で横方向に並びます。
`column`で縦方向に並べることができます。

```html
<!-- index.html -->
<style>
    body {
        display: block flex;
        flex-direction: column;
        gap: 1rem;
    }
</style>

<body>
    <header>ヘッダー</header>
    <main>メインコンテンツ</main>
    <footer>フッター</footer>
</body>
```

`body`を縦方向のフレックスコンテナーにしておくと、ヘッダー・メインコンテンツ・フッターを縦に並べることができます。

## 中央揃えしたい（`justify-content` / `align-items`）

```css
.container {
    display: block flex;
    justify-content: center;  /* 主軸（横方向）の位置 */
    align-items: center;      /* 交差軸（縦方向）の位置 */
    height: 200px;
}
```

`justify-content`で主軸（横方向）の配置、
`align-items`で交差軸（縦方向）の配置を変更できます。

フレックスコンテナーのデフォルトは、主軸が横方向です。
`justify-content: center`で左右中央揃え、
`align-items: center`で上下中央揃えにすると、
要素をコンテナーのど真ん中に配置できます。

## 均等配置したい（`justify-content`）

```css
.nav {
    display: block flex;
    justify-content: space-between;
}
```

`justify-content`で、アイテム間の余白設定を変更できます。

`space-between`でコンテナー幅を基準に均等揃え、
`space-around`で各アイテムの左右に余白をつけて配置、
`space-evenly`でアイテム間と両端の余白をすべて均等揃えにして配置できます。

「左にロゴ、右にナビゲーション」を作るときは`space-between`をよく使います。

## 折り返したい（`flex-wrap`）

```css
.cards {
    display: block flex;
    flex-wrap: wrap;
    gap: 1rem;
}

.card {
    width: 200px;
}
```

```html
<div class="cards">
    <div class="card">1枚目</div>
    <div class="card">2枚目</div>
    <div class="card">3枚目</div>
</div>
```

`flex-wrap: wrap`で、フレックスアイテムの内容を折り返して表示できます。

デフォルトは`nowrap`となっていて、折り返しがありません。
表示幅が足りない場合は、1行に収まるように縮められます。
カード一覧のように「画面が広ければ横に並べ、狭ければ折り返したい」ときに使います。

## 幅を自動調整したい（`flex`）

```css
.item {
    flex: 1;
}
```

`flex`プロパティで、フレックスアイテムの幅を指定できます。
`flex: 1`を指定したアイテムを複数並べると、等幅になります。

```css
.item-a {
    flex: 2;
}
.item-b {
    flex: 1;
}
```

`flex`の値を変えると、アイテムごとの幅の比率を変えられます。
上記は2:1の比率で幅を分ける例です。

```css
.sidebar {
    flex: 0 0 240px;
}

.main {
    flex: 1;
}
```

`flex`の3値構文は、「伸びやすさ・縮みやすさ・基準の幅」をまとめて指定できます。
上記のサンプルでは、
サイドバー（`.sidebar`）を固定幅（240px）にして、
本文（`.main`）を残りの幅というレイアウトにしています。

## 並び順を変えたい（`order`）

```css
.item-a { order: 2; }
.item-b { order: 1; }
```

`order`プロパティで、HTMLの記述順を変えずに、表示上の並び順だけを入れ替えられます。
数値が小さいアイテムほど先に表示されます。初期値は`0`です。

画面が狭いときだけ特定の要素を先頭に出す、といった調整に使います。
ただし読み上げ順やキーボード操作の順序はHTMLのままなので、多用しないほうがよいです。

## リファレンス

- [フレックスボックスの基本概念](https://developer.mozilla.org/ja/docs/Web/CSS/CSS_flexible_box_layout/Basic_concepts_of_flexbox)
- [display](https://developer.mozilla.org/ja/docs/Web/CSS/display)
- [justify-content](https://developer.mozilla.org/ja/docs/Web/CSS/justify-content)
- [align-items](https://developer.mozilla.org/ja/docs/Web/CSS/align-items)
- [flex](https://developer.mozilla.org/ja/docs/Web/CSS/flex)
