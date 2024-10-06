# HTTPしたい（`httpx`）

```python
import httpx

try:
    r = httpx.get("https://httpbin.org/get")
    r.raise_for_status()
    print(f"{r.status_code}: {r.reason_phrase}")
except Exceptions as e:
    print(f"error: {e}")
```

`httpx`でウェブページのソースを取得できます。
非同期（`async`）に対応しています。
[requests](./python-requests.md)の操作感と同じなので、移行もしやすいです。

## モックしたい（`@patch(httpx.get)`）

```python
from unittest.mock import patch

@patch("pathlib.Path.write_text")
@patch("httpx.get")
def test_httpx(mock_get, mock_write):
    # テスト用の文字列
    text_data = "モックしたテキストデータ"

    # response.is_success の返り値をモック
    # response.text の返り値をモック
    mock_get.return_value.is_success = True
    mock_get.return_value.text = text_data


    関数(引数)
    # 内部で requests.get している関数
    #   response = httpx.get(url="URL", follow_redirects=True)
    #   p = Path("ファイル名")
    #   p.write_text(response.text)

    # httpx.get の呼び出しを確認
    mock_get.assert_called_once_with(url="URL", follow_redirects=True)
    # Path.write_text の呼び出しを確認
    mock_write.assert_called_once_with(text_data)
```

`httpx.get`でGETリクエストして取得したレスポンス（＝テキストデータ）を
`Path.write_text`でファイルに保存する関数のユニットテストのサンプルです。

関数のロジックを確認するためのユニットテストの場合、
実際にGETリクエストを発生させたり、
ファイルを作成したりする必要はありません。

`httpx.get`と`pathlib.Path.write_text`をモックし、
`assert_called_once_with(引数)`で、
それぞれの関数が適切な引数で呼び出されたことを確認しています。

## リファレンス

- [HTTPX](https://www.python-httpx.org/)
