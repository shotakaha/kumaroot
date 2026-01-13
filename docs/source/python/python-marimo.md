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

## 編集したい（`marimo edit`）

```console
$ marimo edit notebook.py
```

## 実行したい（`marimo run`）

```console
$ marimo run notebook.py
```

## 新規作成したい（`marimo new`）

```console
$ marimo new
$ marimo new "prompt text"
$ marimo new prompt.txt
```

`marimo new`コマンドで新しいノートブックを作成できます。
引数を指定しない場合は、空のノートブックが立ち上がります。
プロンプト文字列もしくはファイルを指定すると、Marimo AIがノートブックをプロトタイプしてくれます。

:::{seealso}

ヘルプにあったプロンプトを実際に入力してみました。

```console
$ uvx marimo new "Plot an interactive 3D surface with matplotlib."

Before using marimo's Text-To-Notebook AI feature, you should know:

1. Your prompt will be sent to marimo's API at `https://ai.marimo.app/`
2. The API uses OpenAI/Anthropic's models to convert your prompt into a notebook
3. Your prompt is securely stored for caching purposes (fast response times)
4. No personal data beyond the prompt itself is collected
5. You can revoke consent at any time by modifying ~/.marimo/state.toml

Do you accept these terms? (y/n)
```

利用条件に同意すると、
`numpy`や`matplotlib`などをインポートするノートブックが作成されました。
この段階ではファイルは`/var/folders/`の中に一時的な名前になっていますが、
`Cmd + S`で任意のパスに保存できます。

最初のセルを実行すると`ModuleNotFoundError`が発生しましたが
ノートブック上に表示された`Missing packages`ダイアログにしたがうだけで
スムーズに`uv`を使ってインストールできました。

:::
