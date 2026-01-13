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

`intro | dataflow | ui | markdown | plots | sql | layout | fileformat | markdown-format | for-jupyter-users`のトピックごとのサブコマンドがあります。
この順番で確認するのが公式でオススメされています。

Jupyter Notebookを使ったことがある場合は`for-jupyter-users`から確認してもいいかもしれません。

## 編集したい（`marimo edit`）

```console
$ marimo edit notebook.py
```

`marimo edit`コマンドでノートブックを編集できます。
引数なしで実行するとMarimoのスタート画面が起動します。

## 実行したい（`marimo run`）

```console
$ marimo run notebook.py
$ marimo run --sandbox notebook.py
```

`marimo run`コマンドでノートブックを実行できます。
`--sandbox`オプションで、`uv`で隔離した環境で実行できます。

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

## 移行したい（`marimo convert`）

```console
$ marimo convert notebook.ipynb --output marimo.py
$ marimo convert notebook.md --output marimo.py
$ marimo convert notebook.py --output marimo.py
```

`marimo convert`コマンドで、既存のJupyter NotebookをMarimo Notebookに変換できます。

入力にしていできるファイル形式は
ノートブック形式（`.ipynb`）、
Markdown形式（`.md`）、
スクリプト形式（`.py`）がサポートされています。

`--output`オプションで、出力ファイル名を指定できます。
指定がない場合は標準出力（`stdout`）に変換した結果が表示されます。

:::{note}

Jupyter Notebook -> Marimo Notebookへの一方向変換コマンドです。

:::

## 配布したい（`marimo export`）

```console
$ marimo export html marimo_nb.py
$ marimo export html-wasm marimo_nb.py
$ marimo export ipynb marimo_nb.py
$ marimo export md marimo_nb.py
$ marimo export script marimo_nb.py
```

`marimo export`コマンドでMarimoノートブックを配布できる形式に変換できます。
配布形式は`export`のサブコマンドとして用意されてます。

:::{note}

既存のMarimo Notebookに対して、配布できる形式のスナップショットを作成するコマンドのようです。

`convert`の逆操作ではないようです（要確認）。

:::

## チェックしたい（`marimo check`）

```console
$ marimo check .
$ marimo check marimo_nb.py --fix
```

`marimo check`コマンドでMarimo Notebookの構文チェックができます。
`--fix`オプションで自動修正できます。
`--strict`オプションでwarningもerrorとみなし厳格チェックできます。
CIなどで使う際に有効かもしれません。

## Marimo or Jupyter

Marimo NotebookとJupyter Notebookは解析のフェーズに合わせて
使い分けるのがよさそうです。

解析の方向性を模索している段階では、セルの実行順序に依存しないJupyter Notebookのほうが思いつくままに試行錯誤できてよさそうです
（この段階ではソースコードもGit管理しなくてもいいかも）。

ある程度、方向性が固まってきて、データセットを変更しながら反復処理するような段階でMarimo Notebookに移行して、ソースコードを管理しながら解析を進めるのがよさそうです。
