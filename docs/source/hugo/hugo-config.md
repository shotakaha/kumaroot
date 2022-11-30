# 設定ファイル（``/config/``）

プロジェクトの設定をファイルに保存できる。
設定に``TOML`` / ``YAML`` / ``JSON``が利用できる。
僕は``TOML``で設定するのが好きです。

## デフォルトの設定ファイルを使いたい

```text
/config.toml
```

プロジェクトルートにある``config.toml``が自動で読み込まれます。

## 設定ファイルを切り替えたい

```bash
$ hugo --config 設定ファイル
$ hugo --config 設定ファイル1,設定ファイル2,設定ファイル3
```

``hugo --config 設定ファイル``を使ってビルド時に設定ファイルの切り替えができる。
設定ファイルは複数指定できる。

## 設定ファイルを場合分けしたい

```text
/config/_default/config.toml  # デフォルト設定（デバッグ用？）
/config/gitlab/config.toml    # GitLab Pagesに公開する設定
/config/www2/config.toml      # www2に公開する設定
/config/環境名/config.toml
```

ローカルでの開発、GitLab Pagesへの公開、本番環境への公開など、それぞれの場合に応じて設定ファイルを作成できる。
公開先によっては``baseURL``を変更する必要がある場合などに便利です。

また、設定ファイルを切り替える

```bash
$ hugo -e 環境名
$ hugo -e gitlab  # デフォルト + GitLab Pagesの設定
$ hugo -e www2    # デフォルト + 公開設定
```

## リファレンス

- [Configure Hugo](https://gohugo.io/getting-started/configuration/)
