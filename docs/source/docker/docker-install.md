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
Docker version 28.5.1, build e180ab8

// Docker Composeのバージョンを確認
$ docker compose version
Docker Compose version v2.40.3-desktop.1
```

## 起動しない場合

```console
$ docker container ls
Cannot connect to the Docker daemon at unix:///Users/shotakaha/.docker/run/docker.sock. Is the docker daemon running?
```

``docker``コマンドを使う場合には、
あらかじめ``Docker Desktop``を起動しておく必要があります。
