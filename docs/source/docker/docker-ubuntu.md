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

```console
$ docker compose up -d
[+] Running 2/2
 ✔ ubuntu Pulled
   ✔ f29bcb9f3dcd Pull complete
[+] Running 2/2
 ✔ Network docker-ubuntu_default  Created
 ✔ Container my-ubuntu            Started

$ docker compose ls
NAME             STATUS        CONFIG FILES
docker-ubuntu    running(1)    docker-ubuntu/compose.yaml

$ docker container ls
CONTAINER ID   IMAGE          COMMAND       CREATED         STATUS         PORTS     NAMES
f7539a2ffecf   ubuntu:24.10   "/bin/bash"   4 minutes ago   Up 4 minutes             my-ubuntu

$ docker compose down
docker compose down
[+] Running 2/1
 ✔ Container my-ubuntu            Removed
 ✔ Network docker-ubuntu_default  Removed
```

## リファレンス

- [Ubuntu Official Image - DockerHub](https://hub.docker.com/_/ubuntu/)
