# テーマしたい（`/themes/`）

[Hugo Themes](https://themes.gohugo.io/)からテーマを選択できます。

## テーマを追加したい

```console
$ git submodule add テーマのリポジトリURL themes/テーマ名
```

ほとんどのテーマはGitHubで公開されているため、サブモジュールとして追加できます。
サブモジュールは``themes/テーマ名``に追加します。

```toml
# hugo.toml
theme = ["テーマ名"]
```

設定ファイル（``hugo.toml``）で``theme``の変数に``テーマ名``を指定します。

:::{note}

Hugoの設定ファイルやテンプレートファイルはとくに決まりごとがありません。
テーマは複数インストールできますが、お互いに切り替えることが難しい場合もあります。

:::
