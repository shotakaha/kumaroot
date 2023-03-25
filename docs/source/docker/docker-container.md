# コンテナを起動したい（``docker container run``）

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

``イメージ名:タグ``を指定して、コンテナを起動します。
タグを指定しない場合は最新版（``latest``）のイメージが適用されます。
起動中のコンテナ情報は``docker ps``で確認できます。

``docker run``コマンドにはたくさんのオプションがあります。
これらのオプションを使うことで、公開されているイメージを少しだけカスタマイズしてローカル開発ができます。

## コンテナに名前をつけたい（``--name``）

```bash
$ docker container run --name コンテナ名
```

``--name``オプションを使って、コンテナに名前をつけることができます。
デフォルトではDockerがランダムなコンテナ名（≠イメージ名）を割り当てます。
僕は``my-イメージ名``という名前をよく使います。

コンテナの状態を確認したり、停止や削除などのコンテナ操作をする際に、コンテナ名がついていると便利です。
ただし、同じ名前のコンテナは起動できないので、違う名前にするか、再起動する場合は、一度停止＆削除する必要があります。

## バックグラウンドで起動したい（``-d`` / ``--detach``）

```bash
$ docker container run -d イメージ名
```

``-d``オプションを使って、コンテナをバックグラウンドで起動できます。

## ポートを指定したい（``-p`` / ``--publish``）

```bash
$ docker container run -p ホスト側:コンテナ側
```

``-p``オプションを使って、ポート番号を指定できます。
ポート番号は``ホスト側:コンテナ側``の形式で記述します。
``http://localhost:ホスト側のポート番号``でコンテナにアクセスできます。

## 作業ディレクトリを指定したい（``-w`` / ``--workdir``）

```bash
$ docker container run -w コンテナ内の作業ディレクトリ
```

デフォルトの作業ディレクトリ``/（ルートディレクトリ）``になっています。
``-w``オプションを使ってコンテナ内の作業ディレクトリを指定できます。


## ボリュームを指定したい（``-v`` / ``--volume``）

```bash
$ docker container run -v ホスト側（named volume）:コンテナ側
$ docker container run -v ホスト側（bind volume）:コンテナ側
```

``-v``オプションを使って、データの保存先を指定できます。
保存先のパスは``ホスト側:コンテナ側``の形式で記述します。
``named volume``と``bind volume``のどちらでも同じように指定できます。

## コンテナ内のターミナルを使いたい（``-it`` / ``--interactive --tty``）

```bash
$ docker container run -it イメージ名 [コマンド]
$ docker container exec -it コンテナ名 [コマンド]

# Ubuntuコンテナのデフォルトシェル（sh）を起動したい
$ docker container run -it ubuntu:latest

# 起動しているUbuntuコンテナ（my-ubuntu）のbashを起動したい
$ docker container exec -it my-ubuntu bash
```

``-it``オプションを使って、コンテナ内のターミナル（``sh``）に接続できます。
すでに起動しているコンテナに接続する場合は``docker container exec``します。
