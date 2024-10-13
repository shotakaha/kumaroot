# 対話処理を自動化したい（`expect`）

```tcl
#!/usr/bin/expect

spwan <コマンド>
expect "<プロンプト>"
send "<コマンドに送信する入力>\r"
```

`expect`で対話処理を自動化できます。

データベースのバックアップや、
リモートサーバーへ接続する時には、
パスワードを入力するためのプロンプトが表示されます。
そのような対話型プロンプトが表示される作業を
`spawn` / `expect` / `send` で手順通りにならべることで、自動化できます。

:::{note}

パスワードなど秘匿すべき文字列は、環境変数と組み合わせるとよいです。

expectコマンドのPython実装である[pexpect](https://pexpect.readthedocs.io/en/stable/)パッケージと、[dotenvx](https://dotenvx.com/)を組み合わせるとよいと思います。

:::

## SSH接続したい

```tcl
#!/usr/bin/expect

# SSH接続を開始
spawn ssh ユーザー名@ホスト名（or IPアドレス）

# プロンプト表示を待つ
expect "password:"

# パスワードを送信
send "パスワード\r"

# ログインを確認
expect "$"

# コマンドを実行（ls）
send "ls\r"

# セッションを終了
send "exit\r"
expect eof
```

## データベースをダンプしたい

```tcl
#!/usr/bin/expect

# 変数
set db_user "ユーザー名"
set db_user_password "パスワード"
set db_name "データベース名"
set output_filename "バックアップ/ファイル名.sql"

# mysqldumpコマンドを実行
spawn mysqldump -u $user -p $db_name > $output_filename

# プロンプト待機
expect "Enter password:"

# パスワードを送信
send "$db_user_password\r"

# コマンドの実行を待つ
expect eof
```
