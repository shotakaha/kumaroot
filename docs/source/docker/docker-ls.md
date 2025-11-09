# リソースを一覧したい（``docker ... ls``）

``docker``の管理コマンド（``Management Commands``）の``ls``サブコマンドで、イメージ、コンテナー、ボリューム、ネットワーク、プラグインなどのリソース一覧を表示できます。

## イメージ一覧を確認したい（``docker image ls``）

```console
$ docker image ls
```

ダウンロード済みのイメージ一覧を表示できます。

:::{note}

`docker images`、`docker image list`、`docker image ls`はすべて同じコマンドです。

:::

## コンテナー一覧を確認したい（``docker container ls``）

```console
$ docker container ls
```

起動中のコンテナー一覧を表示できます。

```console
$ docker container ls --all
```

`--all`オプションで、停止中のコンテナーも含めて表示します。

:::{note}

`docker ps`、`docker container ps`、`docker container list`、`docker container ls`はすべて同じコマンドです。

:::

## ボリューム一覧を確認したい（``docker volume ls``）

```console
$ docker volume ls
```

作成済みのボリューム一覧を表示できます。

## ネットワーク一覧を確認したい（``docker network ls``）

```console
$ docker network ls
```

作成済みのネットワーク一覧を表示できます。

## プラグイン一覧を確認したい（``docker plugin ls``）

```console
$ docker plugin ls
```

インストール済みのプラグイン一覧を表示できます。

## リファレンス

- [Docker CLI reference - docs.docker.com](https://docs.docker.com/reference/cli/docker/)
- [docker image ls - docs.docker.com](https://docs.docker.com/reference/cli/docker/image/ls/)
- [docker container ls - docs.docker.com](https://docs.docker.com/reference/cli/docker/container/ls/)
- [docker volume ls - docs.docker.com](https://docs.docker.com/reference/cli/docker/volume/ls/)
- [docker network ls - docs.docker.com](https://docs.docker.com/reference/cli/docker/network/ls/)
- [docker plugin ls - docs.docker.com](https://docs.docker.com/reference/cli/docker/plugin/ls/)
