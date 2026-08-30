# コンテナクエリしたい（`@container`）

```css
/* 監視対象のコンテナーを宣言する */
.card-list {
    container-type: inline-size;
}

/* .card-list の幅が 400px 以上のとき、中の .card を横並びにする */
@container (min-width: 400px) {
    .card {
        display: block flex;
        gap: 1rem;
    }
}
```

`@container`ルールは、`@media`と似ていますが、条件に使うのが「画面の幅」ではなく「親要素（コンテナー）の幅」です。

同じ部品をサイドバーとメインの両方に置くような場合、
置かれた場所の幅に応じて見た目を変えられるので、部品を使い回しやすくなります。
ページ全体のレイアウトはメディアクエリ、その中の部品はコンテナクエリ、と使い分けます。

## コンテナーを宣言したい（`container-type`）

```css
.card-list {
    container-type: inline-size;
}
```

`@container`で幅を見てもらうには、親要素に`container-type`を指定して「これがコンテナーだ」と宣言します。

- `inline-size` … 横幅だけを監視する。ほとんどの場合これを使う
- `size` … 横幅と高さの両方を監視する。高さの計算が必要になるので使いどころは限られる
- `normal` … 監視しない（初期値）

`@container`のクエリは、いちばん近い「コンテナー宣言された祖先要素」を基準にします。
その要素自身ではなく、中の子要素にスタイルが当たります。

## 名前をつけて指定したい（`container-name`）

```css
.sidebar {
    container-type: inline-size;
    container-name: sidebar;
}

.main {
    container-type: inline-size;
    container-name: main;
}

/* sidebar コンテナーの幅だけを見る */
@container sidebar (min-width: 300px) {
    .card {
        font-size: 1.1rem;
    }
}
```

コンテナーが入れ子になっていると、`@container`がどのコンテナーを見るのか分かりにくくなります。

`container-name`で名前を付け、`@container 名前 (条件)`と書くと、その名前のコンテナーだけを対象にできます。

```css
/* container-type と container-name をまとめて書く */
.sidebar {
    container: sidebar / inline-size;
}
```

`container`ショートハンドで`名前 / タイプ`をまとめて指定することもできます。

## コンテナーの幅を単位に使いたい（`cqi`）

```css
@container (min-width: 400px) {
    .card h2 {
        font-size: max(1.25rem, 4cqi);
    }
}
```

コンテナクエリ専用の長さの単位があり、コンテナーの大きさに対する割合で指定できます。

- `cqw` … コンテナーの幅の1%
- `cqh` … コンテナーの高さの1%
- `cqi` … コンテナーのインライン方向（横書きなら幅）の1%
- `cqb` … コンテナーのブロック方向（横書きなら高さ）の1%

`4cqi`なら「コンテナー幅の4%」です。
コンテナーが広がると文字も一緒に大きくなる、といった調整ができます。

## ブラウザ対応

コンテナクエリはモダンブラウザで使えます（Chrome / Edge 105、Firefox 110、Safari 16 以降）。

古い環境も対象にする場合は、`@media`で近い挙動のフォールバックを書いておくと安全です。

## リファレンス

- [@container](https://developer.mozilla.org/ja/docs/Web/CSS/@container)
- [container-type](https://developer.mozilla.org/ja/docs/Web/CSS/container-type)
- [container-name](https://developer.mozilla.org/ja/docs/Web/CSS/container-name)
- [コンテナークエリーの使用](https://developer.mozilla.org/ja/docs/Web/CSS/CSS_containment/Container_queries)
