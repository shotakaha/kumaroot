# モックしたい（``unittest.mock``）

```python
from unittest.mock import MagicMock
from unittest.mock import patch
from unittest.mock import mock_open
```

`unittest`はPythonの標準モジュールです。
`unittest.mock`は、そこに含まれているモック用のモジュールです。

:::{note}

ユニットテストに[pytest](./python-pytest.md)を使っている場合は、`pytest-mock`を使うとよいです。

:::

## MagicMockしたい（``MagicMock``）

```python
from unittest.mock import MagicMock

mock = MagicMock()
mock.メソッド名.return_value = 返り値
mock.メソッド名.return_value = [返り値]
```

`MagicMock`でモック用のオブジェクトを作成できます。
モックは**万能の空箱**のようなイメージで、任意のメソッドを追加して、その返り値を設定できます。

:::{hint}

ユニットテストを作成するとき、どの部分をモックするかを考えることが重要です。
経験が圧倒的に不足していて悩んでいましたが、最近では、ChatGPTに聞きながら作っています。

:::

## パッチしたい（`@patch`）

```python
from unittest.mock import patch

@patch("モジュール名.クラス名")
def test_テスト関数(モック名):
    """ユニットテストの説明"""
    # テストを書く
    # モック名.メソッド名.return_value = モック値
```

``@patch``デコレーターで引数に指定した関数をモックできます。

## 複数パッチしたい（``@patch``）

```python
# @デコレーターの順番と引数の順番の対応に注意
@patch("モジュール名.クラス名3")  # => モック名3 で受け取る
@patch("モジュール名.クラス名2")  # => モック名2 で受け取る
@patch("モジュール名.クラス名1")  # => モック名1 で受け取る
def test_テスト関数(モック名1, モック名2, モック名3):
    """複数のモックを使ったテスト"

    モック名1.メソッド名.return_value = ...
    モック名2.メソッド名.return_value = ...
    モック名3.メソッド名.return_value = ...
```

ひとつのテスト関数に、複数の``@patch``デコレーターを使用できます。
テスト用の関数の引数で、それぞれのモックを受け取ることができます。
デコレーターの順番と引数の順番の対応に注意が必要です。

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

## シリアル通信をモックしたい（``MagicMock``）

```{code-block} python
---
caption: パッケージ名/daq.py:read_event
---
def read_event(port: serial.Serial) -> list[str]:
    data = port.readline().decode("UTF-8").strip().split()
    return data
```

```{code-block} python
---
caption: tests/test_daq_read_event.py
---
from unittest.mock import MagicMock
from .daq import read_event

def test_daq_read_event():
    # Arrange: モックを作成
    mock_port = MagicMock
    mock_port.readline().decode.return_value = "値1 値2 値3 値4"

    # Act: データ読み込みを実行
    data = read_event(port)

    # Assert: 型の一致を確認
    assert isinstance(data, list)
```

シリアル通信でデータを取得するための`read_event`という関数のテストです。

``read_event``では、PySerial（`serial.Serial`）を使ってシリアル通信をしていますが、ユニットテストでは接続がない状態で確認できるようにしたいです。
そのために`MagickMock`で``serial.Serial``オブジェクトをモックしています。

また``read_event``では``readline()``でデータを取得しています。
検出器が返すデータ形式がスペース区切りの文字列になっているため
``mock_port.readline().decode.return_value = "値1 値2 ..."``としています。

ただし、実際の検出器からのデータは、ある程度ランダムな数値です。
そのため、返ってくる値そのものを検証する意味はありません。
ここでは、得られたオブジェクトの型が正しいかどうかで検証することにしました。

:::{tip}

実際の改良として``FakeEvent``クラスを作成し、
``mock_port.readline().decode.return_value = FakeEvent().to_tsv_string()``でモックしました。
``FakeEvent``クラスは、擬似データを生成するためのクラスで、測定データが取りうる範囲からランダムな値を返します。

:::

## ファイル処理をモックしたい（``mock_open``）

```python
from unittest.mock import MagicMock, mock_open

@patch("pathlib.Path.open", new_callable=mock_open)
def test save_events(mock_open):
    # Arrange: ファイルをモック
    fname = Path("remove_this_file_if_exists.csv")

    # Act: ファイルを開き、データを追記する
    n = 5
    events = []
    with fname.open("x") as f:
        for _ in range(n):
            event = read_event(port)  # 上でモックした値
            f.write(event + "\n")
            events.append(event)

    # Assert
    ## 取得したイベント数を確認
    assert len(events) == n

    ## ファイルを開いたモードと回数を確認
    mock_open.assert_called_once_with("x")

    ## writeが呼ばれた回数を確認
    handle = mock_open()
    assert handle.write.call_count == n
```

``mock_open``で、実際にファイルを作ったり、書き込んだりせずに、ファイル処理をテストできます。
ファイルは作成されないので、
ファイルが開けたかどうか、``read``／``write``処理が想定回数呼び出せたかどうか、などでアサートします。

このサンプルでは``@patch``デコレータで、``pathlib.Path.open``をモックしています。
この関数のスコープの中で呼ばれる``open``関数は、``mock_open``に置き換えられています。

``mock_open``も``MagicMock``と同じように関数／メソッドを呼び出した回数を記録しています。
そのため``関数名.call_count``でアサートできます。

## HTTPリクエストをモックしたい

- [](./python-requests.md)
- [](./python-httpx.md)

## リファレンス

- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
