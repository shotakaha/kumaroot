# Docker の使い方

`Docker`は**コンテナ型仮想化技術**を使ったプラットフォームです。
アプリケーションとその依存関係をまとめたイメージからコンテナを生成することで、異なるOSでも一貫した実行環境を構築できます。

コンテナのイメージは`Docker Hub`に代表されるレジストリで公開されています。
また`Docker Compose`を使って複数のコンテナを管理できます。

コンテナは **ephemeral（≒使い捨て）** が前提です。
ひとつのコンテナに、ひとつの機能を持たせるようにすることで、開発環境の構築や運用・更新を簡単にできます。
個人開発の場合、必ずしも導入する必要はないですが、機能は知っておいたほうがよいかもしれません。

## 環境構築したい

```{toctree}
---
maxdepth: 2
---
docker-setup
```

:::{note}

このサイトでは`docker compose`を入り口にしています。
複数コンテナはもちろんですが、単一コンテナの場合も、
既存のイメージを利用するのであれば`compose.yaml`を作るのがよいと思います。

よりカスタマイズ／オプティマイズしたイメージが欲しくなったら、
`Dockerfile`に手を出してみるとよいと思います
（というか、手を出したくなると思います）。

:::

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
