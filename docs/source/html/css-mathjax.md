# MathJaxしたい（`MathJax`）

```html
<script id="MathJax-script" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
```

MathJaxは、ウェブページ上でTeX記法の数式をきれいに表示するためのライブラリです。

`\(...\)`や`$$...$$`のように書いた数式を、読み込み時にブラウザ上で組版します。
サーバー側の処理は不要で、JavaScriptを読み込むだけで動きます。

同じ用途のKaTeXより対応しているTeXコマンドが多いのが特長です。
一方で、表示はKaTeXより遅めです。

## 読み込みたい

```html
<script id="MathJax-script" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
```

`tex-mml-chtml.js`は「TeX入力・MathML入力・HTML出力」がすべて入った構成です。
まずはこれを読み込めば動きます。

`async`を付けると、読み込みが終わった時点で`<body>`全体を自動で組版します。
`id="MathJax-script"`は、MathJaxが自身の設定を探すときの目印です。

用途にあわせて、より軽い構成も選べます。

| ファイル | 構成 |
| --- | --- |
| `tex-mml-chtml.js` | TeX + MathML 入力、HTML 出力（全部入り） |
| `tex-chtml.js` | TeX 入力のみ、HTML 出力 |
| `tex-svg.js` | TeX 入力のみ、SVG 出力 |

## 数式を書きたい

```html
<p>ピタゴラスの定理は \( a^2 + b^2 = c^2 \) です。</p>

<p>解の公式:</p>
\[ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \]
```

MathJax 3の既定の区切り記号は次のとおりです。

- `\(...\)` … 文中に埋め込むインライン数式
- `\[...\]`、`$$...$$` … 独立した行に中央寄せで表示するディスプレイ数式

インラインの`$...$`は、通貨記号との衝突を避けるため既定では無効です。

## `$...$`を有効にしたい

```html
<script>
    window.MathJax = {
        tex: {
            inlineMath: [["$", "$"], ["\\(", "\\)"]]
        }
    };
</script>
<script id="MathJax-script" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
```

`window.MathJax`に設定を代入してから本体を読み込みます。
設定の`<script>`は、かならず本体スクリプトより**前**に置きます。

`tex.inlineMath`に`["$", "$"]`を加えると、`$...$`をインライン数式として扱います。

## LaTeXパッケージを使いたい（`tex.packages`）

MathJaxは`.sty`ファイルそのものは読み込めませんが、
主要なLaTeXパッケージの機能をTeX拡張として持っています。
`\usepackage`のかわりに、`loader.load`で取得し、`tex.packages`の`[+]`に追加します。

```html
<script>
    window.MathJax = {
        loader: {
            load: ["[tex]/physics", "[tex]/mhchem", "[tex]/mathtools"]
        },
        tex: {
            packages: { "[+]": ["physics", "mhchem", "mathtools"] }
        }
    };
</script>
<script id="MathJax-script" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
```

よく使う拡張と、相当するLaTeXパッケージは次のとおりです。

| 拡張 | 相当するパッケージ | 例 | 既定 |
| --- | --- | --- | --- |
| `ams` | `amsmath` / `amssymb` | `align`、`\text`、`\mathbb` | 有効 |
| `newcommand` | （`\newcommand`） | `\newcommand{\R}{\mathbb{R}}` | 有効 |
| `physics` | `physics` | `\dv{f}{x}`、`\bra{\psi}` | 追加 |
| `mhchem` | `mhchem` | `\ce{H2O}`、`\pu{22.4 L}` | 追加 |
| `mathtools` | `mathtools` | `\coloneqq`、`\prescript` | 追加 |
| `cancel` | `cancel` | `\cancel{x}`、`\cancelto{0}{x}` | 追加 |
| `color` | `color` | `\color{red}{x}` | 有効 |
| `boldsymbol` | `bm` | `\boldsymbol{\alpha}` | 追加 |

`[+]`は「既定の拡張リストに追加する」という意味の指定です。

## ページ内で読み込みたい（`\require`）

```html
<p>電場は \(\require{physics} \grad V\) で表せます。</p>
```

`\require{拡張名}`を数式の中に書くと、その拡張をその場で読み込めます。
設定を書き換えられないページや、特定のページだけで拡張が必要なときに使います。

`tex-mml-chtml.js`など`autoload`拡張を含む構成では、
`\ce{...}`や`\dv{...}`のような拡張のコマンドを書くだけで自動的に読み込まれることもあります。

## あとから追加した数式を描画したい（`typesetPromise`）

```html
<div id="target"></div>

<script>
    document.getElementById("target").innerHTML = "\\( \\sqrt{2} \\)";
    MathJax.typesetPromise([document.getElementById("target")]);
</script>
```

`async`による自動組版は最初の読み込み時に一度だけ動きます。
JavaScriptであとから数式を追加したときは、`MathJax.typesetPromise(要素の配列)`を呼んで組版し直します。

- 引数を省略すると、ページ全体を対象にします
- 同期版の`MathJax.typeset()`もありますが、通常は`typesetPromise`を使います

## リファレンス

- [MathJax Documentation](https://docs.mathjax.org/en/latest/)
- [Getting Started with Components](https://docs.mathjax.org/en/latest/web/start.html)
- [Configuring and Loading MathJax](https://docs.mathjax.org/en/latest/web/configuration.html)
- [Typesetting Dynamic Content](https://docs.mathjax.org/en/latest/web/typeset.html)
