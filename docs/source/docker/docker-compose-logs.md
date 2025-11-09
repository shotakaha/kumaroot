# ログを確認したい（``docker compose logs``）

```console
// すべてのコンテナのログを確認する
$ docker compose logs

// 特定のサービスのログを確認する
$ docker compose logs サービス名
```

`docker compose logs`コマンドで、コンテナのログを表示できます。
コンテナの動作確認やデバッグ時に使用します。

サービス名を指定しない場合は、すべてのコンテナのログが表示されます。
`サービス名`は`compose.yaml`の`services:`セクションで定義したコンテナの名前です。

## ログをファイルに保存したい

```console
$ docker compose logs > logs.txt

// 特定のサービスのログを保存する
$ docker compose logs サービス名 > service-logs.txt
```

表示したログをリダイレクトしてファイルに保存できます。

## ログの末尾を確認したい（`--tail`）

```console
$ docker compose logs --tail 10

// 最新100行のログを表示する
$ docker compose logs --tail 100

// 特定のサービスの最新50行を保存する
$ docker compose logs --tail 50 サービス名 > recent-logs.txt
```

`--tail`オプションで、ログの末尾から指定行数分を取得できます。
デフォルトは`--tail 10`で、最新10行が表示されます。
数字を指定することで、取得する行数を変更できます。

## リアルタイムで更新したい（`-f / --follow`）

```console
$ docker compose logs --follow
$ docker compose logs -f

// 特定のサービスをリアルタイムで監視する
$ docker compose logs -f サービス名

// ログの最新50行から監視を開始
$ docker compose logs --tail 50 --follow

// ログを確認しながら保存する
$ docker compose logs -f | tee logs.txt
```

`--follow`オプションで、ログの更新をリアルタイムで表示できます。
新しいログが出力されるたびに画面に追加されます。

`--tail`と組み合わせると、最新N行から監視を開始できます。
確認しながらファイルに保存する場合は、[teeコマンド](../command/command-tee.md)で分岐するとよいです。
