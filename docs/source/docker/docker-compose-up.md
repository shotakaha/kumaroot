# コンテナを作成したい（`compose up`）

```console
$ docker compose up -d
```

`docker compose up`コマンドでコンテナを作成できます。
ローカルにイメージがない場合は、プルしてから実行されます。
`-d / --detach`はバックグラウンド実行するためのオプションです。
ほとんどの場合でつけておけばOKです。

## コンテナを一時停止したい（`compose stop`）

```console
// 複数コンテナを一時停止
$ docker compose stop
```

`docker compose stop`コマンドで、作成したコンテナを一時停止できます。

## コンテナを再開したい（`compose start`）

```console
// 複数コンテナを再開
$ docker compose start
```

`docker compose start`コマンドで、停止したコンテナを再開できます。
コンテナが作成されてない場合、エラーになります。
