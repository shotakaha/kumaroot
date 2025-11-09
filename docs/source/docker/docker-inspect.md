# リソースの詳細を確認したい（``docker ... inspect``）

``docker``の管理コマンド（``Management Commands``）の``inspect``サブコマンドで、イメージ、コンテナー、ボリューム、ネットワーク、プラグインなどのリソースの詳細情報をJSON形式で表示できます。

## イメージの詳細を確認したい（``docker image inspect``）

```console
$ docker image inspect イメージ名
```

特定のイメージの詳細情報をJSON形式で表示できます。
イメージIDやタグ、作成日時、アーキテクチャなどの詳細を確認できます。

## コンテナーの詳細を確認したい（``docker container inspect``）

```console
$ docker container inspect コンテナー名
```

特定のコンテナーの詳細情報をJSON形式で表示できます。
IPアドレス、マウントされたボリューム、環境変数、ポートマッピングなどの詳細を確認できます。

## ボリュームの詳細を確認したい（``docker volume inspect``）

```console
$ docker volume inspect ボリューム名
```

特定のボリュームの詳細情報をJSON形式で表示できます。
マウントポイントやドライバーの種類などを確認できます。

## ネットワークの詳細を確認したい（``docker network inspect``）

```console
$ docker network inspect ネットワーク名
```

特定のネットワークの詳細情報をJSON形式で表示できます。
接続されているコンテナーやIPAMの設定などを確認できます。

## プラグインの詳細を確認したい（``docker plugin inspect``）

```console
$ docker plugin inspect プラグイン名
```

特定のプラグインの詳細情報をJSON形式で表示できます。

## リファレンス

- [Docker CLI reference - docs.docker.com](https://docs.docker.com/reference/cli/docker/)
- [docker image inspect - docs.docker.com](https://docs.docker.com/reference/cli/docker/image/inspect/)
- [docker container inspect - docs.docker.com](https://docs.docker.com/reference/cli/docker/container/inspect/)
- [docker volume inspect - docs.docker.com](https://docs.docker.com/reference/cli/docker/volume/inspect/)
- [docker network inspect - docs.docker.com](https://docs.docker.com/reference/cli/docker/network/inspect/)
- [docker plugin inspect - docs.docker.com](https://docs.docker.com/reference/cli/docker/plugin/inspect/)
