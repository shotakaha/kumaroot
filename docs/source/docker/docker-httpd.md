# ウェブサーバーしたい（``httpd``）

```bash
$ docker run -d -p 8080:80 --name my-httpd httpd
```

代表的なApacheをDockerを使って遊んでみようと思います。
Apacheコンテナのイメージ名は[httpd](https://hub.docker.com/_/httpd/)です。
ポート番号を8080番（``-p 8080:80``）し、コンテナの名前を``my-httpd``（``--name httpd``）として起動しています。
コンテナが起動したらブラウザで``http://localhost:8080``を開いて「It works!」と表示されていればOKです。

コンテナには任意の名前をつけることができます。
僕はテスト時には``my-イメージ名``とつけることにしています。
以下では、このコンテナ名を使って、起動したコンテナに``docker exec -it``でログインしています。

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

公式レジストリから取得したイメージには、（使い慣れた）コマンドが入っていないことがあります。
コンテナの中で``apt-get``を使って追加できます。
この場合は``less``と``vim``をインストールしています。

## 設定ファイルを確認したい（``httpd.conf``）

```bash
$ docker exec -it my-httpd bash
(my-httpd) $ find . -name httpd.conf
./conf/original/httpd.conf
./conf/httpd.conf
(my-httpd) $ less conf/httpd.conf
```

Apacheサーバー設定のファイル名は``httpd.conf``です。
ファイルの場所が分からない場合は[findコマンド](../command/command-find.md)で検索できます。
このコンテナでは{file}``/usr/local/apache2/conf/httpd.conf``にありました。

## トップページを変更したい

```bash
$ docker exec -it my-httpd bash
(my-httpd) $ grep "DocumentRoot" conf/httpd.conf
DocumentRoot "/usr/local/apache2/htdocs"
(my-httpd) $ vi htdocs/index.html
```

まず、設定ファイル（{file}`httpd.conf`）の中で、ドキュメントルートとなっているディレクトリを探します。
設定ファイルに対して[grepコマンド](../command/command-grep.md)を使い``DocumentRoot``という文字列を検索しました。
すると、ドキュメントルートは{file}`/usr/local/apache2/htdocs/`であることが分かりました。

トップページを変更する場合は{file}`htdocs/index.html`を編集すればよさそうです。
また、他にもウェブサーバーで公開したいファイルは、このドキュメントルートの下に配置すればOKです。

## リファレンス

- [httpd - DockerHub](https://hub.docker.com/_/httpd)
- [Apache 2.4 ドキュメント](https://httpd.apache.org/docs/2.4/ja/)
