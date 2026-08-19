# パッケージ管理したい（`hatch`）

```console
// 新規プロジェクト作成
$ hatch new my-project

// 依存関係のインストール（pyproject.tomlの内容を反映）
$ hatch env create

// パッケージの実行とテスト
$ hatch run python main.py
$ hatch test

// コードチェック
$ hatch check

// バージョン管理
$ hatch version patch

// パッケージ公開
$ hatch build
$ hatch publish
```

`hatch`は、PyPA（Python Packaging Authority）傘下のプロジェクト管理ツールです。
プロジェクトの初期化、仮想環境の管理、テスト、コードチェック、パッケージのビルドと公開まで、Pythonプロジェクトのライフサイクル全体をカバーします。

`pyproject.toml`を軸に設定し、複数のPython環境を自動で構築・管理できます。
バージョン管理コマンド（`hatch version`）を内蔵している点が、他のツールにはない特徴です。

:::{note}
Pythonでは、
パッケージ管理には`pip`、
バージョン管理には`pyenv`、
プロジェクト管理には`poetry`
のように、
複数のツールがまるで戦国時代のように群雄割拠しています。

`hatch`は、PyPAが管理する公式寄りのツールという立ち位置で、
とくにパッケージのビルド・公開まわり（`hatchling`ビルドバックエンド）で存在感があります。
[uv](./python-uv.md)や[poetry](./python-poetry.md)と比べると、
依存パッケージの追加・削除は`pyproject.toml`を直接編集する運用が前提になっている点が特徴的です。

:::

## インストールしたい（`hatch`）

```console
// Homebrewでインストール
$ brew install hatch

$ which -a hatch
/opt/homebrew/bin/hatch

$ hatch --version
Hatch, version 1.18.0
```

`hatch`はHomebrewでインストールできます。
`pipx install hatch`や`uv tool install hatch`でもインストールできます。

:::{note}
公式ドキュメントでは`pipx`を使ったインストールが推奨されています。
挙動はどの方法でもほぼ同じで、専用の仮想環境を作ってから実行コマンドを`PATH`の通った場所にリンクします。
:::

## 新規プロジェクトしたい（`hatch new`）

```console
$ hatch new my-project
my-project
├── src
│   └── my_project
│       ├── __about__.py
│       └── __init__.py
├── tests
│   └── __init__.py
├── LICENSE.txt
├── README.md
└── pyproject.toml
```

`hatch new`コマンドでプロジェクトを初期化できます。
`src/<パッケージ名>/`レイアウトが自動生成され、`__about__.py`にバージョン情報が保存されます。
`author`や`license`などのメタデータは、Gitの設定（`user.name`、`user.email`）から自動で入力されます。

```console
$ cat my-project/pyproject.toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-project"
dynamic = ["version"]
description = ''
readme = "README.md"
requires-python = ">=3.8"
license = "MIT"
...
dependencies = []

[tool.hatch.version]
path = "src/my_project/__about__.py"
```

プロジェクトのメタデータは`pyproject.toml`の`[project]`セクションに保存されます。
このファイルはユーザーが直接編集することを想定しています。

:::{note}

`requires-python`のデフォルトは`>=3.8`と古めです。
実際に使うPythonバージョンに合わせて、作成後に書き換えておくとよいです。

:::

### 対話形式で作りたい（`hatch new -i`）

```console
$ hatch new -i
Project name: my-project
Description []: サンプルプロジェクト
```

`-i`（`--interactive`）オプションで、プロジェクト名や説明などを対話的に入力しながら作成できます。
`hatch new my-project`のように名前を直接指定する方法との違いは、対話中に説明文などの追加項目を入力できる点だけです。

### 既存ディレクトリに追加したい（`hatch new --init`）

```console
$ cd my-project
$ hatch new --init
Project name: my-project
Description []:
Wrote: pyproject.toml
```

