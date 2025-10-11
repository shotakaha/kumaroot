# 一時的にコマンド実行したい

```console
$ docker compose run --rm コンテナ名 コマンド
```

`docker compose run`で、一時的にコンテナを起動し、コマンドを実行できます。
`--rm`オプションを必ずつけて、実行後にコンテナが残らないようにするのが基本です。

## LaTeXしたい

```console
$ docker compose run --rm texlive latexmk main.tex
```

TeX Liveコンテナの`latexmk`コマンドでコンパイルしてみました。

## リファレンス

- [docker compose run - docs.docker.jp](https://docs.docker.jp/engine/reference/commandline/compose_run.html)
