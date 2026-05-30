# Nginxしたい（`nginx`）

```{literalinclude} ../../examples/docker/nginx.yaml
---
language: yaml
---
```

## コンテナーを起動したい

```console
$ docker compose up -d
```

## コンテナーで操作したい

```console
$ docker compose exec nginx bash
```

## コンテナーを終了したい

```console
$ docker compose down
```

## Nginxについて

Nginxは高速で軽量なウェブサーバーのDockerイメージです。起動後、ブラウザで `http://localhost:8080` を開いて「Welcome to nginx!」と表示されればOKです。ローカルの `./html` ディレクトリがNginxのドキュメントルート（`/usr/share/nginx/html`）にマウントされているため、このディレクトリにHTMLファイルを配置すればウェブサーバーで公開できます。コンテナー内で `apt-get install` を使ってツールを追加することもできます。
