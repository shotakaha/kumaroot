# PostgreSQLしたい（`postgresql`）

```yaml
services:
  db:
    image: postgres:16.4
    restart: always
    # 共有メモリのサイズ
    shm_size: 128mb
    environment:
      # 管理者用パスワード（必須）
      POSTGRES_PASSWORD: example
      # 管理者ユーザー名（オプション）
      POSTGRES_USER: ユーザー名（デフォルトはpostgres）
      # データベースの初期設定
      # POSTGRES_DB
      # POSTGRES_INITDB_ARGS
      # POSTGRES_INITDB_WALDIR
      # POSTGRES_HOST_AUTH_METHOD
      # PGDATA

  adminer:
    image: adminer
    restart: always
    ports:
      - 8083:8080
```

## セットアップしたい

UbuntuコンテナにPostgreSQLをインストールして、操作方法を確認しました。

```yaml
services:
  ubuntu:
    image: ubuntu:24.10
    tty: true
```

- 起動

```console
$ docker compose up -d
[+] Running 2/2
 ✔ Network docker-ubuntu_default     Created        0.0s
 ✔ Container docker-ubuntu-ubuntu-1  Started        0.1s
```

- コンテナにログイン

```console
$ docker compose exec ubuntu bash
root@afb2548c7f89:/#
```

- PostgreSQLをインストール

```console
root@afb2548c7f89:/# apt update
root@afb2548c7f89:/# apt upgrade
root@afb2548c7f89:/# apt-cache search postgresql
root@afb2548c7f89:/# apt install postgresql
Summary:
  Upgrading: 0, Installing: 85, Removing: 0, Not Upgrading: 0
  Download size: 88.1 MB
  Space needed: 365 MB / 29.6 GB available
root@afb2548c7f89:/# apt install postgresql-contrib
Summary:
  Upgrading: 0, Installing: 1, Removing: 0, Not Upgrading: 0
  Download size: 11.8 kB
  Space needed: 17.4 kB / 29.2 GB available

root@afb2548c7f89:/# which -a psql
/usr/bin/psql
/bin/psql

root@afb2548c7f89:/# psql --version
psql (PostgreSQL) 16.4 (Ubuntu 16.4-1build1)

root@afb2548c7f89:/# psql
psql: error: connection to server on socket failed:
    No such file or directory
    Is the server running locally and accepting connections on that socket?
```

- サービスを起動

```console
root@afb2548c7f89:/# service postgresql status
16/main (port 5432): down

root@afb2548c7f89:/# service postgresql start
 * Starting PostgreSQL 16 database server

root@afb2548c7f89:/# service postgresql status
16/main (port 5432): online
```

- データベースに接続

```console
// ユーザーを postgres に変更
root@afb2548c7f89:/# su postgres

// データベースに接続
postgres@afb2548c7f89:/$ psql
psql (16.4 (Ubuntu 16.4-1build1))

postgres=#
```

- データベースを一覧

```console
postgres=# \l
                                                   List of databases
   Name    |  Owner   | Encoding | Locale Provider | Collate |  Ctype  | ICU Locale | ICU Rules |   Access privileges
-----------+----------+----------+-----------------+---------+---------+------------+-----------+-----------------------
 postgres  | postgres | UTF8     | libc            | C.UTF-8 | C.UTF-8 |            |           |
 template0 | postgres | UTF8     | libc            | C.UTF-8 | C.UTF-8 |            |           | =c/postgres          +
           |          |          |                 |         |         |            |           | postgres=CTc/postgres
 template1 | postgres | UTF8     | libc            | C.UTF-8 | C.UTF-8 |            |           | =c/postgres          +
           |          |          |                 |         |         |            |           | postgres=CTc/postgres
(3 rows)
```

- データベースを作成

```console
postgres=# CREATE DATABASE new_database;
CREATE DATABASE

postgres=# \l
                                                     List of databases
     Name     |  Owner   | Encoding | Locale Provider | Collate |  Ctype  | ICU Locale | ICU Rules |   Access privileges
--------------+----------+----------+-----------------+---------+---------+------------+-----------+-----------------------
 new_database | postgres | UTF8     | libc            | C.UTF-8 | C.UTF-8 |            |           |
 postgres     | postgres | UTF8     | libc            | C.UTF-8 | C.UTF-8 |            |           |
 template0    | postgres | UTF8     | libc            | C.UTF-8 | C.UTF-8 |            |           | =c/postgres          +
              |          |          |                 |         |         |            |           | postgres=CTc/postgres
 template1    | postgres | UTF8     | libc            | C.UTF-8 | C.UTF-8 |            |           | =c/postgres          +
              |          |          |                 |         |         |            |           | postgres=CTc/postgres
(4 rows)
```

- データベースを終了

```console
postgres=# \q
postgres@afb2548c7f89:/$
```

## リファレンス

- [postgres - DockerHub](https://hub.docker.com/_/postgres/)
