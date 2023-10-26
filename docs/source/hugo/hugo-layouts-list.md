# 一覧ページしたい（``/layouts/_default/list.html``）

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
