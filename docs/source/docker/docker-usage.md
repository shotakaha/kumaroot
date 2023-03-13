# Docker の使い方

Dockerはコンテナ型仮想化技術を使ったプラットフォームです。
プロダクション環境の構築や複製作業を簡単にしたり、
開発環境の構築をサポートするために使います。

ここでは主に、複数のパソコンで同じ開発環境を構築する手順を整理します。
{file}`Dockerfile`というビルドスクリプトをベースにコンテナイメージを作成します。
作成したイメージを元にコンテナを起動します。

``Docker``にはデスクトップアプリ``Docker Desktop``があります。
コンテナ管理／イメージ管理／ボリューム管理に関する情報やその操作はデスクトップアプリのGUIも頼るとよいと思います。

```{toctree}
---
maxdepth: 1
---
docker-install
docker-tutorial
docker-build
docker-run
docker-volume
docker-compose
docker-ubuntu
docker-wordpress
```
