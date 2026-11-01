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

`docker compose exec`でコンテナー内で操作できます。
`compose.yaml`で設定したサービス名（`db`）を指定し、`psql`コマンドでデータベースに接続できます。
`-U`オプションでユーザー名を指定します。

## コンテナーを終了したい

```console
$ docker compose down
$ docker compose down --volumes
```

`docker compose down`でコンテナーを終了できます。
`--volumes`オプションをつけると named volume も削除されます。

## ポートを変更したい

```yaml
    ports:
      - "${POSTGRES_PORT:-5432}:5432"
```

`POSTGRES_PORT`でホスト側のPostgreSQLのポートを変更できます。
デフォルト値は`5432`です。

```yaml
    ports:
      - "${ADMINER_PORT:-8080}:8080"
```

`ADMINER_PORT`でホスト側のAdminerのポートを変更できます。
デフォルト値は`8080`です。

```console
$ env POSTGRES_PORT=5433 ADMINER_PORT=8090 docker compose up -d
```

`env`コマンドで環境変数を一時的に変更してコンテナーを起動できます。
別のコンテナーがすでに同じポートを使用している場合に使います。

恒久的に変更したい場合は、`compose.yaml`を直接編集するか、`.env`ファイルを作成して環境変数を設定します。


## Adminerしたい

`localhost:8080`でAdminerにアクセスできます。
ポートを変更した場合は、`localhost:<ADMINER_PORT>`でアクセスします。
ログイン画面で、以下の情報を入力してログインします。

| 項目 | 値 |
| --- | --- |
| データベース種類 | `PostgreSQL` |
| サーバー | `db` （サービス名） |
| ユーザー名 | `postgres` （`POSTGRES_USER`の値）|
| パスワード | `postgres_pass` （`POSTGRES_PASSWORD`の値） |
| データベース | `postgres` or `POSTGRES_DB`の値 |


## PostgreSQLについて

PostgreSQLをDockerで起動します。認証情報は環境変数で設定し、データはnamed volumeで永続化しています。環境変数は`.env`で変更します。上記サンプルでは、デフォルト値を指定しているため、`.env`ファイルがなくても動作します。

Adminerはマルチプラットフォーム対応のデータベース管理ツールで、ブラウザから簡単にPostgreSQLを管理できます。コンテナー内で `psql` コマンドを使ってSQLを実行したり、ホストからデータを投入・バックアップしたりできます。
