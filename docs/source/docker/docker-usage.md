# Docker の使い方

Dockerはコンテナ型仮想化技術を使ったプラットフォームです。
プロダクション環境の構築や複製作業を簡単にしたり、
開発環境の構築をサポートするために使います。

ここでは主に、複数のパソコンで同じ開発環境を構築する手順を整理します。
{file}`Dockerfile`というビルドスクリプトをベースにコンテナイメージを作成します。
作成したイメージを元にコンテナを起動します。

``Docker``にはデスクトップアプリ``Docker Desktop``があります。
コンテナ管理／イメージ管理／ボリューム管理に関する情報やその操作はデスクトップアプリのGUIも頼るとよいと思います。

## コンテナしたい（`docker`）

```{toctree}
---
maxdepth: 1
---
docker-install
docker-tutorial
docker-ls
docker-image-pull
docker-image-build
docker-container
docker-container-run
docker-container-exec
docker-volume
```

## Dockerfileしたい

```{toctree}
---
maxdepth: 1
---
docker-dockerfile-from
docker-dockerfile-workdir
docker-dockerfile-shell
docker-dockerfile-run
docker-dockerfile-cmd
```

## 複数コンテナしたい（`docker compose`）

```{toctree}
---
maxdepth: 1
---
docker-compose
docker-compose-ls
docker-compose-up-down
docker-compose-start-stop
```

## 実践例

``docker``や``docker-compose``を使って、実際にコンテナで遊んでみました。

```{toctree}
---
maxdepth: 1
---
docker-ubuntu
docker-busybox
docker-httpd
docker-nginx
docker-wordpress
docker-python3
docker-mystmd
docker-hugo
docker-raspi
```