`--init`オプションで、既存のディレクトリに`pyproject.toml`を追加できます。
プロジェクト名の入力を求められるので、ディレクトリ名などを入力してください。
`hatch new`と違って、`src/`レイアウトや`README.md`、`LICENSE.txt`は生成されず、`pyproject.toml`のみが追加されます。

### CLIツールを作りたい（`hatch new --cli`）

```console
$ hatch new --cli my-cli-tool
```

`--cli`オプションで、コマンドラインインターフェイスを持つプロジェクトとして作成できます。
`pyproject.toml`の`[project.scripts]`にエントリーポイントが自動登録されます。

## 仮想環境したい（`hatch env`）

```console
$ cd my-project

// 仮想環境を作成
$ hatch env create
Creating environment: default
Installing project in development mode
Checking dependencies

// 環境一覧を確認
$ hatch env show
       Standalone
┏━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━┓
┃ Name    ┃ Type    ┃ Dependencies ┃ Scripts ┃
┡━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━┩
│ default │ virtual │              │         │
└─────────┴─────────┴──────────────┴─────────┘

// 環境の保存先を確認
$ hatch env find
~/.local/share/hatch/env/virtual/my-project/xxxxxxxx/my-project
```

`hatch env create`コマンドで仮想環境を明示的に作成できます。
`hatch shell`や`hatch run`を実行したときにも、環境がなければ自動的に作成されます。
`hatch env show`で作成済みの環境一覧、`hatch env find`で環境の実際の保存先を確認できます。

デフォルトの保存先はプロジェクトディレクトリの外（`~/.local/share/hatch/env/`配下）です。
`.venv`のようにプロジェクト内に作られる`uv venv`や`poetry env`（`virtualenvs.in-project`設定時）とは異なる点に注意してください。

```console
// 仮想環境の中に入る
$ hatch shell
You are about to enter a new shell, exit as you usually would e.g. by typing `exit` or pressing `ctrl+d`...
(my-project) $ exit
```

`hatch shell`コマンドで、仮想環境をアクティブ化したサブシェルに入れます。
`uv venv`や`poetry env activate`と違って、`source`コマンドを使わずに直接シェルへ入れる点が特徴です。
抜けるときは`exit`か`Ctrl+D`を使います。

```console
// 環境を削除
$ hatch env remove
Removing environment: default

// すべての環境を削除
$ hatch env prune
```

`hatch env remove`コマンドで、現在の環境を削除できます。
`hatch env prune`コマンドで、プロジェクトに紐づくすべての環境（テスト用・ビルド用なども含む）を一括削除できます。

:::{note}

`hatch env show`はデフォルトで、ユーザーが`pyproject.toml`の`[tool.hatch.envs.*]`で定義した環境のみを表示します。
`hatch test`や`hatch build`が内部的に使う環境（`hatch-test`、`hatch-build`など）も見たい場合は、`-i`（`--internal`）オプションを付けます。

:::

## 依存関係を管理したい（`pyproject.toml`）

```toml
[project]
dependencies = [
  "requests>=2.28.0",
]
```

`hatch`には、`uv add`や`poetry add`に相当する「パッケージ追加」専用コマンドがありません。
`pyproject.toml`の`dependencies`を直接編集してから、`hatch env create`（や`hatch run`）で環境に反映する運用が前提です。

```console
// 現在の依存関係を確認
$ hatch dep show requirements
requests>=2.28.0
```

`hatch dep show requirements`コマンドで、現在定義されている依存関係を`requirements.txt`形式で確認できます。

:::{note}

`[project]`セクションの`dependencies`はプロジェクト全体の依存関係です。
`[tool.hatch.envs.<環境名>]`セクションに`dependencies`を追加すると、その環境だけに依存パッケージを追加できます。
テスト専用のパッケージなどは、後者で環境ごとに分けておくと管理しやすいです。

:::

### ロックファイルを使いたい（`hatch dep lock`）

```toml
[tool.hatch.envs.default]
locked = true
installer = "uv"
```

