# アクセシビリティしたい（a11y）

```html
<img src="chart.png" alt="2026年の売上は前年比20%増">

<button type="button">メニューを開く</button>

<nav aria-label="パンくずリスト">...</nav>
```

アクセシビリティとは、目や耳、手の動きなどに制約がある人を含め、
できるだけ多くの人がウェブサイトを使えるようにすることです。
英語の"accessibility"は`a`と`y`のあいだに11文字あるので「a11y」と略します。

基本は「意味に合ったHTMLタグを正しく使う」ことです。
特別なことをしなくても、`button`や`nav`、見出しタグを適切に使うだけで、
スクリーンリーダーやキーボード操作にかなり対応できます。

## 画像に代替テキストしたい（`alt`）

```html
<!-- 内容を伝える画像：altで内容を説明する -->
<img src="chart.png" alt="2026年の売上は前年比20%増">

<!-- 装飾だけの画像：altを空にする -->
<img src="divider.png" alt="">
```

`img`タグには必ず`alt`属性を付けます。

`alt`は、画像が表示できないときや、スクリーンリーダーで読み上げるときに使われるテキストです。
画像が内容を伝えているなら、その内容を文章で書きます。
飾りだけの画像なら`alt=""`と空にして、読み上げの対象から外します。

`alt`属性そのものを書かないのは避けます。
書かないと、スクリーンリーダーがファイル名をそのまま読み上げてしまうことがあります。

## ボタンとリンクを使い分けたい

```html
<!-- ページを移動する：a タグ -->
<a href="/signup">登録ページへ</a>

<!-- その場で操作する：button タグ -->
<button type="button">送信</button>
```

「別のページに移動する」なら`a`タグ、「その場で何かを実行する」なら`button`タグを使います。

`div`や`span`に`onclick`を付けてボタン代わりにするのは避けます。
`button`タグなら、キーボードのTabキーで選べて、EnterやSpaceで実行でき、
スクリーンリーダーも「ボタン」と読み上げます。
`div`だとこれらを全部自分で用意しなければなりません。

## 見出しで構造を示したい

```html
<h1>ページのタイトル</h1>

<h2>大きな節</h2>
<h3>その中の小さな節</h3>

<h2>次の大きな節</h2>
```

見出し（`h1`〜`h6`）は、文字を大きくするための飾りではなく、文書の構造を示すタグです。

スクリーンリーダーの利用者は、見出しだけを拾い読みしてページの全体像をつかみます。
`h1`から順に、レベルを飛ばさずに使います（`h2`の次にいきなり`h4`にしない）。

見た目の大きさはCSSの`font-size`で調整し、レベルの選択は構造で決めます。

## フォーム部品にラベルしたい（`label`）

```html
<label for="email">メールアドレス</label>
<input type="email" id="email" name="email">
```

すべての入力欄には`label`タグを対応させます。

`label`の`for`属性と`input`の`id`属性を同じ値にすると、2つが結びつきます。
結びつくと、ラベルをクリックしても入力欄にフォーカスが移り、
スクリーンリーダーも入力欄と一緒にラベルを読み上げます。

プレースホルダー（`placeholder`）はラベルの代わりになりません。
入力し始めると消えてしまい、何の欄か分からなくなるためです。

## キーボードだけで操作できるようにしたい

```css
/* フォーカスの枠を消さない */
a:focus-visible,
button:focus-visible {
    outline: 2px solid #0066cc;
    outline-offset: 2px;
}
```

マウスを使わず、Tabキーで移動し、Enterで実行する人がいます。

`a`や`button`など標準のタグを使っていれば、キーボード操作は自動で効きます。
このとき、いまどこにフォーカスがあるかを示す枠（フォーカスリング）を消さないことが大切です。

`outline: none`で枠を消すと、キーボード利用者が現在位置を見失います。
デザイン上の理由で変えたい場合は、`outline`を消すのではなく、見える別のスタイルに置き換えます。

## 意味を補足したい（`aria-label`）

```html
<!-- テキストのないボタンに名前を付ける -->
<button type="button" aria-label="検索">
    <svg>...</svg>
</button>

<!-- 複数の nav を見分けられるようにする -->
<nav aria-label="パンくずリスト">...</nav>
```

`aria-*`属性は、HTMLタグだけでは伝えきれない情報を、スクリーンリーダーに補足するしくみです。

アイコンだけのボタンに`aria-label`で名前を付けたり、
同じ種類の要素が複数あるときに`aria-label`で区別したりします。

ARIAは「HTMLで足りないときの最後の手段」です。
`button`で済むところを`div`＋`role="button"`で書く、といった使い方はしません。
まず正しいHTMLタグを使い、それでも足りない部分だけARIAで補います。

## リファレンス

- [アクセシビリティ](https://developer.mozilla.org/ja/docs/Web/Accessibility)
- [HTML: アクセシビリティの基礎知識](https://developer.mozilla.org/ja/docs/Learn_web_development/Core/Accessibility/HTML)
- [ARIA](https://developer.mozilla.org/ja/docs/Web/Accessibility/ARIA)
- [ARIA の使い方の第一規則](https://www.w3.org/TR/using-aria/#rule1)
- [WebAIM](https://webaim.org/)
