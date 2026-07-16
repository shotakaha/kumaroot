# 時刻したい（`time`）

```python
import time

# UNIX時間を取得（1970-01-01からの経過秒数）
ut = time.time()

# UNIX時間をローカル時刻（struct_time）に変換
now = time.localtime(ut)

# struct_timeを文字列に変換
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
# 0.5秒待機
time.sleep(0.5)
```

`time.sleep`で一時停止できます。
時間は秒で指定します。

## 経過時間したい（`time.monotonic` / `time.monotonic_ns`）

```python
# 計測開始
started = time.monotonic()

# メイン処理を実行
for i in range(100):
    # なんらかの処理
    time.sleep(0.1)  # workloadを模擬

# 計測終了
stopped = time.monotonic()
elapsed = stopped - started
```

`time.monotonic`は、単調増加する時間カウンターです。
絶対に後戻りすることがないため、経過時間の計測に適しています。

`time.monotonic_ns`は、同じ性質をもつナノ秒精度の整数版です。
浮動小数点の誤差を避けたい場合や、より高い精度が必要な場合に使います。

```python
started = time.monotonic_ns()
# ...
elapsed_ns = time.monotonic_ns() - started
```

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
        # タイムアウト時の処理（break / raise / retryなど）
        break

    # なんらかの処理

    # ビジーループを避ける（CPU使用率を下げる）
    # 〆切を超えない範囲でintervalだけ待機する
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
# 計測開始
started = time.perf_counter()

# メイン処理を実行
for i in range(1000000):
    pass

# 計測終了
stopped = time.perf_counter()
elapsed = stopped - started
```

`time.perf_counter`で精度が高い時刻を取得できます。
`time.monotonic`と同様、ナノ秒精度の整数を返す`time.perf_counter_ns`もあります。

:::{note}

`time.perf_counter`は、スリープ中の時間も含めた「実時間（wall clock time）」を計測します。
CPUが実際に処理に使った時間（スリープ中を除く）だけを知りたい場合は、
`time.process_time`を使ってください。

:::
