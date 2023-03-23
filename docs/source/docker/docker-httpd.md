# apacheしたい（``httpd``）

```bash
$ docker run -d -it -p 8080:80 --name my-httpd httpd
```

Apacheコンテナのイメージ名は``httpd``です。
ポート番号を8080番（``-p 8080:80``）し、コンテナ名を``my-httpd``（``--name httpd``）として起動しています。

コンテナが起動したらブラウザで``http://localhost:8080``を開いて「It works!」と表示されていればOKです。

## コマンドを追加したい（``apt-get``）

```bash
$ docker excec -it my-httpd bash
(my-httpd) $ apt-get update
(my-httpd) $ apt-get install less
(my-httpd) $ which less
/usr/bin/less
(my-httpd) $ apt-get install vim
(my-httpd) $ which vim
/usr/bin/vim
```

コンテナには（使い慣れた）コマンドが入っていないことがあります。
``apt-get``を使って追加でインストールできます。
この場合は``less``と``vim``をインストールしています。

## 設定ファイルを確認したい（``httpd.conf``）

```bash
$ docker exec -it my-apache bash
(my-apache) $ find . -name httpd.conf
./conf/original/httpd.conf
./conf/httpd.conf
(my-apache) $ less conf/httpd.conf
```

Apacheのサーバー設定は``httpd.conf``に書かれています。
ファイルの場所は``find``コマンドで検索しましょう。
このコンテナ内では``/usr/local/apache2/conf/httpd.conf``にありました。

## トップページを変更したい

```bash
$ docker exec -it my-httpd bash
(my-httpd) $ grep "DocumentRoot" conf/httpd.conf
DocumentRoot "/usr/local/apache2/htdocs"
(my-httpd) $ vi htdocs/index.html
```

まず、トップページを表示しているファイルを探します。
設定ファイル（``httpd.conf``）に書かれているドキュメントルート（``DocumentRoot``）を調べたところ、``/usr/local/apache2/htdocs/``であることが分かりました。

なので、トップページは``htdocs/index.html``を編集すればOKです。
他にもApacheコンテナで公開したいファイルは、このドキュメントルートの下に配置すればOKです。


## リファレンス

- [httpd - DockerHub](https://hub.docker.com/_/httpd)
