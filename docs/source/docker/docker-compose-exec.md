# コンテナ内でコマンド実行したい（``docker compose exec``）

```console
$ docker compose exec <サービス名> <コマンド>
```

`docker compose exec`は、`compose.yaml`で管理しているコンテナの中でコマンドを実行できるコマンドです。

`<サービス名>`は`compose.yaml`の`services:`セクションで定義したコンテナの名前です。
`<コマンド>`は、コンテナ内で実行したいシェルコマンド（例：`ls`、`bash`、`python script.py`など）です。

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

TTY（teletypewriter）は対話的なターミナルセッションのことで、デフォルトではコンテナに割り当てられます。
パイプで出力を別のコマンドに渡す場合は、`-T`オプションで TTY を無効にする必要があります。

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

```yaml
services:
  app:
    image: python:3.12
    working_dir: /app
```

`working_dir`を設定すると、`docker compose exec`でコマンドを実行する際、その設定されたディレクトリが作業ディレクトリとなります。

## シェルを起動したい（`bash`）

```console
$ docker compose exec コンテナ名 bash
root@ランダム:/作業ディレクトリのパス#
```

[bashコマンド](../command/command-bash.md)でコンテナ内のシェルを起動できます。
リモートサーバーにログインしたときのように、対話的にコンテナ内を操作できます。

シェルを起動した後は、コンテナ内で自由にコマンドを実行できます。
シェルから抜ける（ホスト側に戻る）には、`exit`コマンドを実行してください。

## リファレンス

- [docker compose exec](https://docs.docker.jp/engine/reference/commandline/compose_exec.html)
