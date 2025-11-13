# BusyBoxしたい（`busybox`）

```console
$ docker run -it --rm busybox
```

BusyBoxはLinuxの基本的なコマンドが揃った軽量イメージです。
約300～400個のUNIXコマンド（アプレット）を単一バイナリに統合しており、イメージサイズは1～2MBと非常に軽量です。
特定のコマンドをまとめたコンテナーを作成するときや、デバッグ、テストに活躍します。

## コマンドを確認したい

```console
$ docker run --rm busybox busybox --list
```

`busybox --list`コマンドで、利用可能なコマンド一覧を確認できます。
BusyBoxには以下のようなコマンドが含まれています。

- **ファイル操作：** `cat`, `ls`, `rm`, `cp`, `mv`, `mkdir`, `find`
- **ネットワーク：** `ping`, `wget`, `ip`, `route`, `nslookup`
- **テキスト処理：** `grep`, `sed`, `awk`, `echo`, `head`, `tail`
- **システム管理：** `mount`, `umount`, `ps`, `top`, `kill`
- **圧縮：** `gzip`, `tar`, `unzip`

## composeしたい

```yaml
services:
  app:
    image: myapp:latest
    depends_on:
      init-check:
        condition: service_completed_successfully
    ports:
      - "8080:8080"

  # データベース起動待ち用コンテナー
  init-check:
    image: busybox
    command: >
      sh -c "
        echo 'Waiting for database...'
        until wget -q -O- http://db:5432 > /dev/null 2>&1; do
          echo 'Database not ready, waiting...'
          sleep 2
        done
        echo 'Database is ready!'
      "
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: password
```

BusyBoxはスタンドアロンで動作させるより、`docker compose`などのマルチコンテナー環境と
組み合わせて補助的なサービスとして活用するとよいツールです。

上記は、アプリケーション起動前に依存サービスの準備ができるまで待機するサンプルです。

## ログ監視したい

```yaml
services:
  web:
    image: nginx:latest
    volumes:
      - logs:/var/log/nginx

  api:
    image: myapi:latest
    volumes:
      - logs:/var/log/app

  # ログ監視コンテナー
  log-monitor:
    image: busybox
    command: tail -f /logs/nginx/access.log /logs/app/app.log
    volumes:
      - logs:/logs
    depends_on:
      - web
      - api

volumes:
  logs:
```

複数のサービスのログを集約して監視するサンプルです。

## ボリュームを初期化したい

```yaml
services:
  app:
    image: myapp:latest
    volumes:
      - data:/app/data
    depends_on:
      data-init:
        condition: service_completed_successfully

  # データディレクトリの初期化
  data-init:
    image: busybox
    command: >
      sh -c "
        echo 'Initializing data directory...'
        mkdir -p /data/uploads
        mkdir -p /data/config
        echo 'Initialization complete'
      "
    volumes:
      - data:/data

volumes:
  data:
```

起動時に共有ボリュームを初期化するサンプルです。

## ネットワーク診断したい

```yaml
services:
  web:
    image: nginx:latest
    networks:
      - app-net

  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: password
    networks:
      - app-net

  # 診断用コンテナー（開発時のみ）
  debug:
    image: busybox
    command: sh
    stdin_open: true
    tty: true
    networks:
      - app-net

networks:
  app-net:
```

開発時にサービス間の通信をテストするサンプルです。

```bash
$ docker-compose run --rm debug sh

# コンテナー内でネットワークテスト
/ # ping web
/ # nslookup db
/ # wget -O- http://web
```

起動後にシェルを起動し診断を実行できます。

## 最小サイズのイメージを作りたい

```dockerfile
FROM busybox:latest

# アプリケーションをコピー
COPY my-app /usr/local/bin/
RUN chmod +x /usr/local/bin/my-app

ENTRYPOINT ["/usr/local/bin/my-app"]
```

または、マルチステージビルド：

```dockerfile
FROM golang:1.21 as builder
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o myapp .

FROM busybox:latest
COPY --from=builder /app/myapp /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/myapp"]
```

GoアプリやRustアプリなど、単一バイナリで動くアプリであれば、
BusyBoxを使って軽量なアプリケーション用の最小イメージを作成できます。

## BusyBoxの特徴

### メリット

- **超軽量なイメージサイズ**
  1～2MBの非常にコンパクトなイメージ。ネットワーク転送、ストレージが効率的。

- **200以上のUNIXコマンド搭載**
  基本的なファイル操作、テキスト処理、ネットワーク診断コマンドが利用可能。

- **マルチコンテナー環境に最適**
  Init Container、Sidecar、デバッグコンテナーなど補助的な役割で活躍。

- **依存関係が最小**
  glibc、追加パッケージが不要で、セキュリティリスクが低い。

### デメリット

- **スタンドアロン用途には不向き**
  メインアプリケーションのベースイメージとしては機能が不足する場合がある。

- **高度な機能がない**
  パッケージマネージャー、開発ツール、シェルスクリプト機能が限定的。

- **エラーメッセージが簡潔**
  問題診断時に詳細な情報が得られないことがある。

### 最適な用途

- Kubernetes Init Container（起動待ちチェック用）。
- Sidecar Container（ログ監視、メトリクス収集）。
- マルチコンテナー環境での診断・デバッグ用。
- 単一バイナリアプリケーションのベースイメージ。
- 軽量で高速なコンテナーが必要な環境。
- IoT、エッジコンピューティング環境。

## リファレンス

- [BusyBox - DockerHub](https://hub.docker.com/_/busybox)
- [BusyBox Official](https://busybox.net/)
- [Alpine Linux Wiki - BusyBox](https://wiki.alpinelinux.org/wiki/BusyBox)
