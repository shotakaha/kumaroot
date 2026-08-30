# カスケードしたい

```css
p {
    color: black;
}

p {
    color: red;
}
```

CSSは、1つの要素に対していくつものスタイルを指定できます。
スタイルの設定は「カスケード」と呼ばれるルールにしたがって決まります。

上記サンプルでは、同じ段落タグ（`<p>`）に文字色を2回指定しています。
1つ目の`color: black;`は黒、
2つ目の`color: red;`は赤ですが、
この場合は赤が採用されます。

:::{note}

"Cascade"は「滝のように流れる」という意味です。

:::

## 詳細度したい（specificity）

```css
a {
    color: blue;
}

.link {
    color: green;
}
```

```html
<a href="URL" class="link">リンク</a>
```

CSSのカスケードルールの1つ目は「詳細度（specificity）」です。

詳細度は、セレクターの種類によって割り当てられている「点数」を加算した値です。
複数のセレクターが同じ要素にぶつかったとき、詳細度が高い方が採用されます。

点数の目安は次のとおりです。

| セレクターの種類 | 点数 | 例 |
| --- | --- | --- |
| IDセレクター（ID selector） | 100 | `#header` |
| クラスセレクター（Class selector） | 10 | `.link` |
| 属性セレクター（Attribute selector） | 10 | `[type="text"]` |
| 擬似クラス（Pseudo-class） | 10 | `:hover` |
| タイプセレクター（Type selector） | 1 | `a` |
| 擬似要素（Pseudo-element） | 1 | `::before` |
| ユニバーサルセレクター（Universal selector） | 0 | `*` |

セレクターを`#main .list li a`のようにつなげて書くと、それぞれの点数が足し算されます。
この例だと`100 + 10 + 1 + 1`で、合計111点です。

セレクターを長くつなげるほど点数が上がり、あとから別のスタイルで上書きするのが難しくなります。
ふだんはクラスセレクター1つで指定して、点数をなるべくそろえておくと管理が楽になります。

## 記述順したい

```css
.button {
    background: gray;
}

.button {
    background: blue;
}
```

カスケードルールの2つ目は「記述順」です。
詳細度の点数が同じスタイルどうしがぶつかったときは、あとに書かれたほうが採用されます。

上のサンプルは、どちらも`.button`で点数が同じです。
あとに書いた青が採用され、ボタンの背景は青になります。

この「あと」には、ファイルを読み込む順番もふくまれます。
`<link>`タグや`@import`でCSSファイルを複数読み込むと、うしろに読み込んだファイルの指定が優先されます。
だから、自分で上書きしたいCSSは、フレームワークのCSSより下に置きます。

## 上書きを強制したい（`!important`）

```css
.alert {
    color: red !important;
}

#box .alert {
    color: gray;
}
```

カスケードルールの3つ目は「`!important`」です。
`!important`を付けたスタイルは
詳細度や記述順を無視して最優先されます。

上のサンプルでは、`#box .alert`のほうが点数は高いです。
それでも`!important`がついた赤が勝つので、文字色は赤になります。

`!important`は強力ですが、これに勝つにはさらに`!important`を重ねるしかなく、原因を追いにくいCSSになります。
自分で書くCSSでは基本的に使いません。
フレームワークのCSSをどうしても一部だけ上書きしたい、といった場面にとどめます。

:::{warning}

`!important`をあちこちで使っているとしたら、詳細度の設計がうまくいっていないサインです。
セレクターをクラス1つにそろえるなど、書き方を見直すほうが先です。

:::

## 継承したい（`inherit`）

```css
body {
    color: #333;
    font-family: system-ui, sans-serif;
}
```

`color`や`font-family`など一部のプロパティは、親要素に指定した値を子要素が自動的に受け継ぎます。
このしくみを継承といいます。

上のサンプルでは、`body`に文字色とフォントを指定しています。
中にある`p`や`a`に何も指定しなくても、同じ文字色とフォントが適用されます。

継承されるのは、`font-size`や`line-height`など、文字まわりのプロパティが中心です。
`margin`、`padding`、`border`、`background`などは継承されず、要素ごとに指定する必要があります。

```css
.card {
    color: inherit;
    border: initial;
}
```

継承するかどうかは、キーワードで指定し直すこともできます。
`inherit`は親の値を受け継ぎ、`initial`はそのプロパティの初期値に戻します。

## いまの文字色を使い回したい（`currentColor`）

```css
.icon {
    fill: currentColor;
    border: 1px solid currentColor;
}
```

`currentColor`は、その要素にいま効いている`color`の値を指す特別なキーワードです。

上のサンプルでは、アイコンの塗りつぶしと枠線に`currentColor`を指定しています。
`color`を変えるだけで、アイコンの色も枠線の色も一緒に変わります。
色の指定を1か所にまとめられるので、テーマ色の管理が楽になります。

## リファレンス

- [カスケード](https://developer.mozilla.org/ja/docs/Web/CSS/CSS_cascade/Cascade)
- [詳細度](https://developer.mozilla.org/ja/docs/Web/CSS/CSS_cascade/Specificity)
- [継承](https://developer.mozilla.org/ja/docs/Web/CSS/CSS_cascade/Inheritance)
- [!important](https://developer.mozilla.org/ja/docs/Web/CSS/important)
