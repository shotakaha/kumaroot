# インストール

```bash
$ brew install --cask docker
```

Homebrewを使って``Docker Desktop``をインストールします。
``docker``という名前で``formula``と``cask``の両方があって紛らわしいですが、``Docker Desktop``を使いたい場合は``cask``の方をインストールしてください。

また、``docker``コマンドを使う場合には``Docker Desktop``を起動しておく必要があります。

```bash
# Dockerのバージョンを確認した
$ docker --version
Docker version 20.10.20, build 9fdeb9c

# Docker Composeのバージョンを確認した
$ docker compose version
Docker Compose version v2.12.1

# Dockerイメージがないことを確認した
$ docker images
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE

# Dockerコンテナがないことを確認した
$ docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
