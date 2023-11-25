# CSS変数したい

```css
/* 変数を定義 */
--変数名: 値

/* 変数を取得 */
プロパティ名: var(--変数名)
```

[カスタムプロパティ](https://developer.mozilla.org/ja/docs/Web/CSS/Using_CSS_custom_properties)を使って変数を宣言できます。
設定した変数の値は[var関数](https://developer.mozilla.org/ja/docs/Web/CSS/var)で取得できます。

```{note}

いつのまにかCSSで変数が使えるようになっていました。
mdnドキュメントは定期的に確認したほうがいいんだなと感じました。

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
