# モックしたい（``unittest.mock``）

```python
from unittest.mock import MagicMock
```

## シリアル通信をモックしたい（``MagicMock``）

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
ファイルが開けたかどうか、``read``／``write``処理が想定回数呼び出せたかどうか、などでアサートできます。

ここでは``@patch``デコレータで、``pathlib.Path.open``をモックしています。
この関数のスコープの中で呼ばれる``open``間数は、``mock_open``に置き換えられます。

``mock_open``も``MagicMock``と同じように関数／メソッドを呼び出した回数を記録しています。
そのため``関数名.call_count``でアサートできます。

## リファレンス

- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
