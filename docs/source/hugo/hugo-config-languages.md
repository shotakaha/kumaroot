# 言語設定したい（`[languages]`）

```toml
defaultContentLanguage = "ja"
defaultContentLanguageInSubdir = true

[languages]
[languages.ja]
  locale = "ja-JP"
  label = "日本語"
  title = "日本語のサイト名"
  weight = 0

[languages.en]
  locale = "en-US"
  label = "English"
  title = "英語のサイト名"
  weight = 10
```

Hugoはデフォルトで[多言語サイト](https://gohugo.io/content-management/multilingual/)に対応できます。

全体設定でデフォルトの言語と言語別サブディレクトリの設定を定義します。
デフォルトの言語は`en`（英語）です。

サイトで使用する言語の設定は`[languages]`セクションで定義します。
日本語は`[languages.ja]`、英語は`[languages.en]`のように、言語コードごとにサブセクションを作ります。
言語ごとの詳細設定は、それぞれの言語セクションの中で定義します。

:::{note}

以前は`languageCode`・`languageName`という設定キーでしたが、Hugo v0.158.0で非推奨になりました。
新しく書く場合は`locale`・`label`を使います。

:::

`locale`は[RFC5646](https://datatracker.ietf.org/doc/html/rfc5646)で定義されている言語コード（`ja-JP`、`en-US`など）を設定します。
他の言語を追加したい場合も同じ要領です。たとえばフランス語なら、次のセクションを追加します。

```toml
[languages.fr]
  locale = "fr-FR"
  label = "Français"
  title = "フランス語のサイト名"
  weight = 20
```

## 多言語コンテンツを作成したい

Hugoでは、ファイル名を基準にした方法と、サブディレクトリ名を基準にした方法で多言語に対応するコンテンツを管理できます。
どちらを選択するかは、作成する用途に合わせて決めることになると思います。
それぞれに一長一短あると思いますが、混ぜるのは危険です（たぶん）。

## ファイル名したい

```console
/content/about/index.ja.md  # ==> {BaseURL}/ja/about/index.html
/content/about/index.en.md  # ==> {BaseURL}/en/about/index.html
```

複数の言語のページを作成する場合、
ファイル名を`{ファイル名}.{言語コード}.md`にします。
`{言語コード}`を省略した場合は、デフォルトの言語に設定されます。

とくに理由がなければ、多言語コンテンツのファイル名は揃えるとよいです。
これらは、自動で言語スイッチャーに登録されます。
ファイル名が異なる場合でも、フロントマターで同じ`translationKey`を設定することで、異なる言語間の関係を張ることができます。

## 翻訳ページを表示したい（`.Translations`）

```html
{{ if .IsTranslated }}
<h4>{{ i18n "translations" }}</h4>
<ul>
    {{ range .Translations }}
    <li>
        <a href="{{ .RelPermalink }}" hreflang="{{ .Language.Locale }}">
            {{ .LinkTitle }} ({{ or .Language.Label .Language.Name }})
        </a>
    </li>
    {{ end }}
</ul>
{{ end }}
```

`.IsTranslated`で翻訳コンテンツがあるかを確認して、順序なしリスト（`ul`）で表示します。

翻訳コンテンツは`.Translations`に格納されています。
`{{ range .Translations }}...{{ end }}`で、現在の言語を除いた関連する翻訳コンテンツをループし、
それぞれのコンテンツのURL（`.RelPermalink`）、言語コード（`.Language.Locale`）、タイトル（`.LinkTitle`）、言語名（`.Language.Label`）を取り出して表示します。

## 全言語を確認したい（`hugo.Sites`）

```html
{{ range hugo.Sites }}
<li><a href="{{ .Home.RelPermalink }}">{{ .Language.Label }}</a></li>
{{ end }}
```

:::{note}

以前は`.Site.Languages`でサイト全体の言語一覧を取得していましたが、Hugo v0.156.0で非推奨になりました。
言語スイッチャーのようにページに関係なく全言語を一覧したい場合は`hugo.Sites`を、
現在のページに存在する翻訳だけを一覧したい場合は`.Translations`（または自分自身も含めた`.AllTranslations`）を使います。

:::

## リファレンス

- [Multilingual Mode - gohugo.io](https://gohugo.io/content-management/multilingual/)
- [Language configuration - gohugo.io](https://gohugo.io/configuration/languages/)
- [.Translations - gohugo.io](https://gohugo.io/methods/page/translations/)
- [.AllTranslations - gohugo.io](https://gohugo.io/methods/page/alltranslations/)
- [.IsTranslated - gohugo.io](https://gohugo.io/methods/page/istranslated/)
- [hugo.Sites - gohugo.io](https://gohugo.io/functions/hugo/sites/)
