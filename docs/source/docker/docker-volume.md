# データを保存したい（``volume``）

```bash
$ docker volume create ボリューム名
$ docker volume ls
```

コンテナ内に作成したデータは、コンテナを削除すると消えてしまいます。
``docker volume``コマンドで保存先を作成することで、簡単にデータを保存できます。

保存先（＝ボリューム）には``named volume``と``bind volume``の2種類あります。
``named volume``はDockerが勝手に（＝内部パス``/var/lib/docker/volumes/...``）に作成してくれるボリュームです。
``binde volume``は自分でパス指定が必要なボリュームです。
やりたいことに応じて使い分けます。

## ボリュームの詳細を知りたい

```bash
$ docker volume inspect ボリューム名
```

``named volume``を使ったときに、データが保存されているパスなどの詳細を確認できます。
