# リアルタイム描画したい（`matplotlib.animation.FuncAnimation`）

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# データを準備する
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# キャンバスを作成
fig, ax = plt.subplots()
xdata = []
ydata = []
line, = ax.plot(x, y)  # 初期の線を描画

# アニメーションの更新関数
def update(frame):
    xdata.append(frame)
    ydata.append(np.random.rand())  # ランダムな値を追加

    line.set_data(xdata, ydata)  # 線のデータを更新
    ax.relim()  # 軸の範囲を再計算
    ax.autoscale_view()  # 軸の範囲を自動調整

    return line,  # 更新された線を返す

# アニメーションを作成
ani = FuncAnimation(
    fig,          # アニメーションを描画するFigureオブジェクト
    update,       # 更新関数
    frames=100,   # フレーム数
    interval=50,  # フレーム間の時間（ミリ秒）
    blit=True     # 描画の最適化
)

# アニメーションを表示
plt.show()
```

`FuncAnimation`を使って、リアルタイムでグラフを更新できます。
更新関数を定義し、フレームごとに呼び出されるようにします。
フレーム数や更新間隔を指定して、アニメーションの速度や長さを調整できます。
オプションで`blit=True`を指定すると、描画の最適化が行われ、パフォーマンスが向上します。

## 実用的なリアルタイムモニターしたい

```python
from collections import deque
import threading
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# データバッファ
class DataBuffer:
    def __init__(self, maxlen=100):
        self.x = deque(maxlen=maxlen)  # 時間軸のデータを保持
        self.y = deque(maxlen=maxlen)  # 値のデータを保持
        self.lock = threading.Lock()   # スレッドセーフなロック

    # データを追加するメソッド
    def push(self, x, y):
        with self.lock:
            self.x.append(x)
            self.y.append(y)

    # データのスナップショットを取得するメソッド
    def snapshot(self):
        with self.lock:
            return self.x, self.y

# データ生成スレッド
def data_generator(buffer: DataBuffer):
    t = 0  # 時間の初期値
    while True:
        value = np.random.rand()  # ランダムな値を生成
        buffer.push(t, value)
        t += 0.1
        time.sleep(0.1)  # データ生成の間隔

def dashboard(buffer: DataBuffer):

    # レイアウトを定義
    panels = [
        ["main", "main", "side"],
        ["main", "main", "side"],
    ]

    # キャンバスを作成
    fig, axs = plt.subplot_mosaic(
        panels,    # 割付を指定
        figsize=(8, 4),   # 横長のキャンバスを作成
        layout="constrained",  # レイアウト調整
    )

    # main: メインのグラフを初期化
    line, = axs['main'].plot([], [], lw=2, label="Random Data")
    axs['main'].set_xlim(0, 20)
    axs['main'].set_ylim(0, 1)
    axs['main'].legend()

    # side: サイドパネルにテキストを表示
    txt = axs["side"].text(
        0.5,
        0.5,
        "",
        ha="center",
        va="center",
    )
    axs["side"].axis("off")

    def update(frame):
        x, y = buffer.snapshot()

        if len(x) == 0:
            return line, txt

        # deque -> list に変換してから描画
        x = list(x)
        y = list(y)

        # グラフを更新
        line.set_data(x, y)

        # 最新の20秒分を表示
        axs["main"].set_xlim(max(0, x[-1] - 20), x[-1])

        # サイドパネルのテキストを更新
        txt.set_text(f"Latest Value: {y[-1]:.2f}")

        return line, txt

    ani = FuncAnimation(
        fig,
        update,
        interval=100,  # 描画の更新間隔
    )

    plt.show()

if __name__ == "__main__":
    # データバッファを作成
    buffer = DataBuffer(maxlen=200)

    # データ生成スレッドを開始
    t = threading.Thread(
        target=data_generator,
        args=(buffer,),
        daemon=True,  # メインスレッドが終了したら自動的に終了する
    )
    t.start()

    # ダッシュボードを開始
    dashboard(buffer)
```

実用的なリアルタイムモニターを作成する場合には、
データを取得する処理と、グラフを更新する処理は分けて設計する必要があります。

上記のサンプルでは、データ取得とグラフ更新の橋渡しをするために、
スレッドセーフなデータバッファクラス（`DataBuffer`）を定義しています。
このクラスでは`deque`を使って、一定数のデータを保持し、スレッド間で安全にデータをやり取りできるようにしています。

グラフ更新に遅延が生じても、データ取得には影響せず、リアルタイムモニターとしての機能が保たれます。
