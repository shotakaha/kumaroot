# ハイパーリンクしたい（`a`）

```html
<a href="リンク先のURL">リンクテキスト</a>
```

`a`タグは、ハイパーリンクを表示するタグです。
`href`属性にリンク先のURLを指定します。
内部ページへのリンクは相対パスで指定することもできます。

## 外部リンクしたい（`rel="noopener noreferrer"`）

```html
<a target="_blank" rel="noopener noreferrer" href="外部サイトのURL">
```

`rel`属性には現在の文書とリンク先の関係を記述します。
外部サイトにリンクする際は、上のような属性を追加します。

`rel="noopener"`は、新しく開いたページから`window.opener`経由で元のページを操作できないようにする値です。
これにより、開いた側が元のページを不正なサイトへ誘導する（タブナビング）攻撃を防げます。
`rel="noreferrer"`は、新しく開いたページに現在のページのリファラー情報を渡さないようにする値です。

内部サイトへ、自分で管理しているサイトへのリンクであればこれらの設定はなくてもOKです。

:::{note}

`rel`属性に設定する値は`noreferrer`です。
HTTPリクエストヘッダーのフィールド名は`Referer`です。
スペルミスがそのまま標準化されてしまったそうです。

:::

:::{note}

最近のブラウザでは`target="_blank"`は自動的に`noopener`相当の挙動になるため、
省略しても`window.opener`経由の操作はできません。
とはいえ古いブラウザとの互換性や、意図を明確にする意味でも明示しておくのが安全です。
なお`noreferrer`（リファラーを送らない）はこの自動適用の対象外なので、必要な場合は明示する必要があります。

:::

## 別タブしたい（`target`）

```html
<a target="_blank" href="...">
```

`target`属性でリンク先のURLを表示する場所を変更できます。
`target="_blank"`属性は、リンクをクリックすると別タブ（or別ウィンドウ）で開くようにします。

- `target="_self"`: 現在のページ（デフォルト）
- `target="_blank"`: 新しいタブ
- `target="_parent"`: 親コンテキスト
- `target="_top"`: 最上位の親コンテキスト

`target="_blank"`を使うときは、上記の「外部リンクしたい」で紹介した`rel="noopener noreferrer"`もあわせて指定しておきましょう。

## リファラーしたい（`referrerpolicy`）

`referrerpolicy`で、リンクをたどるときにリファラーを送信するか設定できます。
以前は`rel`属性でリファラーを動作を設定していましたが、
いつの間にか新しい属性ができていました。

- `referrerpolicy="no-referrer"`: リファラーを送信しない
- `referrerpolicy="origin"`: 参照元ページのオリジンのみに限定してリファラーを送信

## ページャーしたい（`rel="prev"` / `rel="next"`）

```html
<a rel="prev" href="...">前のページ</a>
<a rel="next" href="...">次のページ</a>
```

`rel`属性には現在の文書とリンク先の関係を記述します。
前後のページへのリンクを設定する場合は、`prev`と`next`を指定します。

```html
<a rel="alternate" href="...">代替ページ</a>
<a rel="help" href="...">ヘルプページ</a>
<a rel="license" href=".../license/">MITライセンス</a>
```

他にも、リンク先の関係を表す値がいくつかあります。

## CSSしたい（`a`）

```css
a {
    color: #0066cc;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

a[target="_blank"]::after {
    content: " ↗";
}
```

ブラウザのデフォルトの下線付きリンクは好みが分かれます。
`text-decoration: none`で消しつつ、
`:hover`時だけ下線を表示するのが定番です。
下線を常に消したままにする場合は、地の文と見分けがつくよう色のコントラストを十分につけましょう。

`a[target="_blank"]`のように属性セレクターを使うと、
別タブで開くリンクだけにアイコンを自動で付けられます。
このページの`target`属性の話と組み合わせて使えるテクニックです。

## リファレンス

- [aタグ（アンカー要素）](https://developer.mozilla.org/ja/docs/Web/HTML/Element/a)
- [HTML属性: rel](https://developer.mozilla.org/ja/docs/Web/HTML/Attributes/rel)
