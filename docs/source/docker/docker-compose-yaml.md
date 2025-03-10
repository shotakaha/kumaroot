# コンテナ管理したい（``compose.yaml``）

```console
$ docker compose version
Docker Compose version v2.29.2-desktop.2
```

`docker compose`は複数のコンテナを管理するコマンドです。

```yaml
# compose.yaml

# コンテナの設定
services:
  コンテナ名:
    image: イメージ名
    volumes:
      - data:コンテナのパス

# ボリュームの設定
volumes:
  data:
```

設定ファイルは`compose.yaml`です。
`services`の中に利用するコンテナごとの設定、
`volumes`の中に内部ボリュームの設定を記述できます。

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

## コンテナ設定したい（`services`）

```yaml
services:
  コンテナ名1:
    build: イメージのビルド設定
    command: コンテナ起動時のコマンド
    container_name: コンテナ名
    depends_on: 依存関係のあるコンテナ名
    entrypoint: コンテナ起動時のentrypoint
    env_file: 環境変数をファイルから設定
    environment: 環境変数の設定
    image: イメージ名
    labels: コンテナに追加するラベル
    networks: コンテナに接続するネットワーク
    ports: ポート設定（port forwarding）
    restart: 再起動時の設定（"no" / "always" / "on-failure"など）
    tty: 擬似端末の配置（"false" / "true"）
    volumes: コンテナに接続するボリューム
    working_dir: コンテナ内の作業ディレクトリ

  コンテナ名2:
    image: イメージ名
    ...
```

`services`セクションでコンテナを設定できます。
コンテナごとに必要な設定を記述します。
詳細は[Compose Specification](https://docs.docker.jp/compose/compose-file/index.html)を参照してください。

:::{seealso}

Compose V1の初期には`docker-compose.yaml`の先頭に
`version: "3"`のようにバージョン指定をしていましたが、
Docker Compose 1.27.0以降では`version`キーは不要です。

```console
WARN[0000] ./docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
```

`version`キーを定義している場合は、WARNINGが表示されます。

:::

## ボリューム設定したい（`volumes`）

```yaml
services:
  db:
    image: mariadb:latest
    volumes:
      # 内部ボリューム:コンテナ内のパス
      - db_data:/var/lib/mysql

volumes:
  # 内部ボリュームの作成
  db_data:
```

`volumes`セクションでボリュームを設定できます。
上記はMariaDBコンテナのボリュームの設定例です。
コンテナの`/var/lib/mysql`に作成されるデータベースを
`db_data`という名前をつけてDocker内の内部ボリュームに保存しています。

:::{note}

コンテナ内での作業結果は、基本的にコンテナを
終了（`docker compose down`）したタイミングで削除されます。
作業結果を残したい場合は、内部ボリュームもしくはバインドマウントとして
データを残す必要があります。

:::

## 設定を確認したい（`docker compose config`）

```console
$ docker compose config
$ docker compose config --services
$ docker compose config --images
$ docker compose config --environment
$ docker compose config --variables
$ docker compose config --volumes
```

`docker compose config`コマンドで`compose.yaml`の設定内容を確認できます。

## リファレンス

- [Docker Compose - docs.docker.com](https://docs.docker.com/compose/)
- [Compose Specification - docs.docker.jp](https://docs.docker.jp/compose/compose-file/index.html)
