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

## 複数ポートしたい

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
        while not stop.is_set()
            # Avoid busy loop
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopping all readers...")
        stop.set()


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
