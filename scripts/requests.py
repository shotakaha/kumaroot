# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# # HTTP操作モジュールの比較
#
# - `requests`: https://requests.readthedocs.io/en/latest/user/quickstart/
# - `httpx`: https://www.python-httpx.org/
# - `urllib.request`: https://docs.python.org/3/library/urllib.request.html#module-urllib.request

# リクエストを送るURLは``https://httpbin.org``にする。
# このサーバーは、HTTPリクエストとレスポンスの動作をテストするための無料のサービス。
#
# ``https://httpbin.org/get``はエコーサーバーになっていて、送信したHTTPリクエストの結果を、JSON形式のコンテンツで返してくれます。
# APIの開発やクライアントの挙動をデバッグする際に非常に便利です。

# TARGET_URL = "https://example.com"
TARGET_URL = "https://httpbin.org/get"


# インポート
#
# - `urllib.request`: 標準モジュール
# - `requests`: `poetry add requests --group dev`
# - `httpx`: `poetry add httpx --group dev`

# +
import urllib.request
import urllib.parse
import requests
import httpx
from pathlib import Path

print(f"{requests.__version__=}")
print(f"{httpx.__version__=}")

# -

# # リクエストの作成
#
# 基本となる`GET`メソッドで、URLをリクエストしてみます。
# `urllib`は`urlopen`関数を使います。
# `requests`と`httpx`は`get`関数を使います。

r_url = urllib.request.urlopen(TARGET_URL, timeout=5)
r_req = requests.get(TARGET_URL, timeout=5)
r_hpx = httpx.get(TARGET_URL, timeout=5)


# ## 結果を確認
#
# `urllib`はオブジェクトのアドレスが返ってくるので、実行結果がすぐにはわかりませんが、`requests`と`httpx`はオブジェクトを`print`するだけで実行結果が確認できます。

print(f"{r_url=}")
print(f"{r_req=}")
print(f"{r_hpx=}")


# オブジェクトの型を確認

print(f"{type(r_url)=}")
print(f"{type(r_req)=}")
print(f"{type(r_hpx)=}")


# 関数のシグネチャ
#
# ```python
# urllib.request.urlopen(
#     url,    # str or Requestオブジェクト
#     data=None,
#     timeout=<object object at 0x1022b4840>,
#     *,
#     cafile=None,      # CA情報
#     capath=None,      # CA情報
#     cadefault=False,  # ignored by default
#     context=None,     # ssl.SSLContext instance
# )
# ```
#
# ```python
# requests.get(
#     url,
#     params=None,   # dict
#     **kwargs,      # request(kwargs)
#     )
#
# requests.request(
#     method,    # str: ["GET", "OPTIONS", "HEAD", "POST", "PUT", "PATCH", "DELETE"]
#     url,
#     **kwargs,  # params, data, headers, cookies, timeout, cert,
#     )
# ```
#
# ```python
# httpx.get(
#     url: 'URL | str',
#     *,
#     params: 'QueryParamTypes | None' = None,
#     headers: 'HeaderTypes | None' = None,
#     cookies: 'CookieTypes | None' = None,
#     auth: 'AuthTypes | None' = None,
#     proxy: 'ProxyTypes | None' = None,
#     proxies: 'ProxiesTypes | None' = None,
#     follow_redirects: 'bool' = False,
#     cert: 'CertTypes | None' = None,
#     verify: 'VerifyTypes' = True,
#     timeout: 'TimeoutTypes' = Timeout(timeout=5.0),
#     trust_env: 'bool' = True,
# ) -> 'Response'
# ```

# # ヘッダーを操作したい
#
# - レスポンスのヘッダー確認する
# - リクエストにヘッダーを追加する

# ## レスポンスのヘッダーを確認する
#
# レスポンスで取得したオブジェクトにはヘッダー情報が含まれています。
# `urllib.request`は`r.headers.items()`、
# `requests`と`httpx`は`r.headers`で確認できます。

print(f"{r_url.headers.items()=}")
print(f"{r_req.headers=}")
print(f"{r_hpx.headers=}")


# ## リクエストにヘッダーを追加する
#
# `requests.get`と`httpx.get`は`headers`オプションで、ヘッダー情報を追加できます。
# `urllib.request`では`urllib.request.Request`オジェクトを作成し、`urlopen`に渡すことで、ヘッダー情報を追加できます。

# +
HEADERS = {"user-agent": "kumaroot-test/0.0.1"}

r = urllib.request.Request(url=TARGET_URL, headers=HEADERS, method="GET")
r_url = urllib.request.urlopen(r, timeout=5)
r_req = requests.get(TARGET_URL, headers=HEADERS, timeout=5)
r_hpx = httpx.get(TARGET_URL, headers=HEADERS, timeout=5)

# -

# 追加した情報は、それぞれのモジュールの`Request`オブジェクトで確認できる。

print(f"{r.headers=}")
print(f"{r_req.request.headers=}")
print(f"{r_hpx.request.headers=}")


# レスポンスには含まれない

print(f"{r_url.headers.items()=}")
print(f"{r_req.headers=}")
print(f"{r_hpx.headers=}")


