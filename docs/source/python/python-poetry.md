# パッケージ管理したい（`poetry`）

```console
// 新規プロジェクト作成
$ poetry new my-project
$ cd my-project

// 依存関係の管理
$ poetry add requests pandas
$ poetry add --group dev pytest ruff ipykernel
$ poetry add --group docs sphinx

// 環境をセットアップ
$ poetry install

// スクリプトを実行
$ poetry run python main.py
$ poetry run pytest

// パッケージをビルド・公開
$ poetry build
$ poetry publish
```

`poetry`はPythonの依存関係管理、パッケージングを統合したツールです。
`pyproject.toml`と`poetry.lock`で依存関係を管理し、
仮想環境の構築、テスト実行、パッケージ公開までがシームレスに行えます。

:::{note}

`poetry`は複数の役割を統合しています：
- `pip`と`venv`：パッケージ管理と仮想環境
- `setuptools`：パッケージビルド
- `twine`：パッケージ公開

すべてが1つのツールで完結するため、環境構築が簡単です。

:::

## インストールしたい（`poetry`）

```console
$ pipx install poetry
Installing poetry (version 2.2.1)
Successfully installed poetry

$ poetry --version
Poetry (version 2.2.1)
```

公式ドキュメントでは`pipx`を使ったインストールが推奨されています。

## 新規プロジェクトしたい（`poetry new`）

```console
$ poetry new PROJECT_NAME
Created package project_name in PROJECT_NAME

$ tree -a PROJECT_NAME
PROJECT_NAME
├── README.md
├── project_name
│   └── __init__.py
├── pyproject.toml
└── tests
    └── __init__.py

$ poetry new PROJECT_NAME
Destination ./PROJECT_NAME exists and is not empty
```

`new`コマンドでプロジェクトを初期化できます。
テスト関係のファイルも自動で生成されます。
同名のプロジェクトがすでに存在する場合は、エラーになります
プロジェクト名を省略した場合は、エラーになります。

## 既存プロジェクトを使いたい（``poetry init``）

```console
$ cd プロジェクト名
$ poetry init
```

`init`コマンドで、既存のプロジェクトを初期化できます。
プロンプトの表示にしたがってプロジェクト情報（プロジェクト名、説明、作成者、バージョン番号、ライセンスなど）を入力します。
続けて、必要なパッケージに関するプロンプトが表示されるので、パッケージ名やバージョン番号を入力して、パッケージを選択します。
これらの設定はすべて{file}`pyproject.toml`の``[tool.poetry]``セクションに保存されます。
あとから直接編集できるので、間違えてしまっても大丈夫です。

## パッケージを追加したい（`poetry add`）

```console
$ poetry add requests pandas
$ poetry add --group dev pytest ruff
$ poetry add --group docs sphinx
```

`poetry add`コマンドで、プロジェクトに必要なパッケージを追加します。パッケージを追加すると、{file}`pyproject.toml`に記録され、{file}`poetry.lock`が自動で生成・更新されます。

:::{tip}

**パッケージの追加先：**

- `poetry add requests` - 本番環境（`[tool.poetry.dependencies]`）に追加
- `poetry add --group dev pytest` - 開発環境（`[tool.poetry.group.dev.dependencies]`）に追加
- `poetry add --group docs sphinx` - ドキュメント環境に追加

:::

### 開発環境でのみ使うパッケージを追加したい

```console
$ poetry add --group dev pytest black ruff jupyterlab
```

テストやコード整形など、開発時にのみ必要なパッケージは`--group dev`オプションで追加します。本番環境にはインストールされません。

:::{note}

Poetry v1.3.0以降では、`--group`を使ったグループ化が標準です。以前の`-D`オプションは非推奨になりました。

:::

### ドキュメント環境でのみ使うパッケージを追加したい

```console
$ poetry add --group docs sphinx sphinx_book_theme myst_parser
```

Sphinxなどドキュメント作成専用のパッケージは`--group docs`で追加します。これにより、必要な環境だけに必要なパッケージをインストールできます。

## パッケージをインストールしたい（`poetry install`）

```console
$ poetry install
Creating virtualenv poetry-xx in .venv
Installing dependencies from lock file
...
```

`poetry install`コマンドで、{file}`poetry.lock`に記録されたすべてのパッケージをインストールして、仮想環境をセットアップします。{file}`poetry.lock`がない場合は、{file}`pyproject.toml`から自動で生成されます。

:::{tip}

**初回セットアップの流れ：**

1. `poetry new`や`poetry init`でプロジェクトを初期化
2. `poetry add`でパッケージを追加
3. `poetry install`で仮想環境を構築
4. `poetry run`でコマンドを実行

:::

