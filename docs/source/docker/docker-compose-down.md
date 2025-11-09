# コンテナを削除したい（``docker compose down``）

```console
$ docker compose down
```

`docker compose down`コマンドでコンテナを削除できます。
実行中のコンテナに対してもコマンドを実行でき、
コンテナに紐づいているネットワークも自動で削除できます。
ボリュームは削除されません。

:::{note}

ボリュームは保存されます

`docker compose down`でコンテナは削除されますが、ボリューム内のデータは保存されたままです。
これはデータベースなどの重要なデータを誤って削除しないための安全設計です。
ボリュームも削除したい場合は、`--volumes`オプションを使用してください。

:::

## ボリュームを削除したい（`--volumes`）

```console
$ docker compose down --volumes
```

`-v / --volumes`オプションで、作成したボリュームを削除できます。

デフォルトでは`docker compose down`を実行してもボリュームは削除されず、データは保存されたままです。
これにより、コンテナを削除した後でも、データベースなどのボリューム内のデータを復元できます。
ボリュームの内容が不要な場合は、`--volumes`オプションを追加して完全にクリーンアップしてください。

## イメージを削除したい（`--rmi`）

```console
$ docker compose down --rmi local
$ docker compose down --rmi all
```

`--rmi`オプションで、コンテナ作成に使用したイメージも同時に削除できます。

- `local`: `build:`で指定して自分たちが作成したカスタムイメージのみ削除します。Docker Hubなどから`pull`したイメージは削除されません。
- `all`: すべてのイメージを削除します。`local`で作成したカスタムイメージも、外部から取得したイメージも両方削除されます。


## リファレンス

- [docker compose down - docs.docker.jp](https://docs.docker.jp/engine/reference/commandline/compose_down.html)
