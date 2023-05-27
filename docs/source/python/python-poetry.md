# パッケージ管理したい（``poetry``）

```console
$ poetry new プロジェクト名
$ cd プロジェクト名
$ poetry add パッケージ名
```

パッケージ管理ツールのひとつです。
Pythonのパッケージ管理ツールはいろいろ存在していて、
複雑な歴史的な経緯もあり（？）まったく統一されておらず、
すべてを把握＆理解するのは不可能だと思います。
僕は、たまたま使い始めてみたのですが、使い勝手いいなと感じていて、
いまから使いはじめるなら``poetry``はオススメです。

## インストール

```console
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

公式ドキュメントでは独自スクリプトを使った方法が推奨されています。

```console
$ pipx install poetry
$ which poetry
~/.local/bin/poetry
```

``pip3``のインストールは推奨されてないみたいですが、``pipx``はフルサポートされています。

```console
$ brew install poetry
$ which poetry
/opt/homebrew/bin/poetry
```

Homebrewを使ったインストールでも、とくに問題なく使えました。

:::{caution}

このいずれかひとつの方法でインストールしてください。

:::

## シェル補完したい（``poetry completions``）

```console
$ poetry completions fish > ~/.config/fish/completions/poetry.fish
```

``poetry``コマンドを補完するための設定をシェルに設定します。
``bash``、``zsh``、``fish``の補完に対応しています。

:::{note}

``fish``の補完は、セッション内で最初に実行したときにエラーがでます。
v1.2.0から存在しているバグで、``cleo``パッケージに依存しているようです（[poetry#5929](https://github.com/python-poetry/poetry/issues/5929)）。
v1.5.0になっても治っていません。

:::

## 新規プロジェクトしたい（``poetry new``）

```bash
$ poetry new プロジェクト名
$ cd プロジェクト名
```

新しくプロジェクトを作成する場合は、``poetry new``コマンドを使います。
``プロジェクト名``のディレクトリが作成され、その下に、``pyproject.toml``、``プロジェクト名``（＝プロジェクト本体のソースコード置き場）、``tests``などの必要なファイルが自動で生成されます。

## 既存プロジェクトを使いたい（``poetry init``）

```bash
$ cd プロジェクト名
$ poetry init
```

``poetry init``を実行して、対話的にプロジェクトを初期化できます。
プロンプトの表示にしたがってプロジェクト情報（プロジェクト名、説明、作成者、バージョン番号、ライセンスなど）を入力します。
続けて、必要なパッケージに関するプロンプトが表示されるので、パッケージ名やバージョン番号を入力して、パッケージを選択します。
これらの設定はすべて{file}`pyproject.toml`の``[tool.poetry]``セクションに保存されます。
あとから直接編集できるので、間違えてしまっても大丈夫です。

## パッケージを追加したい（``poetry add``）

```bash
$ poetry add パッケージ名
$ poetry add パッケージ名 -E パッケージ名
$ poetry add --group=dev パッケージ名
$ poetry add --group=docs パッケージ名
```

必要なパッケージ名を{file}`pyproject.toml`に追記して、仮想環境（``.venv``）の中にインストールします。
``-E / --extra``オプションを使って、追加パッケージも指定できます。
パッケージは``[tool.poetry.dependencies]``のセクションに追記され、ロックファイル（``poetry.lock``）が生成されます。

（たしか）``v1.3``からパッケージをグループ化する機能が追加されました。デフォルトは``--group=main``です。
これに伴い``add -D``オプションが非推奨になりました。
これからは代わりに``add --group=dev``する必要があります。
また、ドキュメント生成に必要なパッケージは``--group=docs``、テストに必要なパッケージは``--group=test``のように複数のグループを作って管理することができるようになりました。

## パッケージをインストールしたい（``poetry install``）

```bash
$ poetry install
```

{file}`poetry.lock`にあるパッケージをインストールします。
{file}`poetry.lock`がない場合は、{file}`pyproject.toml`にあるパッケージをインストールして、{file}`poetry.lock`を生成します。

デフォルトでは``{cache-dir}/virtualenvs/``に設定されたパスの仮想環境を作成し、パッケージをインストールします。
``virtualenvs.in-project = true``に設定した場合は、プロジェクト内の``{project-dir}/.venv/``に仮想環境を作成します。

## パッケージを公開したい（``poetry publish``）

```bash
$ poetry build
$ poetry publish -r testpypi  # TestPyPIに公開
$ poetry publish              # PyPIに公開
```

パッケージをビルドしてから公開します。
はじめて公開する場合は必ず``TestPyPI``でテストするのがよいです。
公開する前にリポジトリとAPIトークンの設定が必要です。

## 現在の設定を確認したい（``poetry config``）

```bash
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

```bash
$ poetry config キー名 値
$ poetry config キー名 値 --local
```

変更可能な設定は[PoetryドキュメントのAvailable Settings](https://python-poetry.org/docs/configuration/#available-settings)を参照してください。
Poetry v1.2.0になって設定できる項目が増えました。

### 設定を削除したい

```bash
$ poetry config キー名 --unset
$ poetry config キー名 --unset --local
```

追加した設定を削除する場合はキー名に対して``--unset``します。

## プロジェクト内に仮想環境を作成したい

```bash
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
デフォルトでは{file}``{cache-dir}/virtualenvs``に設定されています。

[virtualenvs.in-project](https://python-poetry.org/docs/configuration/#virtualenvsin-project)を``true``にすると、その設定をカレントディレクトリの{file}``.venv``に変更できます。
GitHub/GitLabなどを通じて複数のマシンで作業する場合は、この値を有効にしておくとよいです。

:::{caution}

すでに{file}`{cache-dir}/virtualenvs/`に仮想環境がある場合は、一度削除（``rm -r``）してから作成しなおしてください。

:::

## システムのパッケージを使いたい

```bash
$ poetry config virtualenvs.option.system-site-packages true
```

[virtualenvs.option.system-site-packages](https://python-poetry.org/docs/configuration/#virtualenvsoptionssystem-site-packages)を``true``にすると、システムのPythonの{file}``site-packages``にインストールが仮想環境から使えるようになります。
開発環境で使うパッケージ（``pytest`` / ``black`` / ``commitizen`` / ``pysen``）などを使うには、これを有効にしておいてもいいかもしれません。

:::{note}

複数のPythonプロジェクトを持っていると、それぞれのプロジェクトの{file}`.venv`にパッケージがインストールされます。
開発環境にだけ必要なパッケージを共通化することで、少しだけでもディスク節約になるかもしれません。

:::

## リポジトリとAPIトークンを設定したい

```bash
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

## リファレンス

[Poetry](https://python-poetry.org/)
: Poetry公式ドキュメントです。

[Configuration - Poetry](https://python-poetry.org/docs/configuration/)
: ``poetry config``するときに参照するページです。とくに[Available Settings](https://python-poetry.org/docs/configuration/#available-settings)のセクションはよく読んでいます。

[poetryを使ってpythonパッケージを作成する - Zennのスクラップ](https://zenn.dev/shotakaha/scraps/9416c30cd7745a)
: 僕のZennスクラップです。Poetryを使ってパッケージを新規作成してPyPIで公開するまでの手順を整理しました。
