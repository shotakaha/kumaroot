# パッケージ管理したい（`poetry`）

```console
// 新規プロジェクト作成
$ poetry new my-project
$ cd my-project

// 依存関係の管理
$ poetry add requests
$ poetry add --group dev pytest
$ poetry add --group docs sphinx
$ poetry remove requests

// 依存関係のインストール
$ poetry install
$ poetry sync

// パッケージの実行とテスト
$ poetry run python main.py
$ poetry run pytest

// パッケージ公開
$ poetry build
$ poetry publish
```

`poetry`は、Pythonの依存関係管理とパッケージングを統合したツールです。
プロジェクトの初期化、依存関係の管理、仮想環境の作成、スクリプトの実行、パッケージのビルドと公開など、Pythonプロジェクトのあらゆる側面を管理できます。

`pyproject.toml`と`poetry.lock`を軸に、依存関係の再現性を保ちます。

:::{note}
Pythonでは、
パッケージ管理には`pip`、
バージョン管理には`pyenv`、
プロジェクト管理には`poetry`
のように、
複数のツールがまるで戦国時代のように群雄割拠しています。

`poetry`は、その中でも早くからプロジェクト管理を統合的に提供してきたツールです。
最近では、Rust製で高速な[uv](./python-uv.md)が同じ立ち位置で急速に普及していますが、
`poetry`は長く使われてきた実績があり、エコシステムも安定しています。

:::

## インストールしたい（`poetry`）

```console
// pipxでインストール
$ pipx install poetry

$ which -a poetry
~/.local/bin/poetry

$ poetry --version
Poetry (version 2.4.1)
```

公式ドキュメントでは`pipx`を使ったインストールが推奨されています。

:::{note}
`uv`がインストール済みであれば、`uv tool install poetry`でもインストールできます。
挙動は`pipx install poetry`とほぼ同じで、どちらも専用の仮想環境を作ってから、実行コマンドを`~/.local/bin/`にリンクします。
:::

## 新規プロジェクトしたい（`poetry new` / `poetry init`）

`poetry`には、プロジェクトを作成する方法が2つあります。
まっさらな状態から作る場合は`poetry new`、既存のディレクトリに`pyproject.toml`だけ追加したい場合は`poetry init`を使います。

### まっさらから作りたい（`poetry new`）

```console
$ poetry new my-project
Created package my_project in my-project

$ find my-project -type f | grep -v .git
my-project/pyproject.toml
my-project/README.md
my-project/src/my_project/__init__.py
my-project/tests/__init__.py
```

`poetry new`コマンドで、新規プロジェクトを作成できます。
`src/<パッケージ名>/`レイアウトと、テスト用の`tests/`ディレクトリが自動生成されます。

```console
$ poetry new my-project
Created package my_project in my-project

$ poetry new my-project
[tomlkit.exceptions.ParseError]
Destination my-project exists and is not empty
```

同名のディレクトリがすでに存在し、中身が空でない場合はエラーになります。

```console
$ cat my-project/pyproject.toml
[project]
name = "my-project"
version = "0.1.0"
description = ""
authors = [
    {name = "Your Name",email = "you@example.com"}
]
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
]

[tool.poetry]
packages = [{include = "my_project", from = "src"}]

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

プロジェクトのメタデータは、`pyproject.toml`の`[project]`セクションに保存されます。
Poetry 2系では、PEP 621に準拠したこの形式が標準です。
`authors`は、Gitの設定（`user.name`・`user.email`）から自動で入力されます。

### 既存ディレクトリに追加したい（`poetry init`）

```console
$ cd my-project
$ poetry init
```

`poetry init`コマンドで、既存のディレクトリに`pyproject.toml`を追加できます。
プロンプトの表示にしたがって、プロジェクト情報（名前、説明、作成者、ライセンスなど）や依存パッケージを対話的に入力します。
`poetry new`と違って、`README.md`や`src/`レイアウトは生成されません。

```console
$ poetry init -n
```

`-n`（`--no-interaction`）オプションで、プロンプトを省略して最小限の`pyproject.toml`のみ生成できます。
あとから直接編集できるので、間違えても大丈夫です。

## 依存パッケージを追加・削除したい（`poetry add` / `poetry remove`）

```console
$ poetry add requests
Using version ^2.34.2 for requests

