# シリアル通信したい（`pyserial`）

```python
import serial

try:
    with serial.Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=1) as com:
        while True:
            if com.in_waiting > 0:
                line = com.readline().decode("utf-8").strip()
                if line:
                    print(f"Received: {line}")
except serial.SerialException as e:
    print(f"Serial error: {e}")
```

`pyserial`パッケージ（`serial`モジュール）でシリアル通信できます。
`Serial`オブジェクトを生成するときに、ポート番号（`/dev/ttyUSB0`や`COM`など）を指定します。
また、オプションで通信速度（`baudrate`）やタイムアウト時間（`timeout`）などを設定できます。

`Serial`オブジェクトはコンテクストマネージャーに対応しているため`with...as`構文を使って
安全にポートを開閉できます。
接続に失敗したときや、通信中にエラーが起きた場合は、`serial.SerialException`で例外を受け取れます。

:::{seealso}

シリアル通信は、データを1ビットずつ連続的（＝シリアル）に送る通信方式です。
身近な例としては、パソコンや周辺機器をつなぐUSBがあります。

IoT機器やマイコンでは、よりシンプルなUART通信がよく利用されます。
UARTでは、1文字（通常8ビッド＝1バイト）を送る際に、
スタートビット →
データビット（通常8ビット） →
パリティビット（任意） →
ストップビット
の順で送信します。

送信側は、クロックのリズムに合わせて流しそうめんのように電気信号を送り出します。
受信側は、この信号を順番どおりに受け取り、1バイト単位のデータに組み立てます。
そのため、送信側と受信側で通信速度（ボーレート）をそろえることが重要です。

:::

:::{note}

高速なシリアル通信が普及する以前は、パラレル通信が主流でした。
パラレル通信は、複数ビットを同時に送る通信方式で、短距離であれば非常に高速です。
一度に大量のデータを送ることができる反面、
配線ケーブルが多くなる、
長距離では信号の到着時がずれて誤動作しやすい、
といった課題があります。

現在では、こうした制約を避けるために
高速なシリアル通信を複数本並列に使う方式が一般的です。

:::

## インストールしたい

```console
uv pip install pyserial
```

モジュール名は`serial`ですが、パッケージ名は`pyserial`です。

## 受信したい（`readline`）

```python
# 受信（パソコン ← デバイス）
# バイト列から文字列に変換
line = com.readline().decode("utf-8").strip()
```

`readline`でデバイスからデータを読み出します。
データはバイト列で送られてくるので、文字列への変換（デコード）が必要です。
`strip()`で改行や余白を削除することが多いです。

```python
if com.in_waiting > 0:
    print("Data available to read")
```

`in_waiting`で、現在バッファーに溜まっているデータのバイト数を確認できます。
つまり、0より大きいということは受信待ちデータがあるということです。

## 送信したい（`write`）

```python
# 送信（パソコン → デバイス）
# バイト列を送信
com.write(b"HELLO\n")

# 文字列をバイト列に変換して送信
com.write("HELLO\n".encode("utf-8"))

# 送信時のブロッキング
com.flush()
```

`write`でデバイスにデータを書き込みます。
書き込むデータはバイト列への変換（エンコード）が必要です。
改行コード（`\n`や`\r\n`）を区切り文字として利用することが多いです。

```python
if com.out_waiting > 0:
    print("Still sending data")
```

`out_waiting`でバッファーに残っているデータのバイト数を確認できます。
つまり、0より大きい場合は未送信データが残っているということです。

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
macOSは`/dev/cu.usbserial-*`
という名前で表示されます。

```python
from typing import List, Dict, Any
from serial.tools import list_ports

def find_serial_ports() -> List[Dict[str, Any]]:
    """List available serial ports with rich metadata."""
    ports = list_ports.comports()

    if not ports:
        raise RuntimeError("No ports found.")

    results: List[Dict[str, Any]] = []
    for p in ports:
        results.append(
            {
                "device": p.device,
                "name": getattr(p, "name", None),
                "description": p.description,
                "hwid": p.hwid,
                "vid": p.vid,
                "pid": p.pid,
                "manufacturer": p.manufacturer,
                "product": p.product,
                "serial_number": p.serial_number,
                "location": p.location,
                "interface": p.interface,
            }
        )
    return results
```

このような関数を定義して、ポート情報を辞書型に変換しておくと利便性があがります。

## 自動検出したい

```python
def auto_detect_serial_port(ports: List[Dict[str, Any]]) -> str:
    """Return a single 'best guess' serial device path from find_serial_ports() results.

    Preference order (first match wins):
      1. /dev/ttyACM*         Linux/WSL2: CDC ACM, Arduino-like
      2. /dev/ttyUSB*         Linux/WSL2: USB-serial adapters
      3. /dev/cu.usbmodem*    macOS: CDC ACM
      4. /dev/cu.usbserial*   macOS: USB-serial adapters
      5. COM*                 Windows: COM ports
      6. /dev/ttyS*           WSL2: often mapped COM in WLS
    """

    if not ports:
        raise RuntimeError("No ports provided to auto-detect from.")

    prefixes = [
        "/dev/ttyACM",
        "/dev/ttyUSB",
        "/dev/cu.usbmodem",
        "/dev/cu.usbserial",
        "COM",
        r"\\.\COM",
        "/dev/ttyS",
    ]

    for prefix in prefixes:
        for p in ports:
            device = (p.get("device") or "").strip()
            if not device:
                continue
            if device.lower().startswith(prefix.lower()):
                return device

    # Fallback: return the very first device if present
    first = (ports[0].get("device") or "").strip()
    if first:
        return first

    raise RuntimeError("No available device path found in the provided port list.")
```

OSごとに使用されているポート名を自動検出できるようにした関数です。
前述の`find_serial_ports`とセットで利用することを想定しています。

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

## 複数デバイスしたい（`concurrent.futures.ThreadPoolExecutor`）

```python
import time
import threading
from concurrent.futures import ThreadPoolExecutor, wait
import serial

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
    )-> None:
    """Block the main thread until Ctrl-C is pressed"""
    try:
        print("Press Ctrl-C to stop.")
        while not stop.is_set():
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopping all readers...")
        stop.set()

if __name__ == "__main__":
    # 停止フラグ
    stop_event = threading.Event()

    # ポートの定義
    ports = [
        ("/dev/ttyUSB0", 9600),
        ("/dev/ttyUSB1", 115200),
    ]

    # スレッドプールで実行
    with ThreadPoolExecutor(max_workers=len(ports)) as ex:
        futures = [ex.submit(read_loop, port, baud, stop_event) for port, baud in ports]

        # 状態確認
        # for f in futures:
        #   print(f.done(), f.running())

        try:
            wait_for_interrupt(stop_event)  # Ctrl-C 待ち
        finally:
            stop_event.set()
            wait(futures)

    print("All readers stopped.")
```

`ThreadPoolExecutor`を使って、複数デバイスの処理を書き換えてみました。
`read_loop`関数と`wait_for_interrupt`関数の内容は同じです。

スレッドの生成と管理を`ThreadPoolExecutor`に任せ、
`ex.submit`でジョブを投入しています。
`submit(fn, /, *args, **kwargs)`というシグネチャを持つため、
実行したい関数（`fn`）と
位置引数（`*args`）、
キーワード引数（`**kwargs`）を
そのまま指定すればOKです。

変数`futures`には、非同期処理の結果（`concurrent.futures.Future`オブジェクト）が入っており、実行結果や例外を後で取得できるようになっています。
