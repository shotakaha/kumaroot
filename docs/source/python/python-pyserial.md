# シリアル通信したい（`pyserial`）

```python
import serial

# ポート名と通信速度を指定して接続
with serial.Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=1) as device:
    # デバイスからデータを読み込む
    line = device.readline().decode("utf-8").strip()
    print(line)
```

`pyserial`パッケージでパソコンとマイコンなどをUSBで接続して、データをやり取りできます。
ポート名（`/dev/ttyUSB0`や`COM1`など）と通信速度（`baudrate`）を指定してセッションを開きます。
`with`構文を使うと、接続や切断が自動で管理されるので安全です。

:::{note}

**シリアル通信について：** シリアル通信は、データを1ビットずつ順番に送る方式です。マイコンやIoT機器との通信に使われます。

**設定オプションについて：**

- **baudrate（通信速度）**：1秒間に送信するビット数です。デバイスと同じ速度に合わせる必要があります。一般的な値は9600、115200などです。デバイスのドキュメントを確認して設定してください。

- **timeout（タイムアウト）**：データ受信を待つ最大時間（秒）です。`timeout=1`と設定すると、1秒間データがなければ`None`を返します。受信ループで無限に待つのを防ぐためにあります。`timeout=None`にすると無限に待ちます。

- **parity（パリティ）**：データの誤り検出方式です。デフォルト値は`PARITY_NONE`（パリティなし）で問題ありません。デバイスが要求する場合のみ変更してください。

- **stopbits（ストップビット）**：データフレームの終わりを示すビット数です。デフォルト値は1で問題ありません。

- **bytesize（データビット）**：1フレームあたりのビット数です。デフォルト値は8です。デバイスが特別な要求をしない限り変更しなくてOKです。

- **rtscts（フロー制御）**：ハードウェアフロー制御の有効/無効です。デフォルト値は`False`です。USBシリアルでは通常不要です。

- **dsrdtr（フロー制御）**：別のハードウェアフロー制御オプションです。デフォルト値は`False`で問題ありません。

**基本的にはデフォルト値でOK：** ほとんどの場合、`baudrate`と`timeout`を指定するだけで十分です。その他のオプションはデバイスのドキュメントに特別な指定がある場合のみ変更してください。

:::

## インストールしたい（`pyserial`）

- `uv pip`でインストール

```console
$ uv pip install pyserial
```

モジュール名は`serial`ですが、パッケージ名は`pyserial`です。

- `pip`でインストール

```console
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install pyserial
```

## 読み出したい（`readline`）

```python
# 受信（パソコン ← デバイス）
# バイト列から文字列に変換
line = device.readline().decode("utf-8").strip()
```

`readline`メソッドで接続先のデバイスからデータを読み出します。
データはバイト型で送られてくるので、文字列への変換（デコード）が必要です。
`strip()`で改行や余白を削除することが多いです。

```python
if device.in_waiting > 0:
    print("Data available to read")
```

`in_waiting`プロパティで、現在バッファーに溜まっているデータのバイト数を確認できます。
つまり、0より大きいということは受信待ちデータがあるということです。

## 書き込みたい（`write`）

```python
# 送信（パソコン → デバイス）
# バイト列を送信
device.write(b"HELLO\n")

# 文字列をバイト列に変換して送信
device.write("HELLO\n".encode("utf-8"))

# 送信時のブロッキング
device.flush()
```

`write`メソッドでデバイスにデータを書き込みます。
書き込むデータはバイト型への変換（エンコード）が必要です。
改行コード（`\n`や`\r\n`）を区切り文字として利用することが多いです。

```python
if device.out_waiting > 0:
    print("Still sending data")
```

`out_waiting`プロパティで、現在のバッファーに残っているデータのバイト数を確認できます。
つまり、0より大きい場合は未送信データが残っているということです。

## 例外処理したい（`serial.SerialException`）

```python
try:
    with serial.Serial(port="dev/ttyUSB0") as device:
        ...
except serial.SerialException as err:
    print(err)
```

`serial.SerialException`でエラーを検出できます。

シリアル通信は、デバイスが接続されていなかったり、
通信に時間がかかりタイムアウトしたり、など
物理的な要因でエラーが発生することがあります。

例外処理は必ず実装しましょう。

## 連続で読み出したい

```python
import serial

try:
    # ポート名と通信速度を指定して接続
    with serial.Serial(port="/dev/ttyUSB0") as device:
        while True:
            # デバイスからデータを読み込む
            if device.in_waiting > 0:
                line = device.readline().decode("utf-8").strip()
                print(line)
except serial.SerialException as err:
    print(f"Serial error: {err}")
except KeyboardInterrupt:
    print("Stopped by user")
```

