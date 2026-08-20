# 単体ページしたい（`/layouts/_default/single.html`）

```html
{{ define "main" }}
  <h1>{{ .Title }}</h1>

  {{ $dateMachine := .Date | time.Format "2006-01-02T15:04:05-07:00" }}
  {{ $dateHuman := .Date | time.Format ":date_long" }}
  <time datetime="{{ $dateMachine }}">{{ $dateHuman }}</time>

  {{ .Content }}
  {{ partial "terms.html" (dict "taxonomy" "tags" "page" .) }}
{{ end }}
```

```html
{{ define "main" }}
<section>
    <article>
        <div>
            <!-- カテゴリー名（ひとつ） -->
            <!-- ページのタイトル -->
            <!-- ページの公開日 -->
            <!-- タグ名（複数） -->
            <!-- 下書きの表示 -->
            <!-- 内容を読むのにかかる時間 -->
            <!-- ページの文字数 -->
        </div>
        <div>
            <!-- SNSボタン -->
        </div>
        <div>
            <!--  カバー画像 -->
        </div>
        <div>
            <!-- 本文 -->
        </div>
    </article>

    <div>
        <!-- 関連ページのリスト -->
    </div>

    <div>
        <!-- 関連サイトのリスト -->
    </div>

    <div>
        <!-- 前のページ -->
        <!-- 次のページ -->
    </div>
</section>
{{ end }}
```

単体ページで適用されるテンプレートです。
[ベーステンプレート](./hugo-layouts-baseof.md)で定義した`main`ブロック（`{{ define "main" }}`）の中身を書いたサンプルです。

## タイトルを表示したい

```go
<h1 class="page-title">{{- .Title -}}</h1>
```

```html
<h1 class="page-title">ページのタイトル</h1>
```

ページのタイトルは`h1`タグで表示します。
クラス名は、利用するCSSフレームワークなどに合わせて適当につけておきます。

## 公開日を表示したい

```go
<time class="datetime" {{ printf `datetime="%s"` (.Date.Format "2006-01-02T15:04:05Z07:00") | safeHTMLAttr }} >
    {{- .Date | time.Format (default "2006-01-02" .Site.Params.date_format) -}}
</time>
```

```html
<time class="datetime" datetime="2023-10-22T10:30:00+09:00">2023-10-22</time>
```

日時や時刻を表示するための[timeタグ](https://developer.mozilla.org/ja/docs/Web/HTML/Element/time)を使います。
`datetime`属性を使って検索エンジンが理解しやすいようにしておきます。

Hugoの日付に関係するページ変数は、`.Date`、`.PublishDate`、`.Lastmod`、`.ExpiryDate`の4種類あります。それぞれの変数のfrontmatter変数との紐付けは[カスタマイズ](https://gohugo.io/getting-started/configuration/#configure-dates)できます。

:::{note}

Hugo（というかGoテンプレート言語）の日付フォーマットはなかなか初見殺しだと思います。
よくある`YYYY-MM-DD HH:MM:SS`のような書式指定子ではなく、`2006-01-02 15:04:05`という具体的な日時そのもの（Goのリファレンス時刻）で書式を表現します。
Hugoを使い始めたころ、この日付にフォーマット指定の意味があると思わず、日付フォーマットが反映されないなぁ？としばらくハマりしました。
フォーマット指定の詳細は[Go言語のソースコード](https://github.com/golang/go/blob/master/src/time/format.go)を確認してください。

:::

## 下書きを表示したい

```html
{{ if .Draft}}
<span class="draft_mode">下書き</span>
<span class="draft_mode">{{ i18n "draft_mode" }}</span>
{{ end }}
```

`.Draft`のページ変数でページの状態を指定できます。
既存のテーマではあまり見当たらないのですが、下書き状態であることが一目でわかると便利だと思います。
多言語サイトの場合は、言語ごとに表記を変更できるようにしておくのもよいと思います。

## カテゴリーを表示したい

```html
<span class="category">🗂️ {{ .Section }}</span>
```

```html
<span class="category">🗂️ posts</span>
```

`.Section`でページが属するトップレベルのセクション名（＝ディレクトリ名）を取得できます。

## タグを表示したい

```html
<span class="tags">
    <ul class="tags">
        {{ range .Params.tags }}
        <li class="tag"><a href="{{ "/tags/" | relURL }}{{ . | urlize }}/">🏷️ {{ . }}</a></li>
        {{ end }}
    </ul>
</span>
```

```html
<span class="tags">
    <ul class="tags">
        <li class="tag"><a href="/tags/hugo/">🏷️ hugo</a></li>
        <li class="tag"><a href="/tags/static-site/">🏷️ static-site</a></li>
    </ul>
</span>
```

フロントマターの`tags`は複数指定できるので、`.Params.tags`を`range`で反復して一覧表示します。

:::{hint}

「カテゴリー」と「タグ」の使い分けに関する、個人的な見解です。

カテゴリーは🗂️フォルダ分けと同じなので、記事に対してひとつだけ、
タグは🏷️ラベル付けと同じなので、記事に対して複数設定できる、というように使い分けています。

Hugoのタクソノミー機能には「ひとつだけ」に制限する機能はないため、
カテゴリーは「セクション」（＝ディレクトリ名）、
タグは「タクソノミー」で設定するように設計するのがよいと考えています。

:::

## 本文したい

```html
<article>
    <h1>{{ .Title }}</h1>
    {{ .Content }}
</article>

{{ range .Page.Resources }}
<article>
    <h2>{{ .Title }}</h2>
    {{ .Content }}
</article>
{{ end }}
```

`.Content`で本文を表示します。
[Leaf Bundle](https://gohugo.io/content-management/page-bundles/#leaf-bundles)（同じディレクトリに複数のMarkdownファイルをまとめたページ構成）を使っている場合は、
`.Page.Resources`で同じバンドル内の他のページリソースも合わせて表示できます。

## リファレンス

- [.Title](https://gohugo.io/methods/page/title/)
- [.Date](https://gohugo.io/methods/page/date/)
- [.Draft](https://gohugo.io/methods/page/draft/)
- [.Section](https://gohugo.io/methods/page/section/)
- [.Params](https://gohugo.io/methods/page/params/)
- [.Content](https://gohugo.io/methods/page/content/)
- [.Resources](https://gohugo.io/methods/page/resources/)
- [Page Bundles](https://gohugo.io/content-management/page-bundles/)
