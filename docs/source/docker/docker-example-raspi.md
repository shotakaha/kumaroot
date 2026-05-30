# Raspberry Piしたい（`raspi`）

```{literalinclude} ../../examples/docker/raspi.yaml
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
$ docker compose exec raspi bash
```

## コンテナーを終了したい

```console
$ docker compose down
```

## Raspberry Piについて

Raspberry Piの開発環境をDockerで構築できます。
サービス名を`raspi`とし、Dockerfileをビルドコンテキストから参照しています。
コンテナーを起動してシェルを実行できます。
このテンプレートを使うことで、ローカルマシンと同じRaspberry Pi環境でアプリケーションをテストしたり、開発したりできます。
コンテナー内で必要なパッケージをインストールしたり、スクリプトを実行したりできます。
