# Docker の使い方

`Docker`は**コンテナ型仮想化技術**を使ったプラットフォームです。

アプリケーションとその依存関係をひとつにまとめたイメージからコンテナを生成することで、
異なるOSでも一貫した実行環境を構築できます。
近年のチーム開発では欠かせないツールとなっています。
個人開発では必須ではありませんが、知っておくと便利です。

一般的な解説サイトでは、`docker`コマンドの使い方や`Dockerfile`の書き方から説明がはじまることが多いですが、
このサイトであえて`docker compose`コマンドを中心に説明することにしました。

:::{note}

`docker compose`は、複数の`docker`コマンドをいい感じにまとめてくれるコンテナ管理ツールです。
まず、`compose`でコンテナ管理に触れているうちに、
その根底にある`docker`コマンドの使い方にも自然と興味が湧いてくるはず、
という考えです。

:::

コンテナイメージは`Docker Hub`をはじめとするコンテナレジストリで公開されています。
はじめはこれらの公開イメージを利用し、単一もしくは複数のコンテナを作成・実行してみるのがよいと思います。
このとき、ひとつのコンテナにはひとつの機能を持たせ、**ephemeral（≒使い捨て）** が基本であることを意識することで、
開発環境の構築や運用・更新をシンプルにできます。

既存のイメージでは、物足りなくなってきたら`Dockerfile`を使って
カスタマイズ／最適化したイメージの作成に取り掛かってみるとよいです。

## 環境構築したい

```{toctree}
---
maxdepth: 2
---
docker-setup
```

## コンテナ管理したい（`docker compose`）

`docker compose`は **複数のコンテナ** を設定・管理するためのツールです。
設定は`compose.yml`に保存します。

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
