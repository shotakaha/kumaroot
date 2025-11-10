# WordPressをBitnamiで構築したい

Bitnamiが提供するWordPressイメージを使用してセキュリティ強化された環境を構築します。
本番環境やセキュリティ重視の場合に推奨される方法です。

## 概要

Bitnamiイメージの特徴：

- **セキュリティ強化** - 最小限のユーザー権限で動作
- **wp-cli同梱** - コマンドラインツールが最初から利用可能
- **SSL/TLS対応** - HTTPSポート（8443）がデフォルトで開放
- **初期ユーザー設定** - 環境変数で管理者アカウント作成可能

利用可能なイメージ：

- [bitnami/wordpress](https://hub.docker.com/r/bitnami/wordpress) - WordPress + Apache + PHP
- [bitnami/mysql](https://hub.docker.com/r/bitnami/mysql) - MySQL
- [bitnami/mariadb](https://hub.docker.com/r/bitnami/mariadb) - MariaDB

## Bitnami + MySQLの構成

### compose.yaml を作成

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

### 環境変数の設定

`.env`ファイルを作成して環境変数をカスタマイズできます：

```env
# .env
WORDPRESS_DB_NAME=my_wordpress
WORDPRESS_DB_USER=wp_user
WORDPRESS_DB_PASSWORD=secure_password
MYSQL_ROOT_PASSWORD=root_password
WORDPRESS_ADMIN_PASSWORD=admin_password
```

## Bitnamiイメージ単体での構成

WordPressとPHPをまとめたワンイメージで、マネージドデータベース（AWS RDS、Azure Databaseなど）を外部で使用する場合：

```yaml
# compose.yaml
services:
  wordpress:
    image: bitnami/wordpress:latest
    ports:
      - "8080:80"
      - "8443:443"
    environment:
      WORDPRESS_DATABASE_HOST: ${DB_HOST:-db.example.com}
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

環境変数でデータベースホストを指定することで、外部のマネージドデータベースと連携できます。

## wp-cliの使用例

Bitnamiイメージにはwp-cliが同梱されているため、コマンドラインからWordPressを管理できます：

### ユーザー管理

```console
# ユーザー一覧を表示
$ docker compose exec wordpress wp user list

# 新規ユーザーを作成
$ docker compose exec wordpress wp user create author author@example.com --user_pass=password --role=author

# ユーザーのパスワードをリセット
$ docker compose exec wordpress wp user update admin --user_pass=newpassword
```

### プラグイン管理

```console
# プラグイン一覧を表示
$ docker compose exec wordpress wp plugin list

# プラグインをインストール
$ docker compose exec wordpress wp plugin install hello-dolly

# プラグインを有効化
$ docker compose exec wordpress wp plugin activate hello-dolly

# プラグインを無効化
$ docker compose exec wordpress wp plugin deactivate hello-dolly

# プラグインをアンインストール
$ docker compose exec wordpress wp plugin delete hello-dolly
```

### テーマ管理

```console
# テーマ一覧を表示
$ docker compose exec wordpress wp theme list

# テーマをインストール
$ docker compose exec wordpress wp theme install twentytwentythree

# テーマを有効化
$ docker compose exec wordpress wp theme activate twentytwentythree
```

### サイト設定

```console
# サイトのURLを変更
$ docker compose exec wordpress wp option update siteurl "https://example.com"
$ docker compose exec wordpress wp option update home "https://example.com"

# サイトのタイトルを変更
$ docker compose exec wordpress wp option update blogname "My WordPress Site"

# サイト情報を表示
$ docker compose exec wordpress wp option list | grep -E "siteurl|home|blogname"
```

### データベース操作

```console
# データベースをバックアップ
$ docker compose exec db mysqldump -u wordpress -pwordpress wordpress > backup.sql

# バックアップを復元
$ docker compose exec -T db mysql -u wordpress -pwordpress wordpress < backup.sql
```

## SSL/TLSの設定

### 自己署名証明書でHTTPSを使用

Bitnamiイメージはデフォルトで自己署名証明書を使用しており、HTTPSポート（8443）でアクセス可能です：

```console
# HTTPSでアクセス
$ open https://localhost:8443
```

ブラウザに警告が表示されますが、これは自己署名証明書であるためです。

### Let's Encryptで正式な証明書を使用

本番環境では、Let's Encryptなどのサービスで正式な証明書を取得し、以下のようにボリュームマウントします：

```yaml
services:
  wordpress:
    image: bitnami/wordpress:latest
    volumes:
      - wordpress_data:/bitnami/wordpress
      - ./certs:/bitnami/apache/conf/bitnami/certs:ro
```

証明書ファイルを`./certs/`ディレクトリに配置します：

```text
./certs/
├── server.crt
└── server.key
```

## トラブルシューティング

### パーミッションエラーが出る

Bitnamiイメージは`bitnami`ユーザーで動作します。
ボリュームのパーミッションを確認：

```console
$ docker compose exec wordpress ls -la /bitnami/wordpress
```

### wp-cliコマンドが失敗する

データベース接続情報が正しいか確認：

```console
$ docker compose exec wordpress wp db check
```

### SSL証明書エラーが出る

自己署名証明書を使用している場合、ブラウザに警告が表示されます。
本番環境では正式な証明書を使用してください。

## よくある使い方

### MariaDBを使いたい

MySQLの代わりにMariaDBを使う場合：

```yaml
db:
  image: bitnami/mariadb:11
  environment:
    MARIADB_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD:-root}
    MARIADB_DATABASE: ${WORDPRESS_DB_NAME:-wordpress}
    MARIADB_USER: ${WORDPRESS_DB_USER:-wordpress}
    MARIADB_PASSWORD: ${WORDPRESS_DB_PASSWORD:-wordpress}
  volumes:
    - db_data:/bitnami/mariadb/data
```

### ボリュームを削除してリセットしたい

```console
$ docker compose down -v
```

`-v`フラグでボリュームも削除され、すべてのデータが初期化されます。

### ログを確認したい

```console
# Wordpressのログ
$ docker compose logs -f wordpress

# データベースのログ
$ docker compose logs -f db
```

### 別のポートを使用したい

```yaml
wordpress:
  ports:
    - "3000:80"
    - "3443:443"
```

## リファレンス

- [bitnami/wordpress - Docker Hub](https://hub.docker.com/r/bitnami/wordpress)
- [bitnami/mysql - Docker Hub](https://hub.docker.com/r/bitnami/mysql)
- [bitnami/mariadb - Docker Hub](https://hub.docker.com/r/bitnami/mariadb)
- [Bitnami WordPress Container - GitHub](https://github.com/bitnami/containers/tree/main/bitnami/wordpress)
- [WordPress 公式ドキュメント](https://wordpress.org/)
- [wp-cli 公式ドキュメント](https://wp-cli.org/)
