# ファイルをコピーしたい（`compose cp`）

```console
// ホスト -> コンテナ
$ docker compose cp ホストOSのパス コンテナ名:コンテナ内のパス

// コンテナ -> ホスト
$ docker compose cp コンテナ名:コンテナ内のパス ホストOSのパス
```

`docker compose cp`でホストPCとコンテナ間のファイルやフォルダのコピーができます。
引数の順番を入れ替えるだけで、双方向のコピーが可能です。
コンテナを指定する書式は`ssh`や`rsync`などと同じです。
