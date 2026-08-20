# 一覧ページしたい（`/layouts/_default/list.html`）

```html
{{ define "main" }}
  <h1>{{ .Title }}</h1>
  {{ .Content }}
  {{ range .Pages }}
    <h2><a href="{{ .RelPermalink }}">{{ .LinkTitle }}</a></h2>
    {{ .Summary }}
  {{ end }}
{{ end }}
```

セクションやタクソノミーなど、複数ページの一覧を表示するテンプレートです。
[ベーステンプレート](./hugo-layouts-baseof.md)で定義した`main`ブロック（`{{ define "main" }}`）の中身を書いたサンプルです。
`.Pages`で配下のページを取得し、`range`で反復してタイトルとサマリーを並べます。

## ページ送りしたい（`.Paginate`）

```html
{{ define "main" }}
<section class="list">
    <!-- リストのタイトル -->
    <div>
        {{ range (.Paginate .RegularPages).Pages.ByLastmod.Reverse }}
            {{ partial "article-card" . }}
        {{ end }}
    </div>
</section>
{{ end }}
```

`.Paginate`で一覧を指定件数ごとに分割できます。
分割件数は[`pagination`の設定](https://gohugo.io/configuration/pagination/)でサイト全体に対して指定します。

`.RegularPages`で子ページ（一覧ページ自身は除く）だけを取得し、
`.ByLastmod.Reverse`で更新日時の新しい順に並び替えています。
`{{ partial "article-card" . }}`は`/layouts/partials/article-card.html`を呼び出す部分テンプレートです。
記事1件分の表示を部分テンプレート側に切り出しておくと、一覧ページと関連記事など複数箇所で使い回せます。

## リファレンス

- [.Pages](https://gohugo.io/methods/page/pages/)
- [.RegularPages](https://gohugo.io/methods/page/regularpages/)
- [Pagination](https://gohugo.io/templates/pagination/)
- [.Paginate](https://gohugo.io/methods/page/paginate/)
- [.ByLastmod](https://gohugo.io/methods/pages/bylastmod/)
- [partial](https://gohugo.io/functions/partials/include/)
