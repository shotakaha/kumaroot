# パッケージ管理したい（``poetry``）

パッケージ管理ツールのひとつです。
Pythonのパッケージ管理ツールはいろいろ存在していて、
複雑な歴史的な経緯もあり（？）まったく統一されておらず、
すべてを把握＆理解するのは不可能だと思います。
僕は、たまたま使い始めてみたのですが、使い勝手いいなと感じていて、
いまから使いはじめるなら``poetry``はオススメです。

## インストール

```bash
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

```bash
$ brew install poetry
```

公式ドキュメントを読むと``pip3``を使ったインストールは推奨していないみたいです。
僕はHomebrewを使ってインストールしていますが、とくに問題なく使えています。

## 新しいプロジェクトをセットアップしたい（``poetry new``）

```bash
$ poetry new プロジェクト名
$ cd プロジェクト名
```

新しくプロジェクトを作成する場合は、``poetry new``コマンドを使います。
``プロジェクト名``のディレクトリが作成され、その下に、``pyproject.toml``、``プロジェクト名``（＝プロジェクト本体のソースコード置き場）、``tests``などの必要なファイルが自動で生成されます。

## 既存のプロジェクトをセットアップしたい（``poetry init``）

```bash
$ cd プロジェクト名
$ poetry init
```

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
```

全体の設定は{file}`~/Library/Preferences/pypoetry/config.toml`に保存されます。
{command}`--local`オプションをつけて設定した項目は、プロジェクト内の{file}`poetry.toml`に保存されます。

### 設定を変更したい

```bash
$ poetry config キー名 値
$ poetry config キー名 値 --local
```

設定可能なキーについては[PoetryドキュメントのAvailable Settings](https://python-poetry.org/docs/configuration/#available-settings)を参照してください。
Poetry v1.2.0になって設定できる項目が増えました。

### 設定を削除したい

```bash
$ poetry config キー名 --unset
$ poetry config キー名 --unset --local
```

## 仮想環境をプロジェクト内に変更したい

```bash
$ poetry config virtualenvs.in-project true --local
```

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

- [Poetry](https://python-poetry.org/)
- [poetryを使ってpythonパッケージを作成する - Zennのスクラップ](https://zenn.dev/shotakaha/scraps/9416c30cd7745a)
