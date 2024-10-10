# 複数のコンテナを使いたい（``compose.yaml``）

```console
$ docker compose version
Docker Compose version v2.29.2-desktop.2
```

```yaml
# compose.yaml
services:
  コンテナ名:
    image: イメージ名
    volumes:
      - ホストOSのパス:コンテナのパス
```

`docker compose`で一度に複数のコンテナを作成・実行できます。
設定は`compose.yaml`で管理します。

:::{caution}

Docker ComposeにはV1とV2があります。
Compose V1は`docker-compose`というコマンド名（pythonで実装？）で、設定ファイルは`docker-compose.yaml`でした。
Compose V2で`docker compose`という`docker`のサブコマンド（Go言語で実装）になり、設定ファイル名は`compose.yaml`が推奨されています。

Compose V1のサポートは2023年6月に終了しています。
また、Docker Desktop v4.33.0（2024年7月）で`docker-compose`コマンドが削除されました。

:::

## 設定したい（`services`）

```yaml
services:
  コンテナ名1:
    image: イメージ名
    build: イメージのビルド設定
    container_name: コンテナ名
    working_dir: コンテナ内の作業ディレクトリ
    command: コンテナ起動時のコマンド
    entrypoint: コンテナ起動時のentrypoint
    depends_on: 依存関係のあるコンテナ名
    networks: コンテナに接続するネットワーク
    volumes: コンテナに接続するボリューム
    environment: 環境変数の設定
    env_file: 環境変数をファイルから設定
    labels: コンテナに追加するラベル
    ports: ポート設定（port forwarding）
    restart: 再起動時の設定（"no" / "always"）
    tty: 擬似端末の配置（"false" / "true"）

  コンテナ名2:
    image: イメージ名
    ...
```

`services`セクションで設定できることを整理しました。

## リファレンス

- [Docker Compose - docs.docker.com](https://docs.docker.com/compose/)
