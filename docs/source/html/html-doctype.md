# HTMLしたい（`doctype`）

```html
<!DOCTYPE html>
<html lang="表示言語">
    <head>
        <meta charset="utf-8">
        <title>ページタイトル | ウェブサイト名</title>
    </head>
    <body>
        <nav>
            ナビゲーション
        </nav>
        <main>
            メインコンテンツ
        </main>
        <footer>
            フッター
        </footer>
    </body>
</html>
```

HTMLの基本的な骨格です。
ここにある各ブロックに、それぞれに適したコンテンツを追加します。
ウェブサイトの見た目は、別ファイルに記述したCSSを使ってデコっていきます。

先頭の`<!DOCTYPE html>`は、この文書がHTML5で書かれていることをブラウザに伝える宣言です。
昔のHTMLではDTD（文書型定義）を指定する長い記述が必要でしたが、HTML5ではこの短い1行だけで済みます。
ブラウザが正しいレンダリングモードで描画するために必要なので、文書の先頭に必ず書いておきます。

## HTML5したい

```html
<!DOCTYPE html>
```

HTML5のDOCTYPE宣言です。
DTDを指定する必要がなくなり、この1行だけで済むようになりました。
特別な理由がなければ、新規に作成するHTML文書はこの宣言を使います。

## HTML4したい

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
    "http://www.w3.org/TR/html4/strict.dtd">
```

HTML4.01 StrictのDOCTYPE宣言です。
非推奨要素（`font`タグなど）やスタイル関連の属性を使わない、厳格な文書向けです。

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
```

HTML4.01 TransitionalのDOCTYPE宣言です。
非推奨要素や属性の使用を許容する、移行期向けの緩い仕様です。

:::{note}

どちらもDTDのURLを含む長い記述が必要で、HTML5に比べて書き間違えやすいです。
現在新規にHTML文書を作成する場合は、HTML5を使うのがよいです。

:::

## リファレンス

- [Doctype](https://developer.mozilla.org/ja/docs/Glossary/Doctype)
