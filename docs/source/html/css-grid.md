# グリッドしたい（`display: block grid`）

```css
.container {
    display: block grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
}
```

グリッドレイアウトは、2次元に並べるレイアウト方式です。
親要素を「グリッドコンテナー」、
子要素を「グリッドアイテム」と呼びます。

## 段組したい（`grid-template-columns`）

```css
.container {
    display: block grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
}
```

`grid-template-columns`で、グリッドコンテナーの列数と列幅を指定できます。
`repeat(3, 1fr)`は、3列を指定し、それぞれの列幅を1fr（フレックスレコード）で均等にします。

```css
.container {
    display: block grid;
    grid-template-columns: 1fr 2fr 1fr;
    gap: 1rem;
}
```

`grid-template-columns`で、列数と列幅を個別に指定することもできます。
`1fr 2fr 1fr`は、3列のうち真ん中の列が左右の列の2倍の幅になるように指定しています。

## 行組したい（`grid-template-rows`）

```css
.container {
    display: block grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: 100px 200px;
    gap: 1rem;
}
```

`grid-template-rows`で、グリッドコンテナーの行数と行高を指定できます。
`100px 200px`は、1行目の高さが100px、2行目の高さが200pxになるように指定しています。

## 割り付けしたい（`grid-template-areas` / `grid-area`）

```css
.container {
    display: block grid;
    grid-template-columns: 1fr 2fr 1fr;
    grid-template-rows: 100px 200px;
    grid-template-areas:
        "header header header"
        "sidebar main main"
        "footer footer footer";
    gap: 1rem;
}
.header {
    grid-area: header;
}
.sidebar {
    grid-area: sidebar;
}
.main {
    grid-area: main;
}
.footer {
    grid-area: footer;
}
```

`grid-template-areas`で、グリッドコンテナーの行と列に名前を付けて、グリッドアイテムを割り付けることができます。

親要素に`grid-template-areas`を指定し、子要素に`grid-area`を指定することで、グリッドアイテムの位置を決めることができます。
