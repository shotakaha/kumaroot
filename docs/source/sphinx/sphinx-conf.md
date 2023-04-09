# 基本設定したい（``conf.py``）

Sphinxドキュメントの全体設定は``conf.py``（または``source/conf.py``）で管理します。
``sphinx-quickstart`` したあとは、まず、基本設定しておきます。

```{note}
Sphinxは活発に開発されています。
設定に必要な項目も見直されていたりするので、
昔のバージョンで作り始めたドキュメントがある場合は、
いちど設定を見直してみるといいかもしれません。

実際に、僕もv5系で新規にドキュメントを作成したら
はじめに生成される設定ファイル（``conf.py``と``Makefile``）の項目が
かなりすっきりしていて驚きました。
```

## プロジェクトの情報

```python
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'KumaROOT'
author = 'Shota TAKAHASHI'
copyright = '2015 - 2022, Shota TAKAHASHI'
version = '0.5.0'
release = '0.5.0'
```

## 拡張機能を使いたい

```python
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    ...,
]
```

Sphinxにはさまざまな拡張パッケージがあります。
``pip``などを使ってインストールしたあと、この``extensions = []``の部分に追加して有効化します。
詳しい使い方はそれぞれのパッケージのドキュメントを調べてください。

このドキュメントで使っているパッケージについては[](./sphinx-extensions.md)に整理してあります。

## 図表番号したい

```python
numfig = True

# 図表番号を表示するときのカスタム設定
# フォーマット文字列を辞書型で指定
# デフォルトの設定を書いた後、カスタム設定で上書き
numfig_format = {
    "figure": "Fig. %s",
    "table": "Table %s",
    "code-block": "Listing %s"
}
numfig_format["figure"] = "図 %s"
numfig_format["table"] = "表 %s"
numfig_format["code-block"] = "コード %s"

# 図表番号のスコープ
# 0: 全てのドキュメントで通し番号
# 1: セクション毎に番号を付与（x.1, x.2, x.3, ...）
# 2: サブセクション毎に番号を付与（x.x.1, x.x.2, x.x.3, ...）
# デフォルトは 1
numfig_secnum_depth = 1
```

``numfig``をONにすると、図や表、コードブロックに自動で番号を振ることができます。
また``numref``ロールも使えるようになります。

``numfig_format``を使って、図表番号の表示形式を設定できます。
``%s``は図表番号に置換されます。
デフォルトは英語になっているので、日本語で設定しなおしています。

たくさんの図表を含む文書の場合、図番号はセクションごとに振られているほうが読みやすいかもしれません。
どのように採番するか``numfig_secnum_depth``で設定できます。

## 日付したい（``today_fmt``）

```python
today_fmt = "%Y-%m-%d %H:%M:%S"
html_last_updated_fmt = "%Y-%m-%d %H:%M:%S"
```

``today_fmt``で日付の表示形式を設定できます。
デフォルトは米国式（``"%b %d, %Y``）になっているので、読みやすい形式に変えてしまいましょう。
僕はISO8601形式に準拠した形式が好みです。

また``html_last_updated_fmt``で、HTML出力の最終更新日の表示形式を設定できます。
