# コミット前にチェックしたい（`pre-commit`）

```console
$ pre-commit --version
pre-commit 4.6.2

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

## 設定したい（`.pre-commit-config.yaml`）

```console
$ pre-commit sample-config > .pre-commit-config.yaml
```

`pre-commit sample-config`コマンドで、雛形となる`.pre-commit-config.yaml`を出力できます。
出力される`rev`は固定の古いバージョンなので、次のように書き換えて使うのがオススメです。

```yaml
repos:
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v6.0.0  # 最新バージョンにする
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
$ pre-commit run -a  # 短縮形
```

`pre-commit run --all-files`（短縮形`-a`）で
すべてのファイルに対してチェックを実行します。

`trailing-whitespace`や`end-of-file-fixer`などのフックは自動でファイルを修正します。

## フックを追加したい

```console
$ pre-commit install --install-hooks
$ pre-commit install --install-hooks --hook-type pre-commit
$ pre-commit install --install-hooks --hook-type commit-msg
```

`--install-hooks`で、`.pre-commit-config.yaml`に書かれたフックをインストールできます。
`--hook-type フックタイプ`で、フックのタイミングを追加できます。

### フックのタイミング

フックのタイミングは`[stages]`で変更できます。
デフォルトでは`pre-commit`（コミットの直前）に実行されます。

| Git Hook | タイミング | 設定例 |
| --- | --- | --- |
| `pre-commit` | コミットの直前 | `stages: [pre-commit]` |
| `pre-merge-commit` | マージコミットの直前 | `stages: [pre-merge-commit]` |
| `commit-msg` | コミットメッセージ作成の直後 | `stages: [commit-msg]` |
| `prepare-commit-msg` | コミットメッセージ作成の直前 | `stages: [prepare-commit-msg]` |
| `pre-push` | プッシュの直前 | `stages: [pre-push]` |
| `pre-rebase` | リベースの直前 | `stages: [pre-rebase]` |
| `post-checkout` | ブランチ切り替え後 | `stages: [post-checkout]` |
| `post-commit` | コミット後 | `stages: [post-commit]` |
| `post-merge` | マージ後 | `stages: [post-merge]` |
| `post-rewrite` | コミット書き換え後（`commit --amend`や`rebase`） | `stages: [post-rewrite]` |

`pre-commit install --help`の`--hook-type`で、実際にサポートされているタイミングの一覧を確認できます。

設定ファイルでタイミングを指定する例：

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: detect-private-key
        stages: [pre-push]  # プッシュの直前に実行
```

## フックを確認したい

```console
$ find .git/hooks -type f ! -name "*.sample" -perm -u+x
```

`pre-commit`自身に、フックを一覧する機能はありません。
`.git/hooks/`を直接確認して、フックが追加されているかを確認します。

`find`コマンドを使う場合、`-perm -u+x`のようにハイフンを付けることで、実行可能なファイルだけに絞り込めます

## 事前チェックしたい（`pre-commit-hooks`）

```yaml
repos:
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v6.0.0
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

## ruffしたい（`ruff-pre-commit`）

`ruff`は、Pythonプロジェクトの
リンター＆フォーマッターです。
コミットごとに自動チェックすることで、コードの表記ゆれを抑えることができます。

フックの設定方法は[](./python-ruff.md)に整理しました。

## commitizenしたい（`commitizen`）

`commitizen (cz)`はコミットメッセージの形式を守るためのツールです。
`stages: [commit-msg]`でコミットメッセージを保存したあとにフックがかかるようにしておきます。

フックの設定方法は[](./python-commitizen.md)に整理しました。

## poetryしたい

```yaml
repos:
- repo: ...
- repo: https://github.com/python-poetry/poetry
  rev: 2.4.1
  hooks:
  - id: poetry-check
    args: [--lock]
    stages: [pre-push]
  #- id: poetry-lock
  #- id: poetry-install
- repo: https://github.com/python-poetry/poetry-plugin-export
  rev: 1.10.0
  hooks:
  - id: poetry-export
    args: [--format, requirements.txt, --output, requirements.txt]
    stages: [pre-push]
```

Pythonプロジェクトを`poetry`で管理している場合は、
`poetry-check`（＝`poetry check`）、
`poetry-lock`（＝`poetry lock`）、
`poetry-export`（＝`poetry export`）、
`poetry-install`（＝`poetry install`）
のフックを導入してみるとよいかもしれません。

それぞれに適切な`args`を設定して使うとよいと思います。
また、コミット時ではなくプッシュ時（`pre-push`）に設定するとよいと思います。

:::{caution}

`poetry-export`フックは、`poetry`本体（`python-poetry/poetry`）ではなく、
`poetry-plugin-export`という別リポジトリに移動しました。
`poetry`本体の`repo`を指定すると、
`is not present in repository`エラーになります。
`poetry export`コマンド自体も、`poetry`本体からは削除されており、
別途プラグインとしてインストールしないと使えません。

:::

:::{note}

Read the Docsに公開するために`requirements.txt`が必要です。
このリポジトリも、`poetry-export`フックを使って、
`requirements.txt`を生成できるようにしてあります。

:::

## 脆弱性を検出したい（`Bandit`）

```yaml
repos:
- repo: ...
- repo: ...
- repo: https://github.com/PyCQA/bandit
  rev: 1.9.4
  hooks:
  - id: bandit
    args: ["-r", "ディレクトリ名"]
```

`Bandit`はPythonコードの潜在的なセキュリティ上の問題を検出するリンターです。
`shell=True`を使った`subprocess`呼び出しなど、脆弱性につながりやすいパターンを警告してくれます。
`-r`オプションで、指定したディレクトリを再帰的にスキャンします。

## pytestしたい

```yaml
repos:
- repo: local
  hooks:
  - id: pytest
    name: pytest
    entry: pytest --verbose
    language: system
    pass_filenames: false
    always_run: true
    stages: [pre-push]
```

[pytest](./python-pytest.md)用の公式フックはありません。
`pre-commit`はローカル（`local`）にインストールされているコマンドを使うことができます。
プッシュ時（`pre-push`）にテストを走らせるとよいと思います。

`entry`に実行するコマンドを指定します。
`pass_filenames: false`がないと、変更されたファイル名がそのまま`pytest`の引数として渡されてしまい、
うまく動かないので注意してください。
`always_run: true`で、対象ファイルの変更有無にかかわらず毎回実行します。

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
