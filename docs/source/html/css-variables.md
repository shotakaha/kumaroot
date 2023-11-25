# 全体設定したい（``:root``）

```css
:root {
    --font-family: system-ui, -apple-system;
    --base-color: #150201; /* ジャックドー */
    --accent-color: #cee2df; /* ローヌリバー */
    --sub-color: #00213b; /*ビザンツ・ブルー */
}


body {
    background-color: var(--base-color);
}

body > header {
    background-color: var(--sub-color);
}

body > main {
    background-color: white;
}

body > footer {
    background-color: var(--sub-color);
}
```

[:root](https://developer.mozilla.org/ja/docs/Web/CSS/:root)で、グローバルな[カスタムプロパティ](https://developer.mozilla.org/ja/docs/Web/CSS/Using_CSS_custom_properties)を宣言できます。
カスタムプロパティの値は[var関数](https://developer.mozilla.org/ja/docs/Web/CSS/var)で取得できます。

上記のサンプルでは、ウェブサイトのテーマとなる3色（``--base-color``、``--accent-color``、``--sub-color``）を定義して、全体の背景やヘッダー（＝ナビゲーション部分を想定）とフッターに配色しています。
