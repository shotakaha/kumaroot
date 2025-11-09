# コンテナを確認したい（``docker compose ls``）

```console
// Composeの状態を確認
$ docker compose ls
```

`docker compose ls`で、`compose.yaml`で管理しているコンテナの一覧を表示できます。
出力には各プロジェクト（Composeで管理されているコンテナグループ）の状態、実行中のコンテナ数、基となるファイルなどが表示されます。

複数の`compose.yaml`を管理している場合や、各プロジェクトの実行状態を一覧で確認する際に便利です。
コンテナの状態はDocker Desktopからも確認できます。

:::{note}

Docker Compose v2以降で利用できるコマンドです。

:::

## リファレンス

- [docker compose ls - docs.docker.jp](https://docs.docker.jp/engine/reference/commandline/compose_ls.html)
