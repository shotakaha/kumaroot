# パッケージ管理したい（`uv`）

```console
// 新規プロジェクト作成
$ uv init my-project
$ cd my-project

// 依存関係の管理
$ uv add requests
$ uv add --dev pytest
$ uv add --group docs zensical
$ uv remove requests

// 依存関係のインストール
$ uv sync
$ uv sync --all-groups --all-extras
$ uv sync --dry-run
$ uv audit --preview-features audit-command

// パッケージの実行とテスト
$ uv run main_script.py
$ uv run pytest

// フォーマット
$ uv format --preview-features format-command
$ uv check --preview-features check-command

// パッケージ公開
$ uv build
$ uv publish
```

`uv`は、Pythonのパッケージ管理とプロジェクト管理を統合したツールです。
プロジェクトの初期化、依存関係の管理、仮想環境の作成、スクリプトの実行、パッケージのビルドと公開など、Pythonプロジェクトのあらゆる側面を効率的に管理できます。

Rustで書かれていて超高速に動作するのが特徴です。
`uv.lock`を軸とすることで、依存関係の再現性も高いです。
また、PEP 621やPEP 660などの最新のPythonパッケージ管理の標準に準拠しています。

:::{note}
Pythonでは、
パッケージ管理には`pip`、
バージョン管理には`pyenv`、
プロジェクト管理には`poetry`
のように、
複数のツールがまるで戦国時代のように群雄割拠しています。

`uv`は、これらのツールの機能を統合して提供することで、
この戦いを終わらせようとしています（たぶん）。

:::

## インストールしたい（`uv`）

```console
// Homebrewでインストール
$ brew install uv

$ which -a uv
/opt/homebrew/bin/uv

$ uv --version
uv 0.12.5 (Homebrew 2026-08-14 aarch64-apple-darwin)

$ which -a uvx
/opt/homebrew/bin/uvx

$ uvx --version
uvx 0.12.5 (Homebrew 2026-08-14 aarch64-apple-darwin)
```

`uv`はHomebrewでインストールできます。
一時的に仮想環境を作成してツールを実行する`uvx`コマンドも同時にインストールされます。

:::{note}
`uv`は基本的にシステム全体に1つインストールすれば十分ですが、`pip`や`pipx`、`poetry`などの他のパッケージ管理ツールを使ってプロジェクトごとにインストールすることもできます。
CI/CDでPythonイメージを使う場合は`pipx install uv`するのがよいと思います。
:::

## 仮想環境したい（`uv venv`）

```console
$ cd my-project

// 仮想環境を作成
$ uv venv
Using CPython 3.12.7
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate

// 仮想環境を有効化
$ source .venv/bin/activate       // for bash/zsh
$ source .venv/bin/activate.fish  // for fish
$ .venv\Scripts\activate          // for PowerShell
(.venv) $

// 仮想環境を無効化
(.venv) $ deactivate
```

`uv venv`コマンドで仮想環境を作成できます。
仮想環境にある`activate`スクリプトを実行して、仮想環境を有効化します。

```console
// 任意のパスに仮想環境を作成
$ uv venv /tmp/test-uv/
$ source /tmp/test-uv/bin/activate
```

仮想環境を作成するパスを変更できます。
デフォルトで`.venv`です。

```console
// 特定のPythonバージョンを指定
$ uv venv --python 3.11        // バージョンを指定
$ uv venv --python python3.12  // 実行コマンドを指定
```

`--python`オプションで、仮想環境に使用するPythonを指定できます。
指定したPythonがシステムにインストールされていない場合は、`uv`が自動的にダウンロードしてインストールします。

```console
$ uv venv --system-site-packages
$ uv venv --python 3.14 --system-site-packages
```

`--system-site-packages`オプションで、
作成した仮想環境からシステムのPython環境にアクセスできるようにできます。
[PyROOT](../root/root-pyroot.md)のように、システムのPython環境にインストールされてしまうパッケージを仮想環境から利用したい場合に必要です。

