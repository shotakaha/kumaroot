# WordPressしたい

Docker公式イメージを組み合わせてWordPress環境を構築します。
データベース（MySQL/MariaDB）と連携した実用的な構成を紹介します。

## 概要

WordPressのDocker環境を構築するには、複数の選択肢があります。
このガイドでは公式イメージを中心に紹介します。

### 利用可能なイメージ

#### 公式イメージ（Docker公式）

- [wordpress](https://hub.docker.com/_/wordpress/) - WordPress + Apache + PHP
  - シンプルで軽量
  - PHP 7.4～8.3、Apache2.4対応
  - データベースは別途用意する必要あり
  - 推奨用途：学習、開発環境、カスタマイズ必須な場合

- [mysql](https://hub.docker.com/_/mysql) - MySQL 8.0
  - OracleがメンテナンスするMySQL公式イメージ
  - 推奨用途：汎用的なMySQL環境

- [mariadb](https://hub.docker.com/_/mariadb) - MariaDB 10.x～11.x
  - MariaDB Foundationがメンテナンス
  - MySQL互換で高速
  - 推奨用途：高性能が必要な場合

#### Bitnamiイメージ

- [bitnami/wordpress](https://hub.docker.com/r/bitnami/wordpress) - WordPress + Apache + PHP
  - PHP、Apache、WordPressをまとめたワンイメージ
  - SSL/TLS、wp-cli同梱
  - OCI（Oracle Container Initiative）に準拠
  - 推奨用途：本番環境、セキュリティ重視、オールインワン構成

- [bitnami/mysql](https://hub.docker.com/r/bitnami/mysql) - MySQL
  - Bitnamiがメンテナンス
  - セキュリティ設定が強化されている

- [bitnami/mariadb](https://hub.docker.com/r/bitnami/mariadb) - MariaDB
  - Bitnamiがメンテナンス
  - セキュリティ設定が強化されている

### イメージ選択ガイド

| 用途 | 推奨イメージ | 理由 |
|---|---|---|
| 学習・開発 | wordpress（公式） + mysql（公式） | シンプルでカスタマイズしやすい |
| 本番環境 | bitnami/wordpress + bitnami/mysql | セキュリティ強化、wp-cli同梱 |
| 高性能が必要 | wordpress（公式） + mariadb（公式） | MySQLより高速 |
| 簡単構築 | bitnami/wordpress単体 | PHP、Apache含むオールインワン |

## シンプルな構成（MySQL 8.0 + WordPress）

### compose.yaml を作成

```yaml
# compose.yaml
services:
  wordpress:
    image: wordpress:latest
    container_name: wordpress-dev
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_NAME: ${WORDPRESS_DB_NAME:-wordpress}
      WORDPRESS_DB_USER: ${WORDPRESS_DB_USER:-wordpress}
      WORDPRESS_DB_PASSWORD: ${WORDPRESS_DB_PASSWORD:-wordpress}
      WORDPRESS_TABLE_PREFIX: wp_
    volumes:
      - wordpress_data:/var/www/html
    depends_on:
      - db
    restart: always

  db:
    image: mysql:8.0
    container_name: wordpress-db
    environment:
      MYSQL_DATABASE: ${WORDPRESS_DB_NAME:-wordpress}
      MYSQL_USER: ${WORDPRESS_DB_USER:-wordpress}
      MYSQL_PASSWORD: ${WORDPRESS_DB_PASSWORD:-wordpress}
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD:-root}
    volumes:
      - db_data:/var/lib/mysql
    restart: always

volumes:
  wordpress_data:
  db_data:
```

### 起動と初期設定

```console
# コンテナを起動
$ docker compose up -d

# ブラウザでアクセス
$ open http://localhost:8080

# ログを確認
$ docker compose logs -f wordpress
```

アクセスするとWordPressのセットアップウィザードが表示されます。
管理者情報を入力して初期化を完了します。

### 環境変数の設定

`.env`ファイルを作成して環境変数をカスタマイズできます：

```env
# .env
WORDPRESS_DB_NAME=my_wordpress
WORDPRESS_DB_USER=wp_user
WORDPRESS_DB_PASSWORD=secure_password
MYSQL_ROOT_PASSWORD=root_password
```

## Bitnamiイメージを使った構成

### Bitnami + MySQLの構成

Bitnamiイメージはセキュリティが強化されており、wp-cliが同梱されているため、本番環境に適しています。

```yaml
# compose.yaml
services:
  wordpress:
    image: bitnami/wordpress:latest
    container_name: wordpress-dev
    ports:
      - "8080:80"
      - "8443:443"
    environment:
      WORDPRESS_DATABASE_HOST: db
      WORDPRESS_DATABASE_NAME: ${WORDPRESS_DB_NAME:-wordpress}
      WORDPRESS_DATABASE_USER: ${WORDPRESS_DB_USER:-wordpress}
      WORDPRESS_DATABASE_PASSWORD: ${WORDPRESS_DB_PASSWORD:-wordpress}
      WORDPRESS_USERNAME: admin
      WORDPRESS_PASSWORD: ${WORDPRESS_ADMIN_PASSWORD:-admin123}
      WORDPRESS_EMAIL: admin@example.com
    volumes:
      - wordpress_data:/bitnami/wordpress
    depends_on:
      - db
    restart: always

  db:
    image: bitnami/mysql:8.0
    container_name: wordpress-db
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD:-root}
      MYSQL_DATABASE: ${WORDPRESS_DB_NAME:-wordpress}
      MYSQL_USER: ${WORDPRESS_DB_USER:-wordpress}
      MYSQL_PASSWORD: ${WORDPRESS_DB_PASSWORD:-wordpress}
    volumes:
      - db_data:/bitnami/mysql/data
    restart: always

volumes:
  wordpress_data:
  db_data:
```

### Bitnamiイメージのメリット

- **セキュリティ強化** - 最小限のユーザー権限で動作
- **wp-cli同梱** - コマンドラインツールが最初から利用可能
- **SSL/TLS対応** - HTTPSポート（8443）がデフォルトで開放
- **初期ユーザー設定** - 環境変数で管理者アカウント作成可能

### 起動と初期設定

```console
$ docker compose up -d

# ブラウザでアクセス（HTTP）
$ open http://localhost:8080

# またはHTTPS
$ open https://localhost:8443

# wp-cliで操作
$ docker compose exec wordpress wp user list
```

## Bitnamiイメージ単体での構成

WordPressとPHPをまとめたワンイメージで、データベースは外部に用意する方法：

```yaml
# compose.yaml
services:
  wordpress:
    image: bitnami/wordpress:latest
    ports:
      - "8080:80"
      - "8443:443"
    environment:
      WORDPRESS_DATABASE_HOST: ${DB_HOST:-db}
      WORDPRESS_DATABASE_NAME: ${WORDPRESS_DB_NAME:-wordpress}
      WORDPRESS_DATABASE_USER: ${WORDPRESS_DB_USER:-wordpress}
      WORDPRESS_DATABASE_PASSWORD: ${WORDPRESS_DB_PASSWORD:-wordpress}
      WORDPRESS_USERNAME: admin
      WORDPRESS_PASSWORD: ${WORDPRESS_ADMIN_PASSWORD:-admin123}
    volumes:
      - wordpress_data:/bitnami/wordpress
    restart: always

volumes:
  wordpress_data:
```

このパターンはマネージドデータベース（AWS RDS、Azure Databaseなど）を外部で使用する場合に有効です。

## よくある使い方

### MariaDBを使いたい

MySQL 8.0の代わりにMariaDBを使う場合：

```yaml
db:
  image: mariadb:11
  container_name: wordpress-db
  environment:
    MARIADB_DATABASE: ${WORDPRESS_DB_NAME:-wordpress}
    MARIADB_USER: ${WORDPRESS_DB_USER:-wordpress}
    MARIADB_PASSWORD: ${WORDPRESS_DB_PASSWORD:-wordpress}
    MARIADB_ROOT_PASSWORD: ${MARIADB_ROOT_PASSWORD:-root}
  volumes:
    - db_data:/var/lib/mysql
  restart: always
```

**MySQLとMariaDBの比較：**

| 項目 | MySQL 8.0 | MariaDB 11 |
|---|---|---|
| 公式サポート | Oracle | MariaDB Foundation |
| パフォーマンス | 標準 | 高速（InnoDB最適化） |
| ライセンス | GPL v2 | GPL v2 |
| 互換性 | 標準 | MySQL 互換 |
| 推奨用途 | 汎用 | 高性能が必要な場合 |

### WordPressの管理ツール（wp-cli）を使いたい

wp-cliを使ってコマンドラインで操作できます：

```console
# wp-cli をコンテナ内で実行
$ docker compose exec wordpress wp user create testuser test@example.com --user_pass=password --role=editor

# プラグインをインストール
$ docker compose exec wordpress wp plugin install hello-dolly

# テーマをインストール
$ docker compose exec wordpress wp theme install twentytwentythree

# 現在のサイト情報を表示
$ docker compose exec wordpress wp option list
```

### サイトURLを変更したい

セットアップ後にサイトURLを変更する場合：

```console
$ docker compose exec wordpress wp option update siteurl "https://example.com"
$ docker compose exec wordpress wp option update home "https://example.com"
```

### ボリュームを削除したい（リセット）

すべてのデータを削除して初期化：

```console
# コンテナを停止
$ docker compose down -v

# -v フラグでボリュームも削除される
```

### ポート 80 を別のポートにしたい

```yaml
ports:
  - "3000:80"  # ローカルの 3000 番ポートを使用
```

### 複数の WordPress インスタンスを実行したい

複数のサービスを追加：

```yaml
version: '3.8'

services:
  wordpress1:
    image: wordpress:latest
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db1
      WORDPRESS_DB_NAME: wordpress1
    depends_on:
      - db1

  db1:
    image: mysql:8.0
    environment:
      MYSQL_DATABASE: wordpress1
      MYSQL_ROOT_PASSWORD: root

  wordpress2:
    image: wordpress:latest
    ports:
      - "8081:80"
    environment:
      WORDPRESS_DB_HOST: db2
      WORDPRESS_DB_NAME: wordpress2
    depends_on:
      - db2

  db2:
    image: mysql:8.0
    environment:
      MYSQL_DATABASE: wordpress2
      MYSQL_ROOT_PASSWORD: root

volumes:
  wordpress1_data:
  db1_data:
  wordpress2_data:
  db2_data:
```

### HTTPS（SSL/TLS）を有効にしたい

リバースプロキシ（Nginxなど）を追加：

```yaml
services:
  wordpress:
    # ...既存の設定...

  db:
    # ...既存の設定...

  nginx:
    image: nginx:alpine
    ports:
      - "443:443"
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./certs:/etc/nginx/certs:ro
    depends_on:
      - wordpress
```

### データベースのバックアップを取りたい

```console
# MySQL ダンプを作成
$ docker compose exec db mysqldump -u wordpress -pwordpress wordpress > backup.sql

# バックアップを復元
$ docker compose exec -T db mysql -u wordpress -pwordpress wordpress < backup.sql
```

### WordPress ファイルに直接アクセスしたい

```console
# ローカルにボリュームをマウント（bind volume の場合）
$ docker compose exec wordpress ls -la /var/www/html

# ファイルをコピー
$ docker cp wordpress-dev:/var/www/html/wp-config.php ./wp-config.php
```

### 別のバージョンの WordPress を使いたい

```yaml
wordpress:
  image: wordpress:6.2  # 特定バージョンを指定
```

利用可能なタグ：[WordPress Docker Hub Tags](https://hub.docker.com/_/wordpress?tab=tags)

## トラブルシューティング

### データベース接続エラーが出る

`WORDPRESS_DB_HOST` がデータベースのサービス名と一致していることを確認：

```yaml
# db サービスの場合、以下のように設定
environment:
  WORDPRESS_DB_HOST: db
```

### パーミッションエラーが出る

ボリュームのパーミッションを確認：

```console
$ docker compose exec wordpress ls -la /var/www/html
```

WordPressディレクトリは`www-data`ユーザーが所有する必要があります。

### wp-cliが見つからないエラー

WordPressイメージにwp-cliは含まれていません。
docker-compose内で実行するか、別途インストールしてください：

```console
$ docker compose exec wordpress curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
$ docker compose exec wordpress php wp-cli.phar --version
```

## リファレンス

- [wordpress - Docker Hub](https://hub.docker.com/_/wordpress)
- [mysql - Docker Hub](https://hub.docker.com/_/mysql)
- [mariadb - Docker Hub](https://hub.docker.com/_/mariadb)
- [WordPress 公式ドキュメント](https://wordpress.org/)
- [wp-cli 公式ドキュメント](https://wp-cli.org/)
