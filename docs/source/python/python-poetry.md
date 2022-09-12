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

## 既存のプロジェクトをセットアップしたい

```bash
$ cd MyPROJECT
$ poetry init
```

## パッケージを追加したい

```bash
$ poetry add パッケージ名
$ poetry add -D パッケージ名
```

パッケージ名を{file}`pyproject.toml`の``[tool.poetry.dependencies]``に追加して、
仮想環境の中にインストールします。

## パッケージをインストールしたい

```bash
$ poetry install
```

{file}`pyproject.toml`（or {file}`poetry.lock`）の内容にしたがって、必要なパッケージをインストールします。
デフォルトだと``{cache-dir}/virtualenvs/``に設定されたパスの中に仮想環境が作成されます。
``virtualenvs.in-project = true``に設定した場合は、プロジェクト内の``{project-dir}/.venv/``に仮想環境が作成されます。

## パッケージを公開したい

```bash
$ poetry build
$ poetry publish -r testpypi  # TestPyPIに公開
$ poetry publish              # PyPIに公開
```

パッケージをビルドしてから公開します。
はじめて公開する場合は必ず``TestPyPI``でテストするのがよいです。
公開する前にリポジトリとAPIトークンの設定が必要です。



## 現在の設定を確認したい

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
