# MariaDBしたい（`mariadb`）

```yaml
services:
  db:
    image: mariadb:10.11
    working_dir: /workspace
    restart: always
    environment:
      # 管理者パスワードの設定
      MARIADB_ROOT_PASSWORD: root_pass
      # MARIADB_RANDOM_ROOT_PASSWORD: yes
      # MARIADB_ALLOW_EMPTY_ROOT_PASSWORD: true
      # データベースの設定
      MARIADB_DATABASE: test_db
      MARIADB_USER: test_user
      MARIADB_PASSWORD: test_pass
    volumes:
      # 内部ボリューム（named volume）
      # データベース本体
      - db_data:/var/lib/mysql
      # 外部ボリューム（bind volume）
      # 設定ファイル
      - ./config:/etc/mysql/conf.d
      # 初期化データベース
      - ./backups/:/docker-entrypoint-initdb.d/

  adminer:
    image: adminer
    ports:
      - 8081:80

# named volumes
volumes:
  db_data:
```

既存のデータベース（のダンプ）を、ローカルのDocker環境で確認できるようにします。
MariaDBのイメージはDocker Hubにある公式イメージを使用します。
バージョンは使っているデータベースに合わせます。
また、データベースを確認するためのツールとしてAdminerを使います。
phpMyAdminに比べるとコンテナ設定が簡単です。

