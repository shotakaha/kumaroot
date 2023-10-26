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

``hugo new site``コマンドでHugoサイトのスケルトンを作成せきます。
プロジェクトを初期化したときのディレクトリ構造は上記のとおりです。

それぞれのファイル／ディレクトリの役割を以下に整理しました。

| ディレクトリ名 | ファイル形式 | 役割 |
|---|---|---|
| ``hugo.toml`` | ``.toml`` / ``.yaml`` / ``.json`` | 全体設定ファイル。（``config/_default/hugo.toml``に移動する） |
| ``archetypes`` | ``.md`` | コンテンツを新規作成するときのスケルトンを配置 |
| ``assets`` | ``.scss``など | [Hugo Pipes](https://gohugo.io/hugo-pipes/introduction/)などを使って前処理が必要なファイルを配置 |
| ``content`` | ``.md`` / ``.html`` | コンテンツファイルを配置 |
| ``data`` | ``.csv`` / ``.json``など | データファイルを配置 |
| ``i18n`` | ``.toml`` / ``.yaml`` / ``.json`` | 多言語サイト用。言語ごとの翻訳ファイルを配置 |
| ``layouts`` | ``.html`` | テンプレートファイルを配置 |
| ``static`` | ``.css`` / ``.js`` / ``.png`` / ``jpg``など | 画像やCSS/JSなどの静的ファイルを配置 |
| ``themes`` | - | 外部テーマを配置 |

全体を設定するファイルは``hugo.toml``です。
これは``config/_default/hugo.toml``に移動させます。

``themes``以下に外部テーマをインストールできます。
[Hugo Themes](https://themes.gohugo.io/)などから探してみましょう。
GitHubなどで公開されているテーマは、Gitサブモジュールでインストールするのがよいです。

``layouts``にはテンプレートファイルを配置します。
テンプレートはGoテンプレート言語を使って記述します。
外部テーマを部分的に修正したいときは、ここに同じ名前のファイルを作成することで、レンダリング結果を上書きできます。

## コンテンツしたい（``hugo new content``）

```console
$ cd サイト名
$ hugo new content セクション/コンテンツ.md
$ cat content/セクション/コンテンツ.md
```

``hugo new content``コマンドでコンテンツのスケルトンを作成できます。

## テーマしたい（``hugo new theme``）

```console
$ cd サイト名
$ hugo new theme テーマ名
$ cd themes/テーマ名
$ tree
tree
.
├── LICENSE
├── README.md
├── archetypes
│   └── default.md
├── assets
│   ├── css
│   │   └── main.css
│   └── js
│       └── main.js
├── content
│   ├── _index.md
│   └── posts
│       ├── _index.md
│       ├── post-1.md
│       ├── post-2.md
│       └── post-3
│           ├── bryce-canyon.jpg
│           └── index.md
├── data
├── hugo.toml
├── i18n
├── layouts
│   ├── _default
│   │   ├── baseof.html
│   │   ├── home.html
│   │   ├── list.html
│   │   └── single.html
│   └── partials
│       ├── footer.html
│       ├── head
│       │   ├── css.html
│       │   └── js.html
│       ├── head.html
│       ├── header.html
│       ├── menu.html
│       └── terms.html
├── static
│   └── favicon.ico
└── theme.toml
```

``hugo new theme``コマンドでテーマのスケルトンを作成できます。
