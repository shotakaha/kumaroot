# Nginxしたい

```yaml
services:
  nginx:
    image: nginx
    container_name: my-nginx
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
```

DockerHubにある公式イメージを使って``nginx``を起動します。
ポート8080番を指定し、ローカルの`./html`ディレクトリをNginxのドキュメントルート（`/usr/share/nginx/html`）にマウントしています。

起動・停止コマンドは以下の通りです。

```console
$ docker compose up -d
$ docker compose down
```

コンテナーが起動したらブラウザで`http://localhost:8080`にアクセスすると「Welcome to nginx!」と表示されるはずです。

## エディターを使いたい

```console
$ docker compose exec nginx bash
(my-nginx) $ apt-get update
(my-nginx) $ apt-get install vim
(my-nginx) $ which vim
/usr/bin/vim
```

イメージから起動したコンテナには（使い慣れている）エディタがありません。
``apt-get`` コマンドを使って ``vim`` を追加できます。

## 設定ファイルを確認したい

```console
$ docker compose exec nginx bash
(my-nginx) $ ls -l /etc/nginx/conf.d/
(my-nginx) $ cat /etc/nginx/conf.d/default.conf
```

``nginx``の設定はコンテナー内の``/etc/nginx/conf.d/``に保存されています。
初期設定では``default.conf``しかありません。
このファイルを上書きするか、このディレクトリに設定ファイルを追加します。

このファイルの``location``設定を確認すると、現在表示されているトップページのパスが分かります。
パスは``/usr/share/nginx/html/``に設定されていました。

## リファレンス

- [nginx- DockerHub](https://hub.docker.com/_/nginx)
