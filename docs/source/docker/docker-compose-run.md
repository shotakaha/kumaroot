# 一時的にコマンド実行したい（``docker compose run``）

```console
$ docker compose run --rm <サービス名> <コマンド>
```

`docker compose run`は、コンテナを**一時的に起動**してコマンドを実行するためのコマンドです。
`docker compose exec`と異なり、実行時にコンテナを新規作成します。
実行後にコンテナを自動削除するため、必ず`--rm`オプションをつけるのが基本です。

## コンテナを自動削除したい（`--rm`）

```console
$ docker compose run --rm <サービス名> <コマンド>
```

`--rm`オプションを指定すると、コマンド実行後にコンテナが自動削除されます。
一時的なコンテナを実行する際は、このオプションをつけることでディスク容量の無駄を防げます。

:::{note}

`--rm`を忘れるとコンテナが残ります

`--rm`オプションを忘れると、実行済みのコンテナがどんどんと溜まってしまいます。
`docker compose ps --all`で停止済みコンテナを確認できます。
`docker compose rm <コンテナ名>`でコンテナを手動で削除できます。
`docker container prune`で停止済みコンテナを一括削除できます。

:::

## インタラクティブに実行したい（`-it`）

```console
// シェルを対話的に実行
$ docker compose run --rm -it <サービス名> bash

// Pythonをインタラクティブモードで実行
$ docker compose run --rm -it <サービス名> python
```

`-i`（`--interactive`）と`-t`（`--tty`）オプションを組み合わせると、コンテナ内のシェルやPythonなどを対話的に利用できます。
`-i`は標準入力を開いたままに、`-t`は仮想端末を割り当てます。

## 実行例

```console
// 単発でコマンド実行
$ docker compose run --rm app python script.py

// テストを実行
$ docker compose run --rm app pytest tests/

// データベーションマイグレーション
$ docker compose run --rm web python manage.py migrate

// LaTeXでコンパイル
$ docker compose run --rm texlive latexmk main.tex
```

## リファレンス

- [docker compose run - docs.docker.jp](https://docs.docker.jp/engine/reference/commandline/compose_run.html)
