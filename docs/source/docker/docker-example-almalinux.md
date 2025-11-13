# AlmaLinuxしたい（`almalinux`）

```yaml
# filename: compose.yaml
services:
  almalinux:
    image: almalinux:9
    container_name: my-almalinux
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
$ docker compose exec almalinux bash
root#
```

```console
// コンテナーを終了
$ docker compose down
```

AlmaLinuxのコンテナーを使ってデバッグやテスト、開発環境の構築ができます。
上記のサンプルのように
`tty: true`と`stdin_open: true`を指定しておくと
`docker compose up -d`するだけで対話的にシェルを操作できます。

## パッケージをインストールしたい

```console
// コンテナーを起動
$ docker compose up -d

// コンテナーにログイン
$ docker compose exec almalinux bash

// パッケージリストを更新
root# dnf update -y

// 必要なパッケージをインストール（例：curl, git）
root# dnf install -y curl git build-essential

// インストールを確認
root# curl --version
root# git --version
```

AlmaLinuxコンテナーに`dnf`を使ってツールやライブラリをインストールできます。

## 開発環境として使いたい

Python、Node.jsなどの開発環境をセットアップ：

```yaml
services:
  dev-almalinux:
    image: almalinux:9
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

$ docker compose exec dev-almalinux bash

// Python 開発環境のセットアップ
root# dnf install -y python3 python3-pip
root# python3 --version

// Node.js 開発環境のセットアップ
root# dnf install -y nodejs npm
root# node --version

// プロジェクトディレクトリで作業
root# cd /workspace
root# ls -la
```

## テスト環境として使いたい

```yaml
services:
  almalinux-8:
    image: almalinux:8
    container_name: test-almalinux-8
    tty: true
    stdin_open: true
    command: /bin/bash

  almalinux-9:
    image: almalinux:9
    container_name: test-almalinux-9
    tty: true
    stdin_open: true
    command: /bin/bash
```

`compose.yaml`に複数のAlmaLinuxバージョンを定義し
一括で起動し、それぞれのバージョンでアプリケーションのテストを実行するサンプルです。

```console
$ docker compose up -d

$ docker compose exec almalinux-8 bash
root# dnf update -y
root# dnf install -y your-package
root# your-test-command

// 別ターミナルで他のバージョンもテスト
$ docker compose exec almalinux-9 bash
```

## AlmaLinuxのバージョンについて

| バージョン | リリース日 | サポート終了 | 特徴 |
|---|---|---|---|
| 8 (8.10) | 2021年3月 | 2029年5月 | 安定版、RHEL互換 |
| 9 (9.5) | 2023年3月 | 2032年5月 | 最新推奨版、高い互換性 |

**LTS（Long Term Support）**
AlmaLinuxはRHEL互換性を重視しており、メジャーバージョン（8、9）は8年間の標準サポートが提供されます。

AlmaLinux 9は最新版であり、より新しいツールチェーンとライブラリが利用可能なため、新規プロジェクトでの使用をオススメします。
ただし、既存システムとの互換性が必要な場合はAlmaLinux 8を選択してください。

## リファレンス

- [AlmaLinux Official Image - DockerHub](https://hub.docker.com/_/almalinux)
- [AlmaLinux公式ドキュメント](https://almalinux.org/)
- [Docker公式ドキュメント](https://docs.docker.com/)