`hatch dep lock`コマンドで、PEP 751形式のロックファイル（`pylock.toml`）を生成できます。
`uv.lock`や`poetry.lock`と違って、環境ごとに`locked = true`を明示しないと有効になりません。
また`hatch dep sync`（ロックファイルの内容を環境に反映するコマンド）を使うには、`installer = "uv"`の指定も必要です（デフォルトの`pip`インストーラーは未対応）。

```console
$ hatch dep lock
Locking environment: default

$ hatch dep sync
Syncing from lockfile
Synced environment `default` from `pylock.toml`
```

:::{note}

この機能は2026年時点でもまだ実験的な位置づけです。
`uv`や`poetry`のように「デフォルトでロックファイルを使う」運用ではなく、`hatch`はオプトインの機能として提供しています。
再現性を重視しないプロジェクトでは、ロック機能を使わずに`dependencies`の直接編集だけで運用しても問題ありません。

:::

## パッケージを実行したい（`hatch run`）

```console
$ hatch run python main.py
Hello, World!

$ hatch run pytest
===== test session starts =====
tests/test_example.py .                                       [100%]
1 passed
```

`hatch run`コマンドで、プロジェクトの仮想環境を使って外部コマンドやスクリプトを実行できます。
仮想環境の手動アクティベーションは不要です。

```toml
[tool.hatch.envs.default.scripts]
format = "ruff format ."
lint = "ruff check ."
```

`pyproject.toml`の`[tool.hatch.envs.<環境名>.scripts]`に、よく使うコマンドをエイリアスとして登録できます。

```console
$ hatch run format
$ hatch run lint
```

登録したエイリアスは、`hatch run <エイリアス名>`で実行できます。

```console
// 環境名を指定して実行
$ hatch run types:check
```

`環境名:コマンド`の形式で、`default`以外の環境を指定して実行できます。
環境を省略した場合は、`-e`オプション（や`HATCH_ENV`環境変数）で指定した環境、それもなければ`default`環境が使われます。

## コードをチェックしたい（`hatch check`）

```console
$ hatch check
```

