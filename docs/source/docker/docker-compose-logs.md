# ログを確認したい（`compose logs`）

```console
// Composeのログを確認する
$ docker compose logs

// 特定のサービスのログを確認する
$ docker compose logs サービス名
```

`docker compose log`コマンドで、コンテナのログを表示できます。
コンテナの動作確認やデバッグ時に使用します。

## ログをファイルに保存したい

```console
$ docker compose logs > logs.txt

// 特定のサービスのログを保存する
$ docker compose logs サービス名 > service-logs.txt
```

表示したログをリダイレクトしてファイルに保存できます。

## ログの末尾を確認したい（`--tail`）

```console
$ docker compose logs --tail

// 最新100行のログを保存する
$ docker compose logs --tail 100 > recent-logs.txt
```

`--tail`オプションで、ログの末尾を取得できます。

## リアルタイムで更新したい（`-f / --follow`）

```console
$ docker compose logs --follow
$ docker compose logs -f

// ログを確認しながら保存する
$ docker compose logs -f | tee logs.txt
```

`--follow`オプションで、ログの更新をリアルタイムで表示できます。

確認しながらファイルに保存する場合は、[teeコマンド](../command/command-tee.md)で分岐するとよいです。
