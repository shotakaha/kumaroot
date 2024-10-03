---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: 'Python 3.10.8 (''.venv'': poetry)'
  language: python
  name: python3
---

---
title: 日時したい（pendulum）
subject: python
keywords: [python, pendulum, time, datetime]
authors: [Shota Takahashi]
exports:
  - format: pdf
---

+++ {"part": "abstract"}

Python標準モジュールの``time``と``datetime``、
そして外部モジュールの``pendulum``を使って、
よくある日時の取り扱いを比べてみました。

+++

``time``と``datetime``は標準モジュールなので、そのまま読み込めます。
``pendulum``は``pip``などを使ってあらかじめ追加しておきます。
今回は最新版のv3系を使いました。

```{code-cell} ipython3
import time
import datetime
import pendulum

pendulum.__version__
```

# 現在時刻を取得したい

スクリプトを実行した時刻など、現在時刻を取得したい場合はよくあります。
現在時刻は、以下のメソッドで取得できます。

1. ``datetime.datetime.now``
2. ``pendulum.now``
3. ``pendulum.from_timestamp``

+++

## datetime

``datetime``モジュールを使う方法です。
これで取得できるのは、タイムゾーン情報が含まれていない`tz-naive`な日時オブジェクトです。

```{code-cell} ipython3
# tz-naiveなローカルタイムを取得
dt = datetime.datetime.now()
print(dt)
dt
```

`astimezone`で、タイムゾーン情報を追加した`tz-aware`な日時オブジェクトを取得できます。
タイムゾーン情報は、システムのタイムゾーンを参照します。

```{code-cell} ipython3
# tz-awareなローカルタイムを取得
# パソコンのタイムゾーン情報を利用
dt = datetime.datetime.now().astimezone()
print(dt)
dt
```

``datetime.datetime.now``の引数に``datetime.timezone``を指定して、任意のタイムゾーン情報を持たせることができます。
タイムゾーン情報には、任意の名前をつけることもできます。

以下では、日本標準時（JST / UTC+09:00）を設定しています。

```{code-cell} ipython3
# JSTを自分で定義
# JST: UTC+09:00
jst = datetime.timezone(datetime.timedelta(hours=9), "Asia/Tokyo")
dt = datetime.datetime.now(jst)
print(dt)
dt
```

日時オブジェクトは世界標準時（UTC時刻）に変換できます。
複数のタイムゾーン情報を扱う場合は、UTC時刻で揃えておくと便利かもしれません。
世界標準時は`datetime.UTC`で指定できます。

```{code-cell} ipython3
# 現在のローカルタイムを、UTCに変換
# UTC+09:00 で取得した日時を UTC+00:00 に変換
# i.e. -9h された時刻が取得できる
dt = datetime.datetime.now(datetime.UTC)
print(dt)
dt
```

## pendulum

``pendulum``はデフォルトでタイムゾーン情報を持った日時オブジェクトを作成します。

```{code-cell} ipython3
dt = pendulum.now()
print(dt)
dt
```

```{code-cell} ipython3
dt.format("YYYY-MM-DDTHH[h]mm[m]ss[s]SSSSSS[us]Z")
```

``time.time()``で現在のUNIX時間を取得できます。
``pendulum.from_timestamp``を使って``DateTime``オブジェクトに変換できます。

```{code-cell} ipython3
ut = time.time()
dt = pendulum.from_timestamp(ut)
print(ut)
print(dt)
dt
```

## datetime -> pendulum

``datetime.datetime.now``で取得した日時オブジェクトは、``pendulum.instance()``で``DateTime``オブジェクトに変換できます。
もとの日時オブジェクトがタイムゾーン情報を持たない場合は``UTC``に変換されます。
タイムゾーン情報を持つ場合は、時間差情報が追加されます。

```{code-cell} ipython3
# tz-naiveな日時オブジェクト
# UTC時刻として扱われる
lt = datetime.datetime.now()
dt = pendulum.instance(lt)
print(lt)
print(dt)
dt
```

```{code-cell} ipython3
# tz-awateな日時オブジェクト
lt = datetime.datetime.now().astimezone()
dt = pendulum.instance(lt)
print(lt)
print(dt)
dt
```

```{code-cell} ipython3
# 任意のタイムゾーンを指定
lt = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=4)))
dt = pendulum.instance(lt)
print(lt)
print(dt)
dt
```

# 文字列から日付オブジェクトしたい

```{code-cell} ipython3
date_string = "2024-09-10T22:18:34"
```

```{code-cell} ipython3
datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
```

