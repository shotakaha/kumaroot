# 一覧ページしたい（``/layouts/_default/list.html``）

```html
{{ define "main" }}
<section class="list>
    <!-- リストのタイトル -->
    <div>
        {{ range (.Paginate .RegularPages).Pages.ByLastmod.Reverse }}
            {{ partial "article-card" . }}
        {{ end }}
    </div>
</section>
{{ end }}
```
