# PostgreSQLしたい（`postgresql`）

`compose.yaml` ファイル：

```yaml
services:
  db:
    image: postgres:latest
    container_name: my-postgres
    environment:
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-postgres_password}
      POSTGRES_USER: ${POSTGRES_USER:-postgres}
      POSTGRES_DB: ${POSTGRES_DB:-app_db}
    ports:
      - "5432:5432"
    volumes:
      - db_data:/var/lib/postgresql/data
    shm_size: 128mb

  adminer:
    image: adminer:latest
    container_name: my-adminer
    ports:
      - "8080:8080"
    environment:
      - ADMINER_DEFAULT_SERVER=db
    depends_on:
      - db

volumes:
  db_data:
```

PostgreSQLをDockerで起動します。
認証情報は環境変数で設定し、データはnamed volumeで永続化しています。
環境変数は`.env`で変更します。
上記サンプルでは、デフォルト値を指定しているため、`.env`ファイルがなくても動作します。

Adminerはマルチプラットフォーム対応のデータベース管理ツールで、ブラウザから簡単にPostgreSQLを管理できます。

起動・停止コマンドは以下の通りです。

```console
$ docker compose up -d
$ docker compose down
```

## 動作確認したい

```console
$ docker compose exec db psql -U postgres
psql (16.4 (Debian 16.4-1.pgdg120+1))
Type "help" for help.

postgres=#
```

コンテナー内のPostgreSQLに接続できます。

### 動作確認用SQL

```sql
\l
CREATE DATABASE test_db;
\c test_db
CREATE TABLE hello (id INT PRIMARY KEY, message TEXT);
INSERT INTO hello VALUES (1, 'Hello PostgreSQL!');
SELECT * FROM hello;
```

## 環境変数を設定したい

`.env` ファイルで認証情報を管理することを推奨します：

```env
POSTGRES_PASSWORD=your_password
POSTGRES_USER=your_username
POSTGRES_DB=your_database_name
```

認証情報は環境変数で変更できます。
`.env` ファイルに必要な認証情報を記述し、
ビルドコンテキストのルートに配置してください。

Gitリポジトリで管理している場合は、
`.env`は`.gitignore`に追加して、コミットできないようにしてください。

PostgreSQLの公式イメージでは、以下の初期設定時の認証情報を設定できます。

| 環境変数 | 説明 | 必須 | 備考 |
|---|---|---|---|
| `POSTGRES_PASSWORD` | postgres ユーザーのパスワード | 必須 | セキュリティ上、必ず設定が必要 |
| `POSTGRES_USER` | 管理者ユーザー名 | 任意 | デフォルトは postgres |
| `POSTGRES_DB` | 初期作成するデータベース名 | 任意 | アプリ用DBを自動作成 |
| `POSTGRES_INITDB_ARGS` | initdb へのコマンドラインオプション | 任意 | エンコーディングなどを指定 |

いったん初期化したコンテナーでは、これらの環境変数を変更しても反映されません。
変更を反映させたい場合は、ボリュームを削除して再起動してください。

:::{note}

認証情報は`compose.yaml`にベタ書きせず、
`.env`に保存することが推奨されています。

:::

## ユーザー・パスワードを変更したい

```console
$ docker compose exec db psql -U postgres
postgres=# ALTER USER postgres WITH PASSWORD 'new_password';
ALTER ROLE
postgres=# \q
```

PostgreSQLは最初からpostgresユーザーが存在します。
パスワードを変更する場合は`ALTER USER`コマンドを使用します。

## データベースを確認したい

### Adminerで確認したい

ブラウザで `http://localhost:8080` にアクセスするとAdminerが起動します。

システムに `PostgreSQL` を選択し、サーバー名に `db` を入力し、
ユーザー名に `postgres`、パスワードに設定した値を入力してログインできます。

### psql で確認したい

```console
$ docker compose exec db psql -U postgres
```

コンテナー内のpsqlを起動し、コマンドラインでデータベースを直接操作できます。

```console
postgres=# \l
postgres=# \c app_db
postgres=# \dt
postgres=# SELECT * FROM table_name;
postgres=# \q
```

よく使う psql コマンド：

| コマンド | 説明 |
|---------|------|
| `\l` | データベース一覧を表示 |
| `\c database_name` | データベースに接続 |
| `\dt` | テーブル一覧を表示 |
| `\du` | ユーザー一覧を表示 |
| `\q` | psql を終了 |

## リファレンス

- [postgres - DockerHub](https://hub.docker.com/_/postgres/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
