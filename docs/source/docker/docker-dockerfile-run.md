# RUNしたい（`RUN`）

```docker
RUN コマンド
```

`RUN`でコマンドを実行し、コンテナの中身をカスタマイズできます。
ただし`RUN`ごとにレイヤーが作成され、イメージサイズが増加するため、
まとめることができるコマンド群は、一行にまとめてしまうのが鉄則です。

:::{note}

一行にまとめる場合でも`\`で改行して、読みやすくできます。
2つのコマンドをまとめる場合は`&&`で連結します。

:::

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

`apt-get install`や対話的にインストールするツールですが、
`-y`オプションですべてのプロンプトに自動でyesと答えるようにしています。
また`--no-install-recommends`オプションで、
必要最小限のパッケージのみをインストールしています。

そして最後の`rm -rf`でキャッシュをクリーンアップしています。
（念のため`apt-get clean`も実行しています）

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
`virtualenv`で仮想環境を作成し、そこに`poetry`を追加しています。
ホストPCからコピーした`pyproject.toml`で必要はパッケージをインストールしています。
