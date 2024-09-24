# コミットをチェックしたい（``pre-commit``）

```console
$ pre-commit --version
pre-commit 3.8.0

$ pre-commit install
$ pre-commit run --all-files
```

`pre-commit`はGit hooksを使って、コミット前にコードのチェック作業を自動化できるツールです。
Pythonで書かれていますが、いろいろなプログラミング言語やプロジェクトで使えるようになっています。
設定ファイルは`.pre-commit-config.yaml`です。

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

以下ではフォーマッタに[black](./python-black.md)、リンターに[ruff](./python-ruff.md)を使う方法で設定します。

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
`--all-files``オプションで、カレントディレクトリの下にあるすべてのファイルに対してチェックをかけられます。
``trailing-whitespace``や``end-of-file-fixer``などのフックを有効にしている場合は、
ファイルが修正されます。

## pre-commit-hooksしたい

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: check-added-large-files
        args: ["--maxkb=500"]
      - id: check-merge-conflict
      - id: check-json
      - id: check-toml
      - id: check-yaml
      - id: detect-private-key
      - id: end-of-file-fixer
      - id: trailing-whitespace
        args: ["--markdown-linebreak-ext=md"]
```

`pre-commit-hooks`のフックから、
使うとよさそうなものを選んでみました。

## ruff-pre-commitしたい

```yaml
repos:
  - repo: ...
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.7
    hooks:
      # - id: ruff
      - id: ruff-format
```

`ruff`で`ruff check .``が実行されます。
ファイルは修正されません。

`ruff-format`を有効にすると`ruff format .`が実行されます。
ファイルは修正されます。

## commitizenしたい

```yaml
repos:
- repo: ...
- repo: https://github.com/commitizen-tools/commitizen
  rev: v3.29.0
  hooks:
  - id: commitizen
    stages:
      - commit-msg
```

`cz init`すると追加されているはずのフックです。
`stages: [commit-msg]`でコミットメッセージだけにフックがかかるようになっています。


## poetryしたい

```yaml
repos:
- repo: ...
- repo: https://github.com/python-poetry/poetry
  rev: 1.8.0
  hooks:
  - id: poetry-check
    args: [--lock]
  #- id: poetry-lock
  - id: poetry-export
    args: [--format, requirements.txt, --output, requirements.txt]
  #- id: poetry-install
```

`poetry-check`（＝`poetry check`）、
`poetry-lock`（＝`poetry lock`）、
`poetry-export`（＝`poetry export`）、
`poetry-install`（＝`poetry install`）
のフックが利用できます。

それぞれに`args`を設定して使うとよいと思います。

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

## リファレンス

- [pre-commit](https://pre-commit.com/)
- [pre-commit/pre-commit](https://github.com/pre-commit/pre-commit)
- [pre-commit/pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
- [astral-sh/ruff-pre-commit](https://github.com/astral-sh/ruff-pre-commit)
- [poetry](https://python-poetry.org/docs/pre-commit-hooks)
