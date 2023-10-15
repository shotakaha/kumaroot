# 骨組みしたい（``/layouts/_default/baseof.html``）

```html
<!doctype html>
<html lang="言語コード">
    <head>
        {{ partials "head" .}}
    </head>
    <body>
        <header>
        <!-- メニューなど -->
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

{file}`/layouts/_default/baseof.html`で外骨格を定義できます。
HTMLタグのセマンティックに沿って並べるのがよいと思います。

ウェブサイト内のすべてのページに共通するパーツなので、あまり具体的に**書かない**ことが大事です。
**記事**などの単体テンプレートや、**記事一覧**などの一覧テンプレートは、この骨組みから派生させて設計します。

すべてのテンプレートに共通するパーツは[部分テンプレート機能](https://gohugo.io/templates/partials/)を使うことで、制作にかかる手間を削減できます。
部分テンプレートの中で部分テンプレートを読み込むことができますが、テンプレート構造が把握しにくくなるのでオススメしません。

また、テンプレートごとに変えたいパーツは[ブロックテンプレート機能](https://gohugo.io/templates/base/)を使うことで、テンプレートごとに上書きできます。
