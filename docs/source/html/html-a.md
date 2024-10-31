# ハイパーリンクしたい（`a`）

```html
<a target="_blank" rel="noopener noreferrer" href="外部サイトのURL">
```

`a`タグで別のURLへのリンクを作成できます。
`href`要素にハイパーリンク先のURLを指定します。
外部サイトにリンクする際は、上のような属性を追加します。

`rel="noopener"`属性は、新しく開いたページがブラウザ内の別プロセスで動くようにします。
いま開いているページと、ジャンプ先のサイトを切り離すことができ、セキュリティを高めることができるそうです。
`rel="noreferrer"`属性は、新しく開いたページに現在のページのリファラー情報を渡さないようにします。

これらの``rel``属性の設定は、SEO対策には寄与しないらしいです（真偽不明）。
内部サイトへ、自分で管理しているサイトへのリンクであればこれらの設定はなくてもOKです。

:::{note}

`rel`属性に設定する値は`noreferrer`です。
HTTPリクエストヘッダーのフィールド名は`Referer`です。
スペルミスがそのまま標準化されてしまったそうです。

:::

## 別タブしたい（`target`）

```html
<a target="_blank" href="...">
```

`target`属性でリンク先のURLを表示する場所を変更できます。
``target="_blank"``属性は、リンクをクリックすると別タブ（or別ウィンドウ）で開くようにします。

- `target="_self"`: 現在のページ（デフォルト）
- `target="_blank"`: 新しいタブ
- `target="_parent"`: 親コンテキスト
- `target="_top"`: 最上位の親コンテキスト

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
<a ref="license" href=".../license/">MITライセンス</a>
<a ref="prev" href="...">前のページ</a>
<a ref="next" href="...">次のページ</a>
```


`rel`属性で、現在の文書とリンク先の関係を定義できます。

## リファレンス

- [aタグ（アンカー要素）](https://developer.mozilla.org/ja/docs/Web/HTML/Element/a)
- [HTML属性: rel](https://developer.mozilla.org/ja/docs/Web/HTML/Attributes/rel)
