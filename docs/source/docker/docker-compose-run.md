# 一時的なコマンドしたい（`compose run`）

```console
$ docker compose run --rm コンテナ名 コマンド
```

`docker compose run`で、一時的にコンテナを起動し、コマンドを実行できます。
`--rm`オプションを必ずつけて、実行後にコンテナが残らないようにするとよいです。

## LaTeXしたい

```console
$ docker compose run --rm texlive latexmk main.tex
```

TeX Liveコンテナの`latexmk`コマンドでコンパイルしてみました。
