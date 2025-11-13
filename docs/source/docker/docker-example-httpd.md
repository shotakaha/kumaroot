# Apacheしたい（``httpd``）

```yaml
services:
  web:
    image: httpd:2.4
    container_name: my-httpd
    ports:
      - "8080:80"
```

```console
// コンテナーを起動
$ docker compose up -d

// ブラウザーでアクセス
$ open http://localhost:8080

// コンテナーを終了
$ docker compose down
```

[httpd](https://hub.docker.com/_/httpd/)はApacheウェブサーバーのDockerイメージです。
Docker Composeを使って簡単にApacheサーバーを起動・停止できます。
起動後、ブラウザで `http://localhost:8080` を開いて「It works!」と表示されればOKです。

## パッケージをインストールしたい（``apt-get``）

```console
$ docker compose exec web bash
(my-httpd) $ apt-get update
(my-httpd) $ apt-get install -y vim less
```

公式イメージには最小限のコマンドしか含まれていないため、必要に応じて `apt-get` でツールを追加します。
ここでは `vim` と `less` をインストールしています。

## トップページを変更したい

```console
$ docker compose exec web bash
(my-httpd) $ vi htdocs/index.html
```

Apacheのドキュメントルートはデフォルトで `/usr/local/apache2/htdocs/` です。
このディレクトリ内の `index.html` を編集すれば、トップページが変わります。

新しいHTMLファイルを作成する場合も、同じディレクトリに配置すればウェブサーバーで公開できます。

## ログを確認したい

```console
$ docker compose exec web bash
(my-httpd) $ tail -f logs/access_log
```

Apacheのアクセスログやエラーログは、
コンテナー内の `/usr/local/apache2/logs/` に保存されています。
`-f` オプションで、ログをリアルタイム表示できます。
終了するには `Ctrl+C` を押してください。

## バージョン

| バージョン | リリース日 | サポート終了 | 備考 |
|----------|-----------|----------|------|
| 2.6 | 未リリース | - | 開発中（2.5系として開発継続中） |
| 2.4.65 | 2025年7月23日 | サポート中 | 現在推奨（2.4系の最新版） |
| 2.4.62 | 2024年10月29日 | サポート中 | 安定版 |
| 2.4 | 2012年2月21日 | サポート中 | 長期サポート版 |
| 2.2.34 | 2017年7月11日 | 終了 | レガシー版 |

### 2.4系（推奨）

Apache 2.4系は2012年のリリースから継続的にセキュリティアップデートが提供されています。
Docker Imageの `httpd:2.4` タグは、最新の安定版2.4.xを自動的にプルします。
特定のバージョンを使いたい場合は `httpd:2.4.65` のようにバージョンを指定できます。

### 2.2系（レガシー）

Apache 2.2系は2017年7月にサポートが終了しました。セキュリティ脆弱性への対応がされないため、本番環境での使用は推奨されません。

### 2.6系（開発中）

Apache 2.6系は現在開発中であり、正式リリースはまだされていません。
プロジェクトでは2.4系への継続的な改善に重点を置いています。

## リファレンス

- [httpd - DockerHub](https://hub.docker.com/_/httpd)
- [Apache 2.4 ドキュメント](https://httpd.apache.org/docs/2.4/ja/)
- [Apache HTTP Server - endoflife.date](https://endoflife.date/apache-http-server)
