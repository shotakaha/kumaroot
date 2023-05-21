# ウェブサーバーしたい（``nginx``）

```bash
$ docker run -d -p 8082:80 --name my-nginx nginx
$ docker excec -it my-nginx
(my-nginx) $ nginx
nginx version: nginx/1.23.3
(my-nginx) $ pwd
/
```

最近シェアが増えてきているという``Nginx``の設定方法を確認します。
ここではApacheと同じように、Dockerで起動したNginxサーバーのコンテナを使って、設定内容を調べています。

## サーバーを操作したい

```bash
$ nginx -s stop
$ nginx -s quit
$ nginx -s reload
$ nginx -s reopen
```

## 設定ファイルを確認したい（``nginx.conf``）

```bash
$ find . -name *.conf | grep nginx
./etc/nginx/nginx.conf
./etc/nginx/conf.d/default.conf
```

設定ファイルの名前は``nginx.conf``です。
上のコマンドでは拡張子が``*.conf``で、``nginx``の文字列を含むパスを検索しています。
メインの設定ファイル（``/etc/nginx/nginx.conf``）と、追加のファイル（``/etc/nginx/conf.d/*.conf``）が見つかりました。

設定ファイルには各種の「ディレクティブ」がすでに書き込まれていて、サーバー設定の確認がができます。
また、このディレクティブを書き換えることで設定を変更できます。

Nginxのディレクティブには``simple directive``と``block directive``の主に2種類の書き方があります。
そしてディレクティブの中にディレクティブを持つ構造を``context``と呼びます。

## 設定ファイルのシンタックス確認（``nginx -t``）

```bash
$ nginx -t
$ nginx -T
```

設定ファイルのシンタックス（＝書き方）が正しいかチェックできます。
設定を書き換えた場合、サーバーを再起動する前には必ずチェックするとよいです。

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
