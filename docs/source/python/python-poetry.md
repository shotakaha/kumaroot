# poetry

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

公式ドキュメントを読むと``pip3``を使ったインストールは推奨していないみたい

## 既存のプロジェクトをセットアップする

```bash
cd MyPROJECT
poetry init
```

## パッケージを追加する

```bash
poetry add パッケージ名
poetry add -D パッケージ名
```

## パッケージをインストールする

```bash
poetry install
```

## パッケージをビルドする

```bash
poetry build
```

## パッケージを公開する

```bash
poetry publish              # PyPIに公開
poetry publish -r testpypi  # TestPyPIに公開
```

はじめて公開する場合は必ず``TestPyPI``でテストするのがよいです。
次に書いたリポジトリとAPIトークンの設定をしてください。

### リポジトリの登録

```bash
poetry config repositories.testpypi https://test.pypi.org/legacy/
```

デフォルトの公開先は``PyPI``になっています。
``TestPyPI``に公開したい場合は、以下のようにリポジトリを登録する必要があります。

### APIトークンの登録

```bash
poetry config pypi-token.pypi "PyPIのAPIトークン"
poetry config pypi-token.testpypi "TestPyPIのAPIトークン"
```

``PyPI``と``TestPyPI``に公開するには、あらかじめAPIトークンを発行し、設定しておく必要があります。
