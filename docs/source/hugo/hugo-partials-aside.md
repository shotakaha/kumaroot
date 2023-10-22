# サイドバーしたい（``/layouts/partials/aside.html``）

```html
{{ define "aside" }}
<div>
    <!-- 年別アーカイブ -->
</div>

<div>
    <!-- カテゴリ別アーカイブ -->
</div>

<div>
    <!-- タグクラウド -->
</div>
{{ end }}
```

サイドバーはメインコンテンツではないので[asideタグ](https://developer.mozilla.org/ja/docs/Web/HTML/Element/aside)の中に書くことにします。

サイドバーは、サイト全体で共通しているほうがUXがよいと思いますが、
記事用と固定ページ用で変更するのもアリだと思います。

:::{todo}

- ``/layouts/partials/page-aside.html``
- ``/layouts/partials/post-aside.html``

:::

## 年別アーカイブ

```html
{{ range .Pages.GroupByDate "2006-01" }}
<h3>{{ .Key }}</h3>
<ul>
    {{ range .Pages }}
    <li>{{ .Title }}</li>
    {{ end }}
</ul>
{{ end }}
```


[Group機能](https://gohugo.io/templates/lists/#group-content)を使うとできそうです。
