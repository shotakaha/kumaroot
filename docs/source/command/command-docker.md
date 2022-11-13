# docker

```bash
$ docker run イメージ
```

詳しいことは[](../docker/docker-usage.md)に整理しています。



## 起動しているコンテナを確認したい

```bash
$ docker ps
$ docker ps --all # 停止しているコンテナも確認
```

## コンテナに名前をつけて起動したい

```bash
$ docker run --name コンテナ名 イメージ
```

## コンテナを起動したい

```bash
$ docker start コンテナ名
$ docker stop コンテナ名
```

## リポジトリにあるイメージを使いたい

```bash
$ docker pull イメージ
```

## ダウンロード済みのイメージを確認したい

```bash
$ docker images
```

## コンテナ内のシェルを使いたい

```bash
$ docker exec -it コンテナ名 sh
```

## コンテナを削除したい

```bash
$ docker stop コンテナ名
$ docker rm コンテナ名
```

## コンテナのログを確認したい

```bash
$ docker logs -f container_name
```

## カスタマイズしたイメージを作りたい

```bash
$ docker build -t タグ名 .
```

{file}`.`（カレントディレクトリ）にある{file}`Dockerfile`の中身に沿って、カスタマイズしたイメージを作成できます。
