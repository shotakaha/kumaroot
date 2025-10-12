# 一時的にコマンド実行したい

```console
$ docker compose run --rm <サービス名> <コマンド>
```

`docker compose run`は、コンテナを**一時的に起動**し実行するためのコマンドです。
必ず`--rm`オプションをつけて、実行後にコンテナが残らないようにするのが基本です。

:::{note}

`--rm`を忘れると、コンテナがどんどんと溜まってしまいます。
`docker ps`で消し忘れたコンテナがないか確認できます。
`docker rm <コンテナ名>`でコンテナを手動で削除できます。
`docker container prune`で停止済みコンテナを一括削除できます。

:::

## LaTeXしたい

```console
$ docker compose run --rm texlive latexmk main.tex
```

TeX Liveコンテナの`latexmk`コマンドでコンパイルしてみました。

## リファレンス

- [docker compose run - docs.docker.jp](https://docs.docker.jp/engine/reference/commandline/compose_run.html)
