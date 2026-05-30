# Python3したい（`python3`）

```{literalinclude} ../../examples/docker/python3.yaml
---
language: yaml
---
```

## コンテナーを起動したい

```console
$ docker compose up
```

## コンテナーで操作したい

```console
$ docker compose exec python-app bash
```

## コンテナーを終了したい

```console
$ docker compose down
```

## Python3について

Python3のDockerイメージを使って開発環境を構築できます。
サービス名を`python-app`とし、イメージは`python:3.12-slim`を指定しています。
ボリュームでホストディレクトリを`/app`にバインドマウントすることで、手元のファイルをコンテナ内で処理できるようにしています。

`docker compose up` でコンテナーを起動すると、`command`に設定した`python app.py`が実行されます。
コンテナー内で `pip install` でパッケージをインストールしたり、Pythonスクリプトを実行したりできます。
slim バージョンはイメージサイズが小さく、本番環境にも適しています。
