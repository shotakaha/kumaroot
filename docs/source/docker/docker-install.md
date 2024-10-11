# インストールしたい（`docker`）

```console
$ brew install --cask docker
```

`Docker`はLinuxで動作するソフトウェアなので、
macOS／Windowsの場合は`Docker Desktop`のインストールが必要です。

macOSの場合、Homebrewで``Docker Desktop``をインストールできます。
``docker``という名前で``formula``と``cask``の両方があって紛らわしいですが、``Docker Desktop``は``cask``の方です。

また、``docker``コマンドを使う場合には、
あらかじめ``Docker Desktop``を起動しておく必要があります。

```console
// Dockerのバージョンを確認
$ docker --version
Docker version 27.2.0, build 3ab4256

// Docker Composeのバージョンを確認
$ docker compose version
Docker Compose version v2.29.2-desktop.2

// イメージの状態を確認
$ docker image ls
REPOSITORY                 TAG           IMAGE ID       CREATED         SIZE
python                     3.11-slim     692282a38c50   4 weeks ago     155MB
httpd                      2.4           a3e79aafef7f   2 months ago    178MB
docker/welcome-to-docker   latest        648f93a1ba7d   11 months ago   19MB

// コンテナの状態を確認
$ docker container ls
CONTAINER ID    IMAGE    COMMAND    CREATED    STATUS    PORTS    NAMES

// ボリュームの状態を確認
$ docker volume ls
DRIVER    VOLUME NAME

// Compose状態を確認
$ docker compose ls
NAME    STATUS    CONFIG FILES
```
