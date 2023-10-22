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
