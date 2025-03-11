# コンテナを削除したい（`compose down`）

```console
$ docker compose down
```

`docker compose down`コマンドでコンテナを削除できます。
実行中のコンテナに対してもコマンドを実行でき、
コンテナに紐づいているネットワークも自動で削除できます。
ボリュームは削除されません。

## ボリュームを削除したい（`--volumes`）

```console
$ docker compose down --volumes
```

`-v / --volumes`オプションで、作成したボリュームを削除できます。

## イメージを削除したい（`--rmi`）

```console
$ docker compose down --rmi local
$ docker compose down --rmi all
```

`--rmi`オプションで、コンテナ作成に使用したイメージも同時に削除できます。


## リファレンス

- [docker compose down - docs.docker.jp](https://docs.docker.jp/engine/reference/commandline/compose_down.html)
