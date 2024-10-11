# MariaDBしたい（`mariadb`）

```console
$ docker container run -d
  -v db-data:/var/lib/mysql
  -e MARIADB_ROOT_PASSWORD=root_pass
  -e MARIADB_DATABASE=test_db
  -e MARIADB_USER=test_user
  -e MARIADB_PASSWORD=test_pass mariadb:11.6
```

MariaDBを起動するとき、`-e`オプションで環境変数を設定する必要があります。
環境変数名はDockerHubで確認できます。

この数のオプションを毎回入力するのはミスの元なので、`compose.yaml`で管理するのがよいと思います。

## Composeしたい（`mariadb`）

```yaml
services:
  db:
    image: mariadb:11.5.2-noble
    environment:
      MARIADB_ROOT_PASSWORD: root_pass
      MARIADB_DATABASE: test_db
      MARIADB_USER: test_user
      MADIADB_PASSWORD: test_pass
    volumes:
      - db-data:/var/lib/mysql

# named volumes
volumes:
  db-data:
```

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

## リファレンス

- [mariadb - DockerHub](https://hub.docker.com/_/mariadb)
