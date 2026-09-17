# CSS変数したい

```css
.card {

  /* 変数を定義（このセレクターの中だけで有効） */
  --card-padding: 16px;

  /* 変数を取得 */
  padding: var(--card-padding);
}
```

`--変数名`で、CSS変数（カスタムプロパティ）を定義できます。
定義した変数は、`var(--変数名)`で取得できます。

```{note}
[Can I use](https://caniuse.com/css-variables)で調べると、CSS変数（カスタムプロパティ）は2017年後半に使えるようになっていました。
```

## フォールバックしたい

```css
.card {
  padding: var(--card-padding, 16px);
}
```

`var`関数で、CSS変数を取得できます。
第二引数にフォールバック値を指定できます。
変数が未定義の場合には、このフォールバック値が使われます。

## グローバル変数したい（`:root`）

```css
:root {
    --font-family: system-ui, -apple-system;
    --color-main: #150201; /* ジャックドー */
    --color-sub: #00213b; /* ビザンツ・ブルー */
    --color-accent: #cee2df; /* ローヌリバー */
}


body {
    background-color: var(--color-main);
}

body > header {
    background-color: var(--color-sub);
}

body > main {
    background-color: white;
}

body > main a {
    color: var(--color-accent);
}

body > footer {
    background-color: var(--color-sub);
}
```

`:root`は、HTMLドキュメントのルート要素（`<html>`）を指す擬似クラスです。
このクラスに定義したCSS変数は、ドキュメント全体で使えるグローバル変数として利用できます。

上記のサンプルでは、ウェブサイトのテーマとなる3色（``--color-main``、``--color-sub``、``--color-accent``）を定義して、全体の背景やヘッダー（＝ナビゲーション部分を想定）とフッターに配色し、``--color-accent``はリンクの強調色として使っています。

## リファレンス

- [カスタムプロパティ](https://developer.mozilla.org/ja/docs/Web/CSS/Using_CSS_custom_properties)
- [var関数](https://developer.mozilla.org/ja/docs/Web/CSS/var)
- [:root](https://developer.mozilla.org/ja/docs/Web/CSS/:root)
- [Can I use: CSS Custom Properties](https://caniuse.com/css-variables)
