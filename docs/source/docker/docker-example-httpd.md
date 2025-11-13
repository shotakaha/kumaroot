# ウェブサーバーしたい（``httpd``）

```yaml
services:
  web:
    image: httpd:2.4
    container_name: my-httpd
    ports:
      - "8080:80"
```

Dockerを使ってApacheサーバーで遊んでみようと思います。
Apacheコンテナーのイメージ名は[httpd](https://hub.docker.com/_/httpd/)です。

起動・停止コマンドは以下の通りです。

```console
$ docker compose up -d
$ docker compose down
```

コンテナーが起動したらブラウザで
``http://localhost:8080``
を開いて「It works!」と表示されていればOKです。

## コマンドを追加したい（``apt-get``）

```console
$ docker compose exec web bash
(my-httpd) $ apt-get update

(my-httpd) $ apt-get install less
(my-httpd) $ which less
/usr/bin/less

(my-httpd) $ apt-get install vim
(my-httpd) $ which vim
/usr/bin/vim
```

公式レジストリから取得したイメージには、（使い慣れた）コマンドが入っていないことがあります。
コンテナーの中で ``apt-get`` を使って追加できます。
ここでは ``less`` と ``vim`` をインストールしています。

## 設定ファイルを確認したい（``httpd.conf``）

```bash
$ docker compose exec web bash
(my-httpd) $ find . -name httpd.conf
./conf/original/httpd.conf
./conf/httpd.conf
(my-httpd) $ less conf/httpd.conf
```

Apacheサーバー設定のファイル名は ``httpd.conf`` です。
ファイルの場所が分からない場合は[findコマンド](../command/command-find.md)で検索できます。
このコンテナーでは {file}`/usr/local/apache2/conf/httpd.conf` にありました。

## トップページを変更したい

```bash
$ docker compose exec web bash
(my-httpd) $ grep "DocumentRoot" conf/httpd.conf
DocumentRoot "/usr/local/apache2/htdocs"
(my-httpd) $ vi htdocs/index.html
```

設定ファイル（{file}`httpd.conf`）の中で、ドキュメントルートとなっているディレクトリを探します。
[grepコマンド](../command/command-grep.md)で``DocumentRoot`` という文字列を検索すると、{file}`/usr/local/apache2/htdocs/` であることが分かりました。

トップページを変更する場合は {file}`htdocs/index.html` を編集すればよいです。
また、他にもウェブサーバーで公開したいファイルは、このドキュメントルートの下に配置すればOKです。

## リファレンス

- [httpd - DockerHub](https://hub.docker.com/_/httpd)
- [Apache 2.4 ドキュメント](https://httpd.apache.org/docs/2.4/ja/)
