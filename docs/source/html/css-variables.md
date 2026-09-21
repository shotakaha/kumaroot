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
    font-family: var(--font-family);
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

## フォント設定したい

```css
:root {
    --font-family: system-ui, -apple-system, "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
    --font-family-heading: Georgia, serif;
}

body {
    font-family: var(--font-family);
}

h1, h2, h3 {
    font-family: var(--font-family-heading);
}
```

CSS変数で、サイト全体のフォントをまとめて管理できます。
上記のサンプルでは、
`--font-family`でサイト全体のフォント、
`--font-family-heading`で見出しのフォントを指定しています。

## カラー設定したい

```css
:root {
    --color-surface: #fafafa;
    --color-on-surface: #1a1a1a;
    --color-primary: #8700cb;
    --color-on-primary: #fafafa;
    --color-secondary: #02c930;
    --color-on-secondary: #fafafa;
    --color-accent: #fee000;
    --color-on-accent: #1a1a1a;
    --color-muted: #8700cb30;
    --color-on-muted: #1a1a1a;
}

body {
    background-color: var(--color-surface);
    color: var(--color-on-surface);
}

a {
    color: var(--color-accent);
}

figcaption {
    background-color: var(--color-muted);
    color: var(--color-on-muted);
}

body > header {
    background-color: var(--color-primary);
    color: var(--color-on-primary);
}
```

CSS変数で、サイト全体の配色をまとめて管理できます。
このとき、役割ベースで変数名をつけることをオススメします。

```css
:root {
    --color-border: #cccccc;
    --color-success: #00cc66;
    --color-warning: #ffcc00;
    --color-error: #ff3300;
}
```

また、状態ベースで色を管理しておくのも便利です。

それぞれの変数名の役割と使いどころを以下に整理しました。

| 変数名 | 役割 | 使う場所 |
| --- | --- | --- |
| `--color-surface` | ページ全体の背景色 | `body` |
| `--color-on-surface` | ページ全体の文字色 | `body` |
| `--color-primary` | ブランドの主色 | ヘッダーやボタンなど |
| `--color-on-primary` | ブランドの主色に対する文字色 | ヘッダーやボタンなど |
| `--color-secondary` | 補助色 | ナビゲーションやサイドバーなど |
| `--color-on-secondary` | 補助色に対する文字色 | ナビゲーションやサイドバーなど |
| `--color-accent` | アクセント色 | リンクや強調箇所 |
| `--color-on-accent` | アクセント色に対する文字色 | リンクや強調箇所 |
| `--color-muted` | 控えめな背景色 | ヘルプテキストや小さな文字 |
| `--color-on-muted` | 控えめな文字色 | ヘルプテキストや小さな文字 |
| `--color-border` | 枠線の色 | ボーダーなど |
| `--color-success` | 成功時の色 | チェックボックスや成功メッセージ |
| `--color-warning` | 警告時の色 | アラートや警告メッセージ |
| `--color-error` | エラー時の色 | エラーメッセージ |

## リファレンス

- [カスタムプロパティ](https://developer.mozilla.org/ja/docs/Web/CSS/Using_CSS_custom_properties)
- [var関数](https://developer.mozilla.org/ja/docs/Web/CSS/var)
- [:root](https://developer.mozilla.org/ja/docs/Web/CSS/:root)
- [font-family](https://developer.mozilla.org/ja/docs/Web/CSS/font-family)
- [Can I use: CSS Custom Properties](https://caniuse.com/css-variables)
