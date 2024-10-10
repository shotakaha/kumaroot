# 複数コンテナーを一時停止／再開したい（`stop` / `start`）

```console
// 複数コンテナを一時停止
$ docker compose stop

// 複数コンテナを再開
$ docker compose start
```

`docker compose stop`コマンドで、作成したコンテナを一時停止できます。
`docker compose start`コマンドで、停止したコンテナを再開できます。
コンテナが作成されてない場合、エラーになります。
