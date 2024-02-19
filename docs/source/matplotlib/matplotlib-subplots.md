# キャンバスを分割したい（``matplotlib.pyplot.subplots``）

```python
import matplotlib.pyplot as plt
fig, axs = plt.subplots(2, 3)
axs = axs.ravel()
```

[matplotlib.pyplot.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)を使って、キャンバスを分割できます。

このサンプルでは2行3列に分割しています。
返り値の``axs``は2x3の2次元配列になっています。
順番にループ処理して描画する場合などは、``axs.ravel()``で1次元配列に変換するとよいかもしれません。
