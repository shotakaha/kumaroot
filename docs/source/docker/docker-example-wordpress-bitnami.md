# WordPress (Bitnami) したい（`wordpress-bitnami`）

```{literalinclude} ../../examples/docker/wordpress-bitnami.yaml
---
language: yaml
---
```

## コンテナーを起動したい

```console
$ docker compose up -d
```

## コンテナーで操作したい

```console
$ docker compose exec wordpress bash
```

## コンテナーを終了したい

```console
$ docker compose down
```

## WordPress (Bitnami) について

WordPressをBitnamiのコンテナーイメージで起動します。
Bitnamiイメージは本番環境向けに最適化されており、セキュリティとパフォーマンスが考慮されています。
MySQLデータベースとWordPressをセットで構成しており、認証情報は環境変数で設定します。

環境変数は`.env`で変更できます。
上記サンプルでは、デフォルト値を指定しているため、`.env`ファイルがなくても動作します。
起動後、ブラウザで `http://localhost:8080` を開いて、WordPressにアクセスできます。
コンテナー内で `wp` コマンド（WP-CLI）を使ってWordPressを管理できます。
