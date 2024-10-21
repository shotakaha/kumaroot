# WordPressしたい（`wordpress`）

Dockerを使ってWordPressを構築してみます。

## 作りたいもの

作りたいWordPress環境に必要そうなアイテムを書き出しておきます。
少しずつ調べながら進めていきます。

- WordPress / PHP / MySQL
- wp-cli
- マルチサイト環境
- テーマのインストールと有効化
- 記事の作成
- 記事のインポート

## コンテナを起動したい

```bash
$ docker container run -d -p 8080:80 --name my-wordpress wordpress
```

とりあえず詳細なオプションは考えずにコンテナを起動しました。
``http://localhost:8080``でアクセスし、構築画面にアクセスできることを確認しました。
ダイアログに沿って、データベース名（``wordpress``）、データベースのユーザー名（``wordpress``）、データベースのパスワード（``wordpress``）、データベースホスト（``localhost``）、テーブル接頭辞（``wp_``）を入力しました。

結果、「データベース接続確立エラー」がでました。
データベース系の設定を適当に入力したためか、そもそもデータベースが起動していないからかもしれません。
``docker-compose.yml``を使って、環境変数を設定した構築を試してみます。

## データベースの選定

WordPressのデータベースとしてMySQLとMariaDBが利用できます。
さらにMySQLのバージョンは5系と8系があります。
整理すると、次の3種類です

- MySQL 5
- MySQL 8
- MariaDB



---



- [wordpress](https://hub.docker.com/_/wordpress/)
- [bitnami/wordpress](https://hub.docker.com/r/bitnami/wordpress)


## Composeしたい（`wordpress`）

```yaml
# docker-wordpress/docker-compose.yml

services:
  # WordPressコンテナ
  wordpress:
    image: wordpress
    # 依存関係の設定
    # db -> wordpressの順にコンテナを作成する
    depends_on:
      - db
    # 再起動の設定
    restart: always
    # WordPressの環境変数
    environment:
      # DBのコンテナ名
      WORDPRESS_DB_HOST: db
      # DBのユーザー名
      WORDPRESS_DB_USER: exampleuser
      # DBのパスワード
      WORDPRESS_DB_PASSWORD: examplepass
      WORDPRESS_DB_NAME: exampledb
    # ポート設定
    ports:
      - "8080:80"
    # ボリューム設定
    volumes:
      - wp-data:/var/www/html

  # MySQLコンテナ
  db:
    image: mysql:5.7
    restart: always
    environment:
      MYSQL_DATABASE: exampledb
      MYSQL_USER: exampleuser
      MYSQL_PASSWORD: examplepass
      MYSQL_RANDOM_ROOT_PASSWORD: "1"
    volumes:
      - db-data:/var/lib/mysql

# named volumeの設定
volumes:
    wp-data:
    db-data:
```

### 設定の概要

``version``:
    Docker Composeのフォーマットを指定します。最新のフォーマットのバージョン（``3系``）を指定します。

``services``:
    利用するコンテナの設定を定義します。WordPress用の設定と、データベース（MySQL）用の設定を定義します。

``volumes``:
    データの保存先を指定します。ここではそれぞれ``named volume``で定義していますが、``bind volume``にもできます。というか、たぶん``bind volume``にしておいたほうがよい。

## DockerHubの




## WordPressの設定

WordPressの設定は``wp-config.php``に記述します。
``docker-compose.yml``内の環境変数（``WORDPRESS_*``ではじまる変数）でも変更できます。

- ``-e WORDPRESS_DB_HOST=...``
- ``-e WORDPRESS_DB_USER=...``
- ``-e WORDPRESS_DB_PASSWORD=...``
- ``-e WORDPRESS_DB_NAME=...``
- ``-e WORDPRESS_TABLE_PREFIX=...``
- ``-e WORDPRESS_DEBUG=1``

## リファレンス

- [wordpress - DockerHub](https://hub.docker.com/_/wordpress/)
- [mariadb - DockerHub](https://hub.docker.com/_/mariadb)
- [mysql - DockerHub](https://hub.docker.com/_/mysql)
- [bitnami/wordpress - DockerHub](https://hub.docker.com/r/bitnami/wordpress)
- [bitnami/mariadb](https://hub.docker.com/r/bitnami/mariadb)
- [bitnami/mysql](https://hub.docker.com/r/bitnami/mysql)
- [wordpress-mysql - Awesome Compose](https://github.com/docker/awesome-compose/tree/master/wordpress-mysql)