`while`ループを使って、デバイスから連続でデータを読み出すことができます。`in_waiting`で受信データの有無を確認してから読み込むことで、効率的に処理できます。
`KeyboardInterrupt`をキャッチして`Ctrl-C`で中断できます。

## ファイルに出力したい

```python
import serial
import csv
import time
from pathlib import Path
from datetime import datetime
from typing import Optional, List

# 設定
port_name = "/dev/ttyUSB0"
baud = 9600

# 保存先
now =datetime.now()
ymd = now.strftime("%Y%m%d")
default_filename = now.strftime("%Y%m%d_%Hh%Mm%Ss.csv")
csv_path = Path.cwd() / "data" / ymd / default_filename

def read_line(
    com: serial.Serial,
    *,
    encoding: str = "utf-8"
    ) -> Optional[str]:
    """Read one decoded line from the serial port."""
    if com.in_waiting == 0:
        return None
    raw = com.readline()
    if not raw:
        return None
    line = raw.decode(encoding, errors="ignore").strip()
    return line or None

def write_row(
    writer: csv.writer,
    line: str
    ) -> List[str]:
    """Write a CSV row to the file."""
    parts = line.split()
    timestamp = datetime.now().isoformat(timespec="seconds")
    row = [timestamp] + parts + [len(parts)]
    writer.writerow(row)
    return row

try:
    with serial.Serial(port=port_name, baudrate=baud, timeout=1) as com:
        print(f"[{com.port}] Opened")

        # 接続が成功したときに保存先ディレクトリを作成
        csv_path.parent.mkdir(parents=True, exist_ok=True)

        with csv_path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            print(f"[{com.port}] Listening...")
            while True:
                line = read_line(com)
                if line is None:
                    time.sleep(0.01)
                    continue

                row = write_row(writer, line)
                f.flush()
                print(f"Added: {row}")

except serial.SerialException as e:
    print(f"Serial error: {e}")
except KeyboardInterrupt:
    print(f"Stopped by user.")
```

シリアル通信で取得したデータをCSV形式で保存するサンプルコードです。
ポート接続を確認してから、ファイルを作成する手順になっています。

`read_line`関数では、受信したデータを確認しています。
`write_row`関数では、データを整形してCSVファイルに出力しています。

## ポートを確認したい（`serial.tools.list_ports`）

```python
from serial.tools import list_ports

ports = list_ports.comports()
for p in ports:
    print(f"{p.device} - {p.description}")
```

`serial.tools.list_ports`で利用可能なポートを確認できます。
Linuxは`/dev/tty*`、
Windowsは`COM*`、
macOSは`/dev/cu.usbserial-*`という名前で表示されます。

## 複数デバイスしたい（`threading`）

```python
import serial
import threading
import time

def read_loop(
    port_name: str,
    baudrate: int,
    stop: threading.Event
    ) -> None:
    """Continuously read lines from a serial port and print them."""
    try:
        with serial.Serial(port_name, baudrate, timeout=1) as com:
            print(f"[{port_name}] Opened")
            while not stop.is_set():
                raw = com.readline()
                if not raw:
                    # Avoid busy loop when data is not available
                    time.sleep(0.01)
                    continue
                line = raw.decode("utf-8", errors="replace").strip()
                if line:
                    print(f"[{port_name}] {line}")
    except serial.SerialException as e:
        print(f"[{port_name}] Serial error: {e}")
    finally:
        print(f"[{port_name}] Closed")


def wait_for_interrupt(
    stop: threading.Event,
    interval: float = 0.2
    ) -> None:
    """Block the main thread until Ctrl-C is pressed."""
    try:
        print("Press Ctrl-C to stop.")
        while not stop.is_set():
            # Avoid busy loop
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopping all readers...")
        stop.set()


if __name__ == "__main__":
    # 停止フラグ
    stop_event = threading.Event()

    # デバイスごとのスレッド
    threads = [
        threading.Thread(target=read_loop, args=("/dev/ttyUSB0", 9600, stop_event)),
        threading.Thread(target=read_loop, args=("/dev/ttyUSB1", 115200, stop_event))
    ]

    # スレッドを起動
    for t in threads:
        t.start()

    # 中断（Ctrl-C）待ち
    wait_for_interrupt(stop_event)
    for t in threads:
        t.join()      # サブスレッドの終了を待つ

    print("All readers stopped.")
```

`threading`モジュールと組み合わせて、
複数のデバイスから、同時にシリアル通信でデータを読み出すことができます。

`Ctrl-C`による中断はメインスレッドにしか送られないため、
サブスレッド（`threading.Thread`）の中では受け取れません。
そのため、
`except KeyboardInterrupt`は`read_loop`関数の中ではなく、
メインスレッドの処理として記述します。

その際に、停止フラグ用の`threading.Event()`を作成しておき、
`KeyboardInterrupt`を検知したときに有効にすることで、
サブスレッドを順番かつ安全に停止できます。
