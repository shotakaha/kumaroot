# ノートブックしたい（`marimo`）

```console
$ pip install marimo
```

```console
$ poetry add marimo --group dev
```

```console
$ uv pip install marimo
$ uv tool install marimo
$ uv add marimo --dev
```

## チュートリアルしたい（`marimo tutorial`）

```console
$ marimo tutorial intro
$ marimo tutorial dataflow
$ marimo tutorial ui
$ marimo tutorial --help
```

`marimo tutorial`コマンドでノートブックの使い方を体験できます。
ローカルサーバーが起動し、ブラウザーが自動で立ち上がります。

`intro | dataflow | ui | markdown | plots | sql | layout | fileformat | markdown-format | for-jupyter-users`のトピックごとのサブコマンドがあるので、この順番でひととおり確認してみるとよいです。