:::{note}

Pythonの仮想環境については、
標準ライブラリの[venv](./python-venv.md)や、
その上位互換的な`virtualenv`などがあります。
また、Pythonのバージョン管理ツールである`pyenv`も、仮想環境の管理に利用できます。
`uv venv`コマンドはこれらのツールの機能を統合して提供しています。

:::

## パッケージを追加・削除したい（`uv pip install` / `uv pip uninstall`）

```console
// 仮想環境を作成
$ uv venv

// パッケージを追加
$ uv pip install pandas

// 更新できるパッケージを確認
$ uv pip list --outdated

// パッケージを削除
$ uv pip uninstall pandas
```

`uv pip install`コマンドで仮想環境にパッケージを追加できます。
パッケージは`.venv`の中にインストールされます。
`uv pip list`コマンドで、インストール済みのパッケージを確認できます。
さらに`--outdated`オプションで、更新できるパッケージを確認できます。
`uv pip uninstall`コマンドで仮想環境からパッケージを削除できます。

```console
// 仮想環境が存在しない場合はエラー
$ uv pip install pandas
error: No virtual environment found; run `uv venv` to create an environment, or pass `--system` to install into a non-virtual environment
```

仮想環境が存在しない場合はエラーになります。
エラーメッセージにしたがって仮想環境を作成すればOKです。

:::{note}

`uv pip`コマンドは、カレントディレクトリの`.venv`よりも先に、
環境変数`VIRTUAL_ENV`が指す仮想環境を優先して使用します。
別プロジェクトの仮想環境を`activate`したままのシェルで
`uv pip install`を実行すると、意図せずそちらにインストールしてしまうことがあります。
`echo $VIRTUAL_ENV`で有効化中の仮想環境を確認するか、
一度`deactivate`してから実行するのが安全です。

:::

:::{note}

Pythonのパッケージ管理については、
標準ライブラリの[pip](./python-pip.md)があります。
`uv pip`コマンドは、`pip`コマンドを高速化した実装です。
`pip`との互換性が保たれているため、簡単に乗り換えることができます。

:::

## 新規プロジェクトしたい（`uv init`）

```console
$ uv init --app /tmp/test-uv-app            // スクリプト中心のプロジェクトを作成
$ uv init --app --package /tmp/test-uv-cli  // CLIツールとして配布するプロジェクトを作成
$ uv init --lib /tmp/test-uv-lib            // ライブラリ中心のプロジェクトを作成
$ uv init --bare /tmp/test-uv-bare          // 最小構成のプロジェクトを作成
```

`uv init`コマンドでプロジェクトを初期化できます。
プロジェクトの目的に合わせて、`--app`、`--lib`、`--bare`オプションから選択します。
指定したパスに`pyproject.toml`ファイルや`src/<パッケージ名>/__init__.py`、
`.python-version`ファイルなどが自動生成されます。
また、Gitリポジトリとして設定されます。

デフォルトは`--app`です。
PyPIでパッケージとして公開する予定であれば`--package`オプションを追加します。
利用形態を迷っている場合は、とりあえず`--app --package`オプションで作成しておくとよいです。

```console
$ cat /tmp/test-uv/pyproject.toml
[project]
name = "test-uv"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = []
```

プロジェクトのメタデータは`pyproject.toml`の`[project]`セクションに保存されます。
このファイルはユーザーが直接編集することを想定しています。
`uv init`コマンドで初期化した後は、必要に応じて直接編集してください。

```console
$ uv init /tmp/test-uv
error: Project is already initialized in `/tmp/test-uv` (`pyproject.toml` file exists)
```

`pyproject.toml`がすでに存在する場合はエラーになります。
プロジェクトをリセットしたい場合は、`pyproject.toml`ファイルを削除してから再度`uv init`を実行してください。

