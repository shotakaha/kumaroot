# Nginxしたい

```console
// コンテナを起動
$ docker container run -d -p 8080:80 --name my-nginx nginx

$ docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                  NAMES
ce82e0791213   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp   my-nginx

// コンテナを停止＆削除
$ docker stop my-nginx
$ docker rm my-nginx
```

DockerHubにある公式イメージを使って``nginx``をバックグラウンドで起動（``-d``）します。
ポートは8080番を指定（``-p 8080:80``）し、コンテナ名は``my-nginx``（``--name my-nginx``）としています。
``http://localhost:8080``にアクセスすると「Welcome to nginx!」と表示されるはずです。

## 設定ファイルを確認したい

```console
// nginxを起動した状態でコンテナにログインする
$ docker exec -it my-nginx bash
(my-nginx) $ ls -l /etc/nginx/conf.d/
(my-nginx) $ cat /etc/nginx/conf.d/default.conf
```

``nginx``の設定はコンテナ内の``/etc/nginx/conf.d/``に保存されています。
初期設定では``default.conf``しかありません。
このファイルを上書きするか、このディレクトリに設定ファイルを追加します。

また、このファイルの``location``設定を確認すると、現在表示されているトップページのパスが分かります。
パスは``/usr/share/nginx/html/``に設定されていました。

## エディタを使いたい

```bash
(my-nginx) $ apt-get update
(my-nginx) $ apt-get vim
```

イメージから起動したコンテナには（使い慣れている）エディタがありません。
``apt-get``コマンドを使って``vim``を追加できます。

## HTTPSしたい

## Composeしたい

```yaml
# compose.yaml
services:
  nginx:
    image: nginx:1.22
    ports:
      - "8080:80"
    # bind volumes
    volumes:
      - ./html:/usr/share/nginx/html
```

## リファレンス

- [nginx- DockerHub](https://hub.docker.com/_/nginx)
