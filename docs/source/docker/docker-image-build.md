# コンテナイメージを作成したい（``docker image build``)

```console
$ docker image build パス
$ docker image build .
```

``Dockerfile``からコンテナイメージを作成します。
パスには``Dockerfile``があるディレクトリを指定する必要があります。
カレントディレクトリの場合は``.``を指定します。

## イメージ名したい（``-t`` / ``--tag``）

```console
$ docker image build パス -t イメージ名:タグ
$ docker image build . -t イメージ名:タグ
```

[-t イメージ名:タグ](https://docs.docker.com/reference/cli/docker/image/build/#tag)オプションで、イメージ名を設定できます。
このイメージ名は、後からイメージを参照する際に利用できます。

このようにして、DockerHubのレジストリにあるイメージをベースにして、自分用にイメージをカスタマイズできます。

## イメージを更新したい

```bash
# 起動中のコンテナ情報を確認する
$ docker ls

# コンテナを停止する
$ docker stop コンテナ名

# イメージを再作成する
$ docker build . -t イメージ名

# 新しいイメージでコンテナを起動する
$ docker run イメージ名
```

イメージを更新して、コンテナを再起動する手順を整理しました。
同じコンテナを複数起動するとエラーがでるので、一度停止してから再起動します。

## プラットフォームを変更したい（``--platform``）

```console
$ docker image build --platform=プラットフォーム名
$ docker image build --platform=linux/arm64
```

``--platform``オプションで、利用するプラットフォームに合わせてイメージをビルドできます。
``linux/arm64``はラズパイで使うツールをビルドするときに使いました。

## リファレンス

- [docker image build - docs.docker.com](https://docs.docker.com/reference/cli/docker/image/build/)
