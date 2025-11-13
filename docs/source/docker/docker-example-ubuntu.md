# Ubuntuしたい（`ubuntu`）

```yaml
# filename: compose.yaml
services:
  ubuntu:
    image: ubuntu:24.10
    container_name: my-ubuntu
    tty: true
    stdin_open: true
    command: /bin/bash
```

```console
// コンテナーを起動
$ docker compose up -d
```

```console
// コンテナーにログイン
$ docker compose exec ubuntu bash
root#
```

```console
// コンテナーを終了
$ docker compose down
```

Ubuntuのコンテナーを使ってデバッグやテスト、開発環境の構築ができます。
上記のサンプルのように
`tty: true`と`stdin_open: true`を指定しておくと
`docker compose up -d`するだけで対話的にシェルを操作できます。

## パッケージをインストールしたい

```console
// コンテナーを起動
$ docker compose up -d

// コンテナーにログイン
$ docker compose exec ubuntu bash

// パッケージリストを更新
root# apt update

// パッケージをアップグレード
root# apt upgrade -y

// 必要なパッケージをインストール（例：curl, git）
root# apt install -y curl git build-essential

// インストールを確認
root# curl --version
root# git --version
```

Ubuntuコンテナーに`apt`を使ってツールやライブラリをインストールできます。

## 開発環境として使いたい

Python、Node.jsなどの開発環境をセットアップ：

```yaml
services:
  dev-ubuntu:
    image: ubuntu:24.04
    container_name: my-dev-env
    tty: true
    stdin_open: true
    volumes:
      - ./project:/workspace
    working_dir: /workspace
    command: /bin/bash
```

```console
$ docker compose up -d

$ docker compose exec dev-ubuntu bash

// Python 開発環境のセットアップ
root# apt update && apt install -y python3 python3-pip
root# python3 --version

// Node.js 開発環境のセットアップ
root# apt install -y nodejs npm
root# node --version

// プロジェクトディレクトリで作業
root# cd /workspace
root# ls -la
```

## テスト環境として使いたい

```yaml
services:
  ubuntu-focal:
    image: ubuntu:20.04
    container_name: test-focal
    tty: true
    stdin_open: true
    command: /bin/bash

  ubuntu-jammy:
    image: ubuntu:22.04
    container_name: test-jammy
    tty: true
    stdin_open: true
    command: /bin/bash

  ubuntu-noble:
    image: ubuntu:24.04
    container_name: test-noble
    tty: true
    stdin_open: true
    command: /bin/bash
```

`compose.yaml`に複数のUbuntuバージョンを定義し
一括で起動し、それぞれのバージョンでアプリケーションのテストを実行するサンプルです。

```console
$ docker compose up -d

$ docker compose exec ubuntu-focal bash
root# apt update
root# apt install -y your-package
root# your-test-command

// 別ターミナルで他のバージョンもテスト
$ docker compose exec ubuntu-jammy bash
$ docker compose exec ubuntu-noble bash
```

## Ubuntuのバージョンについて

| バージョン | コードネーム | リリース日 | サポート終了 |
|---|---|---|---|
| 20.04 LTS | Focal Fossa | 2020年4月 | 2025年5月 |
| 22.04 LTS | Jammy Jellyfish | 2022年4月 | 2027年4月 |
| 24.04 LTS | Noble Numbat | 2024年4月 | 2029年4月 |
| 24.10 | Oracular Oriole | 2024年10月 | 2025年7月 |
| 25.04 | Plucky Puffin | 2025年4月 | 2026年1月 |
| 25.10 | Questing Quokka | 2025年10月 | 2026年7月 |

**LTS（Long Term Support）**
バージョンは5年の標準サポート + 5年のESM（Extended Security Maintenance）が提供されます。

暫定版（24.10、25.04など）は9か月間のサポートのみのため、開発・テスト環境での使用に限定し、本番環境では、最新のLTS版である**Ubuntu 24.04 LTS**の使用をオススメします。

## リファレンス

- [Ubuntu Official Image - DockerHub](https://hub.docker.com/_/ubuntu/)
