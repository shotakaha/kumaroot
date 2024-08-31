# サービス管理したい（``systemctl``）

```console
$ systemctl status サービス名
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
