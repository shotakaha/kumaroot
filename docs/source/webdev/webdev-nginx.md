# ウェブサーバーしたい（``nginx``）

```bash
$ docker run -d -p 8082:80 --name my-nginx nginx
$ docker excec -it my-nginx
(my-nginx) $ pwd
/
```

最近シェアが増えてきているという``Nginx``の設定方法を確認します。
Apacheと同じように、Dockerで起動したNginxサーバーのコンテナを使っています。

## 設定ファイルを確認したい

```bash
$ find . -name *.conf | grep nginx
./etc/nginx/nginx.conf
./etc/nginx/conf.d/default.conf
```

設定ファイルの拡張子は``*.conf``で、``nginx``の文字列を含むパスを検索しています。

## ドキュメントルートを確認したい

## ログフォーマットを確認したい

## SSLを有効化したい

## ユーザーごとのディレクトリを有効にしたい
