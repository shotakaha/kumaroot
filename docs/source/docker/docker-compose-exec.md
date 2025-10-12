# コンテナ内でコマンド実行したい（`compose exec`）

```console
$ docker compose exec <サービス名> <コマンド>
```

`docker compose exec`は、`compose.yml`で管理しているコンテナの中でコマンドを実行できるコマンドです。

:::{note}

コンテナが起動していないと`exec`は使えません。
あらかじめ`docker compose up -d`で起動しておく必要があります。

:::

## 実行ユーザーを変更したい（`--user`）

```console
$ docker compose exec --user USERNAME <サービス名> <コマンド>
```

`--user`オプションで、コマンドを実行するユーザーを変更できます。
デフォルトは`root`もしくは`Dockerfile`で指定された`USER`です。

多くの公式イメージでは、デフォルトで`root`ユーザーとして動作するため、とくに指定する必要はありません。
ただし、セキュリティの観点から、rootではないユーザーを使うように設計されているイメージもあります。

```console
$ docker compose exec <サービス名> whoami
```

`whoami`コマンドを実行すると、
実際のコンテナがどのユーザーで動いているか確認できます。

## パイプしたい（`-T` / `--no-tty`）

```console
$ docker compose exec -T <サービス名> <コマンド> | <ホストPC上でのコマンド>
```

`-T`（`--no-tty`）は、仮想端末（TTY）を割り当てないようにするオプションです。
コンテナ側の実行結果をホスト側にパイプしたいときに使います。

```console
// MySQLコンテナのDBを、ホスト側にダンプする
$ docker compose exec -T db mysqldump -uUSERNAME -pPASSWORD --single-transaction DATABASE > dump.sql

// gzip圧縮する
$ docker compose exec -T db mysqldump -uUSERNAME -pPASSWORD --single-transaction DATABASE | gzip > dump.sql.gz
```

上記コマンドはMySQLコンテナから、データベースをダンプするサンプルです。

:::{note}

`-T`を使うと、`bash`などを介した対話的な操作はできなくなります。

:::

## 作業ディレクトリを確認したい（`pwd`）

```console
$ docker compose exec コンテナ名 pwd
```

[pwdコマンド](../command/command-pwd.md)で作業ディレクトリを確認できます。

作業ディレクトリは、
[DockerfileのWORKDIR](./docker-dockerfile-workdir.md)で変更したり、
`compose.yaml`の`working_dir`設定で変更できます。

## シェルを起動したい（`bash`）

```console
$ docker compose exec コンテナ名 bash
root@ランダム:/作業ディレクトリのパス#
```

[bashコマンド](../command/command-bash.md)でコンテナ内のシェルを起動できます。
リモートサーバーにログインしたときのように、コンテナ内を操作できます。

## リファレンス

- [docker compose exec](https://docs.docker.jp/engine/reference/commandline/compose_exec.html)
