# RockyLinuxしたい（`rockylinux`）

```{literalinclude} ../../examples/docker/rockylinux.yaml
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
$ docker compose exec rockylinux bash
```

## コンテナーを終了したい

```console
$ docker compose down
```

## RockyLinuxについて

RockyLinuxのコンテナーを使ってデバッグやテスト、開発環境の構築ができます。上記のサンプルのように `tty: true` と `stdin_open: true` を指定しておくと、`docker compose up -d` するだけで対話的にシェルを操作できます。

RockyLinuxはRHEL互換で、`dnf` コマンドでパッケージをインストールできます。RockyLinux 9は2032年5月31日までのサポートが提供されるため、長期間の安定性が必要なエンタープライズ環境に適しています。
