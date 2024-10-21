# Docker の使い方

`Docker`は**コンテナ型仮想化技術**を使ったプラットフォームです。
アプリケーションとその依存関係をまとめたイメージからコンテナを生成することで、異なるOSでも一貫した実行環境を構築できます。

コンテナのイメージは`Docker Hub`に代表されるレジストリで公開されています。
また`Docker Compose`を使って複数のコンテナを管理できます。

コンテナは **ephemeral（≒使い捨て）** が前提です。
ひとつのコンテナに、ひとつの機能を持たせるようにすることで、開発環境の構築や運用・更新を簡単にできます。
個人開発の場合、必ずしも導入する必要はないですが、機能は知っておいたほうがよいかもしれません。


```{toctree}
---
maxdepth: 1
---
docker-install
docker-tutorial
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
maxdepth: 1
---
docker-compose
docker-compose-ls
docker-compose-up-down
docker-compose-start-stop
docker-compose-exec
docker-compose-cp
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

既存のイメージをベースにして、カスタマイズしたイメージを作成できます。
イメージの作成手順は`Dockerfile`に保存します。

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

## 実践例

``docker``や``docker-compose``を使って、実際にコンテナで遊んでみました。

```{toctree}
---
maxdepth: 2
---
docker-examples-linux
docker-examples-web
docker-examples-databases
docker-examples-cms
docker-examples-others
```
