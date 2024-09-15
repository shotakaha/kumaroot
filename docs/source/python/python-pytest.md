# ユニットテストしたい（``pytest``）

```console
$ pytest
$ pytest --verbose
$ pytest ファイル名
```

`pytest`をプロジェクトのルートディレクトリで実行すると、テストをまとめて実行できます。
``--verbose``オプションで、それぞれのテスト結果を表示できます。

## インストールしたい（``pytest``）

```console
$ pip3 install pytest
$ pipx install pytest
$ uv tool install pytest
```

`pytest`は`pipx`や`uv`などでもインストールできます。

```console
$ pip3 install pytest-mock
```

`pytest-mock`をインストールすると、
[unittest.mock](./python-unittest-mock.md)が使えるようになります。
`pytest-mock`はコマンドラインツールではないため、`pipx`などではインストールできません。

```console
$ poetry add pytest --group test
$ poetry add pytest-mock --group test  # モックを使ったユニットテスト
$ poetry add pytest-cov --group test   # テストカバレッジの計測
$ poetry add pytest-html --group test  # テスト結果をHTMLファイルに出力
```

`poetry`などで開発環境を管理している場合は、
``--group test``などに分類するとよいです。


## ディレクトリ構造

```console
$ cd プロジェクト
$ tree
.
├── 自作パッケージ名
│   ├── __init__.py
│   ├── 自作モジュール1.py
│   ├── 自作モジュール2.py
├── tests
│   ├── __init__.py
│   ├── test_自作モジュール1.py
│   ├── test_自作モジュール2.py
├── poetry.toml
├── pyproject.toml
```

ユニットテスト用のファイルは、``tests``ディレクトリの中に作成します。
ファイル名の先頭は``test_``にします。

上のサンプルは[poetry](./python-poetry.md)で作成したディレクトリ構造です。
自作パッケージと同階層に``tests``ディレクトリを作成し、
その中にユニットテストを作成しています。

## パッチしたい（`@patch`）

```python
@patch("モジュール名.クラス名")
def test_テスト関数(モック名):
    """ユニットテストの説明"""
    # テストを書く
    # モック名.メソッド名.return_value = モック値
```

``@patch``デコレーターで引数に指定した関数をモックできます。

```python
import pytest
from unittest.mock import patch

@patch("subprocess.run")
def test_download(mock_subprocess_run):

    """Test download method"""

    # テスト用URL
    url = TEST_SHARED_URL
    sheet = Sheet(
        url=url,
        filename="output.csv")
    sheet.download()

    mock_subprocess_run.assert_called_with(
        ["wget", "--quiet", "-O", "output.csv", sheet.export_url]
    )
```

上のサンプルは、
``sheet.download``の中で、
``subprocess.run``を使って
`wget`を呼んでいる場合のテストです。

`subprocess.run`をモックすることで、wgetを実行せずにテストできるようにしています。
テスト関数の引数名はモック名にします。
この場合は``mock_subprocess_run``でアクセスできるようになります。

wgetを実行していないため、`filename="output.csv"`に設定したファイルは作成されません。
そのため、``assert_called_with``を使って、指定した引数で関数が呼ばれたかどうかで、動作確認しています。

## 複数パッチしたい（``@patch``）

```python
@patch("モジュール名.クラス名3")
@patch("モジュール名.クラス名2")
@patch("モジュール名.クラス名1")
def test_テスト関数(モック名1, モック名2, モック名3):
    """複数のモックを使ったテスト"

    モック名1.メソッド名.return_value = ...
    モック名2.メソッド名.return_value = ...
    モック名3.メソッド名.return_value = ...
```

ひとつのテスト関数に、複数の``@patch``デコレーターを使用できます。
それぞれのモック名を引数に設定することで、モックにアクセスできるようになりますが、
デコレーターをつける順番に注意が必要です。

## パッチしたい（``patch``）

```python
def test_テスト関数():
    with patch("モジュール名.クラス名") as モック名:
        # テストを書く
```

``@patch``デコレーターは、`patch`関数としてコンテキストマネージャーのように使うことができます。

```python
def test_download():
    with patch("subprocess.run") as mock_subprocess_run:
        url = TEST_SHARED_URL
        sheet = Sheet(...)
        sheet.download()
        mock_subprocess_run.assert_called_with(...)
```



