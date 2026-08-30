# セレクターしたい

```css
セレクター {
    プロパティ名: 値;
}
```

CSSは「どの要素に（セレクター）」「どんな見た目を（プロパティと値）」という組み合わせで書きます。
このページでは、よく使うセレクターを「やりたいこと」から引けるように整理します。

## タグしたい（`p`）

```css
p {
    line-height: 1.7;
}
```

タグ名をそのまま書くと、そのタグすべてに適用されます（タイプセレクター）。
`p`ならページ内のすべての`<p>`が対象です。
本文の行間やフォントなど、全体の土台になるスタイルに使います。

## クラスしたい（`.note`）

```css
.note {
    padding: 1rem;
    background: #f4f4f4;
}
```

```html
<p class="note">補足のテキスト</p>
```

`.クラス名`で、`class`属性にそのクラスを持つ要素だけに適用されます。
同じクラスは何個の要素に付けてもよく、1つの要素に複数のクラスを付けることもできます。
実務でいちばんよく使うセレクターです。

## アイディーしたい（`#header`）

```css
#header {
    position: sticky;
    top: 0;
}
```

```html
<header id="header">...</header>
```

`#id名`で、`id`属性が一致する要素に適用されます。
`id`はページ内で1つだけと決まっているので、ヘッダーやフッターなど「そのページに1つしかない」要素に使います。

迷ったらクラスで統一しておくと、あとで使い回しやすく詳細度（後述）も上がりすぎません。

## グループしたい（`,`）

```css
h1,
h2,
h3 {
    margin-top: 2rem;
}
```

`,`（カンマ）でセレクターを並べると、複数のセレクターに同じスタイルをまとめて指定できます。
1つでも書き間違えると、その行だけでなくグループ全体が無効になる点に注意します。

## 子孫したい（半角スペース）

```css
main p {
    line-height: 1.7;
}
```

セレクターを半角スペースで区切ると、「左の要素の中にある右の要素」が対象になります（子孫結合子）。
`main p`は`<main>`の中のすべての`<p>`で、孫やひ孫の階層でも対象です。

## 直下の子したい（`>`）

```css
nav.breadcrumb > ul {
    display: flex;
    gap: 0.5rem;
}
```

```html
<nav class="breadcrumb">
    <ul>
        <li><a href="URL">HOME</a></li>
        <li>ページタイトル</li>
    </ul>
</nav>
```

`>`は「すぐ下の階層の子」だけが対象です。
子孫結合子（スペース）が階層の深さを問わないのに対し、`>`は1階層だけに限定されます。

## 隣の要素したい（`+` / `~`）

```css
/* h2 のすぐ後ろの p だけ */
h2 + p {
    margin-top: 0;
}

/* h2 より後ろにある同じ階層の p すべて */
h2 ~ p {
    color: #555;
}
```

`+`（隣接兄弟結合子）は「直後の1つ」、`~`（後続兄弟結合子）は「後ろに続く同階層すべて」が対象です。
どちらも同じ親を持つ要素どうしの関係を見ます。

## 属性したい（`[type="text"]`）

```css
input[type="text"] {
    border: 1px solid #ccc;
}

/* https で始まるリンク */
a[href^="https"] {
    color: green;
}

/* .pdf で終わるリンク */
a[href$=".pdf"]::after {
    content: " (PDF)";
}
```

`[属性名="値"]`で、属性の値による絞り込みができます。

- `^=` … その値で始まる
- `$=` … その値で終わる
- `*=` … その値を含む

## 状態したい（`:hover`）

```css
a:hover {
    text-decoration: underline;
}

button:disabled {
    opacity: 0.5;
}

input:focus {
    outline: 2px solid blue;
}
```

`:`で始まる擬似クラスで、要素の「状態」に応じたスタイルを指定できます。
`:hover`（マウスが乗っている）、`:focus`（入力中）、`:checked`（チェック済み）、`:disabled`（無効）などがあります。

## 何番目かしたい（`:nth-child()`）

```css
/* 最初の li */
li:first-child {
    font-weight: bold;
}

/* 偶数番目の行に色を付ける（シマシマ） */
tr:nth-child(even) {
    background: #f4f4f4;
}
```

構造上の位置で要素を選べます。
`:first-child` / `:last-child`のほか、`:nth-child(2)`（2番目）、`:nth-child(odd)` / `:nth-child(even)`（奇数・偶数）、`:nth-child(3n)`（3の倍数）のように書きます。

## 除外したい（`:not()`）

```css
/* .special 以外の li */
li:not(.special) {
    color: #333;
}
```

`:not(セレクター)`で、条件に当てはまる要素を対象から除外できます。
「基本はこう、ただしこれだけは別」というときに使います。

## 前後に飾りしたい（`::before` / `::after`）

```css
.tag::before {
    content: "#";
    color: #999;
}

blockquote::before {
    content: "“";
    font-size: 2rem;
}
```

`::before` / `::after`は擬似要素で、要素の中身の前後に「CSSだけで作った中身」を追加します。
`content`プロパティが必須で、空にするなら`content: ""`と書きます。
アイコンや記号など、HTMLに書くまでもない装飾に使います。

## 詳細度したい

同じ要素に複数のスタイルが当たったときは、セレクターの「詳細度（優先順位）」が高いほうが勝ちます。

| セレクター | 詳細度 |
| --- | --- |
| `#id` | 高（100） |
| `.class` / `[属性]` / `:hover` | 中（10） |
| `p` / `::before` | 低（1） |

詳細度が同じなら、あとに書いたルールが勝ちます。
`!important`を付けると詳細度を無視して最優先になりますが、上書きの上書き合戦になりやすいので多用は避けます。

セレクターをむやみに長く（`#main .list li a.link`）すると詳細度が上がりすぎて後から調整しづらくなります。
基本はクラス1つで指定し、詳細度をなるべくそろえておくと管理が楽です。

## リファレンス

- [CSS セレクター](https://developer.mozilla.org/ja/docs/Web/CSS/CSS_selectors)
- [擬似クラス](https://developer.mozilla.org/ja/docs/Web/CSS/Pseudo-classes)
- [擬似要素](https://developer.mozilla.org/ja/docs/Web/CSS/Pseudo-elements)
- [詳細度](https://developer.mozilla.org/ja/docs/Web/CSS/CSS_cascade/Specificity)