Updating dependencies
Resolving dependencies...

Package operations: 5 installs, 0 updates, 0 removals

  - Installing certifi (2026.7.22)
  - Installing charset-normalizer (3.5.1)
  - Installing idna (3.19)
  - Installing urllib3 (2.7.0)
  - Installing requests (2.34.2)

Writing lock file

$ poetry remove requests
Updating dependencies
Resolving dependencies...

Package operations: 0 installs, 0 updates, 5 removals

  - Removing certifi (2026.7.22)
  - Removing charset-normalizer (3.5.1)
  - Removing idna (3.19)
  - Removing requests (2.34.2)
  - Removing urllib3 (2.7.0)

Writing lock file
```

`poetry add`で依存パッケージを追加、`poetry remove`で依存パッケージを削除できます。

`pyproject.toml`の`[project]`セクションにある`dependencies`にパッケージ情報が記録され、
`poetry.lock`ファイルも自動で更新されます。
バージョンを指定しない場合は、`^2.34.2`のようにキャレット記法（メジャーバージョン内での自動更新を許可）で記録されます。

```console
$ poetry add --dry-run httpx
```

`--dry-run`オプションで、実際にインストールせず、追加・更新されるパッケージを事前に確認できます。

### 開発依存パッケージを追加したい（`--group`）

```console
$ poetry add --group dev pytest
$ poetry add --group dev ruff
$ poetry add --group dev pre-commit
```

`--group`オプションで、依存パッケージをグループ化できます。
`pyproject.toml`の`[dependency-groups]`セクションに、グループごとに記録されます。

開発のみに必要なツールは`--group dev`でまとめておくと便利です。
古い`--dev`（短縮形`-D`）オプションは、現在も`-G dev`のショートカットとして使えますが、複数のグループを使い分けたい場合は`--group`を使うのが分かりやすいです。

### オプション依存パッケージを追加したい（`--optional`）

```console
$ poetry add --optional viz matplotlib
```

`--optional <extra名>`オプションで、パッケージのオプション機能として依存を追加できます。
`pyproject.toml`の`[project.optional-dependencies]`セクションに、指定したextra名で追加されます。
利用者は`pip install my-project[viz]`のように、extra名を指定してインストールできます。

:::{note}

`--group`と`--optional`は似ていますが、目的が異なります。
`--group`（`[dependency-groups]`）は開発・CI用の内部的な依存分類で、パッケージには含まれません。
`--optional`（`[project.optional-dependencies]`）は、利用者が選択してインストールできる公開機能で、パッケージのextrasとして配布されます。

:::

## パッケージをインストール・同期したい（`poetry install` / `poetry sync`）

```console
$ poetry install
Installing dependencies from lock file

No dependencies to install or update

Installing the current project: my-project (0.1.0)
```

`poetry install`コマンドで、`poetry.lock`に記録されたパッケージをインストールできます。
`poetry.lock`がない場合は、`pyproject.toml`から自動で生成されます。
初回実行時は、仮想環境も自動で作成されます。

```console
$ poetry sync
Installing dependencies from lock file

Package operations: 0 installs, 0 updates, 3 removals

  - Removing markdown-it-py (4.2.0)
  - Removing mdurl (0.1.2)
  - Removing rich (15.0.0)

Installing the current project: my-project (0.1.0)
```

`poetry sync`は、仮想環境を`poetry.lock`の内容に完全一致させるコマンドです。
ロックファイルにないパッケージは、アンインストールされます。

:::{note}

`poetry install`は追加・更新のみ行い、環境に残っている余分なパッケージは削除しません。
`poetry sync`（`poetry install --sync`と同等ですが、`--sync`オプションは非推奨）は、ロックファイルの内容と環境を完全に一致させ、余分なパッケージも削除します。

たとえば`poetry run pip install rich`のようにロックファイル管理外でパッケージを追加した場合、
`poetry install`では`rich`は残ったままですが、`poetry sync`を実行すると削除されます。

:::

```console
$ poetry install --no-root
$ poetry install --all-groups
$ poetry install --all-extras
```

`--no-root`オプションで、プロジェクト自身（ルートパッケージ）のインストールを除外できます。
`--all-groups`オプションで、`[dependency-groups]`のすべてのグループを、
`--all-extras`オプションで、`[project.optional-dependencies]`のすべてのextraをインストール対象にできます。
どちらも指定しない場合、デフォルトの対象は`main`グループの依存のみです。

## パッケージを実行したい（`poetry run`）

```console
$ poetry run python main.py
Hello, World!

