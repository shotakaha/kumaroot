# HTTPしたい（`requests`）

```python
import requests

r = requests.get("URL")
print(r)  # <Response [200]>
type(r)   # requests.models.Response
```

`requests`でウェブページのソースを取得できます。
取得した値は`requests.models.Response`オブジェクトに入っています。

## リクエストしたURLを確認したい

```python
r = requests.get("URL")
r.url
```

`url`プロパティでリクエストしたURLを確認できます。

## レスポンス確認したい

```python
r = requests.get("URL")
r.ok           # True
r.status_code  # 200
r.reason       # 'OK'
```

`ok`で接続に成功したかどうかを確認できます。
レスポンスが成功（200（もしくは200番台？））の場合`True`になるので、
`if`文で判定するときに便利です。

`status_code`でレスポンスのステータスコード、
`reason`で値の説明を確認できます。
接続に失敗したときの処理の表示に使えます。

## 接続確認したい（``RequestException``）

```python
URL = "https://example.com

try:
    response = requests.get(URL)
except requests.exceptions.RequestException as e:
    msg = f"Failed to connect URL: {URL}"
    logger.error(msg)
```

`requests.exceptions.RequestException`で
指定したURLにアクセスできない場合などの例外処理できます。

## 取得したコンテンツを確認したい

```python
r.content  # バイナリで表示
r.text     # 文字列で表示
```

エンコーディングが適切でないと``.text``メソッドは文字化けすることがあります。

## エンコーディングを確認したい

```python
r.encoding
r.apparent_encoding
```

## リファレンス

- [requests](https://requests.readthedocs.io/en/latest/)
