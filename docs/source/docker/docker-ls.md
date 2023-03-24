# コンテナの状態を調べたい（``ls``）

```bash
$ docker image ls
$ docker container ls
$ docker volume ls
$ docker network ls
$ docker plugin ls
```

``docker``の管理コマンド（``Management Commands``）は``ls``や``inspect``で詳細を調べることができます。

## イメージを調べたい（``docker image inspect``）

```bash
$ docker image ls
$ docker image inspect イメージ名
```

ダウンロード済みのイメージ一覧を表示して、イメージ名を確認できます。
``docker image ls``は``docker images``と（たぶん）同じです。

## コンテナを調べたい（``docker container inspect``）

```bash
$ docker container ls
$ docker container inspect コンテナ名
```

起動しているコンテナ一覧を表示して、コンテナ名を確認できます。
``docker container ls``は``docker ps``と（たぶん）同じです。

## ボリュームを調べたい（``docker volume inspect``）

```bash
$ docker volume ls
$ docker volume inspect ボリューム名
```

ボリューム一覧を表示して、ボリューム名を確認できます。

## ネットワークを調べたい（``docker network inspect``）

```bash
$ docker network ls
$ docker network inspect ネットワーク名
```

## プラグインを調べたい（``docker plugin inspect``）

```bash
$ docker plugin ls
$ docker plugin inspect プラグイン名
```