$ poetry run pytest
===== test session starts =====
tests/test_main.py .                                       [100%]
1 passed
```

`poetry run`コマンドで、プロジェクトの仮想環境を使って外部コマンドやスクリプトを実行できます。
仮想環境の手動アクティベーションは不要です。

## 仮想環境したい（`poetry env`）

```console
$ poetry env info
Virtualenv
Python:         3.12.7
Implementation: CPython
Path:           ~/.cache/pypoetry/virtualenvs/my-project-3zgY0R6r-py3.12
Executable:     ~/.cache/pypoetry/virtualenvs/my-project-3zgY0R6r-py3.12/bin/python
Valid:          True
```

`poetry env info`コマンドで、現在のプロジェクトに紐づく仮想環境の情報を確認できます。
`poetry install`や`poetry add`をはじめて実行したときに、仮想環境が自動で作成されます。

```console
$ poetry env list
my-project-3zgY0R6r-py3.12 (Activated)
```

`poetry env list`コマンドで、プロジェクトに紐づく仮想環境の一覧を確認できます。

```console
$ poetry env activate
. ~/.cache/pypoetry/virtualenvs/my-project-3zgY0R6r-py3.12/bin/activate
```

`poetry env activate`コマンドは、仮想環境を有効化するコマンド文字列を出力します。
コマンドを直接実行するわけではないので、`eval`と組み合わせて使います。

```console
$ eval $(poetry env activate)
(my-project-py3.12) $ deactivate
```

:::{caution}

Poetry 2.0以降、対話的にシェルへ入る`poetry shell`コマンドは標準では使えなくなりました。
かわりに`poetry env activate`（推奨）か、`shell`プラグインを別途インストールして使う必要があります。
`poetry env activate`は`poetry shell`の完全な代替ではない点に注意してください（サブシェルを起動せず、コマンド文字列を出力するだけです）。

:::

```console
$ poetry env use 3.11
$ poetry env use python3.12
```

`poetry env use`コマンドで、プロジェクトに使用するPythonバージョンを指定して、仮想環境を作り直せます。

```console
$ poetry env remove test-my-project
$ poetry env remove --all
```

`poetry env remove`コマンドで、仮想環境を削除できます。
`--all`オプションで、プロジェクトに紐づくすべての仮想環境を削除できます。

## プロジェクト内に仮想環境を作成したい

```console
$ poetry config virtualenvs.in-project true
$ poetry install
$ ls -la
.venv/
```

デフォルトではPoetryキャッシュ内（`~/.cache/pypoetry/virtualenvs/`）に仮想環境が作成されますが、
`virtualenvs.in-project = true`に設定すると、プロジェクト内に`.venv`が作成されます。

GitHubやGitLabなどでチーム開発する場合、プロジェクト内に仮想環境があると管理しやすくなります。

:::{caution}

すでにキャッシュ内に仮想環境がある場合は、新しい設定で`poetry install`する前に、
`poetry env remove --all`で古い環境を削除してください。

:::

## システムのPythonパッケージを使いたい

```console
$ poetry config virtualenvs.options.system-site-packages true
```

`virtualenvs.options.system-site-packages = true`に設定すると、
システムのPython（`site-packages`）にインストールされたパッケージを仮想環境から利用できます。

[PyROOT](../root/root-pyroot.md)のように、通常の`pip install`では入手できず、
システムのパッケージマネージャー経由でしかインストールできないパッケージを、
仮想環境からそのまま利用したい場合に有効です。

## コード品質をチェックしたい（`poetry check`）

```console
$ poetry check
All set!
```

`poetry check`コマンドで、`pyproject.toml`の内容が正しいか、`poetry.lock`と整合しているかを確認できます。

```console
$ poetry check --lock
```

`--lock`オプションで、現在の`pyproject.toml`に対応する`poetry.lock`が存在するかを確認できます。
CIでロックファイルの更新忘れを検知するのに向いています。

## パッケージをビルドしたい（`poetry build`）

```console
$ poetry build
Building my-project (0.1.0)
Building sdist
  - Building sdist
  - Built my_project-0.1.0.tar.gz
