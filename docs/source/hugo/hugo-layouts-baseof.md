# 骨組みしたい（``/layouts/_default/baseof.html``）

```html
<!doctype html>
<html lang="言語コード">
    <head>
        {{ partials "head" .}}
    </head>
    <body>
        <header>
            <!-- ロゴ -->
            <!-- ナビゲーション -->
            <!-- 検索窓 -->
            <!-- 言語切り替え -->
            {{ partials "header . }}
        </header>
        <main>
            {{ block "main" . }}
            <!-- メインコンテンツ -->
            {{ end }}
        <aside>
            {{ block "aside" }}
            <!-- サイドバー -->
            {{ end }}
        </side>
        </main>
        <footer>
            {{ block "footer" }}
            <!-- フッター -->
            {{ end }}
        </footer>
    </body>
    <!-- JSを読み込む -->
</html>
```

{file}`/layouts/_default/baseof.html`ですべてのページの骨格を定義します。
HTMLタグのセマンティックに沿って並べるのがよいと思います。
サイト内のすべてのページに共通するパーツなので、具体的に**書かない**ことが大事です。

### 部分テンプレート

すべてに共通するパーツは[部分テンプレート機能](https://gohugo.io/templates/partials/)を使うことで、テンプレート制作にかかる手間を削減できます。

### ブロックテンプレート

テンプレートの種類によって変えたいパーツは[ブロックテンプレート機能](https://gohugo.io/templates/base/)を使うとよいです。
メインコンテンツに相当する部分は``{{ define "main" }}``と定義し、**記事**などの[単体テンプレート](./hugo-layouts-single.md)や、**記事一覧**などの[一覧テンプレート](./hugo-layouts-list.md)で上書きするとよいと思います。
