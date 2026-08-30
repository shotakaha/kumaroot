# KaTeXしたい（`katex`）

```html
<head>
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/katex@0.18.4/dist/katex.min.css"
          crossorigin="anonymous">

    <script defer
            src="https://cdn.jsdelivr.net/npm/katex@0.18.4/dist/katex.min.js"
            crossorigin="anonymous"></script>
    <script defer
            src="https://cdn.jsdelivr.net/npm/katex@0.18.4/dist/contrib/auto-render.min.js"
            crossorigin="anonymous"
            onload="renderMathInElement(document.body);"></script>
</head>
```

KaTeXは、ウェブページ上でTeX記法の数式をきれいに表示するためのライブラリです。

`$...$`のように書いた数式を、読み込み時にブラウザ上で組版します。
サーバー側の処理は不要で、CSSとJavaScriptを読み込むだけで動きます。

同じ用途のMathJaxより表示が速いのが特長です。
一方で、対応しているTeXコマンドはMathJaxより少なめです。

## 読み込みたい

```html
<!-- 1. スタイルシート -->
<link rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/katex@0.18.4/dist/katex.min.css"
      crossorigin="anonymous">

<!-- 2. 本体 -->
<script defer
        src="https://cdn.jsdelivr.net/npm/katex@0.18.4/dist/katex.min.js"
        crossorigin="anonymous"></script>
```

数式のフォントはCSSファイルに含まれているので、`katex.min.css`は必ず読み込みます。

`katex.min.js`は本体で、数式を組版する`katex.render()`などの関数を提供します。
`defer`を付けて`head`に置くと、HTMLの読み込みを止めません。

## 本文中の数式を一括変換したい（`auto-render`）

```html
<script defer
        src="https://cdn.jsdelivr.net/npm/katex@0.18.4/dist/contrib/auto-render.min.js"
        crossorigin="anonymous"
        onload="renderMathInElement(document.body);"></script>
```

```html
<p>ピタゴラスの定理は $a^2 + b^2 = c^2$ です。</p>

<p>解の公式:</p>
$$ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$
```

`auto-render`拡張を読み込むと、ページ内の`$...$`や`$$...$$`を自動で数式に変換します。

`onload="renderMathInElement(document.body);"`で、
本体スクリプトの読み込み後に`<body>`全体を走査させます。

- `$...$` … 文中に埋め込むインライン数式
- `$$...$$` … 独立した行に中央寄せで表示するディスプレイ数式

## 区切り記号を変えたい

```html
<script>
    document.addEventListener("DOMContentLoaded", () => {
        renderMathInElement(document.body, {
            delimiters: [
                { left: "$$", right: "$$", display: true },
                { left: "\\[", right: "\\]", display: true },
                { left: "\\(", right: "\\)", display: false }
            ]
        });
    });
</script>
```

`$`を通貨記号として使うページでは、`renderMathInElement`の`delimiters`オプションで区切りを変えられます。

上の設定では`$...$`（インライン）を無効にし、`\(...\)`と`\[...\]`だけを数式として扱います。
この場合、`auto-render`の`onload`属性は使わず、自前の`<script>`で呼び出します。

## 1つの数式だけ変換したい（`katex.render`）

```html
<span id="formula"></span>

<script>
    katex.render("c = \\pm\\sqrt{a^2 + b^2}", document.getElementById("formula"), {
        throwOnError: false
    });
</script>
```

特定の要素にだけ数式を入れたいときは、`katex.render(TeX文字列, 要素, オプション)`を直接呼びます。

- 第1引数のTeX文字列では、`\`をJavaScriptの文字列として`\\`とエスケープします
- `throwOnError: false`にすると、記法エラーのとき例外を投げず、赤字でその箇所を表示します

## リファレンス

- [KaTeX 公式サイト](https://katex.org/)
- [ブラウザーでの利用](https://katex.org/docs/browser)
- [対応コマンド一覧](https://katex.org/docs/supported)
- [auto-render 拡張](https://katex.org/docs/autorender)
