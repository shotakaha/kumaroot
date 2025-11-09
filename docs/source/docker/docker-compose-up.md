# コンテナを起動したい（``docker compose up``）

```console
$ docker compose up -d
```

`docker compose up`コマンドで`compose.yaml`で指定したコンテナを起動できます。
`-d / --detach`はバックグラウンド実行するためのオプションです。
ほとんどの場合でつけておけばOKです。
ローカルにイメージがない場合は、プルしてから実行されます。

`-d`オプションをつけない場合は、フォアグラウンド実行となり、コンテナのログが標準出力に表示されます。
開発時のデバッグには便利ですが、本番環境ではバックグラウンド実行することが一般的です。

:::{note}

複数のコンテナを起動する場合、コンテナ間のネットワークの作成も必要です。
`docker compose up`は、
`docker image pull`、
`docker network create`、
`docker container run`、
をまとめて実行してくれます。

:::

## 設定ファイルを変更したい（`docker compose -f`）

```console
$ docker compose -f compose.other.yaml up -d
```

`-f / --file`オプションで設定ファイルを変更できます。
同じような構成だけど少しだけ変えたい場合などに使用できます。

## コンテナを一時停止したい（`compose stop`）

```console
// 複数コンテナを一時停止
$ docker compose stop
```

`docker compose stop`コマンドで、作成したコンテナを一時停止できます。
コンテナはそのまま保存されているため、後で`docker compose start`で再開できます。
コンテナを完全に削除したい場合は、`docker compose down`を使用してください。

## コンテナを再開したい（`compose start`）

```console
// 複数コンテナを再開
$ docker compose start
```

`docker compose start`コマンドで、停止したコンテナを再開できます。
コンテナが作成されてない場合、エラーになります。

## リファレンス

- [docker compose up - docs.docker.jp](https://docs.docker.jp/engine/reference/commandline/compose_up.html)
