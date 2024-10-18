# コンテナしたい（`docker`）

```console
$ docker container run --rm イメージ名:タグ名
```

詳しいことは[](../docker/docker-usage.md)に整理しています。

:::{note}

なにかしらの`docker`コマンドを実行して、次のメッセージが表示される場合は`Docker Desktop`アプリの起動が必要です。

```console
$ docker [SOME_DOCKER_CMD]
Cannot connect to the Docker daemon...
Is the docker daemon running?
```

:::

## イメージ名を検索したい（`docker search`）

```console
$ docker search キーワード

$ docker search ubuntu
$ docker search wordpress
```

`docker search`コマンドで、DockerHubにあるイメージ名を検索できます。

## コンテナに名前をつけたい

```console
$ docker run --name コンテナ名 イメージ:タグ名
$ docker container run --name コンテナ名 イメージ:タグ名
```

## 起動しているコンテナを確認したい

```console
$ docker ps
$ docker container ps

// 停止しているコンテナも確認
$ docker container ps --all
```

## 既存のコンテナを起動／停止したい

```console
$ docker container start コンテナ名
$ docker container stop コンテナ名
```

## ダウンロード済みのイメージを確認したい

```console
$ docker image ls
REPOSITORY                         TAG                           IMAGE ID       CREATED         SIZE
phpmyadmin                         5.2                           3a7ead4cecab   2 weeks ago     572MB
wordpress                          6.6                           20a23bd4a2e5   4 weeks ago     695MB
ubuntu                             24.10                         e967f2622b3a   4 weeks ago     108MB
python                             3.11-slim                     692282a38c50   5 weeks ago     155MB
mariadb                            11.5.2-noble                  e66739c8d350   6 weeks ago     435MB
httpd                              2.4                           a3e79aafef7f   3 months ago    178MB
httpd                              latest                        a3e79aafef7f   3 months ago    178MB
balenalib/raspberrypi4-64-python   bookworm-build-20240429       5eeca56e63bb   5 months ago    1.09GB
balenalib/raspberrypi4-64-python   bullseye-build-20240429       4b9714fe0218   5 months ago    939MB
balenalib/raspberrypi3-python      3.9-bookworm-build-20240429   a07637ab6f91   5 months ago    832MB
docker/welcome-to-docker           latest                        648f93a1ba7d   11 months ago   19MB

```

## コンテナ内のシェルを使いたい

```console
$ docker container exec -it コンテナ名 sh
$ docker container exec -it コンテナ名 bash
```

## コンテナを削除したい

```console
$ docker container stop コンテナ名
$ docker container rm コンテナ名
```

## コンテナのログを確認したい

```console
$ docker logs コンテナ名
$ docker container logs コンテナ名
```

## カスタマイズしたイメージを作りたい

```console
$ docker build --tag タグ名 .
$ docker image build --tag タグ名 .

// Dockerfileのパスを変更
$ docker build --file ファイル名 --tag タグ名 .
```

`docker build`コマンドで、カスタマイズしたイメージを作成できます。
設定は`Dockerfile`で定義します。
