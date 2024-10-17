---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: .venv
  language: python
  name: python3
---

# pexpect

- `pexpect`で対話処理を自動化する
- `rsync`でリモートサーバーからローカルにデータを同期する
- `ssh`ログインしてサーバー情報をファイルに出力する

```{code-cell} ipython3
import os

import pexpect

print(f"{pexpect.__version__=}")
```

環境変数を読み込む

```{code-cell} ipython3
import dotenv

dotenv.load_dotenv()
```

```{code-cell} ipython3
hostname = os.environ.get("HOST")
username = os.environ.get("USER")
password = os.environ.get("PASSWORD")
```

- `pexect.spwan`で`rsync`コマンドを実行する
- ホストに接続すると表示される`password:`という文字列を`expect`する

```{code-cell} ipython3
options = ["-auvz", "--dry-run", '--rsync-path="~/.local/bin/rsync"']
src = f"{username}@{hostname}:~/README.md"
dest = "."
cmd = (" ").join(["rsync", *options, src, dest])
# cmd
```

```{code-cell} ipython3
child = pexpect.spawn(cmd)
child.expect(["password:"])
```

- `password:`の文字列を確認したら、`sendline`でパスワードを送信する
- パスワード認証に成功すると`rsync`でファイル転送が開始する
- 転送終了の判断のために`pexpect.EOF`を`expect`

```{code-cell} ipython3
child.sendline(password)
child.expect(pexpect.EOF)
child.terminate()
```

- 転送時に標準出力に表示された内容は、`expect`でマッチした文字列の前（`before`）で確認できる
- `before`はバイナリー文字列になっているため`.decode("utf-8")`でテキスト文字列に変換する

```{code-cell} ipython3
print(child.before.decode("utf-8"))
# print(child.after.decode("utf-8"))
```

- `pexpect.pxssh`モジュールを使ってSSH接続する
- `ssh`接続してファイルを作成する

```{code-cell} ipython3
from pexpect import pxssh
```

- ログインに必要な情報を準備する
- パスワードはソースコードにベタ書きせず、環境変数などから読み込む

```{code-cell} ipython3
hostname = os.environ.get("HOST")
username = os.environ.get("USER")
password = os.environ.get("PASSWORD")
```

- `pexpext.pxssh.pxssh()`オブジェクトを初期化する
  - `encoding="utf-8"`を指定すると、`.decode`が不要になる
- `.login`でSSHログインする
  - 初回のパスワード認証時にはRSAキーを`known_hosts`に登録する必要がある
  - そのような処理もうまくやってくれる（らしい）
  - ログインに成功すると`True`が返ってくるので、成功／失敗に使える？
- 接続できないと`ExceptionPxssh`クラスを送出する
  - `Could not establish connection to host`

```{code-cell} ipython3
ssh = pxssh.pxssh(encoding="utf-8")
connected = ssh.login(hostname, username, password)
```

- `uptime`コマンドを実行する
- コマンド実行後に、プロンプトが返ってくるのを待つ
  - `.prompt()`という便利関数がある
  - `.expect("[\\$\\#]")`と同等
- 実行結果は`.before`で確認できる

```{code-cell} ipython3
ssh.sendline("uptime")
ssh.prompt()
print(ssh.before)
```

- `touch`コマンドで空のファイルを作成する

```{code-cell} ipython3
ssh.sendline("netstat")
ssh.prompt()
print(ssh.before)
```

- 終わったらログアウトする

```{code-cell} ipython3
ssh.logout()
```

- `pxssh.pxssh`オブジェクトを調べた
- `.prompt()`で処理を待てるのは、`.PROMPT`が設定されているから
- `.PROMPT`の初期値は``'\\[PEXPECT\\][\\$\\#] '``になってる
  - `\\[PEXPECT\\]` => `[PEXPECT]` : これはよくわからない
  - `[\\$\\#]` => `$`（通常ユーザー） or `#`（管理者ユーザー）

+++

# おまけ

- `pxssh`をまねして、`pexpect.spawn`でSSH接続する

```{code-cell} ipython3
hostname = os.environ.get("HOST")
username = os.environ.get("USER")
password = os.environ.get("PASSWORD")
```

```{code-cell} ipython3
cmd = (" ").join(["ssh", f"{username}@{hostname}"])
PROMPT = "[\\$\\#] "
```

```{code-cell} ipython3
child = pexpect.spawn(cmd)
child.expect("password:")
print(child.before.decode("utf-8"))
```

```{code-cell} ipython3
child.sendline(password)
child.expect(PROMPT)
print(child.before.decode("utf-8"))
```

```{code-cell} ipython3
child.sendline("uptime")
child.expect(PROMPT)
print(child.before.decode("utf-8"))
```

```{code-cell} ipython3
child.sendline("last")
child.expect(PROMPT)
print(child.before.decode("utf-8"))
```

```{code-cell} ipython3
child.terminate(force=True)
```
