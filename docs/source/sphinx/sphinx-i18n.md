# 翻訳したい（``sphinx-itnl``）

```console
$ pip install sphinx-intl
```

`sphinx-intl`で、Sphinxドキュメントを多言語化できます。
元のファイルから翻訳カタログ（``.pot``ファイル）を生成し、
そこから生成した言語ごとの翻訳ファイル（``.po``ファイル）を編集することで、
多言語化を実現しています。

## 設定ファイルしたい

```python
# docs/conf.py

locale_dirs = ["locale/"]
# 関連するオプション設定
# gettext_compact = True
# gettext_location = True
# gettext_uuid = False
# gettext_auto_build = True
# gettext_additional_targets = []
# gettext_last_translator = "FULL NAME <EMAIL@ADDRESS>"
# gettext_language_team = "LANGUAGE <LL@li.org>"
```

``locale_dirs``で、翻訳ファイル（``.po``ファイル）を生成するディレクトリを設定します。
任意のディレクトリを設定できますが、
公式ドキュメントは``locale`ディレクトリを推奨しています。

## 翻訳カタログしたい

```console
$ make gettext
```

``make gettext``で翻訳カタログ（＝``.pot``ファイル）を生成できます。
翻訳カタログは``_build/gettext/``ディレクトリに生成されます。

:::{note}

`gettext`は国際化（i18n）と地域化（l10n）をサポートするライブラリです。
ソースコードから翻訳が必要なテキストを抽出し、
``Portable Object Template (POT)``形式で出力します。
翻訳するひとは、このPOTファイルから作成した``Portable Object (PO)``を編集するという
スキームになっています。

:::

## 翻訳ファイルしたい（``sphinx-intl``）

```console
$ sphinx-intl update -p _build/gettext -l ja -l 言語名
# ./locale/ja/LC_MESSAGES/
# ./locale/言語名/LC_MESSAGES/
```

## リファレンス

- [Internationalization](https://www.sphinx-doc.org/en/master/usage/advanced/intl.html)
- [sphinx.builders.gettext](https://www.sphinx-doc.org/en/master/_modules/sphinx/builders/gettext.html)
- [Sphinxで作る貢献しやすいドキュメント翻訳の仕組み - PyConJP - YouTube](https://www.youtube.com/watch?v=pMt9cbWFQ1M)
- [gettext - GNU](https://www.gnu.org/software/gettext/)
