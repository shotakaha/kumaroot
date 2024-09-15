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
$ pipx install pytest
$ pipx install pytest-mock
```

`pytest-mock`をインストールすると、
[unittest.mock](./python-unittest-mock.md)が使えるようになります。

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

``@patch``デコレーターで、引数に指定した関数をモックできます。

上のサンプルは、
``sheet.download``の中で、
``subprocess.run``を使って
`wget`を呼んでいる場合のテストです。
`subprocess.run`をモックすることで、実際にwgetを実行せずに動作テストできるようにしています。

wgetを実行していないため、`filename="output.csv"`に設定したファイルは作成されません。
そのため、``assert_called_with``を使って、指定した引数で関数が呼ばれたかどうかで、動作確認しています。
