# SSHしたい

デスクトップの設定からSSHを有効にします。

1. {guilabel}`Preferences` → {guilabel}`Raspberry Pi Configuration`を選択する
2. {guilabel}`Interface`タブを選択する
3. {guilabel}`SSH`のトグルボタンを有効にする

:::{note}

OSイメージを作成する時点で、SSH設定を有効にできます。
同じネットワークに接続し、設定したホスト名／ユーザー名／パスワードを使ってすぐにログインできます。

```console
$ ssh ユーザー名@ホスト名.local
// パスワードを入力
```

:::

## パスワードレスしたい

[ssh-keygenでSSH鍵を作成](../command/command-ssh-keygen.md)して、パスワードレスにできます。
必要なコマンドは``ssh-keygen``、``ssh-copy-id``、``ssh-add``の3種類です。

## デーモンしたい（`sshd`）

```console
$ sudo systemctl enable ssh
$ sudo systemctl start ssh
```

`systemctl`を使ってコマンドラインからもSSHを有効にできます。

```console
$ sudo systemctl status ssh
Unit ssh.service not found  # SSHが見つからないことを確認
$ sudo apt install openssh-server
$ sudo systemctl status ssh
ssh.service - loaded  # OpenSSHのインストールを確認
```

SSHが見つからない場合は、`openssh-server`を追加インストールしてからデーモンを有効にします。

:::{note}

OSにUbuntuを選択した場合、デフォルトではSSH接続が有効になっていませんでした。

:::