Building wheel
  - Building wheel
  - Built my_project-0.1.0-py3-none-any.whl
```

`poetry build`コマンドでパッケージをビルドできます。
ビルドすると、`dist/`ディレクトリの中に、
`wheel`形式（`.whl`）と`sdist`形式（`.tar.gz`）のファイルが生成されます。

```console
$ poetry build --format wheel
$ poetry build --format sdist
```

`--format`（短縮形`-f`）オプションで、どちらか片方の形式だけをビルドできます。

## パッケージを公開したい（`poetry publish`）

```console
// 実際にはアップロードせず、動作を確認する
$ poetry publish --dry-run

$ poetry publish
Publishing my-project (0.1.0) to PyPI
 - Uploading my_project-0.1.0-py3-none-any.whl
 - Uploading my_project-0.1.0.tar.gz
```

`poetry publish`で、PyPIにパッケージを公開できます。
`--dry-run`オプションで、実際にアップロードせずに、公開の流れ（認証やファイルチェック）だけを確認できます。
はじめて公開する前の動作確認に便利です。

`--build`オプションを付けると、`poetry build`を省略して、公開前に自動でビルドできます。

:::{seealso}

詳しい公開手順については、僕のZennスクラップ「[poetryを使ってpythonパッケージを作成する](https://zenn.dev/shotakaha/scraps/9416c30cd7745a)」を参照してください。

:::

### TestPyPI／PyPIを設定したい

```console
$ poetry config repositories.testpypi https://test.pypi.org/legacy/
$ poetry config pypi-token.testpypi <your-token>
$ poetry config pypi-token.pypi <your-token>
```

TestPyPIとPyPIに公開するために、リポジトリURLとAPIトークンを設定します。
APIトークンはそれぞれのサービスの個人ページで発行して、コマンドで登録してください。

PyPIはデフォルトの公開先なので、リポジトリのURL設定は不要です。TestPyPIのみ設定が必要です。

```console
// TestPyPIに公開
$ poetry publish -r testpypi --dry-run
$ poetry publish -r testpypi
```

`-r`（`--repository`）オプションで、公開先を切り替えられます。
はじめて公開するパッケージは、まずTestPyPIに公開して動作テストしてからPyPIに本番公開することをオススメします。

:::{note}

PyPIとTestPyPIは、サービスとしては別物です。
それぞれのサービスでアカウントを作成してください。
また、プロジェクトごとにAPIトークンを発行してください。

:::

:::{caution}

PyPIとTestPyPIには、同じ名前のパッケージは登録できません。
プロジェクトを作成する段階で、パッケージ名の重複がないか確認してください。
また、同じバージョンの再アップロード（上書き）もできません。
変更内容に応じてバージョンを更新してください。

:::

他にもプライベートリポジトリなど、さまざまな公開先を設定できます。詳細は[Repositories](https://python-poetry.org/docs/repositories/)を参照してください。

## 設定を管理したい（`poetry config`）

```console
$ poetry config --list
cache-dir = "~/.cache/pypoetry"
...
virtualenvs.create = true
virtualenvs.in-project = null
virtualenvs.path = "{cache-dir}/virtualenvs"
```

`poetry config --list`で、現在のPoetry設定をすべて表示します。
デフォルト設定の詳細は[PoetryドキュメントのAvailable Settings](https://python-poetry.org/docs/configuration/#available-settings)を参照してください。

```console
$ poetry config キー名 値
$ poetry config キー名 値 --local
```

設定値を変更します。
`--local`をつけるとプロジェクト内の`poetry.toml`に保存され、
全体設定は`~/Library/Application Support/pypoetry/config.toml`に保存されます。

```console
$ poetry config キー名 --unset
```

追加した設定を削除する場合は`--unset`オプションを使います。

## リファレンス

- [Poetry](https://python-poetry.org/)
