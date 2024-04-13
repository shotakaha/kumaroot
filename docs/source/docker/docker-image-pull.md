# イメージがほしい（``docker image pull``）

```bash
$ docker image pull イメージ名:タグ
$ docker image pull busybox
$ docker image pull ubuntu:22.04
```

DockerHubなどのレジストリからイメージをダウンロードするコマンドです。
``docker pull``は
``docker image pull``と同じです。

## イメージの一覧を確認したい（``docker image ls``）

```bash
$ docker image ls
```

ダウンロード済みのイメージの一覧を表示してイメージ名などを確認できます。

## イメージを削除したい（``docker image rm``）

```bash
$ docker image rm イメージ名
```

イメージ名を指定して削除します。

## リファレンス

- [docker image pull - docs.docker.com](https://docs.docker.com/reference/cli/docker/image/pull/)
