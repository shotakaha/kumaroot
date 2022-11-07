# Docker の使い方

Dockerはコンテナー型仮想化技術を使ったプラットフォームです。
開発環境の構築をサポートするために使います。

```bash
$ brew install --cask docker
```

Homebrewを使って``Docker Desktop``をインストールします。
``docker``という名前で``formula``と``cask``の両方があって紛らわしいですが、``Docker Desktop``を使いたい場合は``cask``の方をインストールしてください。

また、``docker``コマンドを使う場合には``Docker Desktop``を軌道しておく必要があります
（Dockerデーモン（``/var/run/docker.sock``）と通信できる状態）。

```bash
$ docker --version
Docker version 20.10.20, build 9fdeb9c
$ docker compose version
Docker Compose version v2.12.1
```

```{toctree}
docker-ubuntu
```
