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

## ブロックテンプレートしたい

```html
{{ block "main" . }}
<!-- デフォルトのテンプレートを書くことができます -->
<p>メインブロックが定義されていません。</p>
<p>以下のテンプレートを追加することを検討してください。</p>
<ul>
    <li>ページ用テンプレート: <code>/layouts/_default/single.html</code></li>
    <li>リスト用テンプレート: <code>/layouts/_default/list.html</code></li>
</ul>
{{ end }}
```

ベーステンプレート（``baseof.html``）の中で[ブロックテンプレート機能](https://gohugo.io/templates/base/)を利用できます。
テンプレートの種類によって変えたい部分だけをブロックテンプレートに置き換えることで、テンプレートのメンテナンスコストを減らします。

上記のサンプルでは、メインコンテンツに相当する部分を``{{ define "main" }}``と定義しておき、表示内容は[ページ用テンプレート](./hugo-layouts-single.md)と[リスト用テンプレート](./hugo-layouts-list.md)でそれぞれで上書きすることを想定しています。