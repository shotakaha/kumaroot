# ボックスモデルしたい（`box-sizing`）

```css
.content-box {
    box-sizing: content-box;  /* 初期値 */
    width: 300px;
    padding: 20px;
    border: 5px solid;
}

.border-box {
    box-sizing: border-box;
    width: 300px;
    padding: 20px;
    border: 5px solid;
}
```

ボックスモデルとは、すべての要素を「内容・パディング・枠線・マージンの4つの層でできた箱」として扱うCSSの考え方です。
要素の大きさや余白は、この箱のどの層をどれだけ広げるかで決まります。

`box-sizing`プロパティで、`width`や`height`がどこまでの大きさを指すかを切り替えられます。
はじめに全要素を`border-box`にそろえておくと、幅や高さの計算がわかりやすくなります。

## ボックスモデルを理解したい

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

要素の箱は、内側から順に次の4層でできています。

- **content** … 文字や画像が入る部分
- **padding** … 内容と枠線のあいだの余白
- **border** … 枠線
- **margin** … 枠線の外側、他の要素とのあいだの余白

`width`と`height`が指すのは、初期状態では`content`の層だけです。
`padding`や`border`は`content`の外側に追加されるため、指定した数値より箱が大きく見えます。

## 幅の計算方法を変えたい（`box-sizing`）

```css
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
    /* 見た目の幅は 300px（padding と border は内側に含まれる） */
}
```

`box-sizing`の初期値は`content-box`で、`width`と`height`は内容部分だけの大きさを指します。
このため、パディングや枠線を足すと見た目の大きさが指定値より大きくなります。

`border-box`にすると、`width`と`height`はパディングと枠線を含んだ大きさになります。
「幅300pxの箱」を作りたいときに、指定した数値がそのまま見た目の幅になるので直感的です。
どちらの場合も`margin`は含まれず、常に箱の外側に付きます。

## すべての要素をborder-boxにしたい

```css
*,
*::before,
*::after {
    box-sizing: border-box;
}
```

`box-sizing`は継承されないプロパティなので、全要素にまとめて指定します。
`*`（すべての要素を選ぶセレクター）と擬似要素に`border-box`を指定するのが定番の書き方です。

多くのCSSフレームワークやリセットCSSは、この指定を最初に入れています。
新しくCSSを書き始めるときは、まずこれを書いておくと余白まわりの計算で悩まなくなります。

:::{seealso}

- [](./css-padding.md)
- [](./css-margin.md)
- [](./css-border.md)

:::

## リファレンス

- [box-sizing](https://developer.mozilla.org/ja/docs/Web/CSS/box-sizing)
- [ボックスモデル入門](https://developer.mozilla.org/ja/docs/Learn_web_development/Core/Styling_basics/Box_model)
