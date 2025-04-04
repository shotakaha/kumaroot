# op

```bash
$ brew install --cask 1password-cli
```

パスワード管理ソフト`1password`を操作するコマンドです。
Homebrew Caskを使ってインストールできます。

作成や更新、削除はアプリから実行したほうがよいと思いますが、
ターミナルからユーザー名やパスワードを確認できるので便利です。

## バージョンを確認したい

```console
$ op --version
2.30.3
```

## サインインしたい（`signin`）

```console
$ op signin
```

`op`コマンドをはじめて使う場合、まず`1Password.app`本体の設定が必要です。
設定は[公式ドキュメント](https://developer.1password.com/docs/cli/get-started/)を参照してください。
ここに書いてある通りに進めるとTouchIDを使って認証できるようになります。

## 保管庫を一覧したい

```bash
$ op vault list
ID    NAME
```

`op valut`コマンドで、保管庫を操作できます。

## アイテムを一覧したい（`op item list`）

```console
$ op item list
ID    TITLE    VAULT    EDITED
```

`op item`コマンドで、登録したアイテムを操作できます。

```console
$ op item list | rg アイテム名（の一部）
```

たくさんアイテムを登録している場合は、
[rg](./command-ripgrep.md)などの検索コマンドにパイプして、`TITLE`（アイテム名）を確認します。

## アイテムを取得したい（`op item get`）

```console
$ op item get "アイテム名"
ID:          アイテムのID（ランダムな文字列）
Title:       アイテム名（TITLE）
Vault:       保管庫の名前
Created:     作成日 ago
Updated:     更新日 ago by ユーザー名
Favorite:    false | true
Version:     リビジョン番号
Category:    カテゴリー名
Fields:
  username:    ユーザー名
  password:    パスワード（を取得する方法）
  URL:         ログインURL
```

`op item get`でアイテムの詳細を確認できます。
アイテム名が空白を含む場合は、`"..."`で囲います。

## フィールド名を確認したい

```console
// フィールド名（＝label）を確認
$ op item get "アイテム名" --format json | jq '.fields[] | {label}'

// フィールド名と値を確認
$ op item get "アイテム名" --format json | jq '.fields[] | {label,value}'
```

フィールド名を確認する場合はJSON形式で出力して
[jq](./command-jq.md)コマンドで抽出します。

## フィールドを取得したい

```console
$ op item get "アイテム名" --field ラベル名

// ユーザー名を表示
$ op item get "アイテム名" --field username
```

`--field ラベル名`オプションで、アイテムのフィールドを取得できます。

```console
// パスワードを表示
$ op item get "アイテム名" --field password
[use 'op item get 文字列 --reveal' to reveal]
```

パスワードはそのままでは表示されません。

## パスワードを取得したい

```console
$ op item get "アイテム名" --field password --reveal
（パスワードが表示される）
```

`--reveal`オプションを追加すると、パスワードを確認できます。

```console
$ op item get "アイテム名" --field password --reveal | pbcopy
$ pbpaste
```

[pbcopy](./command-pbcopy.md)コマンドにパイプして、
システムのクリップボードにコピーできます。
クリップポードの内容はそのまま貼り付け（`⌘-v`）たり、
`pbpaste`コマンドで取得したりできます。

## OTPを取得したい（`--otp`）

```console
$ op item get "アイテム名" --otp
NNNNNN
```

ワンタイムパスワードを設定しているアイテムでは
`--otp`でOTPを取得できます。

```console
$ op item get "アイテム名" --otp | pbcopy
$ pbpaste
```

OTPもパイプしてクリップボードにコピーできます。
