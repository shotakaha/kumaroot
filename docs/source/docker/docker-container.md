# コンテナ操作したい（``docker container``）

```bash
# イメージ名を指定してコンテナを起動する
$ docker container run イメージ名:タグ コマンド

# 起動中のコンテナ情報を確認する
$ docker container ps

# 起動中のコンテナに接続する
$ docker container exec コンテナ名 コマンド

# コンテナを停止する
$ docker container stop コンテナ名 [コンテナ名...]

# コンテナを削除する
$ docker container rm コンテナ名 [コンテナ名...]
```

``container``コマンドは、Dockerのコンテナ操作コマンドを整理するために、Docker 17.06以降に導入されたサブコマンドです。
``docker 操作名``と``docker container 操作名``は基本的に同じものです。



## リファレンス

- [docker container - docs.docker.com](https://docs.docker.com/reference/cli/docker/container/)
