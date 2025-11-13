# Nginxしたい（``nginx``）

[nginx](https://hub.docker.com/_/nginx)は高速で軽量なウェブサーバーのDockerイメージです。
Docker Composeを使って簡単にNginxを起動・停止できます。

## セットアップ

まず、`compose.yaml`を作成します。

```yaml
services:
  nginx:
    image: nginx
    container_name: my-nginx
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
```

以下のコマンドで起動・停止できます。

```console
$ docker compose up -d
$ docker compose down
```

起動後、ブラウザで `http://localhost:8080` を開いて「Welcome to nginx!」と表示されればOKです。

ローカルの `./html` ディレクトリがNginxのドキュメントルート（`/usr/share/nginx/html`）にマウントされているため、
このディレクトリにHTMLファイルを配置すればウェブサーバーで公開できます。

## パッケージをインストールしたい（``apt-get``）

コンテナー内に便利なコマンドツールを追加できます。

```console
$ docker compose exec nginx bash
(my-nginx) $ apt-get update
(my-nginx) $ apt-get install -y vim curl
```

公式イメージには最小限のコマンドしか含まれていないため、必要に応じて `apt-get` でツールを追加します。
ここでは `vim` と `curl` をインストールしています。

## HTMLファイルを公開したい

ローカルマシンの `./html` ディレクトリにHTMLファイルを配置します。

```console
$ mkdir -p html
$ cat > html/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <h1>Welcome to my website!</h1>
</body>
</html>
EOF
```

`docker compose up -d` でコンテナーを起動すると、`http://localhost:8080` でこのHTMLファイルが表示されます。

## ログを確認したい

Nginxのアクセスログやエラーログを確認できます。

```console
$ docker compose exec nginx bash
(my-nginx) $ tail -f /var/log/nginx/access.log
```

ログファイルはコンテナー内の `/var/log/nginx/` に保存されています。
`-f` オプションで、ログをリアルタイム表示できます。
終了するには `Ctrl+C` を押してください。

## バージョン

| バージョン | リリース日 | サポート終了 | 備考 |
|----------|-----------|----------|------|
| 1.29（mainline） | 2025年6月24日 | サポート中 | 最新開発版 |
| 1.28（stable） | 2025年4月23日 | サポート中 | 推奨安定版 |
| 1.27 | 2024年5月28日 | 2025年6月24日 | サポート終了予定 |
| 1.26 | 2024年4月23日 | 2025年4月23日 | サポート終了 |

### バージョニング体系

nginxは「mainline」（開発版）と「stable」（安定版）の2つのブランチを維持しています。

- **mainline**（奇数番号）：最新機能やバグ修正が含まれます。新しい機能が必要な場合に使用します。
- **stable**（偶数番号）：重大なバグ修正のみが提供されます。本番環境での使用に推奨されます。

毎年4月に現在の安定版のサポートが終了し、次の安定版がリリースされます。

Docker Imageの `nginx` タグは、最新の安定版を自動的にプルします。
特定のバージョンを使いたい場合は `nginx:1.28` のようにバージョンを指定できます。

## リファレンス

- [nginx - DockerHub](https://hub.docker.com/_/nginx)
- [NGINX Documentation](https://docs.nginx.com/)
- [nginx - endoflife.date](https://endoflife.date/nginx)