```{code-cell} ipython3
datetime.datetime.fromisoformat(date_string)
```

1. ``datetime.datetime``
2. ``pendulum.datetime``
3. ``pendulum.local``

+++

``(年, 月, 日, 時, 分, 秒, マイクロ秒)``のタプルを与えて、任意の日時オクジェクトを作成できます。
``datetime``モジュールはタイムゾーン情報を持たないため、``tz-naive``なオブジェクトが作成されます。

```{code-cell} ipython3
dt = datetime.datetime(2024, 1, 2, 3, 45, 56)
print(dt)
dt
```

同様のタプルを``pendulum.datetime``に与え、タイムゾーン情報を持った``tz-aware``なオブジェクトが作成できます。
デフォルトでは``UTC``が設定されます。``tz="Asia/Tokyo``オプションを追加すると、日本時刻として作成できます。

```{code-cell} ipython3
dt = pendulum.datetime(2024, 1, 2, 3, 45, 56)
print(dt)
dt
```

``pendulum.local``を使うと、実行環境のタイムゾーンを持った日時オブジェクトが作成できます。
これは``pendulum.datetime(tz="local")``のエイリアスです。

```{code-cell} ipython3
dt = pendulum.local(2024, 1, 2, 3, 45, 56)
print(dt)
dt
```

# 日付を変換したい

ある日時オブジェクトを、別の並びの文字列に変換したいことがあります。
たとえばRSSフィードの日時は``曜日（短縮）, 日 月名（短縮） 年 時:分:秒 +Z``であったり、
ISO8601形式の日時は``年-月-日T時:分:秒+Z``であったりします。

``datetime``モジュールの場合、変換後の文字列は自分で指定する必要があります。
``pendulum``パッケージの場合、よく使われる日時の文字列はプリセットされています。
なるべくプリセットされたものを使うのがよいでしょう。

```{code-cell} ipython3
# RSS形式
dt = datetime.datetime(2024, 1, 2, 3, 45, 56)
dt.strftime("%a, %d %b %Y %H:%M:%S")
```

```{code-cell} ipython3
# ISO8601形式
dt = datetime.datetime(2024, 1, 2, 3, 45, 56)
dt.strftime("%Y-%m-%dT%H:%M:%S")

now = datetime.datetime.now().astimezone()
now.strftime("%Y-%m-%dT%H:%M:%S.%f%z")
```

```{code-cell} ipython3
# RSS形式
dt = pendulum.local(2024, 1, 2, 3, 45, 56)
dt.to_rss_string()
```

```{code-cell} ipython3
# ISO8601形式
dt = pendulum.local(2024, 1, 2, 3, 45, 56)
dt.to_iso8601_string()
```

```{code-cell} ipython3
# ISO8601形式
dt = pendulum.local(2024, 1, 2, 3, 45, 56)
dt.isoformat()
```

# 日付を読み込みたい

すでに保存されたデータから日付を読み込み日時オブジェクトに変換したい場合もよくあります。

1. ``datetime.datetime.strptime``
2. ``pendulum.from_format``
3. ``pendulum.parse``

```{code-cell} ipython3
timestamp = "2024-01-02 03:45:56"
apache_time = "01/Sep/2012:06:05:11 +0000"
```

``datetime``モジュールでは、``datetime.datetime.strptime``を使っいます。

```{code-cell} ipython3
datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
```

```{code-cell} ipython3
datetime.datetime.strptime(apache_time, "%d/%b/%Y:%H:%M:%S +0000")
```

``pendulum``パッケージでは``pendulum.from_format``を使います。
日時の指定子が``datetime``モジュールと異なる点に注意してください。
利用可能な日付トークンは https://pendulum.eustace.io/docs/#tokens で確認できます。

```{code-cell} ipython3
pendulum.from_format(timestamp, "YYYY-MM-DD HH:mm:ss")
```

```{code-cell} ipython3
pendulum.from_format(apache_time, "DD/MMM/YYYY:HH:mm:ss ZZ")
```

```{code-cell} ipython3
pendulum.from_format(timestamp, "YYYY-MM-DD HH:mm:ss", tz="local")
```

```{code-cell} ipython3
pendulum.from_format(apache_time, "DD/MMM/YYYY:HH:mm:ss ZZ", tz="local")
```

``pendulum.parse``で一般的な日付フォーマットをパースできます。
タイムゾーンが指定されていない場合は、``UTC``になります。

```{code-cell} ipython3
pendulum.parse(timestamp)
```

```{code-cell} ipython3
pendulum.parse(timestamp, tz="local")
```
