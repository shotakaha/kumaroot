# requests

```python
import requests

r = requests.get("URL")
```

ウェブページのソースを取得するには[requests](https://requests.readthedocs.io/en/latest/)モジュールを使います。
[Beautiful Soup 4](https://beautiful-soup-4.readthedocs.io/en/latest/)を組み合わせて使う場合が多いです。

## リクエストしたURLを確認したい

```python
r.url
```

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
