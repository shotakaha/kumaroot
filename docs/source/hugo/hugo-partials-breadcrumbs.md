# パンくずしたい（``/layouts/partials/breadcrumbs.html``）

```html
<nav>
    <ul>
        {{- range .Ancestors.Reverse }}
        <li><a href="{{ .RelPermalink }}">{{ .LinkTitle }}</a></li> /
        {{- end }}
        <li>{{ .LinkTitle }}</li>
    </ul>
</nav>
```

```html
<nav>
    <ul>
        <li><a href="URL">親の親ページのタイトル</a></li> /
        <li><a href="URL">親ページのタイトル</a></li> /
        <li>現在ページのタイトル</li>
    </ul>
</nav>
```

[Hugo Codexのブログ記事](https://hugocodex.org/blog/breadcrumbs-since-1-09/)にあったコードを拝借しました。
[Hugo v0.109のリリース](https://github.com/gohugoio/hugo/releases/tag/v0.109.0)で``.Ancestors``が追加され、パンくずリストの作成が簡単になったそうです。

``.Ancestors``は現在のページからトップページまで遡ったページ情報が順番に格納されるページ変数です。
``.Ancestors.Reverse``で逆順にすることで、いわゆる「パンくずリスト」の順番でページを取り出しています。
