# 骨組みしたい（``/layouts/_default/baseof.html``）

```html
<!DOCTYPE html>
<html lang="{{ or site.Language.LanguageCode site.Language.Lang }}"
      dir="{{ or site.Language.LanguageDirection `ltr` }}">
<head>
  {{ partial "head.html" . }}
</head>
<body>
  <header>
    {{ partial "header.html" . }}
  </header>
  <main>
    {{ block "main" . }}{{ end }}
  </main>
  <footer>
    {{ partial "footer.html" . }}
  </footer>
</body>
</html>

```

``hugo new theme``コマンドで作成されるスケルトンを使って、独自のテンプレートを設計できます。
{file}`/layouts/_default/baseof.html`は、すべてのページに共通する骨格を定義するテンプレートです。
なるべく**具体的に書かない**ことが大事です。
HTMLタグのセマンティックに沿って並べるのがよいと思います。

## 表示言語の設定（``lang属性``）

[lang属性](https://developer.mozilla.org/ja/docs/Web/HTML/Global_attributes/lang)には、ウェブサイトに書かれている言語、もしくはユーザーが入力すべき言語を設定します。デフォルト値は``unknown``なので、適切な値を指定することが推奨されています。

[多言語サイトの設定](./hugo-config-languages.md)に書いたように全体設定で``languageCode``を指定します。

## 部分テンプレートしたい

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
