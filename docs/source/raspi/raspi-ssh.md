# SSHしたい

```bash
# SSHサービスを起動
sudo systemctl start ssh

# 自動起動を有効化
sudo systemctl enable ssh

# サービスの状態を確認
sudo systemctl status ssh
```

Raspberry PiにSSH経由でリモートアクセスできるようにセットアップします。
`systemctl`を使ってコマンドラインからSSHを有効にできます。

SSHが見つからない場合は、`openssh-server`を追加インストールしてからデーモンを有効にします：

```bash
sudo apt install openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh
```

## GUIしたい

デスクトップの設定からSSHを有効にします。

1. {guilabel}`Preferences` → {guilabel}`Raspberry Pi Configuration`を選択する
2. {guilabel}`Interface`タブを選択する
3. {guilabel}`SSH`のトグルボタンを有効にする

## SSHで接続したい

OSイメージを作成する時点で、SSH設定を有効にできます。
同じネットワークに接続し、設定したホスト名／ユーザー名／パスワードを使ってすぐにログインできます。

```bash
ssh <ユーザー名>@<ホスト名>.local
# または
ssh <ユーザー名>@<raspi-ip>
```

## パスワードレスしたい

[ssh-keygenでSSH鍵を作成](../command/command-ssh-keygen.md)して、パスワードレスにできます。
必要なコマンドは`ssh-keygen`、`ssh-copy-id`、`ssh-add`の3種類です。

:::{note}

OSにUbuntuを選択した場合、デフォルトではSSH接続が有効になっていません。

:::
