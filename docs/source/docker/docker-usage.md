# Docker の使い方

`Docker`は**コンテナ型仮想化技術**を使ったプラットフォームです。

アプリケーションとその依存関係をひとつにまとめたイメージからコンテナを生成することで、
異なるOSでも一貫した実行環境を構築できます。
近年のおチーム開発では欠かせないツールとなっています。
個人開発では必須ではありませんが、知っておくと便利です。

一般的な解説サイトでは、`docker`コマンドの使い方や`Dockerfile`の書き方から説明がはじまることが多いですが、
このサイトでは`docker compose`コマンドを中心に説明することにしました。

コンテナのイメージは`Docker Hub`をはじめとするコンテナレジストリで公開されています。
まずは、これらの公開イメージを利用し、単一もしくは複数のコンテナを作成・実行してみるのがよいと思います。
このとき、ひとつのコンテナにはひとつの機能をたせ、**ephemeral（≒使い捨て）** 基本であることを
意識することで、開発環境の構築や運用・更新をシンプルにできます。

既存のイメージでは、物足りなくなってきたら`Dockerfile`を使って
カスタマイズ／オプティマイズしたイメージの作成に取り掛かってみるとよいです。

## 環境構築したい

```{toctree}
---
maxdepth: 2
---
docker-setup
```

## コンテナ管理したい（`docker compose`）

`docker compose`は **複数のコンテナ** を管理するためのコマンドです。

```{toctree}
---
maxdepth: 2
---
docker-compose
```

## コンテナしたい（`docker`）

`docker`コマンドは **単一のコンテナ** を管理するためのコマンドです。

```{toctree}
---
maxdepth: 1
---
docker-ls
docker-image-pull
docker-image-build
docker-container
docker-container-run
docker-container-exec
docker-volume
```

## カスタムしたい（`Dockerfile`）

```{toctree}
---
maxdepth: 2
---
docker-dockerfile
```

## 実践例

```{toctree}
---
maxdepth: 2
---
docker-examples
```
