# WordPressを使いたい

WordPressを構築する場合も、Dockerを使うと簡単らしいので試してみます。

WordPressの動作環境には、PHPとMySQL（もしくはMariaDB）が必要です。
それぞれのコンテナが必要なので``docker-compose``でセットアップします。

MySQLはApple Silicon上で動かないという情報をみたので、MariaDBを使うことにします。
そのほかに、ゲストOSをどうするか、ウェブサーバーをApacheにするかNginxにするかを決めます。

## DockerHub

- [wordpress](https://hub.docker.com/_/wordpress/)
- [bitnami/wordpress](https://hub.docker.com/r/bitnami/wordpress)


## docker-compose.yml

```yaml
# docker-wordpress/docker-compose.yml
version: "3"

services:
    wordpress:
        image: wordpress
        restart: always
        ports:
            - 8080:80
        environment:
            WORDPRESS_DB_HOST: db
            WORDPRESS_DB_USER: exampleuser
            WORDPRESS_DB_PASSWORD: examplepass
            WORDPRESS_DB_NAME: exampledb
        volumes:
            - wordpress:/var/www/html

    db:
        image: mysql:5.7
        restart: always
        environment:
            MYSQL_DATABASE: exampledb
            MYSQL_USER: exampleuser
            MYSQL_PASSWORD: examplepass
            MYSQL_RANDOM_ROOT_PASSWORD: "1"
        volumes:
            - db:/var/lib/mysql

volumes:
    wordpress:
    db:
```

### 設定の概要

``version``:
    Docker Composeのフォーマットを指定します。最新のフォーマットのバージョン（``3系``）を指定します。

``services``:
    利用するコンテナの設定を定義します。WordPress用の設定と、データベース（MySQL）用の設定を定義します。

``volumes``:
    データの保存先を指定します。ここではそれぞれ``named volume``で定義していますが、``bind volume``にもできます。というか、たぶん``bind volume``にしておいたほうがよい。

## DockerHubの

- [wordpress](https://hub.docker.com/_/wordpress/)
- [bitnami/wordpress](https://hub.docker.com/r/bitnami/wordpress)


## WordPressの設定

WordPressの設定は``wp-config.php``に記述します。
``docker-compose.yml``内の環境変数（``WORDPRESS_*``ではじまる変数）でも変更できます。

- ``-e WORDPRESS_DB_HOST=...``
- ``-e WORDPRESS_DB_USER=...``
- ``-e WORDPRESS_DB_PASSWORD=...``
- ``-e WORDPRESS_DB_NAME=...``
- ``-e WORDPRESS_TABLE_PREFIX=...``
- ``-e WORDPRESS_DEBUG=1``
