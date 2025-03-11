# コンテナ内でコマンド実行したい（`compose exec`）

```console
$ docker compose exec コンテナ名 コマンド
```

`docker compose exec`コマンドで、コンテナの中でコマンドを実行できます。

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
