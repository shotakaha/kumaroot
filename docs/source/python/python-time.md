# 時刻したい（`time`）

```python
import time

# Get unixtime (since epoch 1970-01-01)
ut = time.time()

# Convert to unixtime to local time (= struct_time)
now = time.localtime(ut)

# Convert struct_time to string
timestamp = time.strftime("%Y-%m-%d %H:%M:%S", now)
```

`time`モジュールは、時間を操作できる標準ライブラリです。
`time.sleep`で処理を一時停止する場合に使います。

:::{note}

日付を操作したい場合は、
[datetime](./python-datetime.md)、
[pendulaum](./python-pendulum.md)、
が適しています。

:::

## 一時停止したい（`time.sleep`）

```python
# sleep for 0.5 seconds
time.sleep(0.5)
```

`time.sleep`で一時停止できます。
時間は秒で指定します。

## 時間差を計測したい（`time.monotonic` / `time.monotonic_ns`）

```python
# Get start time position
started = time.monotonic()

# Run main process
for i in range(10000000000):
    pass

# Get stopped time position
stopped = time.monotonic()
elapsed = stopped - started
```

`time.monotonic`は、単調増加する時間カウンターです。
絶対に後戻りすることがないため、経過時間の計測に適しています。

```python
timeout = 5
started = time.monotonic()

while True:
    if time.monotonic() - started > timeout:
        print("timeout")
        break
```

タイムアウト処理やリトライ処理に利用できます。

:::{note}

`time.time`で取得できる時刻情報は、パソコンのシステム時刻に依存します。
NTP同期や手動で時計が変更された場合、時刻が前後にずれることがあります。
このような場合、`end - start`で計算した経過時間が負の値になる可能性があります。

一方で、`time.monotonic`は、絶対に後戻りしない時間カウンターです。
単一の値に意味はなく「時間差（経過時間）」にのみ意味があります。
システム時刻の変更の影響を受けないため、経過時間が負になることはありません。

プロセスの経過時間やタイムアウト計測には`time.monotonic`を使うべきです。

:::

## 精密計測したい（`time.perf_counter`）

```python
# Get started time (in unixtime)
started = time.perf_counter()

# Run main process
for i in range(10000000000):
    pass

# Get stopped time
stopped = time.perf_counter()
elapsed = stopped - started
```

`time.perf_counter`で精度が高い時刻を取得できます。
