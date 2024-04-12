# シェルしたい（``docker exec``）

```console
$ docker exec オプション コンテナ名 コマンド
$ docker exec -it コンテナ名 bash
```

``docker exec``コマンドで、コンテナ内で新しいコマンドを実行できます。
コンテナなあらかじめ起動しておく必要があります。
停止中（or 一時停止中）のコンテナに対して実行するとエラーになります。

``-it``オプションは``-i / --interactive``と``-t / --tty``のことで、コンテナ内のシェルを起動して操作したい場合に必須のオプションです。

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

- [docker exec](https://docs.docker.jp/engine/reference/commandline/exec.html)
