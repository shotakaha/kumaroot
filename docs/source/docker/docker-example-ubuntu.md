# Ubuntuしたい（`ubuntu`）

```yaml
# compose.yaml
services:
  ubuntu:
    image: ubuntu:24.10
    tty: true
```

[ubuntu](https://hub.docker.com/_/ubuntu/)イメージでコンテナを起動します。
さまざまなバリアントがあるので、用途にあったタグを選択します。

Ubuntuは半年に1回のリリースされ、そのうち4回に1回が長期サポート版（LTS）というリリースサイクルです。
Ubuntuをベースにしたイメージの場合、タグ名にコードネームが含まれていることが多いので、
最近のものについてはある程度覚えておくとよいと思います。

| バージョン | コードネーム |
|---|---|
| 20.04 LTS | Focal Fossa |
| 22.04 LTS | Jammy Jellyfish
| 24.04 LTS | Noble Numbat |
| 24.10 | Oracular Oriole |

## コンテナ操作したい

- 起動

```console
$ docker compose up -d
[+] Running 2/2
 ✔ ubuntu Pulled
   ✔ f29bcb9f3dcd Pull complete
[+] Running 2/2
 ✔ Network docker-ubuntu_default  Created
 ✔ Container my-ubuntu            Started
```

- 状態を確認

```console
$ docker compose ls
NAME             STATUS        CONFIG FILES
docker-ubuntu    running(1)    docker-ubuntu/compose.yaml

$ docker container ls
CONTAINER ID   IMAGE          COMMAND       CREATED         STATUS         PORTS     NAMES
f7539a2ffecf   ubuntu:24.10   "/bin/bash"   4 minutes ago   Up 4 minutes             my-ubuntu
```

- コンテナにログイン

```console
$ docker compose exec ubuntu bash
root# apt update
root# apt upgrade
```

- 削除

```console
$ docker compose down
docker compose down
[+] Running 2/1
 ✔ Container my-ubuntu            Removed
 ✔ Network docker-ubuntu_default  Removed
```

## コマンドしたい

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

ちょっとした確認であれば、`docker`コマンドを叩いたほうた早いかもしれません。
Ubuntuコンテナをバックグラウンドで起動（``-d``）します。
コンテナ名は``my-ubuntu``（``--name my-ubuntu``）にしました。
起動したコンテナに接続（``docker exec -it``）し``bash``を起動します。
使い終わったら、
`docker container stop`と
`docker container rm`で片付けておきます。

## リファレンス

- [Ubuntu Official Image - DockerHub](https://hub.docker.com/_/ubuntu/)
