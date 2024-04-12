# コマンドしたい（``docker container exec``）

```console
$ docker exec オプション コンテナ名 コマンド
$ docker container exec オプション コンテナ名 コマンド    // Docker 17.06以降で導入
$ docker exec -it コンテナ名 bash
```

``docker container exec``コマンドで、コンテナ内で新しいコマンドを実行できます。
コンテナなあらかじめ起動しておく必要があります。
停止中（or 一時停止中）のコンテナに対して実行するとエラーになります。

:::{note}

``docker exec``と``docker container exec``は同じものです。
``docker container exec``は、Dockerコマンドを整理するために17.06以降で導入されたコマンドです。
最新のドキュメントでは``docker container exec``の利用が推奨されているそうです。

:::

## シェルしたい（``-it``）

```console
$ docker container exec -it コンテナ名 bash
$ docker container exec -it my-ubuntu bash
```

``-it``オプションは``-i / --interactive``と``-t / --tty``のことで、コンテナ内のシェルを起動して操作したい場合に必須のオプションです。
起動していないコンテナに対しては[docker container run](./docker-run.md)を使います。

## バックグラウンドしたい（``-d`` / ``--detach``）

```console
$ docker exec -d コンテナ名 コマンド
```

``-d``オプションで、コマンドをバックグラウンド実行できます。

## 環境変数したい（``-e`` / ``--env``）

```console
$ docker exec --env 環境変数名=値 コンテナ名 コマンド
```

``--env 環境変数=値``オプションで、コマンド実行時の環境変数を設定できます。

## 作業ディレクトリを変えたい（``-w`` / ``--workdir``）

```console
$ docker exec --workdir 作業ディレクトリ コンテナ名 コマンド
```

``--workdir パス``オプションで、コンテナ内の作業ディレクトリを変更できます。

## ユーザーを変えたい（``-u`` / ``--user``）

```console
$ docker exec --user ユーザー名 コンテナ名 コマンド
```

``--user ユーザー名|UID``オプションで、コマンドを実行するユーザーを変更できます。

## リファレンス

- [docker exec - docs.docker.jp](https://docs.docker.jp/engine/reference/commandline/exec.html)
- [docker container exec - docs.docker.jp](https://docs.docker.jp/engine/reference/commandline/container_exec.html)
- [docker container exec - docs.docker.com](https://docs.docker.com/reference/cli/docker/container/exec/)
