# 新規作成したい（``hugo new``）

```console
$ hugo new site サイト名
$ tree サイト名
サイト名
├── archetypes
│   └── default.md
├── assets
├── content
├── data
├── hugo.toml
├── i18n
├── layouts
├── static
└── themes
```

``hugo new site``でプロジェクトを初期化できます。
プロジェクト構造は上記のとおりです。

それぞれのファイル／ディレクトリの役割を以下に整理しました。

| ディレクトリ名 | 役割 |
|---|---|
| ``hugo.toml`` | 全体設定ファイル。（``config/_default/hugo.toml``に移動する） |
| ``archetypes`` | コンテンツを新規作成するときのスケルトンを配置 |
| ``assets`` | （確認する） |
| ``content`` | コンテンツファイルを配置 |
| ``data`` | JSONやCSVなどのデータファイルを配置 |
| ``i18n`` | 多言語サイト用。言語ごとの翻訳ファイルを配置 |
| ``layouts`` | テンプレートファイルを配置 |
| ``static`` | 画像やCSS/JSなどの静的ファイルを配置 |
| ``themes`` | 外部テーマを配置 |

全体を設定するファイルは``hugo.toml``です。
これは``config/_default/hugo.toml``に移動させます。

``themes``以下に外部テーマをインストールできます。
[Hugo Themes](https://themes.gohugo.io/)などから探してみましょう。
GitHubなどで公開されているテーマは、Gitサブモジュールでインストールするのがよいです。

``layouts``にはテンプレートファイルを配置します。
テンプレートはGoテンプレート言語を使って記述します。
外部テーマを部分的に修正したいときは、ここに同じ名前のファイルを作成することで、レンダリング結果を上書きできます。
