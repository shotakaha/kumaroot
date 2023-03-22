# apacheしたい（``httpd``）

```bash
$ docker run -d -it -p 8080:80 --name my-httpd httpd
```

Apacheサーバのイメージの名前は``httpd``です。
ポート番号を8080番に指定（``-p 8080:80``）し、コンテナ名を``my-httpd``（``--name httpd``）にして起動しています。

## エディタを使いたい（``vi``）

```bash
$ docker excec -it my-httpd bash
(my-httpd) $ apt-get update
(my-httpd) $ apt-get install vim
```

デフォルトのコンテナにはエディタが入っていません。
``apt-get install vim``して``vim``をインストールしておきます。

## 設定ファイルを編集したい（``httpd.conf``）

```bash
$ docker exec -it my-apache bash
(my-apache) $ find . -name httpd.conf
./conf/original/httpd.conf
./conf/httpd.conf
(my-apache) $ vi ./conf/httpd.conf
```

Apacheの設定は``httpd.conf``で書き換えることができます。
ファイルの場所が分からないときは``find``コマンドで検索しましょう。
このコンテナ内では``/usr/local/apache2/conf/httpd.conf``にあるので``vim``で編集します。

## リファレンス

- [httpd - DockerHub](https://hub.docker.com/_/httpd)
