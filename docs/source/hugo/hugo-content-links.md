# リンクしたい（`{{% ref %}}` / `{{% relref %}}`）

- 本文

```markdown
詳細は[こちらの外部サイト](外部サイトURL)をご覧ください
```

- 出力

```html
詳細は<a href="外部サイトURL">こちらの外部サイト</a>をご覧ください
```

外部サイトのURLにリンクする場合は、通常のMarkdown記法でOKです。

## 内部ページしたい

- ショートコード

```go
{{% ref "ファイルのパス" %}}
{{% relref "ファイルのパス" %}}
```

- 本文

```markdown
詳細は[こちらのリンク]({{% relref "ファイルのパス" %}} "title属性")をご覧ください
```

サイト内のページにリンクする場合は、コンテンツ用のファイル名からパーマリンクを取得する必要があります。
そのために、ビルトインされている`{{< relref >}}`もしくは`{{< ref >}}`ショートコードを使います。

- `relref`: 該当するパーマリンクの相対パスを取得
- `ref`: 該当するパーマリンクの絶対パスを取得

## 他言語ページしたい

- ショートコード

```go
{{% relref path="ファイル名" lang="言語コード" %}}
```

- 本文

```markdown
関連する英語ページは[こちらのページ]({{% relref path="ファイル名" lang="言語コード" %}} "英語ページのタイトル")です。
```

## 設定したい

```toml
# hugo.toml
refLinkErrorLevel = "ERROR"
refLinksNotFoundURL = "リンク先が参照できなかったときに埋め込むURL"
```

`relref`や`ref`でリンク先が参照できなかった場合の挙動を設定できます。
リンクエラーが多い場合は、一時的に`WARNING`に変更してもよいかもしれません。

## リファレンス

- [Links and cross references](https://gohugo.io/content-management/cross-references/)
- [ref](https://gohugo.io/content-management/shortcodes/#ref)
- [relref](https://gohugo.io/content-management/shortcodes/#relref)
- [SHORTCODE.Ref OPTIONS](https://gohugo.io/methods/shortcode/ref/)
- [SHORTCODE.RelRef OPTIONS](https://gohugo.io/methods/shortcode/relref/)
