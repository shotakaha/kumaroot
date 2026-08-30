# ボックスモデルしたい（`box-sizing`）

```css
*,
*::before,
*::after {
    box-sizing: border-box;
}
```

ボックスモデルとは、すべての要素を「内容・パディング・枠線・マージンの4つの層でできた箱」として扱うCSSの考え方です。
要素の大きさや余白は、この箱のどの層をどれだけ広げるかで決まります。

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

`box-sizing`プロパティは、`width`や`height`で指定した数値が「箱のどこからどこまで」を指すかを切り替えます。
初期値は`content-box`で、いちばん内側の`content`（内容）の幅を基準にします。
このため、`padding`や`border`を足すと、見た目の幅は指定した数値より大きくなります。

なお`margin`は常に箱の外側です。
`box-sizing`をどう設定しても、`margin`が`width`や`height`に含まれることはありません。

## 全要素の基準をそろえたい（`border-box`）

```css
*,
*::before,
*::after {
    box-sizing: border-box;
}
```

`border-box`を指定すると、`width`と`height`が指す範囲が`content + padding + border`に変わります。
`padding`と`border`は箱の内側に収まり、指定した数値がそのまま見た目の幅になります。

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

`border-box`のほうが「指定した数値＝見た目の幅」で計算しやすいため、
多くのCSSフレームワークやリセットCSSは、この指定を最初に入れています。

`box-sizing`は継承されないプロパティなので、`*`（すべての要素を選ぶセレクター）と擬似要素にまとめて指定します。
新しくCSSを書き始めるときは、まずこれを書いておくと余白まわりの計算で悩まなくなります。

:::{seealso}

- [](./css-padding.md)
- [](./css-margin.md)
- [](./css-border.md)

:::

## リファレンス

- [box-sizing](https://developer.mozilla.org/ja/docs/Web/CSS/box-sizing)
- [ボックスモデル入門](https://developer.mozilla.org/ja/docs/Learn_web_development/Core/Styling_basics/Box_model)
