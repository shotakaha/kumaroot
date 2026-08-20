# テーマしたい（`/themes/`）

[Hugo Themes](https://themes.gohugo.io/)からテーマを選択できます。

## テーマを追加したい

```console
$ git submodule add https://github.com/nunocoracao/blowfish.git themes/blowfish
```

ほとんどのテーマはGitHubで公開されているため、サブモジュールとして追加できます。
サブモジュールは`themes/テーマ名`に追加します。

```toml
# hugo.toml
theme = ["blowfish"]
```

設定ファイル（`hugo.toml`）で`theme`の変数にテーマ名（`blowfish`）を指定します。

:::{note}

Hugoの設定ファイルやテンプレートファイルはとくに決まりごとがありません。
テーマは複数インストールできますが、お互いに切り替えることが難しい場合もあります。

:::

## テーマを固定したい

```console
$ cd themes/blowfish
$ git switch --detach v2.106.0
HEAD is now at a89d96e4 🐛 Pin fixed headers to the viewport top explicitly

$ cd ../..
$ git add themes/blowfish
$ git commit -m "pin blowfish theme to v2.106.0"

$ git submodule status
 a89d96e4dd63b0a1c1129d795ef4b56e491da1df themes/blowfish (v2.106.0)
```

サブモジュールの中に入って`git switch --detach`でタグやコミットを指定すると、テーマのバージョンを固定できます。
タグはブランチではないので、`--detach`オプションが必要です。
サブモジュールが指すコミットは親リポジトリ側にも記録する必要があるので、
`themes/テーマ名`を`git add`してコミットするところまでがワンセットです。

## テーマを更新したい

```console
$ git submodule update --remote themes/blowfish
Submodule path 'themes/blowfish': checked out 'ca56ac78a3806de12a3ef5f609c310919f6e7bda'

$ git submodule status
+ca56ac78a3806de12a3ef5f609c310919f6e7bda themes/blowfish (v3.2.0)

$ git add themes/blowfish
$ git commit -m "update blowfish theme"
```

`--remote`オプションをつけて`git submodule update`を実行すると、
テーマのリモートリポジトリの最新コミット（既定ではデフォルトブランチのHEAD）まで更新されます。
`git submodule status`の先頭の`+`は、親リポジトリが記録しているコミットとサブモジュールの実際のコミットがずれていることを示しています。
更新後は、固定のときと同じく`git add`・`git commit`を忘れずに行います。

## テーマを削除したい

```console
$ git submodule deinit -f themes/blowfish
Cleared directory 'themes/blowfish'
Submodule 'themes/blowfish' (https://github.com/nunocoracao/blowfish.git) unregistered for path 'themes/blowfish'

$ git rm themes/blowfish
rm 'themes/blowfish'

$ git commit -m "remove blowfish theme"
```

`git rm`だけではサブモジュールの登録情報が`.git/`以下に残ってしまうため、
先に`git submodule deinit`でサブモジュールの登録を解除してから`git rm`します。

`git submodule`の代わりに、Goのパッケージ管理の仕組みを使ってテーマを管理する[モジュールしたい](./hugo-modules.md)という方法もあります。
