# 多言語サイトしたい（``.Site.Languages``）

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

Hugoはデフォルトで[多言語サイト](https://gohugo.io/content-management/multilingual/)に対応できます。

全体設定でデフォルトの言語と言語別サブディレクトリの設定を定義します。
デフォルトの言語は``en``（英語）です。

サイトで使用する言語の設定は``[languages]``セクションで定義します。
日本語は``[languages.ja]``、フランス語は``[languages.fr]``で設定できます。
言語ごとの詳細設定は、それぞれの言語セクションの中で定義します。
``languageCode``は[RFC5646](https://datatracker.ietf.org/doc/html/rfc5646)で定義されている言語コードをすべて小文字で設定します

## 多言語コンテンツを作成したい

Hugoでは、ファイル名を基準にした方法と、サブディレクトリ名を基準にした方法で多言語に対応するコンテンツを管理できます。
どちらを選択するかは、作成する用途に合わせて決めることになると思います。
それぞれに一長一短あると思いますが、混ぜるのは危険です（たぶん）。



### ファイル名で管理したい

全体設定に追記することはとくにありません。
コンテンツファイルの名前を以下のように``{ファイル名}.{言語名}.md``にします。
``{言語名}``を省略した場合は、デフォルトの言語に設定されます。

```console
/content/about.ja.md  # {BaseURL}/ja/about/
/content/about.en.md  # {BaseURL}/en/about/
```

とくに理由がなければ、多言語コンテンツのファイル名は揃えるとよいです。
これらは、自動で言語スイッチャーに登録されます。
ファイル名が異なる場合でも、frontmatterで同じ``translationKey``を設定することで、異なる言語間の関係を張ることができます。

### サブディレクトリ名で管理したい（``contentDir``）

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

言語ごとの詳細設定で``contentDir``を指定します。
コンテンツ数が多くなる場合は、こちらの方法がよいかもしれません。

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
