# BusyBoxしたい（`busybox`）

```{literalinclude} ../../examples/docker/busybox.yaml
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
$ docker compose exec app bash
```

## コンテナーを終了したい

```console
$ docker compose down
```

## BusyBoxについて

BusyBoxはLinuxの基本的なコマンドが揃った軽量イメージです。
約300～400個のUNIXコマンド（アプレット）を単一バイナリに統合しており、イメージサイズは1～2MBと非常に軽量です。
特定のコマンドをまとめたコンテナーを作成するときや、デバッグ、テストに活躍します。
マルチコンテナー環境での Init Container や Sidecar Container、デバッグコンテナーなど補助的な役割で活躍し、依存関係が最小で、セキュリティリスクが低いのが特徴です。
`docker compose exec app bash` でコンテナー内のシェルを起動し、診断を実行できます。
