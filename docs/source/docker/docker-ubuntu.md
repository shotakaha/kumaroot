# Ubuntuを使いたい

```bash
$ docker run -d --name my-ubuntu ubuntu
$ docker exec -it my-ubuntu bash
```

Ubuntuコンテナをバックグラウンドで起動（``-d``）します。
コンテナ名は``my-ubuntu``（``--name my-ubuntu``）としています。
起動したコンテナに接続（``docker exec -it``）し``bash``に切り替えます。

## コンテナを削除したい

```bash
# コンテナ名を確認する
$ docker ps

# コンテナを停止する
$ docker stop my-ubuntu

# コンテナを削除する
$ docker rm my-ubuntu
```

起動時に指定したコンテナ名を使って、コンテナを停止（``stop``）してから削除（``rm``）します。

## リファレンス

- [Ubuntu Official Image - DockerHub](https://hub.docker.com/_/ubuntu/)
