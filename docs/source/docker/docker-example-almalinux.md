# AlmaLinuxしたい（`almalinux`）

```{literalinclude} ../../examples/docker/almalinux.yaml
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
$ docker compose exec almalinux bash
```

## コンテナーを終了したい

```console
$ docker compose down
```

## AlmaLinuxについて

AlmaLinuxのコンテナーを使ってデバッグやテスト、開発環境の構築ができます。上記のサンプルのように `tty: true` と `stdin_open: true` を指定しておくと、`docker compose up -d` するだけで対話的にシェルを操作できます。

AlmaLinuxはRHEL互換で、`dnf` コマンドでパッケージをインストールできます。AlmaLinux 9 は2032年5月31日までの10年間サポートが提供されるため、長期間の安定性が必要なプロジェクトに適しています。
