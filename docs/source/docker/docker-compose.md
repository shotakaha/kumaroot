# 複数のコンテナを使いたい（``compose.yaml``）

```yaml
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

## リファレンス

- [Docker Compose - docs.docker.com](https://docs.docker.com/compose/)
