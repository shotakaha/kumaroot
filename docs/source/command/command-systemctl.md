# サービス管理したい（`systemctl`）

```console
// サービス（ユニット）一覧
$ systemctl list-units --type service

// サービス詳細
$ systemctl status
$ systemctl status サービス名

// サービス状態
$ systemctl is-active|is-enabled|is-failed サービス名

// サービス制御
$ systemctl start|stop|restart|reload サービス名
```

`systemctl`はLinuxで使用するサービス管理コマンドです。
`systemd`デーモンを管理するコマンドで、
システム起動時にサービスを開始したり、
サービスの開始、停止、再起動、ステータスを確認したりできます。
また、システム全体のシャットダウンや再起動もできます。

:::{note}

少し古めのLinuxでは``service``コマンドが使用できます。
`/etc/init.d/`に置かれたinitスクリプトを使って、
サービスの起動、停止、再起動、ステータスの確認ができます。
`systemctl`と`service`で引数の順番が異なります。

```console
$ service サービス名 status
```


現在は、多くのディストリビューションで`systemd`が採用されるようになっていて`systemctl`の使用が推奨されています。
`service`コマンドが`systemctl`のラッパーになっている場合もあるみたいです。

:::

## Apacheしたい（`httpd`）

```console
$ systemctl status httpd
$ systemctl cat httpd
$ systemctl start|stop|restart|reload httpd

// ログ確認
$ journalctl -u httpd

// 設定ファイルの文法チェック
$ apachectl configtest
Syntax OK
```

RHEL系は`httpd`、
Debian系は`apache2`というサービス名で
Apacheサーバーを制御できます。

:::{note}

Apacheには本体の実行ファイル（`httpd` / `apache`）と、専用の管理スクリプト（`apachectl`）も存在します。

サービス制御には`systemctl`で十分ですが、
個別の制御には`apachectl`などを使うことができることを覚えておくとよいです。

たとえば、上記サンプルにある設定ファイルの文法チェックは`apachectl`のサブコマンドです。

:::

## SSHしたい（`sshd`）

```console
$ systemctl status sshd
$ systemctl restart sshd
```

`sshd`はOpenSSHのサーバー側のデーモンです。
サーバー側の`sshd`が起動していないと、SSH接続ができません。

```console
// 設定ファイルの文法チェック
$ sshd -t

// 設定を確認
$ sshd -T
$ sshd -T | grep passwordauthentication
```
