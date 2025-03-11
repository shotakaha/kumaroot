# コンテナを確認したい（`compose ls` / `compose logs`）

```console
// Composeの状態を確認
$ docker compose ls

// Composeのコンテナを確認
// docker container ls に相当
$ docker compose ps

// Composeのログを確認
$ docker compose logs

// Composeのプロセスを確認
$ docker compose top
```

`compose.yaml`をベースに作成したコンテナの状態を確認できます。
コンテナの状態はDocker Desktopからも確認できます。

## リファレンス

- [docker compose ls - docs.docker.jp](https://docs.docker.jp/engine/reference/commandline/compose_ls.html)