# # クエリ操作したい
#
# - リクエストするときにクエリ（＝パラメーター）を追加したい
#
# `requests.get`と`httpx.get`は`params`オプションで追加できる。
# `urllib`モジュールでは、`urllib.parse.urlencode`でURLを作成し、`urlopen`または、`urllib.request.Request`に渡すことで追加できる。

# +
HEADERS = {"user-agent": "kumaroot-test/0.0.1"}
PARAMS = {"key1": "valu1", "key2": "value2"}

# クエリ付きURLの作り方は力づく
PARAMS_URL = TARGET_URL + "?" + urllib.parse.urlencode(query=PARAMS)
r = urllib.request.Request(url=PARAMS_URL, headers=HEADERS, method="GET")
r_url = urllib.request.urlopen(r, timeout=5)

r_req = requests.get(TARGET_URL, headers=HEADERS, params=PARAMS, timeout=5)
r_hpx = httpx.get(TARGET_URL, headers=HEADERS, params=PARAMS, timeout=5)

# -

print(f"{r_url.url=}")
print(f"{r_req.request.url=}")
print(f"{r_hpx.request.url=}")


# # ステータスを確認したい
#
# ``httpbin.org/status/ステータスコード``を使って、200番台（SUCCESS）以外の状態のレスポンスを確認できます。
# `urllib.request`は例外処理が必要です。
# `requests`と`httpx`は不要です。

# +
import urllib.request
import urllib.error

# TARGET_URL = "https://httpbin.org/status/200"
TARGET_URL = "https://httpbin.org/status/401"

try:
    r_url = urllib.request.urlopen(TARGET_URL, timeout=5)
except urllib.error.HTTPError as e:
    print(e)
    print(f"{e.url=}")
    print(f"{e.code=}")
    print(f"{e.reason=}")

r_req = requests.get(TARGET_URL, timeout=5)
r_hpx = httpx.get(TARGET_URL, timeout=5)

# -

# 例外処理が発生すると、`r_url`が生成されないため、以下は`requests`と`httpx`のレスポンスを確認する

print(f"{r_req.status_code=}")
print(f"{r_hpx.status_code=}")


print(f"{r_req.ok=}")
print(f"{r_hpx.is_success=}")


print(f"{r_url.reason=}")
print(f"{r_req.reason=}")
print(f"{r_hpx.reason_phrase=}")


# # レスポンスを確認
#
# - `r.text` : `str`
# - `r.content` : `bytes`
# - `r.json()` : `dict`

# +
TARGE_URL = "https://httpbin.org/get"

r_url = urllib.request.urlopen(TARGET_URL, timeout=5)
r_req = requests.get(TARGET_URL, timeout=5)
r_hpx = httpx.get(TARGET_URL, timeout=5)

# -

# ## `urllib.request`
#
# - `read()`: レスポンスのデータをbytes形式で一括で読み込む
# - `readline()`: レスポンスから1行ずつデータを読み込む
# - `readlines()`: レスポンスのすべての行をリスト型で読み込む
#
# これらの関数はデータを「ストリーム」で読み込むため、終端で空になる

# +
data = r_url.read()
content = data.decode("utf-8")

with open("content_urllib.txt", "w") as f:
    print(content)
    f.write(content)


# +
content = r_req.text

with open("content_requests.txt", "w") as f:
    print(content)
    f.write(content)


# +
r_hpx.encoding = "utf-8"
content = r_hpx.text

with open("content_httpx.txt", "w") as f:
    print(content)
    f.write(content)

# -

# # 実際のユースケースで確認

# +
DUMMY_URL = "https://docs.google.com/spreadsheets/d/16Sc_UgShNuxMfRnBiFsjmfThE1VfVhJf3jgmxNvFeEI/edit?gid=0#gid=0"
EXPORT_URL = "https://docs.google.com/spreadsheets/d/16Sc_UgShNuxMfRnBiFsjmfThE1VfVhJf3jgmxNvFeEI/export?gid=0&format=csv"

BASE_URL = "https://docs.google.com/spreadsheets/d/16Sc_UgShNuxMfRnBiFsjmfThE1VfVhJf3jgmxNvFeEI/export"
PARAMS = {"gid": "0", "format": "csv"}


# +
# クエリ付きURLの作り方は力づく
PARAMS_URL = BASE_URL + "?" + urllib.parse.urlencode(query=PARAMS)
r = urllib.request.Request(url=PARAMS_URL, headers=HEADERS, method="GET")
r_url = urllib.request.urlopen(r, timeout=5)

r_req = requests.get(BASE_URL, headers=HEADERS, params=PARAMS, timeout=5)
# r_req.encoding = "utf-8"

r_hpx = httpx.get(
    BASE_URL, headers=HEADERS, params=PARAMS, timeout=5, follow_redirects=True
)
# r_hpx.encoding = "utf-8"


# +
data = r_url.read()
content = data.decode("utf-8")
p = Path("content_urllib.csv")
p.write_text(content, encoding="utf-8")
print(f"saved {p}")

###

p = Path("content_requests.csv")
p.write_text(r_req.text, encoding="utf-8")
print(f"saved {p}")

###

p = Path("content_httpx.csv")
p.write_text(r_hpx.text, encoding="utf-8")
print(f"saved {p}")

