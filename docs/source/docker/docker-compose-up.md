# コンテナを作成したい（`compose up`）

```console
$ docker compose up -d
```

`docker compose up`コマンドでコンテナを作成できます。
ローカルにイメージがない場合は、プルしてから実行されます。
`-d / --detach`はバックグラウンド実行するためのオプションです。
ほとんどの場合でつけておけばOKです。
