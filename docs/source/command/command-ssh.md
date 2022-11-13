# ssh

```bash
$ ssh ユーザー名@接続先ホスト名
$ ssh 接続先ホスト名 -l ユーザー名
```

リモートサーバーへログインするときに使うコマンドです。
接続元と接続先でユーザー名が同じ場合、ユーザー名の指定を省略できます。
また、{file}`~/.ssh/config`に接続に関する情報やエイリアスを保存できます。

## ssh設定したい

{file}`~/.ssh/config`の設定例を列挙します。

### エイリアスを設定したい

```
Host エイリアス名
HostName ホスト名
User ユーザー名
```

### 認証鍵を設定したい

```
Host *
    AddKeysToAgent yes
    UseKeychain yes
    IdentityFile ~/.ssh/id_ed25519
```
