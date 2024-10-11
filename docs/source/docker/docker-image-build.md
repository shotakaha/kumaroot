# コンテナイメージを作成したい（``docker image build``)

```console
$ docker image build パス
$ docker image build .
```

`docker image build`コマンドで、
``Dockerfile``でカスタマイズしたイメージを作成できます。
パスには``Dockerfile``があるディレクトリを指定する必要があります。
カレントディレクトリの場合は``.``を指定します。

## イメージ名したい（``-t`` / ``--tag``）

```console
$ docker image build パス -t イメージ名:タグ
$ docker image build . -t イメージ名:タグ
```

`-t`オプションで、イメージ名:タグ設定できます。
イメージ名をつけとくと、あとからイメージを参照するときに便利です。

## イメージを更新したい

```console
// 起動中のコンテナ情報を確認する
$ docker container ls

// コンテナを停止する
$ docker container stop コンテナ名

// イメージを再作成する
$ docker image build . -t イメージ名

// 新しいイメージでコンテナを起動する
$ docker container run イメージ名
```

イメージをカスタムしているときのデバッグ手順です。
イメージを更新して、コンテナを再起動して確認しています。
同じコンテナを複数起動するとエラーがでるため、一度停止してから再起動します。

## プラットフォームを変更したい（``--platform``）

```console
$ docker image build --platform=プラットフォーム名

// raspberry pi用のイメージ
$ docker image build --platform=linux/arm64
```

``--platform``オプションで、イメージをビルドするプラットフォーム（＝OSとアーキテクチャ）を変更できます。

| Platform | OS | Architecture | 対象機器 |
|---|---|---|---|
| `linux/amd64` | Linux | 64bit x86 | Intel / AMD |
| `linux/arm64` | Linux | 64bit ARM | Apple Silicon / Raspberry Pi4 |
| `linux/arm/v7` | Linux | 32bit ARM | Raspberry Pi3 |
| `windows/amd64` | Windows | 64bit x86 | WindowsPC |


## リファレンス

- [docker image build - docs.docker.com](https://docs.docker.com/reference/cli/docker/image/build/)
