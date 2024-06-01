# モックしたい（``unittest.mock``）

```python
from unittest.mock import MagicMock
```

## シリアル通信をモックしたい

:パッケージ名/daq.py:read_event:

```python
def read_event(port: serial.Serial) -> list[str]:
    data = port.readline().decode("UTF-8").strip().split()
    return data
```

:tests/test_daq_read_event.py:

```python
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

シリアル通信でデータを取得する場合に作成したモックです。
これは、検出器からの応答がスペース区切りの文字列になっている場合にテストしたものです。

``read_event``のユニットテストを作成する場合、接続がない状態でテストできるようにすると便利です。
そのために、``serial.Serial``オブジェクトを``MagicMock``します。

また``read_event``で``readline()``でデータを読み込んでいるため、
その関数／メソッドの返り値を、測定データを模した形式でモックしています。

実際の検出器からのデータは、ある程度ランダムな数値になるはずです。
そのため、値を検証するのではなく、得られたオブジェクトの型で検証することにしました。

:::{tip}

実際には``readline``の``return_value``を``FakeEvent``という自作クラスでモックしました。
``FakeEvent``は、測定データが取りうる範囲からランダムな値を返すクラスです。

:::

## ファイルをモックしたい

```python
from unittest.mock import MagicMock, mock_open
```

## リファレンス

- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
