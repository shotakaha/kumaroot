# ページの種類を確認したい（`.Kind`）

```go
{{ .Kind }}
```

Hugoは`/content/`以下のファイル構成から、ページの「種類（Kind）」を自動的に判定します。
`.Kind`や`.IsHome`などの変数を使うと、テンプレート内でページの種類ごとに表示を出し分けられます。

```go
{{ if .IsHome }}
  <p>ここはトップページです</p>
{{ else if .IsSection }}
  <p>ここは一覧ページです</p>
{{ else }}
  <p>ここは記事ページです</p>
{{ end }}
```

`_default/list.html`や`_default/single.html`のような共通テンプレートの中で、
ページの種類に応じて表示を切り替えたいときに使います。

## 種類の一覧を確認したい

| ページ階層 | コンテンツ | テンプレート | パーマリンク | `.Kind` | `.IsHome` | `.IsNode` | `.IsPage` | `.IsSection` |
|---|---|---|---|---|---|---|---|---|
| トップページ | `/content/_index.md` | `/layouts/index.html` | `/` | `home` | `true` | `true` | `false` | `false` |
| カスタム404 | | `/layouts/404.html` | `/404.html` | `404` | `false` | `false` | `false` | `false` |
| セクション | `/content/sec/_index.md` | `/layouts/_default/list.html` | `/sec/` | `section` | `false` | `true` | `false` | `true` |
| サブセクション | `/content/sec/sub/_index.md` | `/layouts/_default/list.html` | `/sec/sub/` | `section` | `false` | `true` | `false` | `true` |
| 記事リスト | `/content/posts/_index.md` | `/layouts/_default/list.html` | `/posts/` | `section` | `false` | `true` | `false` | `true` |
| 記事 | `/content/posts/first_post.md` | `/layouts/_default/single.html` | `/posts/first_post/` | `page` | `false` | `false` | `true` | `false` |
| 記事 | `/content/posts/release/awesome_release.md` | `/layouts/_default/single.html` | `/posts/release/awesome_release/` | `page` | `false` | `false` | `true` | `false` |
| タクソノミー名 | (frontmatter) | `/layouts/_default/taxonomy.html` | `/tags/` | `taxonomy` | `false` | `true` | `false` | `false` |
| タクソノミー | (frontmatter) | `/layouts/_default/term.html` | `/tags/タグ名/` | `term` | `false` | `true` | `false` | `false` |

`.Kind`はページの種類を表す文字列を返します。
`.IsHome`・`.IsNode`・`.IsSection`・`.IsPage`は、それぞれ真偽値を返す便利変数です。

:::{note}

`.IsNode`は「一覧系のページ（記事そのものではないページ）」で`true`になります。
トップページ・セクション・タクソノミーは`.IsNode`が`true`ですが、
404ページだけは`.IsNode`も`.IsPage`も`false`になる特殊なケースです。

:::

## リファレンス

- [Page Variables](https://gohugo.io/variables/page/)
- [.Kind](https://gohugo.io/methods/page/kind/)
- [.IsHome](https://gohugo.io/methods/page/ishome/)
- [.IsNode](https://gohugo.io/methods/page/isnode/)
- [.IsSection](https://gohugo.io/methods/page/issection/)
- [.IsPage](https://gohugo.io/methods/page/ispage/)
- [Glossary: page kind](https://gohugo.io/quick-reference/glossary/#page-kind)
