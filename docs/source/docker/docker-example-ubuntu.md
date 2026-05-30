# Ubuntuしたい（`ubuntu`）

```{literalinclude} ../../examples/docker/ubuntu.yaml
---
language: yaml
---
```

## コンテナーを起動したい

```console
$ docker compose up -d
```

## コンテナーで操作したい

```console
$ docker compose exec ubuntu bash
```

## コンテナーを終了したい

```console
$ docker compose down
```

## Ubuntuについて

Ubuntuのコンテナーを使ってデバッグやテスト、開発環境の構築ができます。上記のサンプルのように `tty: true` と `stdin_open: true` を指定しておくと、`docker compose up -d` するだけで対話的にシェルを操作できます。

コンテナーを起動したら、`apt update` と `apt install` でパッケージをインストールできます。例えば `curl` や `git` といった基本的なツール、あるいは `python3`、`nodejs` といった開発環境を追加できます。Ubuntu 24.04 LTS は2029年4月までのサポートが保証されており、安定性が必要なプロジェクトに適しています。
