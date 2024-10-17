# 対話処理を自動化したい（`pexpect`）

```python
import pexpect

child = pexpect.spawn("コマンド")
child.expect("待ち文字列")
child.sendline("別のコマンド")
child.expect("待ち文字列")
child.terminate()
```

`pexpect`は[expect](../command/command-expect.md)をPythonで実行できるようにしたツールです。
リモートサーバーとRsyncやSSHなどするときに必要なパスワード入力などの
対話処理を含んだ手順を自動化できます。

Pure Pythonで書かれており、
expectやTcl、その他のC言語モジュールを必要としません。
また、文字のエスケープや改行処理もうまく扱ってくれるため
素のexpectより読み書きしやすいと思います。

## コマンド送信したい（`sendline`）

```python
child.sendline("コマンド")
```

`sendline`でコマンドを送信できます。
CRLFの改行コード（`\r\n`）付きで送信してくれるので、
コマンドを記入するだけでよいです。

## 処理待ちしたい（`expect`）

```python
# str型
child.expect("文字列")

# list[str]型
child.expect(["文字列1", "文字列2"])
# =0: 文字列1にマッチ
# =1: 文字列2にマッチ
```

`expect`に処理が終わった時に表示される文字列を指定することで、
直前のコマンドの処理を待つことができます。
引数は、`str`型と`list[str]`型で指定でき、正規表現も使えます。
返り値はマッチした文字列のインデックスになっています。

## プロンプト待ちしたい

```python
PROMPT = ["\\$", "\\#", pexpect.EOF]
child.sendline("コマンド")
child.expect(PROMPT)
```

標準的なサーバー設定のプロンプト表示は、`$`が一般ユーザー、`#`が管理者ユーザーとなっています。
`$`もしくは`#`を待つことでサーバー内での作業を続けることができます。

## パスワード待ちしたい

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
```

rsyncやSSH接続ではパスワード入力を要求されます。
多くの場合`password:`の文字列が表示されるため、`.expect`することで接続確認ができます。
また、接続できなかったときの文字列を確認することで、例外として処理できます。

上のサンプルでは`ok`と`ng`のリストを定義し、
マッチしたときに返ってくる文字列のインデックスを利用して
簡単な成功／失敗の判断をしています。

## パスワード送信したい（`sendline`）

```python
import os
from dotenv import load_dotenv

# 環境変数（.env）を読み込む
load_dotenv()
password = os.environ.get("PASSWORD")

child.sendline(password)
```

利用することが多いパスワード送信部分のサンプルです。
パスワードのベタ書きを避けるため、
`.env`に環境変数として定義し`dotenv`モジュールで読み込んでいます。

```conf
# プロジェクト/.env
PASSWORD=パスワード
```

`.env`ファイルは、プロジェクトルートに作成し、必要な環境変数を定義しておきます。

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
リモートサーバーからファイルを取得したときの表示される内容のサンプルです。
これを再現するように`pexpect`で手順を並べていきます。

```python
import pexpect

# rsyncを開始
child = pexpect.spawn("rsync -auvz SRC_REMOTE DEST_LOCAL")
child.expect("password:")     # パスワード認証を確認
child.sendline("パスワード")    # パスワードを送信
child.expect(pexpect.EOF)     # 処理が終わることを確認
result = child.before.decode("utf-8") # 結果を取得
print(result)
```

`password:`の文字列が表示されたあとに、パスワードを送信しています。
`pexpect.EOF`を`.expect`することで、
ファイル転送の処理の完了を待つことができます。

実行した結果は`before`にバイナリ文字列で保存されています。
テキストデータが欲しいので`utf-8`でデコードしています。

:::{note}

`child.expect("文字列")`で待っていた**文字列**とマッチした場合、
`child.before`と`child.after`にマッチした前後の情報がバイナリ文字列で保存されています。
なので、`child.before`で実行結果が確認できます。

:::

## SSH接続したい（`pexpect.pxssh`）

```console
$ ssh ユーザー名@ホスト名
ユーザー名@ホスト名's password: （パスワードを入力）
Last login: 日時 from IPアドレス
[ユーザー名@ホスト名 ~]$ uptime
21:41  up 6 days, 11:26, 4 users, load averages: 2.30 3.65 4.16
[ユーザー名@ホスト名 ~]$ df -h
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
...
[ユーザー名@ホスト名 ~]$ exit
logout
```

SSH接続して、いくつかのコマンドを実行したときに内容のサンプルです。
この手順を`pexpect.pxssh`モジュールを使って並べます。

```python
from pexpect import pxssh

ssh = pxssh.pxssh(encoding="utf-8")
ssh.login(hostname, username, password)

ssh.sendline("uptime")
ssh.prompt()
print(ssh.before)

ssh.sendline("df -h")
ssh.prompt()
print(ssh.before)

ssh.logout()
```

`pexpect.pxssh`モジュールで簡単にSSH接続できます。
`pexpect.spawn`で書いた場合と比べると、
ログイン処理（`.login`）とプロンプト待ち（`.prompt`）が簡単に書けるようになっています。

```python
import pexpect

# 待機するプロンプト表示
PROMPT = ["\\$", "\\#", pexpect.EOF]

# SSH接続を開始する
child = pexpect.spawn("ssh ユーザー名@ホスト名")
child.expect("password:")

# パスワードを送信してログインする
child.sendline("パスワード")
child.expect(PROMPT)

# コマンド（uptime）を実行
child.sendline("uptime")
child.expect(PROMPT)
print(child.before.decode("utf-8"))

# コマンド（df -h）を実行
child.sendline("df -h")
child.expect(PROMPT)
print(child.before.decode("utf-8"))

# コマンド（exit）を実行
child.sendline("exit")
child.expect(PROMPT)
print(child.before.decode("utf-8"))

child.terminate()
```

## リファレンス

- [pexpect](https://pexpect.readthedocs.io/en/stable/)
