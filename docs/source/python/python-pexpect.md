# 対話処理を自動化したい（`pexpect`）

```python
import pexpect

child = pexpect.spawn("ssh ユーザー名@ホスト名")
child.expect("password:")
child.sendline("パスワード")
child.expect("ユーザー名@ホスト名")
child.sendline("exit")
```

`pexpect`は[](../command/command-expect.md)をPythonで実行できるようにしたツールです。
文字のエスケープや改行処理をうまく扱ってくれます。

## SSH接続したい

```console
$ ssh ユーザー名@ホスト名
ユーザー名@ホスト名's password: （パスワードを入力）
Last login: 日時 from IPアドレス
[ユーザー名@ホスト名 ~]$ ls
Downloads  README.md
```

上のサンプルは、ターミナルからSSH接続してディレクトリを確認するときのプロンプト表示です。

```python
# SSH接続を開始する
child = pexpect.spawn("ssh ユーザー名@ホスト名")

# パスワードを要請されたことを確認する
child.expect("password:")
# パスワードを送信する
child.sendline("パスワード")

# ログインしたことを確認する
child.expect("Last login:")
# lsコマンドを送信する
child.sendline("ls")
```

`pexpect`で処理を再現してみました。
最初は`spawn`コマンドで開始します。
その後、プロンプト表示を`expect`で確認し、
続きの処理コマンドを`sendline`で送信するという手順を繰り返します。

`expect`では正規表現（の短文マッチ）を使って、プロンプトに表示された内容を確認できます。
