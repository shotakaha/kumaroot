# 対話処理を自動化したい（`pexpect`）

```python
import pexpect

child = pexpect.spawn("ssh ユーザー名@ホスト名")
child.expect("password:")
child.sendline("パスワード")
child.expect("ユーザー名@ホスト名")
child.sendline("exit")
```

`pexpect`は[expect](../command/command-expect.md)をPythonで実行できるようにしたツールです。
SSHやFTPなど対話処理が必要な手順を自動化できます。

Pure Pythonで書かれており、
expectやTcl、その他のC言語モジュールを必要としません。
また、文字のエスケープや改行処理をうまく扱ってくれます。

## プロンプト待ちしたい（`expect`）

```python
# str型
child.expect("文字列")

# list[str]型
child.expect(["文字列1", "文字列2"])
```

`expect`で直前のコマンド処理の結果を確認できます。
引数には`str`型や`list[str]`型を指定できます。
返り値はマッチした文字列のインデックスになっています。

```python
# 接続成功したとき
ok = ["password:"]
# 接続失敗したとき
ng = ["Connection refused", "Timed out"]
connected = child.expect([*ok, *ng])
# =0: "password:" にマッチ
# =1: "Connection refused" にマッチ
# =2: "Timed out" にマッチ

# 接続失敗
if connected > 0:
    child.terminate(force=True)
    sys.exit()

# 接続成功
child.sendline("パスワード")
...
```

リストを指定した場合、マッチした文字列のインデックスが
返ってくることを利用して、簡単な成功／失敗の判断ができます。

## パスワード送信したい（`sendline`）

```python
import os
from dotenv import load_dotenv
import pexpect

# 環境変数（.env）を読み込む
load_dotenv()
pw = os.environ.get("PASSWORD")
child.sendline(pw)
```

`sendline`で文字列／コマンドを送信できます。
このサンプルは、よく利用するパスワード送信部分の抜粋です。
パスワードのベタ書きを避けるため、
`.env`に環境変数として定義し
`dotenv`モジュールで読み込んでいます。

```conf
# プロジェクト/.env
PASSWORD=パスワード
```

`.env`ファイルは、プロジェクトルートに作成し、
必要な環境変数を定義しておきます。

:::{caution}

パスワード情報などが含まれている`.env`は
Gitリポジトリに追加しないように気をつけてください。
うっかりコミットしないように`.gitignore`に追記しておきます。

:::

## rsyncしたい

```console
$ rsync -auvz SRC_REMOTE DEST_LOCAL
ユーザー名@ホスト名's password: 🔑（ログインパスワードを入力）
receiving file list ... done
同期したファイル名...

sent XX bytes  received XXXX bytes  XX.XX bytes/sec
total size is XXXXXXXXXX  speedup is XXXXXX.XX
```

[rsync](../command/command-rsync.md)で
リモートサーバーからファイルを取得したときの
ターミナル表示のサンプルです。
これを`pexpect`すると以下のようになります。

```python
import pexpect

# 事前準備
src = "ユーザー名@ホスト名:パス/"
dest = "./パス/"
options = ["-auvz", "--dry-run"]
cmd = (" ").join(["rsync", *options, src, dest])
# rsync -auvz --dry-run SRC DEST

# Rsyncを開始
child = pexpect.spawn(cmd)
# パスワード認証を確認
child.expect("password:")
# パスワードを送信
child.sendline("パスワード")
# 処理が終わることを確認
child.expect(pexpect.EOF)

# 結果を取得
result = child.before.decode("utf-8")
print(result)
```

`password:`の文字列が表示されていたら、
パスワードを送信できるようにしました。
また、`pexpect.EOF`を`expect`することで、
ファイル転送の処理の完了を待つことができます。

実行した結果は`before`にバイナリ文字列で保存されています。
テキストデータが欲しいので`utf-8`でデコードしています。

:::{note}

`child.expect("文字列")`で待っていた**文字列**とマッチした場合、
`child.before`と`child.after`にマッチした前後の情報がバイナリ文字列で保存されています。
なので、`child.before`で実行結果が確認できます。

:::

## SSH接続したい

```console
$ ssh ユーザー名@ホスト名
ユーザー名@ホスト名's password: （パスワードを入力）
Last login: 日時 from IPアドレス
[ユーザー名@ホスト名 ~]$ ls
Downloads  README.md
[ユーザー名@ホスト名 ~]$ exit
logout
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

## リファレンス

- [pexpect](https://pexpect.readthedocs.io/en/stable/)
