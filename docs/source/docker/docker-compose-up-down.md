# コンテナを作成／削除したい（`compose up` / `compose down`）

```console
// 複数コンテナを作成
$ docker compose up -d

// 複数コンテナを削除
$ docker compose down
```

`docker compose up`コマンドでコンテナを作成できます。
ローカルにイメージがない場合は、プルしてから実行されます。
`-d / --detach`はバックグラウンド実行するためのオプションです。
ほとんどの場合でつけておけばOKです。

## コンテナを削除したい（`compose down`）

```console
$ docker compose down
```

`docker compose down`コマンドでコンテナを削除できます。
実行中のコンテナに対してもコマンドを実行でき、
コンテナに紐づいているネットワークも自動で削除できます。
ボリュームは削除されません。

```console
$ docker compose down --volumes
```

`-v / --volumes`オプションで、作成したボリュームを削除できます。

```console
$ docker compose down --rmi local
$ docker compose down --rmi all
```

`--rmi`オプションで、コンテナ作成に使用したイメージも同時に削除できます。
