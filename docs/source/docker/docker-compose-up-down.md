# コンテナを作成／削除したい（`compose up` / `compose down`）

```console
// 複数コンテナを作成
$ docker compose up -d

// 複数コンテナを削除
$ docker compose down
```

`docker compose up`コマンドでコンテナを作成できます。
ローカルにイメージがない場合は、プルしてから実行されます。
`-d / --detach`オプションでバックグラウンド実行します。
とりあえずつけておけばOKです。

`docker compose down`コマンドでコンテナを削除できます。
実行中のコンテナに対してもコマンドを実行でき、
コンテナに紐づいているネットワークも自動で削除できます。