デフォルトではPoetryキャッシュ内に仮想環境が作成されます。プロジェクト内に`.venv`を作成したい場合は、[プロジェクト内に仮想環境を作成したい](#プロジェクト内に仮想環境を作成したい)を参照してください。

## スクリプトを実行したい（`poetry run`）

```console
$ poetry run python main.py
# スクリプトが実行される

$ poetry run pytest
# テストが実行される

$ poetry run black .
# コード整形が実行される
```

`poetry run`コマンドで、セットアップした仮想環境内でコマンドを実行します。これにより、プロジェクトの依存関係が正確に反映された環境でスクリプトが動作します。

## パッケージ環境を確認したい（`poetry check`）

```console
$ poetry check
All set!
```

`poetry check`でプロジェクトの設定が正しいか確認できます。`--lock`オプションで{file}`poetry.lock`の整合性も検証します。

## パッケージをビルドしたい（`poetry build`）

```console
$ poetry build
Building パッケージ名 (バージョン番号)
  - Building sdist
  - Built パッケージ名-バージョン番号.tar.gz
  - Building wheel
  - Built パッケージ名-バージョン番号-py3-none-any.whl
```

`build`コマンドでパッケージをビルドできます。

## パッケージを公開したい（`poetry publish`）

```console
$ poetry publish -r testpypi
Publishing my_project (0.1.0) to testpypi
 - Uploading my_project-0.1.0-py3-none-any.whl
 - Uploading my_project-0.1.0.tar.gz
```

`poetry publish`でパッケージをPyPIに公開します。はじめて公開する場合は、必ずTestPyPIでテストしてから本番のPyPIに公開してください。事前にリポジトリとAPIトークンの設定が必要です。

:::{seealso}

詳しい公開手順については、僕のZennスクラップ「[poetryを使ってpythonパッケージを作成する](https://zenn.dev/shotakaha/scraps/9416c30cd7745a)」を参照してください。

:::

### TestPyPI／PyPIを設定したい

```console
$ poetry config repositories.testpypi https://test.pypi.org/legacy/
$ poetry config pypi-token.testpypi <your-token>
$ poetry config pypi-token.pypi <your-token>
# 設定が保存される
```

TestPyPIとPyPIに公開するために、リポジトリURLとAPIトークンを設定します。APIトークンはそれぞれのサービスの個人ページで発行して、コマンドで登録してください。

PyPIはデフォルトの公開先なので、リポジトリのURL設定は不要です。TestPyPIのみ設定が必要です。

他にもプライベートリポジトリなど、さまざまな公開先を設定できます。詳細は[Repositories](https://python-poetry.org/docs/repositories/)を参照してください。

## 設定を管理したい

### 現在の設定を確認したい（`poetry config --list`）

```console
$ poetry config --list
cache-dir = "~/Library/Caches/pypoetry"
virtualenvs.create = true
virtualenvs.in-project = null
virtualenvs.path = "{cache-dir}/virtualenvs"
```

`poetry config --list`で現在のPoetry設定をすべて表示します。デフォルト設定の詳細は[PoetryドキュメントのAvailable Settings](https://python-poetry.org/docs/configuration/#available-settings)を参照してください。

### 設定を変更したい

```console
$ poetry config キー名 値
$ poetry config キー名 値 --local
# 設定が更新される
```

設定値を変更します。`--local`をつけるとプロジェクト内の{file}`poetry.toml`に保存され、全体設定は{file}`~/Library/Application Support/pypoetry/config.toml`に保存されます。

### 設定を削除したい

```console
$ poetry config キー名 --unset
# 設定が削除される
```

追加した設定を削除する場合は`--unset`オプションを使います。

## プロジェクト内に仮想環境を作成したい

```console
$ poetry config virtualenvs.in-project true
$ poetry install
$ ls -la
.venv/
```

デフォルトではPoetryキャッシュ内に仮想環境が作成されますが、`virtualenvs.in-project = true`に設定すると、プロジェクト内に{file}`.venv`が作成されます。

GitHubやGitLabなどでチーム開発する場合、プロジェクト内に仮想環境があると管理しやすくなります。

:::{caution}

すでにキャッシュ内に仮想環境がある場合は、新しい設定で`poetry install`する前に古い環境を削除してください。

:::

## システムのPythonパッケージを使いたい

```console
$ poetry config virtualenvs.options.system-site-packages true
# 設定が更新される
```

`virtualenvs.options.system-site-packages = true`に設定すると、システムのPython（`site-packages`）にインストールされたパッケージを仮想環境から利用できます。

複数のプロジェクトで共有する開発ツール（`pytest`、`black`など）を節約したい場合に有効です。

## リファレンス

- [Poetry](https://python-poetry.org/)
