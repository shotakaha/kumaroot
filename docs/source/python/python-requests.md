# HTTPしたい（`requests`）

```python
import requests

r = requests.get("https://example.com")
print(r)  # <Response [200]>
type(r)   # requests.models.Response
```

`requests`でウェブページのソースを取得できます。
取得した値は`requests.models.Response`オブジェクトに入っています。

## リクエストしたい（``get``）

```python
r = requests.get("https://example.com/get")
r = requests.head("https://example.com/get")
r = requests.options("https://example.com/get")
r = requests.post("https://example.com/post", data={"key": "value"})
r = requests.put("https://example.com/put", data={"key": "value"})
r = requests.delete("https://example.com/delete")

# リクエストしたURLを確認
r.url
```

HTTPのリクエストメソッドに対応したメソッドで、リクエストできます。
`url`プロパティでリクエストしたURLを確認できます。

## タイムアウトしたい（`timeout`）

```python
r = requests.get("URL", timeout=秒数)
```

`timeout`オプションで、リクエストのタイムアウト秒を設定できます。
サーバーからの応答がない場合に備えて、設定するとよいオプションです。

## クエリしたい（`params`）

```python
payload = {
    "key1": "value1",
    "key2": "value2",
    }
r = requests.get("URL", params=payload)

# クエリ付きのURLを確認
r.url
# URL?key1=value1&key2=value2
```

`get`メソッドの`params`オプションで、リクエストにクエリを追加できます。

## ヘッダーしたい（`headers`）

```python
headers = {"user-agent": "my-app/0.0.1"}
r = requests.get("URL", headers=user_agent)
```

`get`メソッドの`headers`オプションで、リクエストにヘッダーを追加できます。
ユーザーエージェントなどを設定できます。

```python
# 自作ツールの場合
headers = {"User-Agent": "ツール名/バージョン (ホームページ)"}
```

ユーザーエージェント情報は、だれからのアクセスかを示す情報です。
自作ツールの場合、上記のような形式が一般的な形式のようです。

```python
headers = {"User-Agent": "Mozilla/5.0 (OS情報) レンダリングエンジン ブラウザー名/バージョン Safari互換性/バージョン"}

# Google Chrome (v115.0) / WindowsPC
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

# Mozilla Firefox (v102.0) / WindowsPC
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}

# Safari (v16.0) / macOS13
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"}

# MS Edge (v114.0) / WindowsPC
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79"}
```

:`Mozilla/5.0`:
Netscape Navigatorとの互換性を示すための値。現在は、そのような効能はなく、慣例的に`Mozilla/5.0`と書かれているそうです。

:OS情報:
括弧内にOS名とバージョン情報を記述します。
WindowsPCの場合は`(Windows NT 10.0; Win64; x64)`、
macOSの場合は`(Macintosh; Intel Mac OS X 13_0)`
のようになります。

:レンダリングエンジン / Gecko互換性:
ブラウザで使用しているレンダリングエンジンの情報を記述します。
FireFoxでは`Gecko/バージョン`、
ChromeやSafariでは`AppleWebkit/バージョン (KHTML, like Gecko)`となります。

:ブラウザー情報:
ブラウザー名とバージョン情報を記述します。
FireFoxの場合は`Firefox/バージョン`、
Safariの場合は`Version/16.0`、
ChromeやChromeベースの場合は`Chrome/バージョン`、
Edgeの場合は`Edg/バージョン`と書くようです。

:Safari互換性:
WebKitベースのブラウザーのSafari互換性の情報を記述します。

ブラウザーのUA情報のサンプルと、記述されている項目を整理しました。

ただし、自作ツールでアクセス／スクレイピングするときに、
UA情報を偽装することは行儀がよくない作法だそうです。
（もしくは利用規約で禁止されてることもあるかもしれません）

## レスポンスのステータスを確認したい

```python
r = requests.get("URL")
r.ok           # True
r.status_code  # 200
r.reason       # 'OK'
```

`ok`プロパティで接続に成功したかどうかを確認できます。
レスポンスが成功（200（もしくは200番台？））の場合`True`になるので、
`if`文で判定するときに便利です。

```python
if r.ok:
    # SUCCESS時
    # 取得した内容をファイルに保存する
    p = Path("response.txt")
    with p.open("w, encoding="utf-8") as f:
        f.write(r.text)
else:
    msg = f"URL might be invalid or inaccessible. Status:{r.status_code} - {r.reason}"
    logger.warning(msg)
```

`status_code`でレスポンスのステータスコード、
`reason`で値の説明を確認できます。
接続に失敗したときの処理の表示に使えます。

`raise_for_status`でも同様の処理ができます（たぶん）。

## 例外処理したい（``RequestException``）

```python
URL = "https://example.com

try:
    response = requests.get(URL)
except requests.exceptions.RequestException as e:
    msg = f"Failed to connect URL: {URL}"
    logger.error(msg)
```

`requests.exceptions.RequestException`は、
requestsモジュールの例外クラスの親分です。

## レスポンスの内容を確認したい

```python
r.content  # バイナリで表示
r.text     # 文字列で表示
r.json()   # 辞書型
r.headers  # 辞書（みたいな）型
r.cookies  # 辞書（みたいな）型
```

エンコーディングが適切でないと``.text``メソッドは文字化けすることがあります。

## リファレンス

- [requests](https://requests.readthedocs.io/en/latest/)
- [httpx](https://www.python-httpx.org/)
- [urllib](https://docs.python.org/3/library/urllib.html)
