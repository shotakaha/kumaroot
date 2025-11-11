# コミット前にチェックしたい（`pre-commit`）

```console
$ pre-commit --version
pre-commit 4.4.0

$ pre-commit install
$ pre-commit run --all-files
```

`pre-commit`は[Git Hooks](../git/git-hooks.md)を使って、
コミット前などにコードのチェック作業などを自動化できるツールです。
設定ファイルは`.pre-commit-config.yaml`です。
Pythonで書かれていますが、いろいろなプログラミング言語やプロジェクトで使えるようになっています。

コミット時に自動的にリンターやフォーマッターを実行することで、
コード品質を保ち、後戻り作業を減らすことができます。

:::{note}

[commitizen](./python-commitizen.md)を有効にすると、自動で追加されます。

:::

## インストールしたい（`pre-commit`）

複数のインストール方法から選べます：

- pipでインストール

```console
$ pip3 install pre-commit
$ pip3 install -U pre-commit  # アップグレード
```

- pipxでインストール

```console
$ pipx install pre-commit
$ pipx upgrade pre-commit
```

- poetryで依存関係に追加

```console
$ poetry add pre-commit --group=dev
```

- uvでインストール（推奨）

```console
$ uv tool install pre-commit
$ uv tool upgrade pre-commit
```

## 設定ファイルを作成したい（`.pre-commit-config.yaml`）

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

## フックをインストールしたい（`install`）

```console
$ pre-commit install
```

`pre-commit install`でGit Hooksを有効化できます。
`.pre-commit-config.yaml`の設定が完了したら実行してください。

## フックを実行したい（`run`）

```console
$ pre-commit run --all-files
```

`pre-commit run --all-files`で
すべてのファイルに対してチェックを実行します。

`trailing-whitespace`や`end-of-file-fixer`などのフックは自動でファイルを修正します。

### フックしたい（`stages`）

フックのタイミングは`[stages]`で変更できます。
デフォルトでは`pre-commit`（コミットの直前）に実行されます。

| Git Hook | タイミング | 設定例 |
|---|---|---|
| `pre-commit` | コミットの直前 | `stages: [pre-commit]` |
| `commit-msg` | コミットメッセージ作成の直後 | `stages: [commit-msg]` |
| `pre-push` | プッシュの直前 | `stages: [pre-push]` |
| `post-checkout` | ブランチ切り替え後 | `stages: [post-checkout]` |
| `post-commit` | コミット後 | `stages: [post-commit]` |
| `post-merge` | マージ後 | `stages: [post-merge]` |

設定ファイルでタイミングを指定する例：

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: detect-private-key
        stages: [pre-push]  # プッシュの直前に実行
```

### 複数のフックをインストールしたい

```console
$ pre-commit install --install-hooks --hook-type pre-commit --hook-type commit-msg
```

`--install-hooks --hook-type フックタイプ`でフックのタイミングを追加できます。

```yaml
# .pre-commit-config.yaml
default_install_hook_types:
  - pre-commit
  - commit-msg
  - pre-push
```

`.pre-commit-config.yaml`で有効にするフックタイプを指定できます。

## フックを確認したい

```console
$ find .git/hooks -type f ! -name "*.sample" -perm u+x
```

`.git/hooks/`でフックを確認できます。

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
