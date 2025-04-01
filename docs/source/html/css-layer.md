# レイヤーしたい（`@layer`）

```css
@layer レイヤー名;

/* レイヤーの優先度 : 低 -> 高 */
@layer reset, base, layout, theme, components, overrides
```

`@layer`でCSSのレイヤー名を定義できます。
レイヤー名を複数並べることで、優先度を設定できます。

## リセットしたい

```css
@layer reset {
    html, body {
        marign: 0;
        padding: 0;
    }
}
```

`reset`レイヤーには、ブラウザ間での違いを吸収するための設定を記述します。
従来の`reset.css`や`normalize.css`を参考に、
自分の用途に必要なものを設定するとよいです。

## フォントしたい

```css
@layer base {
    body {
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 16px;
        line-height: 1.75;
        color: #222222;
        background-color: #ffffff;
    }

    a {
        text-decoration: none;
        color: #0066cc;
    }
}
```

`base`レイヤーでは、テキスト表示に関連した設定を記述します。

## レイアウトしたい

```css
@layer layout {
    .container {
        max-width: 960px;
        margin: 0 auto;
    }
}
```

`layout`レイヤーは、

## テーマしたい

```css
@layer theme {
    .red {
        text: #ff0000;
    }
}
```

`theme`レイヤーでは、サイト全体の色味などを変更できるクラスを記述するとよいです。

## コンポーネントしたい

```css
@layer components {
    h1 {
        font-size: 2.4rem;
        color: #004488;
    }

    pre {
        background-color: #f4f4f4;
        border-left: 4px solid #cccccc;
        padding: 0.5em;
    }
}
```

見出しやコードブロックなどの要素を設定するためのレイヤーです。

## リファレンス

- [@layer - mdn docs](https://developer.mozilla.org/ja/docs/Web/CSS/@layer)
