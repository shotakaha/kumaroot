# MariaDBしたい（`mariadb`）

```console
$ docker container run --detach
  --env MARIADB_ROOT_PASSWORD=root_pass
  --env MARIADB_DATABASE=test_db
  --env MARIADB_USER=test_user
  --env MARIADB_PASSWORD=test_pass mariadb:11.6
  --volume db-data:/var/lib/mysql
```

MariaDBを起動するとき、`-e`オプションで環境変数を設定する必要があります。
この数のオプションを毎回入力するのはミスの元なので、`compose.yaml`で管理するのがよいと思います。
初回起動時は、これらの値でデータベースが初期化されます。

| 変数名 | 説明 |
|---|---|
| `MARIADB_ROOT_PASSWORD` | DBのrootパスワード |
| `MARIADB_DATABASE` | DB名 |
| `MARIADB_USER` | DBのユーザー名 |
| `MARIADB_USER_PASSWORD` | DBユーザーのパスワード |
| `MARIADB_ALLOW_EMPTY_ROOT_PASSWORD=1` | |
| `MARIADB_RANDOM_ROOT_PASSWORD=1` | |

設定できる変数名はDockerHubで確認できます。

## Composeしたい（`mariadb`）

```yaml
services:
  db:
    image: mariadb:11.5.2-noble
    container_name: mariadb
    restart: always
    environment:
      MARIADB_ROOT_PASSWORD: root_pass
      MARIADB_DATABASE: test_db
      MARIADB_USER: test_user
      MARIADB_PASSWORD: test_pass
    volumes:
      # データベース本体（named volumeに保存）
      - db-data:/var/lib/mysql
      # 外部データを使う場合
      # 初期化SQL（bind volumeで同期）
      #- ./initdb.d:/docker-entrypoint-initdb.d
      # 設定ファイル（bind volumeで同期）
      # - ./conf.d:/etc/mysql/conf.d

  adminer:
    image: adminer
    container_name: adminer
    restart: always
    ports:
      - 8081:8080


# named volumes
volumes:
  db-data:
```

`environment`キーで、MariaDBのデータベースを初期化／接続するための情報を設定しています。

:::{note}

より実用的には、パスワード情報はベタ書きするのではなく、
`.env`などに保存して環境変数として読み込めるようにするのがよいです。

:::

`volumes`キーで、データの保存先を設定しています。
データベース本体は`named volume`で設定しています。
設定ファイルや、起動時に外部データベースを使いたい場合は、
`bind volume`で読み込ませることができます。

`adminer`はMySQL/MariaDBなどのデータベースを、ブラウザから操作できるツールです。
`localhost:8081`でアクセスできるようにしました。

:::{note}

`adminer`自身はすでに開発がdeprecatedな状態なのですが、
軽量なのでテスト用にはちょうどよいと思います。
本番で使う場合は`phpMyAdmin`を使うほうがいいかもしれません。

:::



```console
// 設定を確認
$ docker compose config
name: docker-mariadb
services:
  db:
    environment:
      MARIADB_DATABASE: test_db
      MARIADB_PASSWORD: test_pass
      MARIADB_ROOT_PASSWORD: root_pass
      MARIADB_USER: test_user
    image: mariadb:11.5.2-noble
    networks:
      default: null
    volumes:
      - type: volume
        source: db-data
        target: /var/lib/mysql
        volume: {}
networks:
  default:
    name: docker-mariadb_default
volumes:
  db-data:
    name: docker-mariadb_db-data

// Composeを起動
$ docker compose up -d
[+] Running 9/9
 ✔ db Pulled
   ✔ 25a614108e8d Pull complete
   ✔ 9ecb4eecca9c Pull complete
   ✔ 35745a5f0897 Pull complete
   ✔ bb6982bee1d3 Pull complete
   ✔ 722a6dac2c26 Pull complete
   ✔ fc059a825764 Pull complete
   ✔ 677b7c31cba3 Pull complete
   ✔ 610d14c9e7f5 Pull complete
[+] Running 3/3
 ✔ Network docker-mariadb_default   Created
 ✔ Volume "docker-mariadb_db-data"  Created
 ✔ Container docker-mariadb-db-1    Started

// Composeの状態を確認
$ docker compose ls
NAME              STATUS        CONFIG FILES
docker-mariadb    running(1)    docker-mariadb/compose.yaml

// コンテナの状態を確認
$ docker compose ps
NAME                   IMAGE                   COMMAND                   SERVICE   CREATED          STATUS          PORTS
docker-mariadb-db-1    mariadb:11.5.2-noble    "docker-entrypoint.s…"    db        4 minutes ago    Up 4 minutes    3306/tcp

// コンテナ（db）内で mariadb --version を実行
$ docker compose exec db mariadb --version
mariadb from 11.5.2-MariaDB, client 15.2 for debian-linux-gnu (aarch64) using  EditLine wrapper

// コンテナ（db）内のシェル（/bin/bash）を起動
$ docker compose exec db /bin/bash

// （コンテナ内#） MariaDBのバージョンを確認
root@28add7da43c1:/# mariadb --version
mariadb from 11.5.2-MariaDB, client 15.2 for debian-linux-gnu (aarch64) using  EditLine wrapper

// （コンテナ内#） MariaDBに接続
root@28add7da43c1:/# mariadb -u test_user -D test_db -p
Enter password:    // <- test_userのパスワードを入力（compose.yamlで設定したパスワード）

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 5
Server version: 11.5.2-MariaDB-ubu2404 mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [test_db]> \q
Bye.

// （コンテナ内#） シェルを終了
root@28add7da43c1:/# exit
exit

// Composeを一時停止
$ docker compose stop
[+] Stopping 1/1
 ✔ Container docker-mariadb-db-1  Stopped

// Composeの状態を確認
$ docker compose ls
NAME                STATUS              CONFIG FILES

$ docker compose ps
NAME      IMAGE     COMMAND   SERVICE   CREATED   STATUS    PORTS

// コンテナを削除
$ docker compose down
[+] Running 2/0
 ✔ Container docker-mariadb-db-1   Removed
 ✔ Network docker-mariadb_default  Removed```
```

## リストアしたい

```yaml
services:
  db:
    image: mariadb:11.5.2-noble
    environment:
      MARIADB_ROOT_PASSWORD: root_pass
      MARIADB_DATABASE: test_db
      MARIADB_USER: test_user
      MARIADB_PASSWORD: test_pass
    volumes:
      - db-data:/var/lib/mysql
      - ./backup.sql:/docker-entrypoint-initdb.d/backup.sql

# named volumes
volumes:
  db-data:
```

ダンプしたデータベースがある場合、
コンテナ内の`/docker-entrypoint-initdb.d/`にマウントすることで、
コンテナ起動時にデータベースをリストアできます。

:::{seealso}

- [mariadb-dump](https://mariadb.com/kb/en/mariadb-dump/)
- [mariabackup](https://mariadb.com/kb/en/mariabackup/)

:::

## セットアップしたい

UbuntuコンテナにMariaDBをインストールしてセットアップ手順を確認してみました。

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
