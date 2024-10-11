# Ubuntuを使いたい

```console
// コンテナを起動
$ docker container run -d --name my-ubuntu ubuntu

// コンテナの状態を確認
$ docker container ls

// コンテナ内のBashを起動
$ docker container exec -it my-ubuntu bash

// コンテナを停止＆削除
$ docker container stop my-ubuntu
$ docker container rm my-ubuntu
```

Ubuntuコンテナをバックグラウンドで起動（``-d``）します。
コンテナ名は``my-ubuntu``（``--name my-ubuntu``）にしました。
起動したコンテナに接続（``docker exec -it``）し``bash``を起動します。
使い終わったら、
`docker container stop`と
`docker container rm`で片付けておきます。

## Composeしたい

```yaml
# compose.yaml
services:
  ubuntu:
    image: ubuntu:24.10
    tty: true
```

```comsole
$ docker compose up -d
$ docker compose ls
$ docker compose down
```

## リファレンス

- [Ubuntu Official Image - DockerHub](https://hub.docker.com/_/ubuntu/)
