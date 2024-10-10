# コミットをチェックしたい（``pre-commit``）

```console
$ pre-commit --version
pre-commit 3.8.0

$ pre-commit install
$ pre-commit run --all-files
```

`pre-commit`は[Git Hooks](../git/git-hooks.md)を使って、コミット前などにコードのチェック作業などを自動化できるツールです。
`pre-commit`以外にも`commit-msg`や`pre-push`などさまざまなフックに対応しています。
設定ファイルは`.pre-commit-config.yaml`です。
Pythonで書かれていますが、いろいろなプログラミング言語やプロジェクトで使えるようになっています。

:::{note}

[commitizen](./python-commitizen.md)を有効にすると、自動で追加されます。

:::

## インストールしたい（`pre-commit`）

- `pip`でインストール

```console
$ pip3 install pre-commit
$ pip3 install -U pre-commit
```

- `pipx`でインストール

```console
$ pipx install pre-commit
$ pipx upgrade pre-commit
```

- `poetry`でインストール

```console
$ poetry add pre-commit --group=dev
```

- `uv`でインストール

```console
$ uv tool install pre-commit
$ uv tool upgrade pre-commit
```

## 設定したい（`.pre-commit-config.yaml`）

```yaml
repos:
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v4.6.0  # 最新バージョンにする
  hooks:
  - id: trailing-whitespace
  - id: end-of-file-fixer
  - id: check-added-large-files
- repo: リポジトリ
  rev: バージョン
  hooks:
  - id: フック名
```

`.pre-commit-config.yaml`にフック情報を記述します。
設定できるフックは[Supported Hooks](https://pre-commit.com/hooks.html)で確認できます。

## フックしたい（`run`）

```console
$ pre-commit run --all-files
```

`run`コマンドでフックの確認ができます。
`--all-files`オプションで、カレントディレクトリの下にあるすべてのファイルに対してチェックを実行します。
``trailing-whitespace``や``end-of-file-fixer``などのフックを有効にしている場合、ファイルが自動で修正されます。

## pre-commit-hooksしたい

```yaml
repos:
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v4.6.0
  hooks:
  - id: detect-private-key
  - id: trailing-whitespace
    args: ["--markdown-linebreak-ext=md"]
  - id: end-of-file-fixer
  - id: check-case-conflict
  - id: check-merge-conflict
  - id: check-added-large-files
    args: ["--maxkb=500"]
  - id: check-json
  - id: check-toml
  - id: check-yaml
  - id: name-tests-test
    args: [--pytest-test-first]
```

`pre-commit-hooks`のフックから、
使うとよさそうなものを選んでみました。

## ruff-pre-commitしたい

`ruff`は、Pythonプロジェクトの
リンター＆フォーマッターです。
コミットごとに自動チェックすることで、コードの表記ゆれを抑えることができます。

フックの設定方法は[](./python-ruff.md)に整理しました。

## commitizenしたい

`commitizen (cz)`はコミットメッセージの形式を守るためのツールです。
`stages: [commit-msg]`でコミットメッセージを保存したあとにフックがかかるようにしておきます。

フックの設定方法は[](./python-commitizen.md)に整理しました。

## poetryしたい

```yaml
repos:
- repo: ...
- repo: https://github.com/python-poetry/poetry
  rev: 1.8.0
  hooks:
  - id: poetry-check
    args: [--lock]
    stages: [pre-push]
  #- id: poetry-lock
  - id: poetry-export
    args: [--format, requirements.txt, --output, requirements.txt]
    stages: [pre-push]
  #- id: poetry-install
```

Pythonプロジェクトを`poetry`で管理している場合は、
`poetry-check`（＝`poetry check`）、
`poetry-lock`（＝`poetry lock`）、
`poetry-export`（＝`poetry export`）、
`poetry-install`（＝`poetry install`）
のフックを導入してみるとよいかもしれません。

それぞれに適切な`args`を設定して使うとよいと思います。
また、コミット時ではなくプッシュ時（`pre-push`）に設定するとよいと思います。

:::{note}

Read the Docsに公開するために`requirements.txt`が必要です。
このリポジトリも、も`poetry-export`フックを使って、
`requirements.txt`を生成できるようにしてあります。

:::

## 脆弱性を検出したい（`Bandit`）

```yaml
repos:
- repo: ...
- repo: ...
- repo: https://github.com/PyCQA/bandit
  rev: 1.7.4
  hooks:
  - id: bandit
    args: ["-r", "ディレクトリ名"]
```

## nbstripoutしたい

```yaml
repos:
- repo: ...
- repo: https://github.com/kynan/nbstripout
  rev: 0.5.0
  hooks:
  - id: nbstripout
```

Jupyter Notebookを使っている場合、
実行結果を削除したファイルをコミットしたい場合があります。
`nbstripout`でコミット前に出力をクリアできます。

:::{note}

`.ipynb`ファイルは、実行結果を残しているといつのまにか間に肥大化している可能性があります。
また、デバッグ用途に使っている場合、
うっかりとシークレット情報を出力に残したままにしてしまう可能性もあります。
そのようなことを回避したい場合、このツールは有用です。
:::

## pytestしたい

```yaml
repos:
- repo: local
  hooks:
  - id: pytest
    name: pytest
    entrypoint: pytest --verbose
    stages:
      - [pre-push]
    language: system
```

[pytest](./python-pytest.md)用のフックはGitHub上にはないようです。
`pre-commit`はローカル（`local`）にインストールされているコマンドを使うことができます。
プッシュ時（`pre-push`）にテストを走らせるとよいと思います。

:::{note}

テストはCI/CDでも実行しているかもしれません。
ローカルからのプッシュ前に確認を追加することで、
パイプライン時間の無駄遣いを減らすことができます。

:::

## リファレンス

- [pre-commit](https://pre-commit.com/)
- [pre-commit/pre-commit](https://github.com/pre-commit/pre-commit)
- [pre-commit/pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
- [astral-sh/ruff-pre-commit](https://github.com/astral-sh/ruff-pre-commit)
- [poetry](https://python-poetry.org/docs/pre-commit-hooks)
