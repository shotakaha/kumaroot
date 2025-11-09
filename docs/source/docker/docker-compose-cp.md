# ファイルをコピーしたい（``docker compose cp``）

```console
// ホスト -> コンテナ
$ docker compose cp ホストOSのパス コンテナ名:コンテナ内のパス

// コンテナ -> ホスト
$ docker compose cp コンテナ名:コンテナ内のパス ホストOSのパス
```

`docker compose cp`でホストPCとコンテナ間のファイルやフォルダのコピーができます。
引数の順番を入れ替えるだけで、双方向のコピーが可能です。
コンテナを指定する書式は`ssh`や`rsync`などと同じです。

`コンテナ名:コンテナ内のパス`の形式で、コロン（`:`）でコンテナ名とコンテナ内のパスを区切ります。
パスは絶対パスでも相対パスでも指定できます。
相対パスの場合はコンテナの作業ディレクトリ（`WORKDIR`）が基準になります。

## ホストからコンテナにコピーしたい

```console
$ docker compose cp config.yaml app:/etc/config.yaml
$ docker compose cp ./data/ db:/data/
```

ホスト側のファイルやディレクトリをコンテナにコピーできます。
例えば、設定ファイルをコンテナにコピーしたり、データをコンテナ内に転送する際に使用します。

## コンテナからホストにコピーしたい

```console
$ docker compose cp app:/var/log/app.log ./logs/
$ docker compose cp db:/var/lib/mysql/data.sql ./backup/
```

コンテナ内のファイルやディレクトリをホスト側にコピーできます。
例えば、ログファイルをホスト側に取得したり、データベースのバックアップをホスト側に保存する際に使用します。

:::{note}

targetディレクトリについて

ファイルをコピーする際、targetがディレクトリの場合は自動的にファイルがそのディレクトリ内に配置されます。
targetディレクトリが存在しない場合は、自動で作成されます。
ファイルのタイムスタンプと権限も保持されます。

:::

## リファレンス

- [docker compose cp - docs.docker.jp](https://docs.docker.jp/engine/reference/commandline/compose_cp.html)