### スクリプトしたい（`uv init --app`）

```console
$ uv init --app /tmp/test-uv-app
Initialized project `test-uv-app` at `/tmp/test-uv-app`

$ find /tmp/test-uv-app -type f | grep -v .git
/tmp/test-uv-app/pyproject.toml
/tmp/test-uv-app/README.md
/tmp/test-uv-app/.python-version
/tmp/test-uv-app/main.py
```

`--app`は、スクリプトの作成に適したオプションです。
`uv init`のデフォルトで、トップレベルに`main.py`が生成されるシンプルな構成です。
`uv run main.py`で直接実行できるため、使い捨てスクリプトや小規模なアプリに向いています。

### CLIしたい（`uv init --app --package`）

```console
$ uv init --app --package /tmp/test-uv-cli
Initialized project `test-uv-cli` at `/tmp/test-uv-cli`

$ find /tmp/test-uv-cli -type f | grep -v .git
/tmp/test-uv-cli/pyproject.toml
/tmp/test-uv-cli/README.md
/tmp/test-uv-cli/.python-version
/tmp/test-uv-cli/src/test_uv_cli/__init__.py
```

`--app --package`は、CLIツールの作成に適したオプションです。
`main.py`ではなく、`src/<パッケージ名>/__init__.py`に`main()`関数が生成されます。
CLIのエントリーポイントは、`pyproject.toml`の`[project.scripts]`に自動登録されます。
`uv run test-uv-cli`のようにコマンド名で実行できます。

### ライブラリしたい（`uv init --lib`）

```console
$ uv init --lib /tmp/test-uv-lib
Initialized project `test-uv-lib` at `/tmp/test-uv-lib`

$ find /tmp/test-uv-lib -type f | grep -v .git
/tmp/test-uv-lib/pyproject.toml
/tmp/test-uv-lib/README.md
/tmp/test-uv-lib/.python-version
/tmp/test-uv-lib/src/test_uv_lib/__init__.py
/tmp/test-uv-lib/src/test_uv_lib/py.typed
```

`--lib`は、ライブラリの作成に適したオプションです。
`src/<パッケージ名>/`レイアウトで生成されます。
`py.typed`ファイルも同時に生成され、型情報を配布するライブラリであることを示します。
`--no-package`とは併用できません（エラーになります）。

### 最小構成したい（`uv init --bare`）

```console
$ uv init --bare /tmp/test-uv-bare
Initialized project `test-uv-bare` at `/tmp/test-uv-bare`

$ find /tmp/test-uv-bare -type f | grep -v .git
/tmp/test-uv-bare/pyproject.toml
```

`--bare`は、`pyproject.toml`のみの最小構成用のオプションです。
`README.md`や`.python-version`、Gitリポジトリの初期化も行われません。
既存のプロジェクトに、後から`pyproject.toml`だけ追加したい場合に向いています。

## 依存パッケージを追加・削除したい（`uv add` / `uv remove`）

```console
// dependenciesに追加
$ uv add requests
Resolved 6 packages in 0.10s
   Building my-project @ file:///path/to/my-project
      Built my-project @ file:///path/to/my-project
Prepared 1 package in 0.02s
Installed 6 packages in 0.01s
 + certifi==2026.7.22
 + charset-normalizer==3.5.1
 + idna==3.19
 + my-project==0.1.0 (from file:///path/to/my-project)
 + requests==2.34.2
 + urllib3==2.7.0

// パッケージを削除
$ uv remove requests
Resolved 1 package in 0.01s
Uninstalled 6 packages in 0.01s
 - certifi==2026.7.22
 - charset-normalizer==3.5.1
 - idna==3.19
 - requests==2.34.2
 ~ my-project==0.1.0 (from file:///path/to/my-project)
 - urllib3==2.7.0
```

`uv add`で依存パッケージを追加、
`uv remove`で依存パッケージを削除できます。

