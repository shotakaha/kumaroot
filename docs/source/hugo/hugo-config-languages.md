# 多言語サイトしたい（``.Site.Languages``）

Hugoはデフォルトで[多言語サイト](https://gohugo.io/content-management/multilingual/)に対応できます。

```toml
defaultContentLanguage = "ja"
defaultContentLanguageInSubdir = true

[languages]
  [languages.ja]
    languageCode = "ja"
    languageName = "日本語"
    title = "日本語のサイト名"
    weight = 0
  [languages.en]
    languageCode = "en"
    languageName = "English"
    title = "英語のサイト名"
    weight = 10
```

[RFC5646](https://datatracker.ietf.org/doc/html/rfc5646)で定義されている言語コードを設定できます。
デフォルトは``en``（英語）です。
日本語は``ja``で設定できます。

## 多言語コンテンツを作成したい

{file}`content/_index.ja.md`のように``{ファイル名}.{言語名}.md``で言語別のコンテンツを作成できます。
言語名を省略した場合は、デフォルトの言語に設定されます。

言語ごとに``contentDir``を設定し、言語別にサブディレクトリを作成して運用することもできます。
コンテンツ数が多くなる場合は、こちらの方法がよいかもしれません。

```toml
[languages]
  [languages.ja]
    languageCode = "ja"
    languageName = "日本語"
    title = "日本語のサイト名"
    contentDir = "content/ja"
    weight = 0
  [languages.en]
    disabled = false
    languageCode = "en"
    languageDirection = "ltr"
    languageName = "English"
    title = "英語のサイト名"
    contentDir = "content/en"
    weight = 10
```

## 言語ごとの切り替え

```console
/content/about.ja.md  # {BaseURL}/ja/about/
/content/about.en.md  # {BaseURL}/en/about/
```

多言語コンテンツを作成する場合は、ファイル名を揃えるとよいです。
これらは、自動で言語スイッチャーに登録されます。

ファイル名が異なる場合でもfrontmatterで同じ``translationKey``に設定することで、言語間の関係を張ることができます。

## 翻訳ページを表示したい

```html
{{ if .IsTranslated }}
<h4>{{ i18n "translations" }}<h4>
<ul>
    {{ range .Translations }}
    <li>
        <a href="{{ .Permalink }}">{{ .Lang }}: {{ .Title }}{{ if .IsPage }}({{ i18n "wordCount" . }}){{ end }}</a>
    </li>
    {{ end }}
</ul>
{{ end }}
```

上記サンプルは[公式ページからの写経](https://gohugo.io/content-management/multilingual/#reference-translated-content)です。
``.IsTranslated``で翻訳コンテンツがあるかを確認して、順序なしリスト（``ul``）で表示します。

翻訳コンテンツは``{{ .Translations }}``に格納されています。
``{{ range .Translations }}...{{ end }}``で、関連する翻訳コンテンツ（のオブジェクト）をループし、
それぞれのコンテンツのURL（``{{ .Permalink }}``）、言語名（``{{ .Lang }}``）、ページのタイトル（``{{ .Title }}``）を取り出して表示します。
ページ型（``.IsPage``）の場合は、さらに本文の文字数（``{{ .wordCount }}``）も表示します。
