# MariaDBしたい（`mariadb`）

```yaml
services:
  db:
    image: mariadb:11.5.2-noble
    container_name: mariadb
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
      # データベース本体（named volumeに保存）
      - db-data:/var/lib/mysql
      # 設定ファイル（bind volumeでマウント）
      - ./config:/etc/mysql/conf.d
      # 既存のデータベース（bind volumeでマウント）
      - ./backup/:/docker-entrypoint-initdb.d/

# named volumes
volumes:
  db-data:
```

`mariadb`イメージを使ってコンテナを起動します。
MariaDBデータベースは、コンテナの初回起動時に初期化されます。
データベース名やパスワードなど、初期化に必要な情報は
`environment`キーで設定します。
設定できる環境変数は
[MariaDB Knowledge Base](https://mariadb.com/kb/en/mariadb-server-docker-official-image-environment-variables/)
を参照してください。

実用としては、パスワード情報はベタ書きするのではなく
`.env`などに保存して環境変数として読み込むようにします。

`volumes`キーで、データの保存先を設定しています。
データベース本体は`named volume`で設定しています。
設定ファイルや、起動時に外部データベースを使いたい場合は、
`bind volume`でマウントしています。

## コマンドしたい（`docker container run`）

```console
$ docker container run --detach
  --env MARIADB_ROOT_PASSWORD=root_pass
  --env MARIADB_DATABASE=test_db
  --env MARIADB_USER=test_user
  --env MARIADB_PASSWORD=test_pass mariadb:11.6
  --volume db-data:/var/lib/mysql
```

`docker compose`した内容を`docker`コマンドで実行したサンプルです。
`-e / --env`オプションで環境変数を設定できますが、
この数のオプションを毎回入力するのはミスの元なので、
`compose.yaml`で管理するのがよいと思います。

## コンテナを操作したい

- 起動

```console
// コンテナを起動
$ docker compose up -d
```

- 状態を確認

```console
// コンテナの状態を確認
$ docker compose ls
NAME              STATUS        CONFIG FILES
docker-mariadb    running(1)    docker-mariadb/compose.yaml

// コンテナの状態を確認
$ docker compose ps
NAME                   IMAGE                   COMMAND                   SERVICE   CREATED          STATUS          PORTS
docker-mariadb-db-1    mariadb:11.5.2-noble    "docker-entrypoint.s…"    db        4 minutes ago    Up 4 minutes    3306/tcp
```

- コンテナ内のDBにアクセス

```console
// コンテナ（db）内で mariadb --version を実行
$ docker compose exec db mariadb --version
mariadb from 11.5.2-MariaDB, client 15.2 for debian-linux-gnu (aarch64) using  EditLine wrapper
```

- コンテナにログイン

```console
// コンテナ（db）内のシェル（bash）を起動
$ docker compose exec db bash
```

- コンテナ内でDB操作

```console
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
```

- 一時停止

```console
// Composeを一時停止
$ docker compose stop
[+] Stopping 1/1
 ✔ Container docker-mariadb-db-1  Stopped

// Composeの状態を確認
$ docker compose ls
NAME                STATUS              CONFIG FILES

$ docker compose ps
NAME      IMAGE     COMMAND   SERVICE   CREATED   STATUS    PORTS
```

- 削除

```console
// コンテナを削除
$ docker compose down
[+] Running 2/0
 ✔ Container docker-mariadb-db-1   Removed
 ✔ Network docker-mariadb_default  Removed```
```

## リストアしたい（`docker-entrypoint-initdb.d`）

```yaml
services:
  db:
    image: mariadb:11.5.2-noble
    environment:
      # 管理者パスワードの設定（適当でOK）
      MARIADB_ROOT_PASSWORD: 管理者用パスワード
      # ランダムでよい場合
      # MARIADB_RANDOM_ROOT_PASSWORD: yes
      # なしでもよい場合
      # MARIADB_ALLOW_EMPTY_ROOT_PASSWORD: 1

      # データベース設定
      # リストアするデータと同じ内容にする
      MARIADB_DATABASE: データベース名
      MARIADB_USER: ユーザー名
      MARIADB_PASSWORD: パスワード
    volumes:
      # データベース本体（named volume）
      - db-data:/var/lib/mysql
      # 起動時に読み込むデータベースの設定（bind volume）
      # backup.sql をマウント
      # ファイルを個別に指定
      - ./backup.sql:/docker-entrypoint-initdb.d/backup.sql
      # ディレクトリをまるっと指定できる
      # - ./backup/:/docker-entrypoint-initdb.d/

# named volumes
volumes:
  db-data:
```

既存のデータベースMariaDBコンテナに読み込む設定です。
データベースはあらかじめSQLファイルにダンプしておきます。

`volumes`キーを設定し、ダンプしたSQLファイルを`bind volume`としてマウントします。
マウント先はコンテナ内の`/docker-entrypoint-initdb.d/`に設定します。
拡張子は`.sh`、`.sql`、`.sql.gz`、`.sql.xz`、`.sql.zst`にします。
複数のファイルがある場合、アルファベット順に読み込まれます。

`environment`キーにはリストアするデータベースの情報（データベース名、ユーザー名、パスワード）を設定します。
管理者のパスワードは、コンテナ用に設定してOKです。
`MARIADB_ROOT_PASSWORD`で適当な文字列を指定するか、
`MARIADB_RANDOM_ROOT_PASSWORD`で任意の文字列を自動設定できます。

コンテナを起動して、データベースにアクセスできるか確認します。

```console
$ docker compose up -d
$ docker compose ls

// MariaDBコンテナ（サービス名: db）にログイン
$ docker compose exec db bash
# mysql -u ユーザー名 -p
Enter password: パスワード
MariaDB [(none)]> SHOW DATABASES;
MariaDB [(none)]> USE データベース名;
MariaDB [(データベース名)]> SHOW TABLES;
MariaDB [(データベース名)]>
```

:::{seealso}

- [mariadb-dump](https://mariadb.com/kb/en/mariadb-dump/)
- [mariabackup](https://mariadb.com/kb/en/mariabackup/)

:::

## ウェブクライアントしたい（`adminer`）

```yaml
services:
  # MariaDBコンテナの設定
  db:
    image: mariadb:11.5.2-noble
    container_name: mariadb
    restart: always
    environment:
      ...
    volumes:
      - ...

  adminer:
    image: adminer
    container_name: adminer
    restart: always
    ports:
      - 8081:8080

# named volumes
volumes:
  db_data:
```

`adminer`はMySQL/MariaDBなどのデータベースに対応したウェブクライアントツールです。
`localhost:8081`でアクセスして、データベースにログインできます。
`phpMyAdmin`に比べるとコンテナ設定が簡単です。

:::{note}

`adminer`自身はすでに開発がdeprecatedな状態なのですが、
軽量なのでテスト用にはちょうどよいと思います。
本番で使う場合は`phpMyAdmin`を使うほうがいいかもしれません。

:::

## ウェブクライアントしたい（`phpMyAdmin`）

```yaml
services:
```

`phpmyadmin`はMySQL/MariaDBなどのデータベースに対応したウェブクライアントツールです。

## セットアップしたい（`mariadb-secure-installation`）

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