`pyproject.toml`の`[project]`セクションにある`dependencies`にパッケージ情報が記録され、
`uv.lock`ファイルも自動で更新されます。

```console
$ uv add pandas
error: No `pyproject.toml` found in current directory or any parent directory
```

`pyproject.toml`がない場合はエラーになります。
`uv init`コマンドでプロジェクトを初期化してから、`uv add`を実行してください。

### 開発依存パッケージを追加したい（`--group`）

```console
// dependency-groups.devに追加
$ uv add --dev pytest
$ uv add --group dev pre-commit
$ uv add --group dev commitizen
$ uv add --group dev ruff
// dependency-groups.docsに追加
$ uv add --group docs sphinx
```

`--group`オプションで、依存パッケージをグループ化できます。
`pyproject.toml`の`[dependency-groups]`セクションにグループ情報が追加されます。

開発のみに必要なツールは`--group dev`でまとめておくと便利です。
`--dev`オプションは`--group dev`と同じです。

### オプション依存パッケージを追加したい（`--optional`）

```console
// project.optional-dependencies.vizに追加
$ uv add --optional viz matplotlib
```

`--optional <extra名>`オプションで、パッケージのオプション機能として依存を追加できます。
`pyproject.toml`の`[project.optional-dependencies]`セクションに、指定したextra名で追加されます。
利用者は`pip install my-project[viz]`のように、extra名を指定してインストールできます。

:::{note}

`--group`と`--optional`は似ていますが、目的が異なります。
`--group`（`[dependency-groups]`）は開発・CI用の内部的な依存分類で、パッケージには含まれません。
`--optional`（`[project.optional-dependencies]`）は、利用者が選択してインストールできる公開機能で、パッケージのextrasとして配布されます。

:::

## パッケージを同期したい（`uv sync`）

```console
$ uv sync               // dependenciesのみ同期
$ uv sync --dry-run     // 変更内容を確認するだけ
$ uv sync --all-groups  // dependency-groupsも同期
$ uv sync --all-extras  // optional-dependenciesも同期
$ uv sync --all-groups --all-extras  // すべて同期
```

`uv sync`は、仮想環境を`uv.lock`の内容に一致させるコマンドです。
ロックファイルにあるパッケージはインストールされ、
ロックファイルにないパッケージはアンインストールされます。

`--dry-run`オプションは、実際に同期せず、追加・削除されるパッケージを事前に確認できます。

:::{note}

`uv add`（や`uv remove`）コマンドでは`pyproject.toml`と`uv.lock`が更新されます。
`uv sync`コマンドは、それらのファイルを更新せず、`uv.lock`の内容が仮想環境に再現されます。

:::

```console
$ uv sync --group dev
$ uv sync --group docs
$ uv sync --all-groups
```

`--all-groups`オプションで、`[dependency-groups]`に定義されているすべてのグループを同期の対象にできます。
デフォルトの`uv sync`では`dependencies`と`dev`グループが同期の対象になりますが、
`docs`など`dev`以外のグループは含まれません。

```console
$ uv sync --extra viz
$ uv sync --all-extras
```

`--all-extras`オプションで、`[project.optional-dependencies]`に定義されているすべてのextraを同期の対象にできます。
デフォルトの`uv sync`には含まれないため、`--extra <extra名>`もしくは、`--all-extras`で明示的に指定する必要があります。

```console
// パッケージを更新してから同期
$ uv sync --upgrade
```

`--upgrade`オプションで、依存パッケージを最新バージョンに更新してから同期できます。
このオプションは、後述する`uv lock --upgrade`と`uv sync`を組み合わせた動作です。

## パッケージを更新したい（`uv lock`）

```console
$ uv lock
$ uv lock --dry-run
$ uv lock --check
```

`uv lock`は、`pyproject.toml`の内容をもとに、`uv.lock`ファイルを更新するコマンドです。
`--dry-run`オプションで、実際に更新せず、更新されるパッケージを事前に確認できます。

