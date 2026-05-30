# Apacheしたい（`httpd`）

```{literalinclude} ../../examples/docker/httpd.yaml
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
$ docker compose exec web bash
```

## コンテナーを終了したい

```console
$ docker compose down
```

## Apacheについて

Apacheはウェブサーバーのスタンダードです。起動後、ブラウザで `http://localhost:8080` を開いて「It works!」と表示されればOKです。Apacheのドキュメントルートは `/usr/local/apache2/htdocs/` です。このディレクトリ内のHTMLファイルがウェブサーバーで公開されます。コンテナー内で `apt-get install` でツールを追加したり、ログを確認したりできます。Apache 2.4系は継続的にセキュリティアップデートが提供されており、本番環境での使用に適しています。
