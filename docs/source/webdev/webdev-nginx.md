# ウェブサーバーしたい（``nginx``）

```bash
$ docker run -d -p 8082:80 --name my-nginx nginx
$ docker excec -it my-nginx
(my-nginx) $ pwd
/
```

最近シェアが増えてきているという``Nginx``の設定方法を確認します。
Apacheと同じように、Dockerで起動したNginxサーバーのコンテナを使っています。

## 設定ファイルを確認したい（``nginx.conf``）

```bash
$ find . -name *.conf | grep nginx
./etc/nginx/nginx.conf
./etc/nginx/conf.d/default.conf
```

設定ファイルの拡張子は``*.conf``で、``nginx``の文字列を含むパスを検索しています。

設定ファイルに「ディレクティブ」を記述し、モジュールを制御します。
ディレクティブには``simple directive``と``block directive``の主に2種類の書き方があります。
そしてディレクティブの中にディレクティブを持つ場合は``context``と呼びます。

## ポート番号を確認したい（``listen``）

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name localhost;
}
```

## 公開用ディレクトリを確認したい（``location``）

```nginx
server {
    location / {
        root /usr/share/nginx/html;
        index index.html index.htm;
    }
}
```

## ログフォーマットを確認したい（``log_format``）

```nginx
http {
    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for"';

    access_log /var/log/nginx/access.log main;
}
```

Apacheの``combined``ログ形式と同じフォーマットです。

## SSLを有効化したい

## ユーザーごとのディレクトリを有効にしたい


## リファレンス

- [Nginx ドキュメント](https://nginx.org/en/docs/)
