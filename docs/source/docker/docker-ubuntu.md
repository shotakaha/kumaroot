# Ubutuを使いたい

```bash
$ docker pull ubuntu
Using default tag: latest
latest: Pulling from library/ubuntu
301a8b74f71f: Pull complete
Digest: sha256:7cfe75438fc77c9d7235ae502bf229b15ca86647ac01c844b272b56326d56184
Status: Downloaded newer image for

$ docker images
REPOSITORY              TAG       IMAGE ID       CREATED         SIZE
ubuntu                  latest    cdb68b455a14   8 days ago      77.8MB
```

タグを指定しないと``latest``なイメージを取得できます。

## コンテナーを起動したい

```bash
$ docker run -it -d --name my-ubuntu -p 3389:3389 ubuntu:latest
119477a8562d4ab35a92c9f3773419a627d63db78023b55612805321bfe842cf

$ docker ps
CONTAINER ID   IMAGE           COMMAND   CREATED         STATUS         PORTS                    NAMES
119477a8562d   ubuntu:latest   "bash"    5 seconds ago   Up 4 seconds   0.0.0.0:3389->3389/tcp   my-ubuntu
```

## コンテナーにログインしたい

```bash
$ docker exec -it my-ubuntu /bin/bash
root@119477a8562d:/# ls
```

## コンテナーを削除したい

```bash
$ docker ps
$ docker stop コンテナーID
$ docker rm コンテナーID
```

``docker ps``でコンテナーIDを確認したあと、コンテナーを停止（``stop``）してから削除（``rm``）します。

## リファレンス

- [Ubuntu Official Image - DockerHub](https://hub.docker.com/_/ubuntu/)
