# ボックスモデルしたい（`box-sizing`）

```css
/* どちらも width: 300px */
.content-box {
    box-sizing: content-box;  /* 初期値 */
    width: 300px;
    padding: 20px;
    border: 5px solid;
    /* 見た目の幅は 300 + 20*2 + 5*2 = 350px */
}

.border-box {
    box-sizing: border-box;
    width: 300px;
    padding: 20px;
    border: 5px solid;
    /* 見た目の幅は 300px */
}
```

`box-sizing`プロパティで、`width`や`height`で指定した数値の基準を変更できます。
初期値は`content-box`で、いちばん内側の`content`（内容）の幅が基準となっています。

:::{seealso}

- [](./css-padding.md)
- [](./css-margin.md)
- [](./css-border.md)

:::

## 見た目の幅を基準にしたい（`border-box`）

```css
*,
*::before,
*::after {
    box-sizing: border-box;
}
```

`box-sizing: border-box`で、`width`と`height`の基準を`content + padding + border`に変更できます。
`padding`と`border`が基準の内側に含まれるため、指定した数値がそのまま見た目の幅になります。

`box-sizing`は継承されないプロパティなので、`*`（すべての要素を選ぶセレクター）と擬似要素にまとめて指定します。
新しくCSSを書き始めるときは、まずこれを書いておくと余白まわりの計算で悩まなくなります。

:::{tip}

`border-box`のほうが「指定した数値＝見た目の幅」で計算しやすいため、
多くのCSSフレームワークやリセットCSSは、この指定を最初に入れています。

:::

すべてのHTML要素は「長方形の箱」として配置されます。
これは、CSSレイアウトの大前提です。
この箱は、内側から「内容（content）」「内側の余白（padding）」「枠線（border）」「外側の余白（margin）」の4つの層でできています。
要素の大きさや余白は、それぞれの層をどれだけ広げるかで決まります。

```text
+-----------------------------------+
|             margin                |  外側の余白（他の要素との間隔）
|  +-----------------------------+  |
|  |          border            |  |  枠線
|  |  +-----------------------+  |  |
|  |  |       padding         |  |  |  内側の余白（枠線と内容の間隔）
|  |  |  +-----------------+  |  |  |
|  |  |  |    content      |  |  |  |  内容（文字や画像）
|  |  |  +-----------------+  |  |  |
|  |  +-----------------------+  |  |
|  +-----------------------------+  |
+-----------------------------------+
```

デフォルトの`content-box`は`content`の幅を基準とするため、`padding`や`border`を広げると、見た目の幅が大きくなります。

## リファレンス

- [box-sizing](https://developer.mozilla.org/ja/docs/Web/CSS/box-sizing)
- [ボックスモデル入門](https://developer.mozilla.org/ja/docs/Learn_web_development/Core/Styling_basics/Box_model)
