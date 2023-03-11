# コンテナイメージを作成したい（``build``)

```bash
$ docker build -t イメージ名
```

``Dockerfile``をもとにコンテナイメージを作成します。
``-t イメージ名``オプションをつけて、後から参照できるようにしておきます。

## ベースイメージを指定したい（``FROM``）

```dockerfile
FROM イメージ名:タグ
```

``Dockerfile``の先頭に、ベースとして使うイメージ名を指定します。
利用できるイメージ名は[Docker Hub](https://hub.docker.com/)などで検索できます。
