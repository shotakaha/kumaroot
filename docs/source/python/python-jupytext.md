# Jupytextしたい（``jupytext``）

```console
// notebooksをmarkdownに変換
$ jupytext --set-formats ipynb,md:myst ファイル.ipynb
$ jupytext --sync ファイル.ipynb
$ jupytext --sync ファイル.md
```

`jupytext`でノートブック（`ipynb`）をテキスト形式のファイルに変換／ペアリングできます。
ノートブックの使い勝手はそのままに、
Gitなどを使ったファイル管理をより簡単にするためのツールです。

:::{note}

Pythonのコーディングをするときにノートブックは欠かせません。
しかし、ノートブックの中身はJSON形式であるため、Gitなどで管理していてもその差分の確認は（人間には）とても難解です。
マージコンフリクトが生じたときの修正は、とてもとても大変です。

また、図などをそのままにしておくと、`ipynb`形式のファイルはすぐに肥大化してしまいます。
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

## ペアリングしたい（`--set-formats`）

```console
$ jupytext --set-formats ipynb,md:myst ファイル.ipynb
[jupytext] Reading ファイル.ipynb in format ipynb
[jupytext] Updating notebook metadata with '{"jupytext": {"formats": "ipynb,md:myst"}}'
[jupytext] Updating ファイル.ipynb
[jupytext] Updating ファイル.md
```

`--set-formats`オプションで形式を指定することで、
ファイルとファイルをペアリングできます。

上記サンプルでは`ipynb`形式のノートブックと
`md:myst`形式のテキストファイルをペアリングしています。

:::{note}

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

:::

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

プロジェクトルートに配置した`jupytext.toml`
または`pyproject.toml`に
Jupytextの全体設定を記述できます。

`notebook_metadata_filter`で、
ノートブックのメタデータに残す情報を設定できます。

`cell_metadata_filter`で
セルのメタデータに残す情報を設定できます。

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
