# レイヤーしたい（`@layer`）

```css
/* 優先度の低い順に、レイヤー名を宣言する */
@layer reset, base, components, utilities;

@layer reset {
    * {
        margin: 0;
        padding: 0;
    }
}

@layer components {
    .button {
        padding: 0.5rem 1rem;
    }
}
```

`@layer`ルールで、CSSを「レイヤー（層）」に分けて、レイヤーごとの優先順位を決められます。

同じ要素にスタイルがぶつかったとき、**どのレイヤーに属するか**が、セレクターの詳細度よりも先に判定されます。
優先度の高いレイヤーの指定は、詳細度が低くても、優先度の低いレイヤーの指定に勝ちます。

これを使うと、フレームワークのCSSを低いレイヤーに入れておき、
自分のCSSを高いレイヤーに置くことで、詳細度を気にせず上書きできます。

:::{seealso}

- [](./css-cascade.md)
- [](./css-import.md)

:::

## レイヤーの順番を決めたい

```css
@layer reset, base, components, utilities;
```

`@layer 名前, 名前, ...;`と名前だけを並べて宣言すると、その順番が優先度になります。
**あとに書いたレイヤーほど優先度が高い**です。

この宣言をCSSの先頭に置いておけば、
実際のスタイルをどの順番で書いても、優先度は宣言した順で固定されます。

```css
/* 先頭で順番を決めておく */
@layer reset, base, components;

/* 以降は順不同で書いてよい */
@layer components { ... }
@layer reset { ... }
@layer base { ... }
```

## 後からレイヤーに追記したい

```css
@layer components {
    .button { ... }
}

/* 別の場所で同じレイヤーに追記できる */
@layer components {
    .card { ... }
}
```

同じレイヤー名の`@layer`ブロックは、何回書いてもかまいません。
内容はすべてそのレイヤーにまとまります。

ファイルを分けて書いても、同じレイヤー名なら同じ層に入ります。

## レイヤーに入れないCSSしたい

```css
@layer base {
    a { color: blue; }
}

/* レイヤーに入れていない指定 */
a { color: red; }
```

`@layer`で囲まなかった通常のスタイルは、**すべてのレイヤーより優先度が高い**です。

上のサンプルでは、`base`レイヤーの青ではなく、レイヤー外の赤が採用されます。
うっかりレイヤー外に書くと、レイヤーの設計が崩れるので注意します。

## インポートをレイヤーに入れたい（`@import`）

```css
@import url("framework.css") layer(framework);
@import url("mystyles.css") layer(app);
```

`@import`で読み込むCSSも、`layer()`を付けるとレイヤーに入れられます。

フレームワークのCSSをまるごと低い優先度のレイヤーに入れておけば、
自分のCSSから詳細度を気にせず上書きできます。

## レイヤー名の付け方

レイヤー名は自由ですが、役割ごとに分けた次のような命名がよく使われます。

| レイヤー | 役割 |
| --- | --- |
| `reset` | ブラウザ間の差を吸収する初期化（`reset.css` / `normalize.css`相当） |
| `base` | `body`や`a`など、素のタグに対する基本スタイル |
| `tokens` | 色やフォントなどのCSS変数の定義 |
| `layout` | ページ全体の骨組み（コンテナー幅、グリッド） |
| `components` | ボタンやカードなど部品のスタイル |
| `utilities` | `.mt-2`のような単機能クラス。優先度をいちばん高くする |

## リファレンス

- [@layer](https://developer.mozilla.org/ja/docs/Web/CSS/@layer)
- [カスケードレイヤー](https://developer.mozilla.org/ja/docs/Web/CSS/CSS_cascade/Cascade_layers)
