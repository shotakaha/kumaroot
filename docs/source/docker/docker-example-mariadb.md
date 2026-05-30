# MariaDBしたい（`mariadb`）

```{literalinclude} ../../examples/docker/mariadb.yaml
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
$ docker compose exec db mariadb -u root -p
```

## コンテナーを終了したい

```console
$ docker compose down
```

## MariaDBについて

MariaDBをDockerで起動します。認証情報は環境変数で設定し、データはnamed volumeで永続化しています。環境変数は`.env`で変更します。上記サンプルでは、デフォルト値を指定しているため、`.env`ファイルがなくても動作します。

Adminerはマルチプラットフォーム対応のデータベース管理ツールで、ブラウザから簡単にMariaDBを管理できます。コンテナー内で `mariadb` コマンドを使ってSQLを実行したり、ホストからデータを投入・バックアップしたりできます。
