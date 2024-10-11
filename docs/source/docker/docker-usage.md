# Docker の使い方

`Docker`は**コンテナ型仮想化技術**を使ったプラットフォームです。
使い捨てを前提とした**コンテナ**を管理することで、
開発環境の構築や運用が簡単になります。
個人開発の場合、必ずしも導入する必要はないですが、機能は知っておいたほうがよいかもしれません。
コンテナのベースとなるイメージは`Docker Hub`に代表されるレジストリで公開されています。

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

## コンテナ操作したい（`docker compose`）

`docker compose`は複数のコンテナを管理するためのコマンドです。

```{toctree}
---
maxdepth: 1
---
docker-compose
docker-compose-ls
docker-compose-up-down
docker-compose-start-stop
docker-compose-cp
```

## 単一コンテナしたい（`docker`）

`docker`コマンドは、単一のコンテナを管理するためのコマンドです。

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
docker-mariadb
```