```console
// ロックファイルがpyproject.tomlと整合しているか確認（更新はしない）
$ uv lock --check
error: The lockfile at `uv.lock` needs to be updated, but `--check` was provided.

hint: To update the lockfile, run `uv lock`.
```

`--check`オプションで、`uv.lock`が`pyproject.toml`の内容と整合しているかを確認できます。
不整合がある場合はエラーで終了するため、CIでロックファイルの更新忘れを検知するのに向いています。

```console
// 更新できるパッケージを確認
$ uv lock --upgrade --dry-run

// パッケージを一括で更新
$ uv lock --upgrade

// 特定のパッケージだけを更新
$ uv lock --upgrade-package requests
```

`--upgrade`は、積極的にバージョン解決するオプションで、パッケージを最新バージョンに更新できます。
`--upgrade-package`オプションで、指定したパッケージだけを更新できます。
プロジェクト全体を一括更新せず、特定のパッケージのみを上げたい場合に使います。

:::{note}

`uv lock`は、プロジェクトの再現性を優先するコマンドです。
なので、ロックファイル（`uv.lock`）に書かれたバージョンを優先して解決します。
一方で、`--upgrade`オプションは、依存の範囲内であれば既存のロック内容を無視して、それぞれのパッケージを解決可能な最新バージョンまで引き上げます。

`pyproject.toml`を編集した直後は`uv lock`で反映し、
定期的な更新には`uv lock --upgrade`を使います。

:::

## パッケージを実行したい（`uv run`）

```console
$ uv run path/to/script.py
Hello, World!

$ uv run --group dev pytest
===== test session starts =====
tests/test_main.py .                                       [100%]
1 passed
```

`uv run`コマンドで、プロジェクトの仮想環境を使って外部コマンドやスクリプトを実行できます。
`--group`オプションで、依存グループを指定できます。
仮想環境の手動アクティベーションは不要です。

```console
// pyproject.tomlを変更せず、一時的にパッケージを追加して実行
$ uv run --with rich python script.py
$ uv run --with rich --with httpx python script.py
```

`--with`オプションで、`pyproject.toml`に依存として追加せず、
一時的にパッケージを追加した状態でコマンドを実行できます。
複数回指定することで、複数のパッケージを一時的に追加できます。
ちょっとしたパッケージを試したいときや、使い捨てスクリプトの実行に便利です。

```console
// PyPIに公開していない、Gitリポジトリのパッケージを直接指定
$ uv run --with "osechi-kazunoko @ git+https://gitlab.com/osechi/kazunoko" python -c "import kazunoko"
```

`--with`には、`パッケージ名 @ git+<リポジトリURL>`の形式でGitリポジトリを直接指定できます。
PyPIに公開していない自作パッケージや、フォーク版を一時的に試したい場合に使えます。
パッケージ名は`pyproject.toml`の`name`（配布名）を指定し、`import`するモジュール名とは異なる場合がある点に注意してください。

```console
$ source .venv/bin/activate
(.venv) $ python path/to/script.py
```

`uv run`を使わない場合は、仮想環境を手動でアクティベートしてからコマンドを実行してください。

## コードをフォーマットしたい（`uv format`）

```console
$ uv format --preview-features format-command
```

