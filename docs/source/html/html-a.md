# ハイパーリンクしたい（`a`）

```html
<a target="_blank" rel="noopener noreferrer" href="外部サイトのURL">
```

`a`タグで別のURLへのリンクを作成できます。
`href`属性にハイパーリンク先のURLを指定します。
外部サイトにリンクする際は、上のような属性を追加します。

`rel="noopener"`属性は、新しく開いたページから`window.opener`経由で元のページを操作できないようにします。
これにより、開いた側が元のページを不正なサイトへ誘導する（タブナビング）攻撃を防げます。
`rel="noreferrer"`属性は、新しく開いたページに現在のページのリファラー情報を渡さないようにします。

内部サイトへ、自分で管理しているサイトへのリンクであればこれらの設定はなくてもOKです。

:::{note}

`rel`属性に設定する値は`noreferrer`です。
HTTPリクエストヘッダーのフィールド名は`Referer`です。
スペルミスがそのまま標準化されてしまったそうです。

:::

## 別タブしたい（`target`）

```html
<a target="_blank" rel="noopener noreferrer" href="...">
```

`target`属性でリンク先のURLを表示する場所を変更できます。
`target="_blank"`属性は、リンクをクリックすると別タブ（or別ウィンドウ）で開くようにします。

- `target="_self"`: 現在のページ（デフォルト）
- `target="_blank"`: 新しいタブ
- `target="_parent"`: 親コンテキスト
- `target="_top"`: 最上位の親コンテキスト

`target="_blank"`を使うときは、`rel="noopener"`もあわせて指定しておきましょう。
省略すると、開いた先のページから元のページを操作できてしまいます。

## リファラーしたい（`referrerpolicy`）

`referrerpolicy`で、リンクをたどるときにリファラーを送信するか設定できます。
以前は`rel`属性でリファラーを動作を設定していましたが、
いつの間にか新しい属性ができていました。

- `referrerpolicy="no-referrer"`: リファラーを送信しない
- `referrerpolicy="origin"`: 参照元ページのオリジンのみに限定してリファラーを送信

## relしたい（`rel`）

```html
<a rel="alternate" href="...">代替ページ</a>
<a rel="help" href="...">ヘルプページ</a>
<a rel="license" href=".../license/">MITライセンス</a>
<a rel="prev" href="...">前のページ</a>
<a rel="next" href="...">次のページ</a>
```


`rel`属性で、現在の文書とリンク先の関係を定義できます。

## リファレンス

- [aタグ（アンカー要素）](https://developer.mozilla.org/ja/docs/Web/HTML/Element/a)
- [HTML属性: rel](https://developer.mozilla.org/ja/docs/Web/HTML/Attributes/rel)
