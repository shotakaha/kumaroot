# Google Analyticsしたい

```toml
[services]
[services.googleAnalytics]
ID = "G-測定ID"
```

Hugoデフォルトの[内部テンプレート](https://gohugo.io/templates/internal/)を使う場合、
Google Analyticsの測定タグは``[services]``セクションで設定できます。

内部テンプレートを使っているかどうかは、利用するテーマのドキュメント（もしくはソースコード内を検索）を参照してください。

## 内部テンプレート

```go
{{ template "_internal/google_analytics.html" }}
```

## 自作テンプレート

```go
{{ $ga_id := site.Config.Services.GoogleAnalytics.ID }}
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-3VT4D8WRVL"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag("js", new Date());

  gtag("config", "{{ $ga_id }}");
</script>
```

測定IDの設定を自作する場合は、``{{ site.Config.Services.GoogleAnalytics.ID }}``で呼び出します。
これを応用すると、別の測定ツール（たとえば[Matomo](https://matomo.jp/)など）を組み込むことができます。