`uv format`は、プロジェクト内のPythonコードを整形（フォーマット）するコマンドです。
内部では[Ruff](https://docs.astral.sh/ruff/)を利用しています。

```console
// フォーマットを適用せず、崩れがないか確認（CI向け）
$ uv format --preview-features format-command --check

// フォーマット差分を表示
$ uv format --preview-features format-command --diff
```

`--check`オプションで、ファイルを書き換えずにフォーマット崩れの有無だけを確認できます。
フォーマットが必要なファイルがある場合は非ゼロで終了するため、CIでの利用に向いています。
`--diff`オプションで、実際に適用される変更内容を確認できます。

## 型チェックしたい（`uv check`）

```console
$ uv check --preview-features check-command
```

`uv check`は、プロジェクトの型チェックを実行するコマンドです。
内部では[ty](https://docs.astral.sh/ty/)を利用しています。

```console
// 安全に修正できるエラーを自動修正
$ uv check --preview-features check-command --fix
```

`--fix`オプションで、自動修正が可能な型エラーを書き換えてくれます。
未解決のimportなど、自動修正できないエラーはそのまま報告されます。

## 依存関係を監査したい（`uv audit`）

```console
$ uv audit --preview-features audit-command
```

`uv audit`は、プロジェクトの依存関係に既知の脆弱性がないかを監査するコマンドです。
`pip-audit`と同様の役割を、`uv`単体で完結できます。

```console
// 開発用依存グループを除外して監査
$ uv audit --preview-features audit-command --no-dev

// JSON形式で出力（CI連携などに）
$ uv audit --preview-features audit-command --preview-features json-output --output-format json

// 特定の脆弱性IDを無視
$ uv audit --preview-features audit-command --ignore GHSA-xxxx-xxxx-xxxx
```

`--no-dev`オプションで、開発用依存グループを監査対象から除外できます。
`--output-format`オプションで、`json`や`sarif`形式での出力に切り替えられます（`json`形式の利用には`--preview-features json-output`も必要です）。
`--ignore`オプションで、対応が難しい特定の脆弱性IDを一時的に無視できます。

## パッケージをビルドしたい（`uv build`）

```console
$ uv build
Building source distribution...
Building wheel from source distribution...
Successfully built dist/my_package-0.1.0.tar.gz
Successfully built dist/my_package-0.1.0-py3-none-any.whl

$ uv build --wheel
$ uv build --sdist
```

`uv build`コマンドでパッケージをビルドできます。
ビルドすると、`dist/`ディレクトリの中に、
`wheel`形式（`.whl`）と`sdist`形式（`.tar.gz`）のファイルが生成されます。
`--wheel`オプションで`wheel`形式のみ、`--sdist`オプションで`sdist`形式のみをビルドできます。

:::{note}

`wheel`形式はバイナリパッケージで、インストールが高速です。
`sdist`形式はソースパッケージで、古くからある配布形式です。
ビルドに時間がかかりますが、幅広い環境でインストールできます。
通常は両方の形式でビルドしておけばOKです。

:::

## パッケージを公開したい（`uv publish`）

```console
// 実際にはアップロードせず、動作を確認する
$ uv publish --dry-run
$ uv publish
Checking dist/my_package-0.1.0-py3-none-any.whl (12.3KiB)
Uploading my_package-0.1.0-py3-none-any.whl (12.3KiB)
Checking dist/my_package-0.1.0.tar.gz (8.1KiB)
Uploading my_package-0.1.0.tar.gz (8.1KiB)
```

`uv publish`で、PyPIにパッケージを公開できます。
`--dry-run`オプションで、実際にアップロードせずに、公開の流れ（認証やファイルチェック）だけを確認できます。
はじめて公開する前の動作確認に便利です。

```console
// TestPyPIに公開
$ uv publish --publish-url https://test.pypi.org/legacy/
```

`--publish-url`オプションで、公開先を変更できます。
PyPIには、テスト用のTestPyPIというサービスがあります。
はじめて公開するパッケージはは、まずTestPyPIに公開して動作テストしてからPyPIに本番公開することをオススメします。

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

## Pythonを管理したい（`uv python`）

```console
$ uv python pin 3.12
Pinned `.python-version` to `3.12`

$ cat .python-version
3.12

$ uv run python --version
Python 3.12.7
```

`uv python pin`コマンドで、プロジェクトで使用するPythonバージョンを指定します。
設定は`.python-version`ファイルに保存され、`uv`や`pyenv`などのツールで共通に使用されます。

```console
// 特定のバージョンをインストール
$ uv python install 3.12
Downloading cpython-3.12.14-macos-aarch64-none (download) (25.1MiB)
 Downloaded cpython-3.12.14-macos-aarch64-none (download)
Installed Python 3.12.14 in 2.27s
 + cpython-3.12.14-macos-aarch64-none (python3.12)

// 複数バージョンをインストール
$ uv python install 3.11 3.12

$ uv python uninstall 3.12
Searching for Python versions matching: Python 3.12
Uninstalled Python 3.12.14 in 201ms
 - cpython-3.12.14-macos-aarch64-none (python3.12)
```

`uv python install`コマンドで、特定のPythonバージョンをインストールできます。

```console
// 利用可能なバージョンを確認（インストール済みはパス、未インストールは<download available>と表示）
$ uv python list
cpython-3.14.7-macos-aarch64-none     /opt/homebrew/bin/python3.14 -> ../Cellar/python@3.14/3.14.7/bin/python3.14
cpython-3.13.15-macos-aarch64-none    <download available>
cpython-3.12.14-macos-aarch64-none    /opt/homebrew/bin/python3.12 -> ../Cellar/python@3.12/3.12.14/bin/python3.12
...

// インストール済みバージョンのみ確認
$ uv python list --only-installed
cpython-3.14.7-macos-aarch64-none     /opt/homebrew/bin/python3.14 -> ../Cellar/python@3.14/3.14.7/bin/python3.14
cpython-3.12.14-macos-aarch64-none    /opt/homebrew/bin/python3.12 -> ../Cellar/python@3.12/3.12.14/bin/python3.12
```

`uv python list`コマンドで、利用可能なPythonバージョンやインストール済みのバージョンを確認できます。
`--only-installed`オプションで、インストール済みのバージョンのみを表示できます。

:::{note}

`uv init`でプロジェクトを作成すると、`.python-version`が自動で作成されます。
システムにインストールされていないバージョンが指定されている場合、
`uv`は自動的にそのバージョンをダウンロードしてインストールします。

:::

## 外部ツールを使いたい（`uvx` / `uv tool install`）

`ruff`のようなCLIツールをプロジェクトの外で使いたい場合は、`uvx`と`uv tool install`の2つの方法があります。
一度だけ試したい、CIで使い捨てたい、最新版を試したいなど、その場限りの利用には`uvx`が向いています。
`commitizen`や`hugo`のように日常的に何度も使うツールは、`uv tool install`で環境にインストールしておくと便利です。

### 一時的に実行したい（`uvx`）

```console
$ uvx ruff check .
All checks passed!

$ uvx black --version
Downloading black (1.7MiB)
 Downloaded black
Installed 7 packages in 6ms
black, 26.5.1 (compiled: yes)
Python (CPython) 3.12.7

$ uvx --with pandas --with matplotlib jupyter notebook
[notebook starts...]
```

`uvx`は、CLIツールを一時的に実行するコマンドです。

実行対象のコマンドは、永続インストールされず、共有キャッシュ（`uv cache dir`）に保存されます。
キャッシュに存在しない場合は、初回実行時のダウンロードが必要ですが、以後はキャッシュが再利用されます。

### 永続的に使いたい（`uv tool install`）

```console
// 初回のみ実行
$ uv tool update-shell

$ uv tool install ruff
Resolved 1 package in 1ms
Installed 1 package in 2ms
 + ruff==0.16.3
Installed 1 executable: ruff

$ uv tool install commitizen
$ uv tool install hugo
$ uv tool install marimo
$ uv tool install zensical

// インストール済みツールを確認（コマンドはツール名ごとにハイフン付きで列挙される）
$ uv tool list
commitizen v4.17.1
- cz
- git-cz
hugo v0.165.0
- hugo
marimo v0.24.0
- marimo
ruff v0.16.3
- ruff
zensical v0.0.56
- zensical

// ツールをアップグレード
$ uv tool upgrade ruff
Resolved 1 package in 1ms
Nothing to upgrade

// すべてのツールをアップグレード
$ uv tool upgrade --all

// 使わなくなったツールを削除
$ uv tool uninstall mkdocs
Uninstalled 1 executable: mkdocs
```

`uv tool install`は、CLIツールをグローバルにインストールするコマンドです。
`uvx`でお試ししたツールで、日常的に使うようになったものを、`uv tool install`でインストールしておくと便利です。

はじめて使う場合は、
`uv tool update-shell`コマンドを実行して`PATH`の設定が必要です。
`uv tool list`コマンドで、インストール済みのツールを確認できます。
`uv tool upgrade`コマンドで、インストールされたツールをアップグレードできます。
使わなくなったツールは`uv tool uninstall`コマンドで削除できます。

:::{note}

インストールしたツールは、
`~/.local/share/uv/tools/<ツール名>/`にツール本体が配置されます。
実行コマンドへのリンクは、`~/.local/bin/`に作成されます。

`~/.local/bin/`は`pipx`など他のツールとも共有されます。
同名のコマンドがすでに存在する場合はインストールに失敗するため、
置き換える場合はまず古いツールをアンインストールしてください。

:::

### uvxとuv tool installの使い分け

| 用途 | コマンド | 例 |
| --- | --- | --- |
| 一時的に使用 | `uvx` | `uvx pytest script.py` |
| 最新版を試したい | `uvx` | `uvx ruff@0.2.0 check .` |
| 頻繁に使用 | `uv tool install` | `uv tool install ruff` |
| CI/CD環境 | `uv tool install` | Dockerイメージに含める |

:::{note}

`uvx`は`uv tool run`のエイリアスです。
`uvx`（4文字）は`uv tool run`（11文字）よりタイプ数が少なく簡潔なため、通常は`uvx`を使用すればOKです。

:::

## 他のツールと比較したい

`uv`は複数のツールの役割を統合しています。以下は機能比較表です：

### プロジェクト管理

| 機能 | `uv` | `poetry` | `pip` | `pipx` |
| --- | --- | --- | --- | --- |
| プロジェクト初期化 | `uv init` | `poetry init` | × | × |
| 仮想環境作成 | 自動 | 自動 | `python -m venv` | 自動 |

### 依存関係管理

| 機能 | `uv` | `poetry` | `pip` | `pipx` |
| --- | --- | --- | --- | --- |
| パッケージ追加 | `uv add` | `poetry add` | `pip install` | × |
| パッケージ削除 | `uv remove` | `poetry remove` | `pip uninstall` | × |
| 開発用依存 | `uv add --dev` | `poetry add --dev` | 手動管理 | × |
| ロックファイル | `uv lock` | `poetry lock` | `pip freeze` | × |
| 環境同期 | `uv sync` | `poetry install` | `pip install -r` | × |

### 実行と開発

| 機能 | `uv` | `poetry` | `pip` | `pipx` |
| --- | --- | --- | --- | --- |
| スクリプト実行 | `uv run` | `poetry run` | 手動 | × |

### Python管理とツール管理

| 機能 | `uv` | `poetry` | `pip` | `pipx` |
| --- | --- | --- | --- | --- |
| バージョン固定 | `uv python pin` | 外部ツール依存 | × | × |
| バージョンリスト | `uv python list` | × | × | × |
| 一時実行 | `uvx` | × | × | × |
| グローバルインストール | `uv tool install` | × | × | グローバル |

### ビルドと公開

| 機能 | `uv` | `poetry` | `pip` | `pipx` |
| --- | --- | --- | --- | --- |
| ビルド | `uv build` | `poetry build` | `python -m build` | × |
| 公開 | `uv publish` | `poetry publish` | twine | × |
