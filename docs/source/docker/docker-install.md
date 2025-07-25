# インストールしたい（`docker`）

```console
$ brew install --cask docker-desktop
```

`Docker`はLinuxで動作するソフトウェアなので、
macOS／Windowsで使用するには`Docker Desktop`のインストールが必要です。
macOSでは、Homebrewを使ってインストールできます。

:::{note}

以前は`docker`という名前で、`formula`（CLIツール）と`cask`（GUIアプリ）の両方が提供されていて、紛らわしかったのですが、
2025年6月にCaskのほうが`docker-desktop`にリネームされ、区別が明確になりました。

:::

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

## 起動しない場合

```console
$ docker container ls
Cannot connect to the Docker daemon at unix:///Users/shotakaha/.docker/run/docker.sock. Is the docker daemon running?
```

``docker``コマンドを使う場合には、
あらかじめ``Docker Desktop``を起動しておく必要があります。
