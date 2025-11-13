# MariaDBしたい（`mariadb`）

```yaml
services:
  db:
    image: mariadb:latest
    container_name: my-mariadb
    environment:
      MARIADB_ROOT_PASSWORD: ${MARIADB_ROOT_PASSWORD:-root_password}
      MARIADB_DATABASE: ${MARIADB_DATABASE:-app_db}
      MARIADB_USER: ${MARIADB_USER:-app_user}
      MARIADB_PASSWORD: ${MARIADB_PASSWORD:-app_password}
    ports:
      - "3306:3306"
    volumes:
      - db_data:/var/lib/mysql

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

MariaDBをDockerで起動します。
認証情報は環境変数で設定し、データはnamed volumeで永続化しています。
環境変数は`.env`で変更します。
上記サンプルでは、デフォルト値を指定しているため、`.env`ファイルがなくても動作します。

Adminerはマルチプラットフォーム対応のデータベース管理ツールで、ブラウザから簡単にMariaDBを管理できます。

起動・停止コマンドは以下の通りです。

```console
$ docker compose up -d
$ docker compose down
```

## 動作確認したい

```console
$ docker compose exec db mariadb -u root -p
Enter password: # MARIADB_ROOT_PASSWORD (example) を入力
MariaDB [(none)]>
```

コンテナー内のMariaDBに接続できます。

### 動作確認用SQL

```sql
SHOW DATABASES;
CREATE DATABASE test_db;
USE test_db;
CREATE TABLE hello (id INT PRIMARY KEY, message TEXT);
INSERT INTO hello VALUES (1, 'Hello MariaDB!');
SELECT * FROM hello;
```

## 環境変数したい

```env
MARIADB_ROOT_PASSWORD=your_root_password
MARIADB_DATABASE=your_database_name
MARIADB_USER=your_username
MARIADB_PASSWORD=your_password
```

認証情報は環境変数で変更できます。
`.env` ファイルに必要な認証情報を記述し、
ビルドコンテキストのルートに配置してください。

Gitリポジトリで管理している場合は、
`.env`は`.gitignore`に追加して、コミットできないようにしてください。

MariaDBの公式イメージでは、以下の初期設定時の認証情報を設定できます。

| 環境変数 | 説明 | 必須 | 備考 |
|---|---|---|---|
| `MARIADB_ROOT_PASSWORD` | rootユーザーのパスワード | 必須 | セキュリティ上、必ず設定が必要 |
| `MARIADB_DATABASE` | 初期作成するデータベース名 | 任意 | アプリ用DBを自動作成 |
| `MARIADB_USER` | 初期作成するユーザー名 | 任意 | アプリ用ユーザーを自動作成 |
| `MARIADB_PASSWORD` | 上記ユーザーのパスワード | 任意 | `MARIADB_USER`とセットで使う |
| `MARIADB_ALLOW_EMPTY_ROOT_PASSWORD` | rootパスワードを空にする | 任意 | セキュリティ上、オススメしない |
| `MARIADB_RANDOM_ROOT_PASSWORD` | ランダムなrootパスワードを生成 | 任意 | ログに出力されるが、使いづらい |
| `MARIADB_AUTO_UPGRADE` | 自動アップグレードを有効化 | 任意 | 大きなダンプやバージョン移行時に便利 |

いったん初期化したコンテナーでは、これらの環境変数を変更しても反映されません。
変更を反映させたい場合は、ボリュームを削除して再起動してください。

:::{note}

認証情報は`compose.yaml`にベタ書きせず、
`.env`に保存することが推奨されています。

:::

## ヘルスチェックしたい

```yaml
healthcheck:
  test: ["CMD", "mariadb-admin", "ping", "-h", "localhost"]
  interval: 10s
  timeout: 5s
  retries: 5
  start_period: 30s
```

`mariadb-admin`でMariaDBコンテナーが応答可能かを確認しています。

```console
$ docker compose exec db mariadb-admin ping -h localhost -u root -p
Enter password:  # example
mysqld is alive
```

## データベースを初期化したい

```yaml
volumes:
  - db_data:/var/lib/mysql
  - ./setup:/docker-entrypoint-initdb.d
```

Dockerのエントリーポイント機能を使ってデータベースを初期化できます。
データベース（`/var/lib/mysql`）が**空の時**に`/docker-entrypoint-initdb.d/`に配置したSQLファイルを使って初期化されます。

### 初期化用のSQLサンプル

```sql
-- データベースの作成
CREATE DATABASE IF NOT EXISTS sample_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- ユーザーの作成と権限付与
CREATE USER IF NOT EXISTS 'sample_user'@'%' IDENTIFIED BY 'sample_pass';
GRANT ALL PRIVILEGES ON sample_db.* TO 'sample_user'@'%';
FLUSH PRIVILEGES;

-- テーブル作成
USE sample_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 初期データ挿入
INSERT INTO users (name, email) VALUES
('Alice', 'alice@example.com');
```

`init.sql`のようなファイルに保存して、`setup/`に配置してください。

:::{note}

再投入したい場合は、`docker compose down -v`でボリュームを削除して再起動します。

:::

## データベースを手動で投入したい（`mariadb`）

```console
$ docker compose exec -T db \
  mariadb \
  -uroot -pROOT_PASSWORD \
  DATABASE_NAME < dump.sql

$ gunzip -dc dump.sql.gz | docker compose exec -T db \
  mariadb \
  -uroot -pROOT_PASSWORD \
  DATABASE_NAME
```

既存のデータベースを投入する場合は、
コンテナー内で`mariadb`コマンドを実行します。

## データベースをバックアップしたい（`mariadb-dump`）

```console
$ docker compose exec -T db \
  mariadb-dump \
  -uroot -pROOT_PASSWORD \
  --databases DATABASE_NAME \
  --single-transaction \
  --quick \
  --routines \
  --triggers \
  --events \
  | gzip > dump.sql.gz
```

コンテナー側にあるMariaDBデータベース（`DATABASE_NAME`）を、
ホスト側にダンプするサンプルです。

:::{note}

このまま実行すると、ホスト側のターミナルの履歴にパスワードなどが残ります。
実際の運用では`.env`で環境変数を設定し、
`sh -lc`コマンドで読み込ませるとよいです。

:::

:::{seealso}

- [mariadb-dump](https://mariadb.com/kb/en/mariadb-dump/)
- [mariabackup](https://mariadb.com/kb/en/mariabackup/)

:::

## データベースを確認したい

### Adminerで確認したい

ブラウザで `http://localhost:8080` にアクセスするとAdminerが起動します。

サーバー名に `db` を入力し、ユーザー名に `root`、パスワードに `example` を入力してログインできます。

### コマンドラインで確認したい

```console
$ docker compose exec db bash
```

コンテナー内のbashを起動し、コマンドラインでデータベースを直接操作できます。

```console
$ mariadb -u root -p
Enter password:  # rootのパスワードを入力
MariaDB [(none)]> SHOW DATABASES;
MariaDB [(none)]> exit
```

## リファレンス

- [mariadb - DockerHub](https://hub.docker.com/_/mariadb)
- [Container Backup and Restoration - mariadb.com](https://mariadb.com/kb/en/container-backup-and-restoration/)
