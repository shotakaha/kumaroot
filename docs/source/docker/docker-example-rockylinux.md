# RockyLinuxしたい（`rockylinux`）

```yaml
# filename: compose.yaml
services:
  rockylinux:
    image: rockylinux:9
    container_name: my-rockylinux
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
$ docker compose exec rockylinux bash
root#
```

```console
// コンテナーを終了
$ docker compose down
```

RockyLinuxのコンテナーを使ってデバッグやテスト、開発環境の構築ができます。
上記のサンプルのように
`tty: true`と`stdin_open: true`を指定しておくと
`docker compose up -d`するだけで対話的にシェルを操作できます。

## パッケージをインストールしたい

```console
// コンテナーを起動
$ docker compose up -d

// コンテナーにログイン
$ docker compose exec rockylinux bash

// パッケージリストを更新
root# dnf update -y

// 必要なパッケージをインストール（例：curl, git）
root# dnf install -y curl git build-essential

// インストールを確認
root# curl --version
root# git --version
```

RockyLinuxコンテナーに`dnf`を使ってツールやライブラリをインストールできます。

## 開発環境として使いたい

Python、Node.jsなどの開発環境をセットアップ：

```yaml
services:
  dev-rockylinux:
    image: rockylinux:9
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

$ docker compose exec dev-rockylinux bash

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
  rockylinux-8:
    image: rockylinux:8
    container_name: test-rockylinux-8
    tty: true
    stdin_open: true
    command: /bin/bash

  rockylinux-9:
    image: rockylinux:9
    container_name: test-rockylinux-9
    tty: true
    stdin_open: true
    command: /bin/bash
```

`compose.yaml`に複数のRockyLinuxバージョンを定義し
一括で起動し、それぞれのバージョンでアプリケーションのテストを実行するサンプルです。

```console
$ docker compose up -d

$ docker compose exec rockylinux-8 bash
root# dnf update -y
root# dnf install -y your-package
root# your-test-command

// 別ターミナルで他のバージョンもテスト
$ docker compose exec rockylinux-9 bash
```

## RockyLinuxのバージョンについて

| バージョン | リリース日 | サポート終了 | 特徴 |
|---|---|---|---|
| 8 (8.10) | 2021年6月 | 2029年5月 | 安定版、RHEL互換 |
| 9 (9.5) | 2022年7月 | 2032年5月 | 最新推奨版、高い互換性 |

**LTS（Long Term Support）**
RockyLinuxはRHEL互換性を重視しており、メジャーバージョン（8、9）は8年間の標準サポートが提供されます。

RockyLinux 9は最新版であり、より新しいツールチェーンとライブラリが利用可能なため、新規プロジェクトでの使用をオススメします。
ただし、既存システムとの互換性が必要な場合はRockyLinux 8を選択してください。

## RockyLinuxの特徴

### メリット

- **CentOSの直接的な後継**
  CentOSプロジェクト創設者による開発。CentOS 8からの移行に最適。

- **コミュニティドリブン**
  開発がコミュニティによって行われており、ボランティアベースの開発。

- **RHEL互換性が高い**
  Red Hat Enterprise Linuxとの互換性が確保されている。

- **長期サポート（8年）**
  メジャーバージョンごとに8年間の安定したサポート。本番環境に最適。

### デメリット

- **商用サポートが限定的**
  AlmaLinuxのような企業バックのサポートがない。SLAが必要な場合は別途検討が必要。

- **パッケージが古い場合がある**
  最新版のツールが必要な場合、手動でのビルドが必要になることがある。

- **コミュニティ情報がAlmaLinuxより少ない**
  ドキュメント、Q&Aサイトでの情報がAlmaLinuxに比べて少ない。

### 最適な用途

- CentOS 7/8からの移行。
- CentOSを使用していたユーザー。
- オープンソースコミュニティを重視する場合。
- 商用サポートが不要で、コスト重視のシステム。
- RHEL互換が必要な本番環境。

## リファレンス

- [RockyLinux Official Image - DockerHub](https://hub.docker.com/_/rockylinux)
- [RockyLinux公式ドキュメント](https://rockylinux.org/)
- [Docker公式ドキュメント](https://docs.docker.com/)
