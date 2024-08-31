# パッケージ管理したい（``poetry``）

```console
$ poetry new プロジェクト名
$ poetry add pandas matplotlib
$ poetry add --group=dev ipykernel pytests commitizen ruff
$ poetry add --group=docs sphinx_book_theme myst_parser
$ poetry install
$ poetry shell
$ poetry build
$ poetry publish
```

プロジェクトに依存するパッケージを管理したり、PyPIなどに公開するには[Poetry](https://python-poetry.org/)がオススメです。
Pythonのパッケージ管理ツールはいろいろ存在していますが、（おそらく複雑な歴史的な経緯があり）まったく統一されておらず、すべてを把握＆理解するのは不可能だと思います。
僕は、たまたま使い始めてみたのですが、使い勝手がよいなと感じています。

## インストールしたい（``pipx install poetry``）

```console
$ pipx install poetry
$ which poetry
~/.local/bin/poetry

$ poetry --version
Poetry (version 1.8.2)

$ pipx inject poetry poetry-plugin-export
```

公式ドキュメントでは``pipx``を使った方法が推奨されています。
``pip3``のインストールは推奨されてないみたいです。

:::{caution}

Homebrewでもインストールできます。
このいずれかひとつの方法でインストールしてください。

:::

## シェル補完したい（``poetry completions``）

```console
$ poetry completions fish > ~/.config/fish/completions/poetry.fish
```

``poetry``コマンドのシェル補完が使えるようにしておくと便利です。
``bash``、``zsh``、``fish``のシェルに対応しています。

:::{hint}

``fish``のシェル補完を使うと、シェルセッションで最初に実行したときにエラーが表示されます。
v1.2.0から存在しているバグ（[poetry#5929](https://github.com/python-poetry/poetry/issues/5929)）ですが、v1.5.0になっても修正されていません。
そのままでも使うことはできますが、以下のように``sd``コマンドを使って置換して対処できます。

:::{code-block} console
$ poetry completions fish | sd "'([^']+)''" '"$1"\'' > ~/.config/fish/completions/poetry.fish
:::

エラーの原因は、以下のように``__fish_seen_subcommand_from``が使われている部分の引数の文字列の囲み方に問題があるようです。

```diff
- < complete -c poetry -A -n '__fish_seen_subcommand_from 'cache clear'' -l all -d 'Clear all entries in the cache.'
---
+ > complete -c poetry -A -n '__fish_seen_subcommand_from "cache clear"' -l all -d 'Clear all entries in the cache.'
```

:::

## 新規プロジェクトしたい（``poetry new``）

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

## パッケージを追加したい（``poetry add``）

```console
$ poetry add パッケージ名
$ poetry add パッケージ名 -E パッケージ名
$ poetry add --group=dev パッケージ名
$ poetry add --group=docs パッケージ名
```

必要なパッケージ名を{file}`pyproject.toml`に追記して、仮想環境（``.venv``）の中にインストールします。
``-E / --extra``オプションを使って、追加パッケージも指定できます。
パッケージは``[tool.poetry.dependencies]``のセクションに追記され、ロックファイル（``poetry.lock``）が生成されます。

### 開発環境を追加したい（``--group=dev``）

```console
$ poetry add --group=dev pytests
$ poetry add --group=dev commitizen
$ poetry add --group=dev jupyterlab
```

開発に必要なパッケージは``--group=dev``に追加します。
（たしか）``v1.3.0``からグループ化する機能追加され、``add -D``オプションが非推奨になりました。

### ドキュメント環境を追加したい（``--group=docs``）

```console
$ poetry add --group=docs sphinx_book_theme
$ poetry add --group=docs myst_parser
```

ドキュメント作成に必要なパッケージは``--groupd=docs``に追加します。

## パッケージをインストールしたい（``poetry install``）

```console
$ poetry install
```

{file}`poetry.lock`にあるパッケージをインストールします。
{file}`poetry.lock`がない場合は、{file}`pyproject.toml`にあるパッケージをインストールして、{file}`poetry.lock`を生成します。

デフォルトでは``{cache-dir}/virtualenvs/``に設定されたパスの仮想環境を作成し、パッケージをインストールします。
``virtualenvs.in-project = true``に設定した場合は、プロジェクト内の``{project-dir}/.venv/``に仮想環境を作成します。

## パッケージ環境を確認したい（``poetry check``）

```console
$ poetry check
All set!

$ poetry check --lock
All set!
```

## パッケージをビルドしたい（``poetry build``）

```console
$ poetry build
Building パッケージ名 (バージョン番号)
  - Building sdist
  - Built パッケージ名-バージョン番号.tar.gz
  - Building wheel
  - Built パッケージ名-バージョン番号-py3-none-any.whl
```

`build`コマンドでパッケージをビルドできます。

## パッケージを公開したい（``poetry publish``）

```console
// TestPyPIに公開
$ poetry publish -r testpypi
Publishing パッケージ名 (バージョン番号) to testpypi
 - Uploading パッケージ名-バージョン番号-py3-none-any.whl
 - Uploading パッケージ名-バージョン番号.tar.gz

// PyPIに公開
$ poetry publish
Publishing パッケージ名 (バージョン番号) to pypi
 - Uploading パッケージ名-バージョン番号-py3-none-any.whl
 - Uploading パッケージ名-バージョン番号.tar.gz
```

パッケージをビルドしてから公開します。
はじめて公開する場合は必ず``TestPyPI``でテストするのがよいです。
公開する前にリポジトリとAPIトークンの設定が必要です。

:::{seealso}

僕のZennスクラップ「[poetryを使ってpythonパッケージを作成する](https://zenn.dev/shotakaha/scraps/9416c30cd7745a)」に、Poetryを使ってパッケージを新規作成してPyPIで公開するまでの手順を整理しました。

:::

### TestPyPI／PyPIを設定したい

```console
// testpypi という名前で TestPyPIを追加する
$ poetry config repositories.testpypi https://test.pypi.org/legacy/

// TestPyPIの個人ページで発行したAPIトークンを登録する
$ poetry config pypi-token.testpypi <your-token>

// PyPIの個人ページで発行したAPIトークンを登録する
$ poetry config pypi-token.pypi <your-token>
```

TestPyPI／PyPIに公開するために、APIトークンを設定する必要があります。
APIトークンは、それぞれのサービスの個人ページで発行したものをコピペしてください。

他にもさまざまな種類のリポジトリを設定できます。
詳しくは[Repositories](https://python-poetry.org/docs/repositories/)を参照してください。

## 現在の設定を確認したい（``poetry config``）

```console
$ poetry config --list
cache-dir = "~/Library/Caches/pypoetry"
experimental.new-installer = true
experimental.system-git-client = false
installer.max-workers = null
installer.modern-installation = true
installer.no-binary = null
installer.parallel = true
virtualenvs.create = true
virtualenvs.in-project = null
virtualenvs.options.always-copy = false
virtualenvs.options.no-pip = false
virtualenvs.options.no-setuptools = false
virtualenvs.options.system-site-packages = false
virtualenvs.path = "{cache-dir}/virtualenvs"  # ~/Library/Caches/pypoetry/virtualenvs
virtualenvs.prefer-active-python = false
virtualenvs.prompt = "{project_name}-py{python_version}"
```

現在の設定は``poetry config --list``で確認できます。
デフォルトの設定は上記のようになっていました。
全体の設定は{file}`~/Library/Application Support/pypoetry/config.toml`に保存されます。
`--local`オプションをつけて設定した項目は、プロジェクト内の{file}`poetry.toml`に保存されます。

:::{note}

全体の設定は、以前は{file}`~/Library/Preferences/pypoetry/config.toml`に保存されていました。
その状態でもまだ使えるようですが、将来的にはパスを変更したほうがよさそうです。

:::

### 設定を変更したい

```console
$ poetry config キー名 値
$ poetry config キー名 値 --local
```

変更可能な設定は[PoetryドキュメントのAvailable Settings](https://python-poetry.org/docs/configuration/#available-settings)を参照してください。
Poetry v1.2.0になって設定できる項目が増えました。

### 設定を削除したい

```console
$ poetry config キー名 --unset
$ poetry config キー名 --unset --local
```

追加した設定を削除する場合はキー名に対して``--unset``します。

## プロジェクト内に仮想環境を作成したい

```console
# 現在の設定値を確認する
$ poetry config virtualenvs.in-project
null

# 設定を有効にする
$ poetry config virtualenvs.in-project true

# 変更後の設定値を確認する
$ poetry config virtualenvs.in-project
true
```

仮想環境は``virtualenvs.path``で設定されたパスに作成されます。
デフォルトでは{file}``\{cache-dir\}/virtualenvs``に設定されています。

[virtualenvs.in-project](https://python-poetry.org/docs/configuration/#virtualenvsin-project)を``true``にすると、その設定をカレントディレクトリの{file}``.venv``に変更できます。
GitHub/GitLabなどを通じて複数のマシンで作業する場合は、この値を有効にしておくとよいです。

:::{caution}

すでに{file}`\{cache-dir\}/virtualenvs/`に仮想環境がある場合は、一度削除（``rm -r``）してから作成しなおしてください。

:::

## システムのパッケージを使いたい

```bash
$ poetry config virtualenvs.option.system-site-packages true
```

[virtualenvs.option.system-site-packages](https://python-poetry.org/docs/configuration/#virtualenvsoptionssystem-site-packages)を``true``にすると、システムのPythonの{file}``site-packages``にインストールが仮想環境から使えるようになります。
開発環境で使うパッケージ（``pytest`` / ``black`` / ``commitizen`` / ``pysen``）などを使うには、これを有効にしておいてもいいかもしれません。

:::{hint}

複数のPythonプロジェクトを持っていると、それぞれのプロジェクトの{file}`.venv`にパッケージがインストールされます。
開発環境にだけ必要なパッケージを共通化することで、少しだけでもディスク節約になるかもしれません。

:::

## リポジトリとAPIトークンを設定したい

```console
$ poetry config repositories.名前 URL
$ poetry config pypi-token.名前 "APIトークン"
```

``名前``の部分は任意の文字列で構いません。
以下に``PyPI``と``TestPyPI``の設定例を挙げておきます。

```bash
# PyPIの設定
$ poetry config pypi-token.pypi "PyPIのAPIトークン"

# TestPyPIの設定
$ poetry config repositories.testpypi https://test.pypi.org/legacy/
$ poetry config pypi-token.testpypi "TestPyPIのAPIトークン"
```

``PyPI``はデフォルトの公開先になっているため、リポジトリの設定は必要ありません。
``TestPyPI``に公開する場合は、リポジトリのURLを設定する必要があります。
公開先のAPIトークンをそれぞれ事前に発行しておく必要があります。
