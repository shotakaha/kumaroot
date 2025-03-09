# 新旧コマンド対応表

Docker 1.13（2017年1月）から、コマンド体系が変更されました。
従来はフラットなコマンド体系でしたが、
現在は`docker 操作対象 コマンド`というサブコマンド体系になっています。
ウェブの記事を検索すると、旧コマンドで書かれているものも多いため、
よく使うコマンドの新旧対応表を作成しました。

## コンテナ操作（`docker container`）

| 旧コマンド | 新コマンド |
|---|---|
| `docker ps` | `docker container ls` |
| `docker rm <ID>` | `docker container rm <ID>` |
| `docker inspect <ID>` | `docker container inspect <ID>` |
| `docker logs <ID>` | `docker container logs <ID>` |

## イメージ操作（`docker image`）

| 旧コマンド | 新コマンド |
|---|---|
| `docker images` | `docker image ls` |
| `docker rmi <IMAGE>` | `docker image rm <IMAGE>` |
| `docker inspect <IMAGE>` | `docker image inspect <IMAGE>` |

## ボリューム操作（`docker volume`）

| 旧コマンド | 新コマンド |
|---|---|
| `docker volume ls` | 変更なし |
| `docker volume rm <VOLUME>` | 変更なし |

## Compose操作（`docker compose`）

| 旧コマンド | 新コマンド |
|---|---|
| `docker-compose.yaml` | `compose.yaml` |
| `docker-compose <SUBCMD>` | `docker compose <SUBCMD>` |
