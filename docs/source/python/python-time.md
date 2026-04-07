# 時刻したい（`time`）

```python
import time

# Get unixtime (since epoch 1970-01-01)
ut = time.time()

# Convert to unixtime to local time (struct_time)
now = time.localtime(ut)

# Convert struct_time to string
timestamp = time.strftime("%Y-%m-%d %H:%M:%S", now)
```

`time`モジュールは、時間を操作できる標準ライブラリです。
`time.sleep`で処理を一時停止する場合に使います。

:::{note}

日付を操作したい場合は、
[datetime](./python-datetime.md)、
[pendulum](./python-pendulum.md)、
が適しています。

:::

## 一時停止したい（`time.sleep`）

```python
# sleep for 0.5 seconds
time.sleep(0.5)
```

`time.sleep`で一時停止できます。
時間は秒で指定します。

## 経過時間したい（`time.monotonic` / `time.monotonic_ns`）

```python
# Get start time position
started = time.monotonic()

# Run main process
for i in range(100):
    # something to do
    time.sleep(0.1)  # simulate worklaod

# Get stopped time position
stopped = time.monotonic()
elapsed = stopped - started
```

`time.monotonic`は、単調増加する時間カウンターです。
絶対に後戻りすることがないため、経過時間の計測に適しています。

:::{note}

`time.time`で取得できる時刻情報は、パソコンのシステム時刻に依存します。
NTP同期や手動で時計が変更された場合、時刻が前後にずれることがあります。
このような場合、`end - start`で計算した経過時間が負の値になる可能性があります。

一方で、`time.monotonic`は、絶対に後戻りしない時間カウンターです。
単一の値に意味はなく「時間差（経過時間）」にのみ意味があります。
システム時刻の変更の影響を受けないため、経過時間が負になることはありません。

プロセスの経過時間やタイムアウト計測には`time.monotonic`を使うべきです。

:::

```python
timeout = 5
interval = 0.01
deadline = time.monotonic() + timeout

while True:
    now = time.monotonic()

    if now >= deadline:
        print("timeout")
        # handle timeout (break / raise / retry)
        break

    # something todo

    # avoid busy loop (reduce CPU usage)
    # sleep up to interval, but not beyond the deadline
    remaining = deadline - now
    time.sleep(min(interval, remaining))
```

タイムアウト処理やリトライ処理に利用できます。
ループ処理の直前で〆切時刻（`deadline`）を設定し、
ループ内で現在時刻と比較することで、タイムアウトを判定します。

:::{note}

上記サンプルでは、〆切直前にスリープ時間を調整する処理を追加し、
タイムアウト検知の遅延を抑えています。
スリープ時間（`interval`）が長いほど、タイムアウト検知が遅れるので、
この調整は重要です。

:::

## 高精度で計測したい（`time.perf_counter`）

```python
# Get started time position
started = time.perf_counter()

# Run main process
for i in range(10000000000):
    pass

# Get stopped time position
stopped = time.perf_counter()
elapsed = stopped - started
```

`time.perf_counter`で精度が高い時刻を取得できます。