データベース名やパスワードなど、
初期化に必要な情報は`environment`キーで設定します。
設定できる環境変数は
[MariaDB Knowledge Base](https://mariadb.com/kb/en/mariadb-server-docker-official-image-environment-variables/)
を参照してください。

:::{note}

パスワード情報は`compose.yaml`にベタ書きするのではなく
`.env`などに保存して環境変数として読み込むこともできます。

:::

`volumes`キーで、データの保存先を設定しています。
データベース本体は`named volume`で設定しています。
設定ファイルや、起動時に外部データベースを使いたい場合は、
`bind volume`でマウントしています。

## データベースのバックアップ

```console
[server]$ mysqldump データベース名 > backup.sql
```

リモートサーバーでデータベース（をダンプした）バックアップファイル作成します。
このファイルは[rsync](../command/command-rsync.md)などでローカルにダウンロードしてください。

:::{seealso}

- [mariadb-dump](https://mariadb.com/kb/en/mariadb-dump/)
- [mariabackup](https://mariadb.com/kb/en/mariabackup/)

:::

## データベースを初期化

```yaml
volumes:
  - ./backups/:/docker-entrypoint-initdb.d/
```

Dockerのエントリーポイント機能を使って、上記のバックアップを使ってデータベースを初期化できます。
MariaDBなどのデータベース系のイメージでは、
`/docker-entrypoint-initdb.d/`に配置したSQLファイルを使って、
データベースが初期化できるようになっています。

上記のサンプルでは、
バックアップファイルをローカルの`./backups/`に保存し、
コンテナの`/docker-entrypoint-initdb.d/`にバインドマウントしています。

拡張子は`.sh`、`.sql`、`.sql.gz`、`.sql.xz`、`.sql.zst`にします。
複数のファイルがある場合、アルファベット順に読み込まれます。
ファイルの先頭に数字をつけておくことで、読み込む順番を指定できます。

`environment`キーにはリストアするデータベースの情報（データベース名、ユーザー名、パスワード）を設定します。
管理者のパスワードは、コンテナ用に設定してOKです。
`MARIADB_ROOT_PASSWORD`で適当な文字列を指定するか、
`MARIADB_RANDOM_ROOT_PASSWORD`で任意の文字列を自動設定できます。

## サービスを起動したい

```console
// サービスを起動
$ docker compose up -d
```

## サービスを確認したい

```console
// コンテナの状態を確認
$ docker compose ls
NAME              STATUS        CONFIG FILES
docker-mariadb    running(1)    docker-mariadb/compose.yaml

// コンテナの状態を確認
$ docker compose ps
NAME                   IMAGE                   COMMAND                   SERVICE   CREATED          STATUS          PORTS
docker-mariadb-db-1    mariadb:10.11    "docker-entrypoint.s…"    db        4 minutes ago    Up 4 minutes    3306/tcp
```

## データベースを確認したい

```console
$ open http://localhost:8081
```

ブラウザでAdminerにアクセスします。

```console
$ docker compose exec db bash
[root@random:/workspace]# mariadb -u test_user -D test_db -p
Enter password:    # test_userのパスワードを入力

MariaDB [test_db]> show databases;
MariaDB [test_db]> show tables;
MariaDB [test_db]> \q;
Bye

[root@random:/workspace]# exit
```

`db`コンテナ内のbashを起動し、コンテナ内でデータベースを直接操作できます。

## サービスを終了したい

```console
$ docker compose down -v
```

今回のサービスは、データベースの確認用としての利用を想定しています。
`-v`オプションを使って、ボリュームも削除します。

---

## コンテナ操作したい（`docker container run`）

```console
$ docker container run --detach
  --env MARIADB_ROOT_PASSWORD=root_pass
  --env MARIADB_DATABASE=test_db
  --env MARIADB_USER=test_user
  --env MARIADB_PASSWORD=test_pass mariadb:11.6
  --volume db_data:/var/lib/mysql
```

MariaDBコンテナを`docker`コマンドで実行したサンプルです。
`-e / --env`オプションで環境変数を設定できますが、
この数のオプションを毎回入力するのはミスの元なので、
`compose.yaml`で管理するのがよいと思います。

## データベースをセットアップしたい（`mariadb-secure-installation`）

MariaDB本体をセットアップする手順を確認しました。
以下は、Ubuntu（24.10）のコンテナにインストールした結果です。

```yaml
# compose.yml
services:
  ubuntu:
    image: ubuntu:24.10
    tty: true
```

```console
// Ubuntu 24.10 コンテナを起動
$ docker compose up -d
$ docker compose exec ubuntu bash
```

```console
// MariaDBパッケージをインストール
# apt update
# apt upgrade
# apt install mariadb-server mariadb-client
Summary:
  Upgrading: 0, Installing: 75, Removing: 0, Not Upgrading: 0
  Download size: 31.7 MB
  Space needed: 270 MB / 30.4 GB available

# which -a mariadbd
/usr/sbin/mariadbd
/sbin/mariadbd
```

```console
// MariaDBを起動
# service madiadb status
 * MariaDB is stopped.
# service mariadb start
 * Starting MariaDB database server mariadbd    [ OK ]
# service mariadb status
 * /usr/bin/mariadb-admin from 11.4.3-MariaDB, client 10.0 for debian-linux-gnu (aarch64)
Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Server version		11.4.3-MariaDB-1
Protocol version	10
Connection		Localhost via UNIX socket
UNIX socket		/run/mysqld/mysqld.sock
Uptime:			48 sec

Threads: 1  Questions: 61  Slow queries: 0  Opens: 33  Open tables: 26  Queries per second avg: 1.270
```

```console
// データベースのセットアップ
# mariadb-secure-installation
NOTE: RUNNING ALL PARTS OF THIS SCRIPT IS RECOMMENDED FOR ALL MariaDB
      SERVERS IN PRODUCTION USE!  PLEASE READ EACH STEP CAREFULLY!

In order to log into MariaDB to secure it, we'll need the current
password for the root user. If you've just installed MariaDB, and
haven't set the root password yet, you should just press enter here.

Enter current password for root (enter for none):
OK, successfully used password, moving on...

Setting the root password or using the unix_socket ensures that nobody
can log into the MariaDB root user without the proper authorisation.

You already have your root account protected, so you can safely answer 'n'.

Switch to unix_socket authentication [Y/n]  Y
Enabled successfully!
Reloading privilege tables..
 ... Success!

Change the root password? [Y/n] Y
New password: root_pass
Re-enter new password: root_pass
Password updated successfully!
Reloading privilege tables..
 ... Success!

By default, a MariaDB installation has an anonymous user, allowing anyone
to log into MariaDB without having to have a user account created for
them.  This is intended only for testing, and to make the installation
go a bit smoother.  You should remove them before moving into a
production environment.

Remove anonymous users? [Y/n] Y
 ... Success!

Normally, root should only be allowed to connect from 'localhost'.  This
ensures that someone cannot guess at the root password from the network.

Disallow root login remotely? [Y/n] Y
 ... Success!

By default, MariaDB comes with a database named 'test' that anyone can
access.  This is also intended only for testing, and should be removed
before moving into a production environment.

Remove test database and access to it? [Y/n] Y
 - Dropping test database...
 ... Success!
 - Removing privileges on test database...
 ... Success!

Reloading the privilege tables will ensure that all changes made so far
will take effect immediately.

Reload privilege tables now? [Y/n] Y
 ... Success!

Cleaning up...

All done!  If you've completed all of the above steps, your MariaDB
installation should now be secure.

Thanks for using MariaDB!
```

```console
// MariaDBにログイン
# mariadb -u root -p
Enter password: root_pass

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 49
Server version: 11.4.3-MariaDB-1 Ubuntu 24.10

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Support MariaDB developers by giving a star at https://github.com/MariaDB/server
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

// ログアウト
MariaDB [(none)]> exit
Bye
```

```console
// データベース操作
# mariadb -u root -p
Enter password: root_pass

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.001 sec)

MariaDB [(none)]> CREATE DATABASE my_database;
Query OK, 1 row affected (0.001 sec)

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| my_database        |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.001 sec)

MariaDB [(none)]> CREATE USER 'test_user'@'localhost' IDENTIFIED BY 'test_pass';
Query OK, 0 rows affected (0.005 sec)

MariaDB [(none)]> GRANT ALL PRIVILEGES ON my_database.* TO 'test_user'@'localhost';
Query OK, 0 rows affected (0.002 sec)

MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> exit;
Bye
```

```console
// test_userでログイン
# mariadb -u test_user -p
Enter password: test_pass

MariaDB [(none)]> show DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| my_database        |
+--------------------+
2 rows in set (0.001 sec)

MariaDB [(none)]> exit;
Bye
```

```console
// コンテナを終了
# exit

// コンテナを削除
$ docker compose down
```

## リファレンス

- [mariadb - DockerHub](https://hub.docker.com/_/mariadb)
- [Container Backup and Restoration - mariadb.com](https://mariadb.com/kb/en/container-backup-and-restoration/)
