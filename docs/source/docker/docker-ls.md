# コンテナの状態を調べたい（``ls``）

```console
$ docker image ls
$ docker container ls
$ docker volume ls
$ docker network ls
$ docker plugin ls
```

``docker``の管理コマンド（``Management Commands``）は``ls``や``inspect``で詳細を調べることができます。
管理コマンドは、Dockerコマンドを整理するためにDocker 17.06以降に導入されました（たぶん）。

## イメージを調べたい（``docker image inspect``）

```bash
$ docker image ls
$ docker image inspect イメージ名
```

ダウンロード済みのイメージ一覧を表示して、イメージ名を確認できます。
``docker images``、
``docker image list``と
``docker image ls``は同じです。

## コンテナを調べたい（``docker container inspect``）

```bash
$ docker container ls
$ docker container inspect コンテナ名
```

起動しているコンテナ一覧を表示して、コンテナ名を確認できます。
``docker container list``、
``docker container ps``、
``docker ps``と
``docker container ls``は同じです。

## ボリュームを調べたい（``docker volume inspect``）

```bash
$ docker volume ls
$ docker volume inspect ボリューム名
```

ボリューム一覧を表示して、ボリューム名を確認できます。

## ネットワークを調べたい（``docker network inspect``）

```bash
$ docker network ls
$ docker network inspect ネットワーク名
```

## プラグインを調べたい（``docker plugin inspect``）

```bash
$ docker plugin ls
$ docker plugin inspect プラグイン名
```

## リファレンス

- [Docker CLI reference - docs.docker.com](https://docs.docker.com/reference/cli/docker/)
- [docker image ls - docs.docker.com](https://docs.docker.com/reference/cli/docker/image/ls/)
- [docker container ls - docs.docker.com](https://docs.docker.com/reference/cli/docker/container/ls/)
- [docker container inspect - docs.docker.com](https://docs.docker.com/reference/cli/docker/container/inspect/)
- [docker volume ls - docs.docker.com](https://docs.docker.com/reference/cli/docker/volume/ls/)
- [docker network ls - docs.docker.com](https://docs.docker.com/reference/cli/docker/network/ls/)
- [docker plugin ls - docs.docker.com](https://docs.docker.com/reference/cli/docker/plugin/ls/)
