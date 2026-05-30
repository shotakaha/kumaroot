# WordPressしたい（`wordpress`）

```{literalinclude} ../../examples/docker/wordpress.yaml
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

## WordPressについて

WordPressをDockerで起動します。
MySQLデータベースとWordPressをセットで構成しており、認証情報は環境変数で設定します。
環境変数は`.env`で変更できます。

上記サンプルでは、デフォルト値を指定しているため、`.env`ファイルがなくても動作します。
起動後、ブラウザで `http://localhost:8080` を開いて、WordPressの初期セットアップ画面にアクセスできます。
コンテナー内で `wp` コマンド（WP-CLI）を使って、データベースやプラグインを管理できます。
