# コンテナを確認したい（``docker compose ps``）

```console
// 稼働中のコンテナを確認
$ docker compose ps
```

`docker compose ps`で、`compose.yaml`で管理しているコンテナの一覧と状態を表示できます。

`docker container ls`コマンドと同様の機能ですが、`compose.yaml`で定義したコンテナのみが対象になります。
各コンテナのステータス（稼働中、停止中など）やポート情報を確認できます。

## プロセスを確認したい（``docker compose top``）

```console
// コンテナ内で実行中のプロセスを確認
$ docker compose top サービス名
```

`docker compose top`で、コンテナ内で実行中のプロセス一覧を表示できます。
`docker top`コマンドと同様に、PID、ユーザー、メモリ使用率など、プロセスの詳細情報を確認できます。

これは`docker compose ps`と異なり、**コンテナ内部のプロセス**を表示するコマンドです。

## リファレンス

- [docker compose ps - docs.docker.jp](https://docs.docker.jp/engine/reference/commandline/compose_ps.html)
- [docker compose top - docs.docker.jp](https://docs.docker.jp/engine/reference/commandline/compose_top.html)
