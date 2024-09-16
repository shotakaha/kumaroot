# HTTPしたい（`requests`）

```python
import requests

r = requests.get("https://httpbin.org/get", timeout=10)
print(r)  # <Response [200]>
type(r)   # requests.models.Response
```

`requests`でウェブページのソースを取得できます。
取得した値は`requests.models.Response`オブジェクトに入っています。

:::{hint}

[https://httpbin.org](https://httpbin.org)は、
HTTP通信のリクエストとリスポンスの動作テストができる無料のサービスです。
基本的にはエコーサーバーとなっていて、
自分が送ったリクエストの内容を
JSON形式のレスポンスとして受け取ることができます。
APIの開発や、クライアントツールの挙動をデバッグするのに便利です。

:::

## リクエストしたい（``get``）

```python
r = requests.get("https://httpbin.org/get")
r = requests.head("https://httpbin.org/get")
r = requests.options("https://httpbin.org/get")
r = requests.post("https://httpbin.org/post", data={"key": "value"})
r = requests.put("https://httpbin.org/put", data={"key": "value"})
r = requests.delete("https://httpbin.org/delete")

# リクエストしたURLを確認
r.url
```

HTTPのリクエストメソッドに対応したメソッドで、リクエストできます。
`url`プロパティでリクエストしたURLを確認できます。

## レスポンスしたい（``text``）

```python
r = requests.get("https://httpbin.org/get")

r.text     # str
r.content  # bytes
r.json()   # 辞書型
r.headers  # 辞書（みたいな）型
r.cookies  # 辞書（みたいな）型
```

HTMLのソースなどの文字データの場合、`text`メソッドで確認できます。
画像をリクエストした場合は、`content`メソッドでバイナリ形式のデータを確認できます。
REST APIのようにJSON形式のレスポンスは`json()`メソッドで確認できます。

## レスポンスを保存したい

```python
r = requests.get("https://example.com")
content = r.text
p = Path("output.html")

with p.open("w", encoding="utf-8") as f:
    f.write(content)
```

テキスト形式のレスポンスは、通常のファイル出力を使って保存できます。
保存時のエンコーディングは必要に応じて指定してください。

:::{note}

HTML形式のレスポンスを取得した場合、`charset`の値からエンコーディングを自動で判別するみたいです。
自動判別できなかった場合は、デフォルトの`ISO-8859-1`（Latin-1）になってしまいます。
日本語を含んだレスポンスの場合は、文字化けするため、エンコーディングは指定しておく方がよいでしょう。

:::

## タイムアウトしたい（`timeout`）

```python
# requests.get("URL", timeout=秒数)
r = requests.get("URL", timeout=10)
```

`timeout`オプションで、リクエスト時のタイムアウト秒（＝待機時間）を設定できます。
デフォルトでは値が設定されていないため、必ず設定したほうがよいと思います。
設定した待機時間を過ぎてもサーバーからの応答がない場合は`TimeoutError`になります。

## クエリしたい（`params`）

```python
params = {
    "key1": "value1",
    "key2": "value2",
    }
r = requests.get("URL", params=params)

# クエリ付きのURLを確認
r.url
# URL?key1=value1&key2=value2
```

`params`オプションで、リクエスト時にクエリを追加できます。
クエリは辞書型で用意します。

## ヘッダーしたい（`headers`）

```python
headers = {"user-agent": "my-app/0.0.1"}
r = requests.get("URL", headers=headers)
```

`headers`オプションで、リクエストにヘッダーを追加できます。
ユーザーエージェントなどを設定できます。

```python
# 自作ツールの場合
headers = {"User-Agent": "ツール名/バージョン (ホームページ)"}
```

ユーザーエージェント情報は、だれからのアクセスかを示す情報です。
自作ツールの場合、上記のような形式が一般的な形式のようです。

## レスポンスのステータスを確認したい

```python
r = requests.get("https://httpbin.org/status/200")
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
URL = "https://httpbin.org/status/404"

try:
    response = requests.get(URL)
except requests.exceptions.RequestException as e:
    msg = f"Failed to connect URL: {URL}"
    logger.error(msg)
```

`requests.exceptions.RequestException`は、
requestsモジュールの例外クラスの親分です。

## ユーザーエージェント情報

```python
headers = {"User-Agent": "Mozilla/5.0 (OS情報) レンダリングエンジン ブラウザー名/バージョン Safari互換性/バージョン"}
```

上記のサンプルは、ユーザーエージェント情報のテンプレートです。
記述されている項目は以下の整理しました。

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

### 具体例

以下に、UA情報のサンプルを整理しました。
ただし、UA情報を偽装することは行儀がよくない作法だそうです。
なかには利用規約で禁止されてることもあるようです。

- Google Chrome (v115.0) / WindowsPC

```python
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
```

-  Mozilla Firefox (v102.0) / WindowsPC

```python
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}
```

- Safari (v16.0) / macOS13

```python
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"}
```

- MS Edge (v114.0) / WindowsPC

```python
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79"}
```

## リファレンス

- [requests](https://requests.readthedocs.io/en/latest/)
- [httpx](https://www.python-httpx.org/)
- [urllib](https://docs.python.org/3/library/urllib.html)
