# RUNしたい（``RUN``）

```docker
RUN コマンド
```

## パッケージを追加したい（Debian/Ubuntu）

```docker
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    追加したいパッケージ名1 \
    追加したいパッケージ名2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
```

Debian/Ubuntuベースのイメージを使っている場合に、パッケージを追加するコマンドです。
おまじないのように書いておくとよいと思います。

## Poetryしたい（``virtualenv`` / ``poetry``）

```docker
WORKDIR /app

COPY pyproject.toml ./

RUN pip3 install -U virtualenv && virtualenv venv
RUN . venv/bin/activate
RUN pip3 install -U poetry
RUN poetry install
```

[Poetry](../python/python-poetry.md)を使ったPython開発環境を作成するコマンドです。
``virtualenv``で仮想環境を作成し、そこに``poetry``を追加しています。
ホストPCからコピーした``pyproject.toml``で必要はパッケージをインストールしています。
