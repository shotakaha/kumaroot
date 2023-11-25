# CSS変数したい

```css
セレクタ {

  /* 変数を定義 */
  --変数名: 値

  /* 変数を取得 */
  プロパティ名: var(--変数名)
}
```

[カスタムプロパティ](https://developer.mozilla.org/ja/docs/Web/CSS/Using_CSS_custom_properties)を使ってCSS変数を宣言できます。
設定した変数の値は[var関数](https://developer.mozilla.org/ja/docs/Web/CSS/var)で取得できます。

```{note}

[Can I use](https://caniuse.com/css-variables)で調べると、CSS変数（カスタムプロパティ）は2017年後半に使えるようになっていました。
以下のようにグローバル変数として使うのが便利だと思います。

```

## グローバル変数したい（``:root``）

```css
:root {
    --font-family: system-ui, -apple-system;
    --color-main: #150201; /* ジャックドー */
    --color-sub: #00213b; /*ビザンツ・ブルー */
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

body > footer {
    background-color: var(--color-sub);
}
```

[:root](https://developer.mozilla.org/ja/docs/Web/CSS/:root)にカスタムプロパティを設定することで、
グローバル変数として利用できます

上記のサンプルでは、ウェブサイトのテーマとなる3色（``--color-main``、``--color-sub``、``--color-accent``）を定義して、全体の背景やヘッダー（＝ナビゲーション部分を想定）とフッターに配色しています。
