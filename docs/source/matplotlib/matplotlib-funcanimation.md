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