`hatch check`コマンドで、静的解析（lint）・フォーマット確認・型チェックをまとめて実行できます。
内部では[Ruff](https://docs.astral.sh/ruff/)や型チェッカーを利用しています。

```console
// 自動修正を適用
$ hatch check --fix

// リンターのみ実行
$ hatch check code

// フォーマット確認のみ実行
$ hatch check fmt

// 型チェックのみ実行
$ hatch check types
```

`--fix`オプションで、自動修正できる問題を書き換えられます。
`code`（静的解析）、`fmt`（フォーマット確認）、`types`（型チェック）のサブコマンドで、個別に実行することもできます。

:::{note}

過去バージョンにあった`hatch fmt`コマンドは、`hatch 1.18.0`時点では非推奨になっています。
実行すると`hatch check code --fix`と`hatch check fmt --fix`を使うよう案内されます。
既存のドキュメントや記事で`hatch fmt`を見かけたら、`hatch check --fix`に読み替えてください。

:::

## テストしたい（`hatch test`）

```console
$ hatch test
============================= test session starts ==============================
platform darwin -- Python 3.12.7, pytest-9.1.1, pluggy-1.6.0
...
tests/test_example.py .                                                  [100%]
============================== 1 passed in 0.01s ===============================
```

`hatch test`コマンドで、専用の`hatch-test`環境を使ってテストを実行できます。
`pytest`や`coverage`などのテスト用パッケージがあらかじめ含まれており、手動でのインストールは不要です。

デフォルトでは、現在使用中のインタープリターに一致する環境1つだけでテストが実行されます。
複数のPythonバージョンでテストしたい場合は、`pyproject.toml`でマトリクスを定義します。

```toml
[[tool.hatch.envs.hatch-test.matrix]]
python = ["3.11", "3.12", "3.13"]
```

```console
// マトリクスに定義したすべてのバージョンでテスト
$ hatch test --all

// 特定のバージョンだけテスト
$ hatch test --python 3.12

// カバレッジを測定
$ hatch test --cover

// 並列実行
$ hatch test --parallel
```

`--all`オプションで、マトリクスに定義したすべてのバージョンでテストを実行できます。
指定しない場合は、現在の環境に合う1つのバージョンのみが対象になる点に注意してください。

## バージョンを管理したい（`hatch version`）

```console
$ hatch version
0.0.1

$ hatch version patch
Old: 0.0.1
New: 0.0.2

$ hatch version minor
Old: 0.0.2
New: 0.1.0

$ hatch version major
Old: 0.1.0
New: 1.0.0
```

`hatch version`コマンドで、プロジェクトのバージョンを確認・更新できます。
バージョン情報は`hatch new`で生成される`src/<パッケージ名>/__about__.py`に保存され、`pyproject.toml`の`[tool.hatch.version]`がその参照先を指定しています。

- `hatch version patch`：パッチバージョンを上げる（バグ修正）
- `hatch version minor`：マイナーバージョンを上げる（新機能）
- `hatch version major`：メジャーバージョンを上げる（大きな変更）

:::{note}

`uv`や`poetry`には、これに相当するバージョン管理コマンドがありません（`uv version`はサブコマンドとして未提供、`poetry version`は別途存在しますが`hatch`ほど`__about__.py`との連携は強くありません）。
バージョンを頻繁にバンプする運用であれば、`hatch`ならではの利点になります。

:::

## パッケージをビルドしたい（`hatch build`）

```console
$ hatch build
sdist
dist/my_project-0.0.2.tar.gz
wheel
dist/my_project-0.0.2-py3-none-any.whl
```

`hatch build`コマンドでパッケージをビルドできます。
`dist/`ディレクトリの中に、`wheel`形式（`.whl`）と`sdist`形式（`.tar.gz`）のファイルが生成されます。

```console
$ hatch build --target wheel
Inspecting build dependencies
──────────────────────────────────── wheel ─────────────────────────────────────
dist/my_project-0.0.2-py3-none-any.whl

$ hatch build --target sdist
Inspecting build dependencies
──────────────────────────────────── sdist ─────────────────────────────────────
dist/my_project-0.0.2.tar.gz
```

`-t`（`--target`）オプションで、どちらか片方の形式だけをビルドできます。

:::{note}

`uv build`や`poetry build`にある`--dry-run`のようなオプションは、`hatch build`にはありません。
実際に手を動かす前に内容を確認したい場合は、`-c`（`--clean`）オプションを付けずに実行し、生成された`dist/`の中身を確認するのが実用的です。

:::

## パッケージを公開したい（`hatch publish`）

```console
$ hatch publish
Enter your username: __token__
Enter your credentials:
```

`hatch publish`コマンドで、PyPIにパッケージを公開できます。
認証情報が未設定の場合は、初回実行時にユーザー名（`__token__`固定）とAPIトークンの入力を求められます。
一度入力すると、`~/.config/hatch/config.toml`（プラットフォームによって異なる）に保存され、以降は再入力不要です。

```console
// TestPyPIに公開
$ hatch publish -r test
```

`-r`（`--repo`）オプションで、公開先を切り替えられます。
`test`は組み込みのエイリアスで、TestPyPIを指します（`main`がデフォルトのPyPI）。
はじめて公開するパッケージは、まずTestPyPIに公開して動作テストしてからPyPIに本番公開することをオススメします。

```console
// ユーザー名・トークンをオプションで直接指定
$ hatch publish -u __token__ -a <your-token>
```

`-u`（`--user`）・`-a`（`--auth`）オプションで、認証情報をコマンドラインから直接渡せます。
CI環境では、`HATCH_INDEX_USER`・`HATCH_INDEX_AUTH`環境変数で渡すほうが安全です。

:::{note}

`uv publish`や`poetry publish`にある`--dry-run`のようなオプションは、`hatch publish`にもありません。
公開前の確認は、`hatch build`で生成した`dist/`の中身を目視するか、TestPyPIへの公開で代用してください。

:::

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

## リファレンス

- [Hatch](https://hatch.pypa.io/latest/)
