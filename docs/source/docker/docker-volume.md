# ボリュームしたい（``volume``）

```console
// ボリュームの確認
$ docker volume ls

// ボリュームを作成
$ docker volume create ボリューム名

```

`docker volume`コマンドで、コンテナ内のデータを永続化させるためのボリュームを操作できます。
ボリュームに紐づけておかないと、コンテナ内に作成したデータは、コンテナを削除するときに消えてしまいます。

ボリュームには`named volume`と`bind volume`の2種類があります。
`named volume`はDocker内部（＝``/var/lib/docker/volumes/...``）に作成されるボリュームです。
`binde volume`は、ホストPCのパスを、コンテナにマウントするボリュームです。

データベースなど、直接アクセスしなくてもよいデータは`named volume`、
設定ファイルやHTML／CSSなどのようにホストPCと同期させたいデータは`bind volume`で作成するとよいです。

## ボリュームの詳細を知りたい

```console
$ docker volume inspect ボリューム名
```

``named volume``を使ったときに、データが保存されているパスなどの詳細を確認できます。

## Composeしたい（`volumes`）

```yaml
services:
  コンテナ名:
    image: イメージ名:タグ
    volumes:
      # named volume
      - db-data:/var/lib/mysql
      # bind volume
      - ./html:/var/www/html
volumes:
  db-data
```

`compose.yaml`の`volumes`キーでボリュームを設定できます。
`docker compose up -d`するときに自動でボリュームを紐づけてくれます。

コンテナを削除（`docker compose down`）しても、ボリュームは残ります。
ボリュームも削除する場合は`docker compose down --volumes`します。
