# SSH接続したい（``ssh``）

```console
$ ssh ユーザー名@接続先ホスト名
$ ssh 接続先ホスト名 -l ユーザー名
```

リモートサーバーへログインするときに使うコマンドです。
接続元と接続先でユーザー名が同じ場合、ユーザー名の指定を省略できます。
また、{file}`~/.ssh/config`に接続に関する情報やエイリアスを保存できます。

## SSH接続を管理したい

```console
$ touch ~/.ssh/config
```

SSH接続をよく使う場合は、{file}`~/.ssh/config`を作成するととても便利です。

## エイリアスを設定したい

```unixconfig
Host エイリアス名
Hostname ホスト名
User ユーザー名
```

エイリアスを設定すると、好きな名前でSSH接続できます。
ログイン先のサーバー名が長い場合は、打ち間違いを少なくできます。
また、ローカルPCの名とリモート環境のログインユーザー名が異なる場合も、この設定で吸収できます。

## 認証鍵を設定したい

```unixconfig
Host *
    AddKeysToAgent yes
    UseKeychain yes
    IdentityFile ~/.ssh/id_ed25519
```
