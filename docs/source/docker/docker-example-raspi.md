# Raspberry Piしたい（`balenalib`）

DockerコンテナーでRaspberry Pi環境をエミュレートして、自作パッケージが実際のハードウェアで動作するかを事前確認できます。

BalenaがDockerHubに公開しているRaspberry Pi OSのイメージを使用します。RPi3/RPi4、Debianバージョン（bullseye/bookworm）などを組み合わせて選択できます。

**利用可能なイメージ：**
- [balenalib/raspberrypi4-64-python](https://hub.docker.com/r/balenalib/raspberrypi4-64-python)
- [balenalib/raspberrypi4-64-debian](https://hub.docker.com/r/balenalib/raspberrypi4-64-debian)
- [balenalib/raspberrypi3-64-python](https://hub.docker.com/r/balenalib/raspberrypi3-64-python)

## 単一バージョンで確認したい

### Dockerfile を作成

自作パッケージのインストール手順をDockerfileに記述します。
RPi4/bookwormの組み合わせが動作確認済みです。

```dockerfile
FROM balenalib/raspberrypi4-64-python:bookworm-build-20240429

# システムパッケージの更新
RUN apt update && \
    apt upgrade -y && \
    apt autoremove -y && \
    apt install -y pipx

# 自作パッケージのインストール例
RUN pipx install haniwers

# または、ローカルのパッケージをコピーしてインストール
# COPY . /app
# WORKDIR /app
# RUN pip install -e .

ENTRYPOINT ["/bin/bash"]
```

### compose.yaml を作成

```yaml
# compose.yaml
services:
  raspi:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: raspi-dev
    stdin_open: true
    tty: true
```

### 起動と実行

```console
# イメージをビルドしてコンテナーを起動
$ docker compose up -d

# コンテナーに接続
$ docker compose exec raspi bash

# ログを確認
$ docker compose logs -f

# 停止
$ docker compose down
```

## 複数バージョンで確認したい

異なるRaspberry PiのバージョンやDebianバージョンで同時にテストする場合は、
複数のDockerfileを作成して管理します。

### Dockerfileの作成

各バージョン用のDockerfileを作成します。

```dockerfile
# Dockerfile.rpi4-bookworm
FROM balenalib/raspberrypi4-64-python:bookworm-build-20240429
RUN apt update && apt upgrade -y && apt autoremove -y && apt install -y pipx
RUN pipx install haniwers
```

```dockerfile
# Dockerfile.rpi4-bullseye
FROM balenalib/raspberrypi4-64-python:bullseye-build-20240429
RUN apt update && apt upgrade -y && apt autoremove -y && apt install -y pipx
```

```dockerfile
# Dockerfile.rpi3-bookworm
FROM balenalib/raspberrypi3-64-python:bookworm-build-20240429
RUN apt update && apt upgrade -y && apt autoremove -y
```

### compose.yaml を作成

```yaml
# compose.yaml
services:
  rpi4-bookworm:
    build:
      context: .
      dockerfile: Dockerfile.rpi4-bookworm
    container_name: raspi-test-rpi4-bookworm
    stdin_open: true
    tty: true

  rpi4-bullseye:
    build:
      context: .
      dockerfile: Dockerfile.rpi4-bullseye
    container_name: raspi-test-rpi4-bullseye
    stdin_open: true
    tty: true

  rpi3-bookworm:
    build:
      context: .
      dockerfile: Dockerfile.rpi3-bookworm
    container_name: raspi-test-rpi3-bookworm
    stdin_open: true
    tty: true
```

### 起動と実行

```console
# すべてのバージョンをビルド・起動
$ docker compose up -d

# 特定のバージョンに接続
$ docker compose exec rpi4-bookworm bash

# 特定のサービスのログを確認
$ docker compose logs -f rpi4-bookworm

# すべて停止
$ docker compose down
```

## 動作確認済み環境

宇宙線測定ツール（haniwers）のインストール検証では、以下の結果が得られました：

| OS | Python | pipx | 結果 | エラー |
|---|---|---|---|---|
| RPi3 / bullseye | 3.9 | 0.12.3.1 | ❌ 失敗 | Cargo is not installed |
| RPi3 / bookworm | - | 1.1.0 | ❌ 失敗 | pip seemed to fail to build pendulum |
| RPi4 / bullseye | 3.11.2 | ない | ⚠️ パッケージなし | |
| RPi4 / bookworm | 3.11.2 | 1.1.0 | ✅ 成功 | |

**推奨環境：RPi4 / bookworm**

## Raspberry PiおよびDebianバージョンについて

### Raspberry Piのバージョン

| モデル | アーキテクチャ | ハードウェア | 特徴 |
|---|---|---|---|
| RPi3 (Model B+) | ARMv7 (32/64-bit) | 1.4GHz Cortex-A53 | 古いモデル、制限あり |
| RPi4 (Model B) | ARMv8 (64-bit) | 1.5GHz Cortex-A72 | 推奨、高い互換性 |
| RPi5 | ARMv8 (64-bit) | 2.4GHz Cortex-A76 | 最新モデル、高性能 |

### Debianバージョン

| コードネーム | リリース | サポート終了 | 特徴 |
|---|---|---|---|
| bullseye (11) | 2021年8月 | 2026年6月 | 旧バージョン、パッケージ不足の場合あり |
| bookworm (12) | 2023年6月 | 2028年6月 | **推奨**、modern toolchain対応 |
| trixie (13) | 2024年11月 | 2029年6月以降 | テスト用途 |

**推奨構成：RPi4 + bookworm**

RPi4とDebianの組み合わせがもっとも安定しており、Rustコンパイラやpipパッケージのビルドで問題が少ないため、本番環境での使用をオススメします。

## トラブルシューティング

### "Cargo is not installed" エラー

Rustのツールチェーンが必要な場合、RPi3/bullseyeでは動作しません。
RPi4/bookwormの使用をオススメします。

### "pip seemed to fail to build pendulum" エラー

C言語コンパイラが不足している可能性があります。
Dockerfileに以下を追加してください：

```dockerfile
RUN apt install -y build-essential python3-dev
```

## Raspberry Piエミュレーションの特徴

### メリット

- **実ハードウェアなしでテスト可能**
  実Raspberry Piを購入しなくても、Dockerコンテナーで環境をシミュレート可能。

- **複数バージョン同時テスト**
  RPi3、RPi4、異なるDebianバージョンを同時に検証できる。

- **開発～本番まで同じイメージで対応**
  開発環境で検証したイメージをそのまま本番ハードウェアにデプロイできる。

- **CI/CDパイプラインに統合可能**
  自動テスト環境として、Raspberry Pi対応のバイナリを事前検証できる。

### デメリット

- **完全な再現ではない**
  GPIO、SPI、I2Cなどのハードウェアインターフェイスはエミュレートできない。

- **パフォーマンステストは参考値**
  実ハードウェアとCPU性能が異なるため、ベンチマークとして正確ではない。

- **一部パッケージが動作しない**
  Rustコンパイラなど、アーキテクチャ依存のツールで問題が発生することがある。

### 最適な用途

- Raspberry Pi用自作パッケージの動作確認。
- 複数バージョン対応の事前テスト。
- CI/CDパイプラインでの自動テスト。
- Raspberry Piアプリケーション開発の初期段階。
- 実ハードウェアがない環境での開発。

## リファレンス

- [balenalib on Docker Hub](https://hub.docker.com/r/balenalib)
- [Raspberry Pi公式ドキュメント](https://www.raspberrypi.com/)
- [Docker公式ドキュメント](https://docs.docker.com/)
