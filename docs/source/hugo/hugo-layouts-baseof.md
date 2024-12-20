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

``hugo new theme``コマンドで作成されるスケルトンを使って、
テンプレートをカスタマイズできます。
すべてのページに共通する骨格というべきテンプレートは
{file}`/layouts/_default/baseof.html`で定義します。
HTMLタグはセマンティックに沿って並べるのがよいと思います。

ベースとなるこのテンプレートでは
ブロックテンプレートや部分テンプレートを読み込み、
なるべく**具体的に書かない**ことが重要だと思います。

## 表示言語したい（`lang` / `dir`）

```html
<html lang="{{ or site.Language.LanguageCode site.Language.Lang }}"
      dir="{{ or site.Language.LanguageDirection 'ltr' }}">
<head>
```

ページの[lang属性](https://developer.mozilla.org/ja/docs/Web/HTML/Global_attributes/lang)にはウェブサイトに書かれている言語、
もしくはユーザーが入力すべき言語を設定します。
デフォルト値は``unknown``なので、適切な値を指定することが推奨されています。

[多言語サイトの設定](./hugo-config-languages.md)で定義した、サイト全体の言語コードを指定します。

## ブロックテンプレートしたい

```html
{{ define "main" . }}
<!-- デフォルトのテンプレートを書くことができます -->
<p>メインブロックが定義されていません。</p>
<p>以下のテンプレートを追加することを検討してください。</p>
<ul>
  <li>ページ用テンプレート: <code>/layouts/_default/single.html</code></li>
  <li>リスト用テンプレート: <code>/layouts/_default/list.html</code></li>
</ul>
{{ end }}
```

ベーステンプレートの中に**ブロックテンプレート機能**を埋め込んでおきます。
ブロックテンプレートは、いわばプレースホルダーのようなもので、
テンプレートの種類によってカスタマイズしたい部分だけを置き換えることができます。

上記のサンプルでは、メインコンテンツに相当する部分を``{{ define "main" }}``と定義しておき、
表示内容は[ページ用テンプレート](./hugo-layouts-single.md)と[リスト用テンプレート](./hugo-layouts-list.md)でそれぞれで上書きすることを想定しています。

## リファレンス

- [Base templates](https://gohugo.io/templates/base/)
-
