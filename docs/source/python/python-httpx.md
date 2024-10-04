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

## リファレンス

- [HTTPX](https://www.python-httpx.org/)
