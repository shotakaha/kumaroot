# ボックスモデルしたい

```css
* {
    box-sizing: border-box;
}
```

ボックスモデルとは、すべての要素を「内容・パディング・枠線・マージンの4つの層でできた箱」として扱うCSSの考え方です。
要素の大きさや余白は、この箱のどの層をどれだけ広げるかで決まります。

`box-sizing`プロパティで、`width`や`height`がどこまでの幅を指すかを切り替えられます。
はじめに全要素を`border-box`にそろえておくと、幅の計算がわかりやすくなります。

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

`padding`は [余白したい（`padding`）](css-padding.md)、`margin`は [余白したい（`margin`）](css-margin.md)、`border`は枠線の色や太さを指定するプロパティです。

## 幅の計算方法を変えたい（`box-sizing`）

```css
.content-box {
    box-sizing: content-box;  /* 初期値 */
    width: 300px;
    padding: 20px;
    border: 5px solid;
    /* 実際の見た目の幅は 300 + 20*2 + 5*2 = 350px */
}

.border-box {
    box-sizing: border-box;
    width: 300px;
    padding: 20px;
    border: 5px solid;
    /* 実際の見た目の幅は 300px（padding と border は内側に含まれる） */
}
```

`box-sizing`の初期値は`content-box`で、`width`は内容部分だけの幅を指します。
このため、パディングや枠線を足すと見た目の幅が指定値より大きくなります。

`border-box`にすると、`width`はパディングと枠線を含んだ幅になります。
「幅300pxの箱」を作りたいときに、指定した数値がそのまま見た目の幅になるので直感的です。

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

## 枠線を引きたい（`border`）

```css
.box {
    border: 1px solid #cccccc;
}
```

`border`プロパティで、要素の枠線を「太さ・線の種類・色」の順にまとめて指定できます。

線の種類は`solid`（実線）、`dashed`（破線）、`dotted`（点線）などがあります。
一辺だけ引きたいときは`border-top`、`border-bottom`のように方向を付けます。

```css
.quote {
    border-left: 4px solid #0066cc;
    padding-left: 1rem;
}
```

## 角を丸くしたい（`border-radius`）

```css
.card {
    border-radius: 8px;
}

.avatar {
    border-radius: 50%;  /* 正方形なら円になる */
}
```

`border-radius`プロパティで、要素の角を丸くできます。
値が大きいほど丸みが強くなり、`50%`を指定すると正方形は円、長方形は楕円になります。

枠線がなくても、背景色や画像がある要素なら角丸が見た目に効きます。

## リファレンス

- [box-sizing](https://developer.mozilla.org/ja/docs/Web/CSS/box-sizing)
- [ボックスモデル入門](https://developer.mozilla.org/ja/docs/Learn_web_development/Core/Styling_basics/Box_model)
- [border](https://developer.mozilla.org/ja/docs/Web/CSS/border)
- [border-radius](https://developer.mozilla.org/ja/docs/Web/CSS/border-radius)
