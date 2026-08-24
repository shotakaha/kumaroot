# gitしたい（`git`）

```console
$ git status
```

`git`は、分散型バージョン管理システムです。
ソースコードの変更履歴を管理するために使用されます。

詳細は[](../git/git-usage.md)を参照してください。

## インストールしたい（`git`）

```console
$ brew install git
$ git --version
```

`git`はHomebrewでインストールできます。

## 初期設定したい（`git config`）

```console
$ git config --global user.name "名前"
$ git config --global user.email "メールアドレス"
$ git config --global --list
```

`git config --global`で、すべてのリポジトリに共通のユーザー名とメールアドレスを設定します。
コミットのたびに設定する必要はありません。
`--list`で、現在の設定内容を確認できます。

## リファレンス

- [Git](https://git-scm.com)
- [git - GitHub](https://github.com/git/git)
