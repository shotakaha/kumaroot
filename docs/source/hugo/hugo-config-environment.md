# ビルド環境別に設定したい（オススメ）

```txt
config
├── _default
│   ├── hugo.toml
│   ├── languages.en.toml
│   ├── languages.ja.toml
│   ├── menus.en.toml
│   ├── menus.ja.toml
│   └── params.toml
├── production
│   ├── hugo.toml
│   └── params.toml
└── gitlab
     ├── hugo.toml
     └── params.toml
```

[前ページの設定ファイルの分割機能](./hugo-config-environment.md)を使って、
ステージング用やプロダクション用など
環境ごとにディレクトリを分けることができます。

すべての環境に共通する設定は
デフォルト環境は`config/_default/`に作成します。
そして環境ごとに異なる差分を`config/環境名/`に作成します。

多言語サイトにしたい場合も、そのセクションの言語別ファイルを作成するだけで簡単に対応できます。

## ビルド環境を変更したい（`hugo --environment`）

```console
$ hugo -e 環境名

// _default + GitLab Pagesの設定
$ hugo -e gitlab

// _default + 公開設定
$ hugo -e production
```

``--environment``オプションで、用途別に設定を切り替えることができます。
設定ファイルは``/config/環境名/``ディレクトリの以下に配置します。
デフォルトは``/config/_default/``ディレクトリです。

ローカルでの開発（やステージング環境）では``/config/_default/``、
GitLab Pagesでの構築時は``/config/gitlab/``、
本番環境に公開する場合は``/config/production/``の設定ファイルに切り替えて適用されるようにしています。

## テーマごとに設定したい

この機能を使うと、テーマごとの設定を共存させることができます。
Hugoのテーマ作成はとても自由度が高く、テーマ間の互換性はほぼありません。

```console
// 実行: hugo server
/config/_default/hugo.toml

// Blowfishテーマ
// 実行: hugo -e blowfish server
/config/blowfish/[...].toml

// Anankeテーマ
// 実行: hugo -e ananke server
/config/ananke/[...].toml
```

お気に入りのテーマを探す過程で、設定ファイルを毎回書き換えるのは面倒です。
このように、テーマごとに設定ファイル環境を作成すると、その手間がぐっと抑えられます。

## Blowfishの場合

[Blowfishテーマの設定ファイル](https://blowfish.page/docs/configuration/)のセクションでは、次のように設定ファイルを分割しています。

```console
/config/_default/config.toml
/config/_default/languages.ja.toml # 言語関係の設定
/config/_default/menus.ja.toml     # ナビゲーションの設定
/config/_default/params.toml       # テーマ独自の設定
```

多言語サイトにする場合、設定ファイル名も言語ごとに作成できます。


## リファレンス

- [Configuration directory](https://gohugo.io/getting-started/configuration/#configuration-directory)
