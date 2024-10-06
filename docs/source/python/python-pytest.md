# ユニットテストしたい（``pytest``）

```console
$ pytest --version
pytest 8.3.3

$ pytest
$ pytest --verbose
$ pytest ファイル名
```

`pytest`はPythonのユニットテスト群をまとめて実行できるツールです。
プロジェクトのルートディレクトリで実行すればテストをまとめて実行できます。
``--verbose``オプションで、それぞれのテストごとに結果を表示できます。

## インストールしたい（``pytest``）

- `pipx`でインストール

```console
$ pipx install pytest
```

- `poetry`でインストール

```console
$ poetry add pytest --group=test
$ poetry add pytest-mock --group=test  # モックを使ったユニットテスト
$ poetry add pytest-cov --group=test   # カバレッジの計測
$ poetry add pytest-html --group=test  # テスト結果をHTMLファイルに出力
```

`poetry`で管理している場合は``--group=test``に分類するとよいと思います。

- `uv`でインストール

```console
$ uv tool install pytest
$ uv tool install pytest-mock
$ uv tool install pytest-cov
```

`pipx`や`uv`を使ってシステム（の仮想環境）にインストールできます。

テスト結果をHTMLファイルに出力する場合は`pytest-html`のが必要です。
[unittest.mock](./python-unittest-mock.md)を使う場合は、
`pytest-mock`もインストールしておくとよいです。
カバレッジを計測した場合は`pytest-cov`が必要です。

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

## モックしたい

モック／パッチの作り方はまだわかっていないので、
ChatGPTに聞きながら書くことが多いです。

## ファイル書き込みをモックしたい（`pathlib.Path.write_text`）

```python
def 関数名(引数):
    p = Path("ファイル名")
    p.write_text("ファイルの内容", encoding="utf-8")
```

`pathlib.Path.write_text`を使っている関数のユニットテストを作成したときのサンプルです。
関数名や引数名は適当に置き換えて読んでください。

```python
from unittest.mock import patch

@path("pathlib.Path.write_text")
def test_関数名(mock_write):
    # test strings
    text = "ファイル内容"

    # run a function
    関数名(引数)

    # assertion
    # write_textが1回だけ呼ばれたことを確認
    mock_write.assert_called_once_with(text, encoding="utf-8")
```

`pathlib.Path.write_text`をモックします。
`write_text`は内部で`pathlib.Path.open`を使っていますが、
`mock_open`は必要ありません。

:::{note}

`open`関数を使う場合は`mock_open`が必要です。

:::

## HTTPリクエストをモックしたい（`requests.get`）

```python
def 関数名(引数):
    try:
        response = requests.get(url, params, timeout=30)
        response.raise_for_status()
        if response.ok:
            # ファイルに書き込む
            p = Path("ファイル名")
            p.write_text(response.text, encoding="utf-8")
        else:
            msg = "no response"
            raise ValueError(msg)
    except Exceptions as e:
        print(e)
```

`requests`モジュールを使ってURLにアクセスし、
レスポンス（のテキストデータ）をファイルに保存する処理をモックです。
前述したファイル処理のモックを組み合わせています。

```python
from unittest.mock import patch

@patch("pathlib.Path.write_text")
@patch("requests.get")
def test_関数名(mock_get, mock_write):
    # テスト用の文字列
    text = "レスポンスのテキストデータ"

    mock_get.return_value.ok = True
    mock_get.return_value.text = text

    関数名(引数)

    # GETリクエストの呼び出しを確認
    mock_get.assert_called_once_with(url, params, timeout=30)
    # ファイル書き込みの呼び出しを確認
    mock_write.assert_called_once_with(text, encoding="utf-8")
```

`requests.get`をモックします。
`return_value`を使って、テストしたい関数の中の処理で必要な値を設定しています。

また、前述のようにファイル保存の部分もモックしたいので、
`@patch`デコレーターを複数適用しています。
