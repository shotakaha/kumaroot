# 多言語サイトしたい

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
