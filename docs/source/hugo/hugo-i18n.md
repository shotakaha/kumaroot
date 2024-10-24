# 多言語化したい（``/i18n/``）

```html
{{ i18n "見出し文字列" }}
{{ i18n "read_more" }}    <!-- つづきを読む / Read more -->
{{ i18n "word_count" }}   <!-- ○単語 / ○ words -->
{{ i18n "reading_time" }} <!-- ○分で読めます / ○ minutes read -->
```

[lang.Translate](https://gohugo.io/functions/lang/translate/)関数を使って、テンプレートを多言語化できます。
この関数は``i18n``や``T``のエイリアス名で使うことが多いです。

テンプレートで使う一部の文字列を多言語対応したい場合に使います。
たとえば、記事の詳細をクリックするボタンの表示を日本語では「つづきを読む」、英語では「Read More」とできます。

翻訳するために、Hugoの所定の位置に翻訳ファイルを配置し、その中に翻訳の対応表を定義します。

## 翻訳ファイルを作成したい

```console
i18n/
 |--- ja.toml      # 日本語
 |--- en.toml      # 英語
 |--- de.toml      # ドイツ語
 |--- fr.toml      # フランス語
 |--- zh-tw.toml   # 中国語-台湾（繁体字）
```

翻訳ファイルは``/i18n/``ディレクトリに配置します。
ファイル名は言語コードにします。

## 翻訳したい

```toml
# /i18n/ja.toml
[read_more]
other = "つづきを読む"

[word_count]
one = "1文字"
other = "{{ .Count }}文字"

[reading_time]
one = "1分で読めます"
other = "{{ .Count }}分で読めます"
```

```toml
# /i18n/en.toml
[read_more]
other = "Read More"

[word_count]
one = "One word"
other = "{{ .Count }} words"

[reading_time]
one = "One minute read"
other = "{{ .Count }} minutes read"
```

冒頭のサンプルに対応した日英の翻訳ファイルのサンプルです。
``i18n``関数の引数に指定した見出し文字列をセクション名にします。
セクション内のフィールドは[CLDR Language Plural Rules](https://www.unicode.org/cldr/charts/43/supplemental/language_plural_rules.html)の``Category``カラムの文字列を指定できます。

単数形／複数形による数え方の変化は日本語だとあまり馴染みがないかもしれません。
上記のルールを確認しても、日本語は``other``しかありません。
英語の場合は``one``と``other``の他に``two``や``few``を設定することで、
「1st」、「2nd」、「3rd」、「4th」・・・という表記に対応できます。

:::{note}

日本語も「いち」「に」「さん」・・・を「ひとつ」「ふたつ」「みっつ」・・・と数えたりするので「馴染みがない」というのは不正確かもしれません。
むしろバリエーションが多すぎて、ルールとして規定できないというのが正しいのかも？

:::
