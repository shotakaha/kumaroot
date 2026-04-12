# 凡例したい（`matplotlib.axes.Axes.legend`）

```python
import numpy as np
import matplotlib.pyplot as plt

# データを準備する
# ...省略

# キャンバスを作成
fig, ax = plt.subplots()

# グラフを作成
ax.plot(
    x,
    y,
    label="sin(x)", # 凡例に使う名前を指定
)

# グラフのタイトルと軸ラベルを設定
ax.set_title("折れ線グラフの例")
ax.set_xlabel("X軸")
ax.set_ylabel("Y軸")

ax.legend(
    loc="upper right",  # 凡例の位置
    fontsize="small",   # フォントサイズ
    frameon=True,      # 凡例の枠を表示
)  # 凡例を表示

plt.show()
```

`Axes.legend`で凡例を表示できます。
グラフを作成するときに、`label`オプションで凡例に表示する名前を指定しておくと、`legend()`を呼び出すだけで凡例が表示されます。
`loc`オプションで凡例の位置を指定できます。
