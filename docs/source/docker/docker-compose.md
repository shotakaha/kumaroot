# コンテナ管理したい（``compose.yaml``）

```console
$ docker compose version
Docker Compose version v2.29.2-desktop.2
```

`docker compose`は複数のコンテナを管理するコマンドです。

```yaml
# compose.yaml
services:
  コンテナ名:
    image: イメージ名
    volumes:
      - ホストOSのパス:コンテナのパス
```

設定は`compose.yaml`で管理します。

:::{seealso}

Docker ComposeにはV1とV2があります。
Compose V1は`docker-compose`というコマンドです。Pythonで実装された単独ツールで、設定ファイルは`docker-compose.yaml`です。

Compose V2は`docker compose`というサブコマンドです。
Go言語で再実装され、Docker CLIに統合されたことで、より多くの機能を使うことができます。
設定ファイル名は
`docker-compose.yaml`もそのまま使えますが、
`compose.yaml`が推奨されています。

ウェブ検索すると、
V1コマンドの記事もたくさんヒットしますが、
適宜V2に読み替えるのがよさそうです。

:::

:::{caution}

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
詳細は[Compose Specification](https://docs.docker.jp/compose/compose-file/index.html)を参照してください。

:::{seealso}

Compose V1の初期には`docker-compose.yaml`の先頭に
`version: "3"`のようにバージョン指定をしていましたが、
Docker Compose 1.27.0以降では`version`キーは不要です。

:::

## リファレンス

- [Docker Compose - docs.docker.com](https://docs.docker.com/compose/)
- [Compose Specification - docs.docker.jp](https://docs.docker.jp/compose/compose-file/index.html)
