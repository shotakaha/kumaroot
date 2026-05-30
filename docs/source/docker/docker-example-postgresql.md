# PostgreSQLしたい（`postgresql`）

```{literalinclude} ../../examples/docker/postgresql.yaml
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
$ docker compose exec db psql -U postgres
```

## コンテナーを終了したい

```console
$ docker compose down
```

## PostgreSQLについて

PostgreSQLをDockerで起動します。認証情報は環境変数で設定し、データはnamed volumeで永続化しています。環境変数は`.env`で変更します。上記サンプルでは、デフォルト値を指定しているため、`.env`ファイルがなくても動作します。

Adminerはマルチプラットフォーム対応のデータベース管理ツールで、ブラウザから簡単にPostgreSQLを管理できます。コンテナー内で `psql` コマンドを使ってSQLを実行したり、ホストからデータを投入・バックアップしたりできます。
