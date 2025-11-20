# Jupytextしたい（``jupytext``）

```console
// notebooksをmarkdownに変換
$ jupytext --set-formats ipynb,md:myst ファイル.ipynb
$ jupytext --sync ファイル.ipynb
$ jupytext --sync ファイル.md
```

`jupytext`でノートブック（`.ipynb`）をテキスト形式（`.py`、`.md`）のファイルに変換／ペアリングできます。
ノートブックの使い勝手を保ちつつ、
Gitなどのバージョン管理ツールでの運用を快適にするためのツールです。

:::{note}

Pythonのコーディングをするときにノートブックは欠かせません。
しかし、ノートブックの中身はJSON形式であるため、Gitで管理していてもその差分の確認は（人間には）とても難解です。
マージコンフリクトが生じたときの修正は、とてもとても大変です。

また、実行結果に図などが含まれたままにしておくと、`ipynb`形式のファイルはすぐに肥大化してしまいます。
ある程度のサイズになると、Git LFSに追加する必要がでてきます。

Jupytextは、そのような課題を解決してくれます。

:::

## インストールしたい（`jupytext`）

- `pipx`でインストール

```console
$ pipx install jupytext
```

- `poetry`でインストール

```console
$ poetry add jupytext --group=dev
```

- `uv`でインストール

```console
$ uv tool install jupytext
```

## 双方向に同期したい（`--set-formats`）

```console
$ jupytext --set-formats ipynb,md:myst ファイル.ipynb
[jupytext] Reading ファイル.ipynb in format ipynb
[jupytext] Updating notebook metadata with '{"jupytext": {"formats": "ipynb,md:myst"}}'
[jupytext] Updating ファイル.ipynb
[jupytext] Updating ファイル.md
```

`--set-formats`オプションで形式を指定することで、
ファイルとファイルをペアリングし、双方向に同期できます。

上記サンプルでは`ipynb`形式のノートブックと
`md:myst`形式のテキストファイルをペアリングしています。

## 片方向に変換したい（`--to` / `--from`）

```console
// .ipynbから.mdに変換
$ jupytext --to md:myst ファイル名.ipynb

// .ipynbから.pyに変換
$ jupytext --to py:percent ファイル名.ipynb
```

指定したフォーマットに変換できる
`--to フォーマット`（や`--from フォーマット`）オプションもあります。
このオプションはただの変換するだけで、ファイル間のペアリングはされません。
Jupytextを使うのであれば`--set-formats`オプションを使えばよいと思います。

## ディレクトリ分割したい

```console
$ jupytext --set-formats notebooks//ipynb,markdowns//md:myst notebooks/*.ipynb
```

ノートブック用、Markdown用、スクリプト用に
ディレクトリを分割したまま、ペアリングすることもできます。

:::{seealso}

僕はノートブックは機能の確認や単体テスト用に作成することが多く、とりあえず`notebooks`という専用のディレクトリの中で管理することにしています。
この中に同名の`.md`ファイルなどが作成されると、ファイルを開くときに難儀します。
なので、Jupytextで連携したファイルたちはディレクトリを分割して管理することにしています。

:::

## 同期したい（`--sync`）

```console
$ jupytext --sync ファイル.ipynb
[jupytext] Reading ファイル.ipynb in format ipynb
[jupytext] Loading ファイル.md
[jupytext] Unchanged ファイル.ipynb
[jupytext] Updating ファイル.md
```

`--sync`オプションでファイル間の同期をとることができます。
ペアリングしたファイルであれば、どのファイルを編集してもOKです。

## 全体設定したい（`jupytext.toml`）

```toml
# ペアリングの設定
# ディレクトリを分割して連携
[formats]
"notebooks/" = "ipynb"
"markdowns/" = "md:myst"
"scripts/" = "py:light"

# ノートブックのメタデータの設定
notebook_metadata_filter = ""

# セルのメタデータの設定
cell_metadata_filter = ""
```

`jupytext.toml`に、プロジェクト単位のJupytextの全体設定を記述できます。
この設定ファイルはプロジェクトルートに配置します。
もしくは`pyproject.toml`の`[tool.jupytext]`セクションに記述します。

`notebook_metadata_filter`で、
ノートブックのメタデータに残す情報を設定できます。
`cell_metadata_filter`で
セルのメタデータに残す情報を設定できます。

それぞれを空文字列（`""`）にすることで、すべてのメタデータを除去できます。
Gitで管理するときに最適です。

### Markdownフォーマット

- `md`: 標準的なMarkdown形式
- `md:myst`: MyST Markdown形式。Sphinxとの連携向き
- `Rmd`: R Markdown形式
- `qmd`: Quarto形式

### Pythonフォーマット

- `py:percent`: パーセント形式。`# %%`でセルを区切る形式
- `py:light`: ライト形式
- `py:hydrogen`: Hydrogen形式

### Notebookフォーマット

- `ipynb`: Jupyter Notebook形式

## メタデータしたい（`notebook_metadata_filter` / `cell_metadata_filter`）

```toml
# デフォルト値
notebook_metadata_filter="kernelspec,jupytext"
cell_metadata_filter="all,-autoscroll,-collapsed,-scrolled,-trusted,-ExecuteTime"
```

`notebook_metadata_filter`と
`cell_metadata_filter`で
メタデータの扱い方を設定できます。
デフォルト値は上記のように設定されています。
除外する項目は先頭に`-（マイナス）`をつけます。

:::{note}

メタデータフィルターの設定は、記述する順序の影響を受けません。
読みやすさを優先して記述して大丈夫です。

:::

```toml
# Markdownを中心とする推奨設定
notebook_metadata_filter = "jupytext,-kernelspec,-jupytext.text_representation"
cell_metadata_filter = "-all"
```

Markdownを中心にGit管理する場合の推奨設定です。
メタデータを最小限にすることで、差分を確認しやすくなります。

### Notebookのメタデータ

- `jupytext`: Jupytext固有の設定情報。ファイル形式の同期設定などが含まれます。
- `kernelspec`: Kernel情報。除外してOK
- `language_info`: 言語情報
- `widgets`: Widgetの設定
- `varInspector`: Variable Inspectorの設定

### Cellのメタデータ

- `ExecuteTime`: 実行時刻（デフォルト除外）
- `autoscroll`: 自動スクロール（デフォルト除外）
- `collapsed`: セルの折りたたみ（デフォルト除外）
- `scrolled`: スクロール状態（デフォルト除外）
- `trusted`: 信頼状態（デフォルト除外）
- `hide_input` / `hide_output`: 表示制御

## コミットフックしたい

```yaml
# .pre-commit-config.yaml
repos:
- repo: ...
- repo: https://github.com/mwouts/jupytext
  rev: v1.16.4b
  hooks:
  - id: jupytext
    args: [--sync]
```

`pre-commit-hook`も用意されています。
`.pre-commit-config.yaml`に追加することで、
コミット直前に自動的にファイル間の同期をとることができます。

## リファレンス

- [Jupytext](https://jupytext.readthedocs.io/en/latest/)
- [作者（Marc Wouts）の発表動画 - JupyterCon2020](https://youtu.be/SDYdeVfMh48)
