# コンテナを起動したい（``docker container run``）

```console
// 推奨コマンド
$ docker container run オプション イメージ名 コマンド

// 初期コマンド
$ docker run オプション イメージ名 コマンド
```

``docker run``コマンドで``イメージ名:タグ``を指定して、コンテナを起動できます。
タグを指定しない場合は最新版（``latest``）のイメージが適用されます。
起動中のコンテナ情報は``docker container ps``で確認できます。

``docker conteiner run``コマンドにはたくさんのオプションがあります。
これらのオプションを使うことで、公開されているイメージを少しだけカスタマイズしてローカル開発ができます。

## コンテナに名前をつけたい（``--name``）

```bash
$ docker container run --name コンテナ名
```

``--name``オプションで、コンテナに名前をつけることができます。
デフォルトではDockerがランダムなコンテナ名（≠イメージ名）を割り当てます。
僕は``my-イメージ名``という名前をよく使います。

コンテナの状態を確認したり、停止や削除などのコンテナ操作をする際に、コンテナ名がついていると便利です。
ただし、同じ名前のコンテナは起動できないので、違う名前にするか、再起動する場合は、一度停止＆削除する必要があります。

## シェルしたい（``-it``）

```console
$ docker container run -it イメージ名 [コマンド]

// Ubuntuコンテナのデフォルトシェル（sh）を起動したい
$ docker container run -it ubuntu:latest
```

``-it``オプションを使って、コンテナ内のターミナル（``sh``）に接続できます。
すでに起動しているコンテナに接続する場合は[docker container exec](./docker-exec.md)します。

## ポートしたい（``-p`` / ``--publish``）

```console
$ docker container run -p ホスト側:コンテナ側

// localhost:8080 で（コンテナ:80に）アクセス
$ docker container run -p 8080:80 httpd:2.4
```

`-p`オプションを使って、ポート番号を指定し、port forwardingできます。
ポート番号の書式は``ホスト側:コンテナ側``です。
``http://localhost:ホスト側のポート番号``でコンテナにアクセスできます。

## バックグラウンドで起動したい（``-d`` / ``--detach``）

```bash
$ docker container run -d イメージ名
```

``-d``オプションを使って、コンテナをバックグラウンドで起動できます。

## ボリュームを指定したい（``-v`` / ``--volume``）

```console
// named volume
$ docker container run -v ホスト側（named volume）:コンテナ側

// bind volume
$ docker container run -v ホスト側（bind volume）:コンテナ側
```

``-v``オプションを使って、データの保存先を指定できます。
保存先のパスは``ホスト側:コンテナ側``の形式で記述します。
``named volume``と``bind volume``のどちらでも同じように指定できます。

## 作業ディレクトリを指定したい（``-w`` / ``--workdir``）

```bash
$ docker container run -w コンテナ内の作業ディレクトリ
```

デフォルトの作業ディレクトリ``/（ルートディレクトリ）``になっています。
``-w``オプションを使ってコンテナ内の作業ディレクトリを指定できます。


## リファレンス

- [docker container run - docs.docker.com](https://docs.docker.com/reference/cli/docker/container/run/)
