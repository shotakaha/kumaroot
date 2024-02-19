# キャンバスを複雑に分割したい（``matplotlib.pyplot.subplot_mosaic``）

```python
import matplotlib.pyplot as plt

# キャンバスの割付を設定する
# 結合するキャンバスは同じ名前にする
panels = [
    ["A", "A", "E"],
    ["C", ".", "E"]
]
fig, axs = plt.subplot_mosaic(mosaic=panels, layout="constrained")

# axsは辞書型
axs["A"].set_title("Panel A")
axs["C"].set_title("Panel C")
axs["E"].set_title("Edge")
```

[matplotlib.pyplot.subplot_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html)を使って、キャンバスを複雑に分割できます。

第一引数（``mosaic``）は必須の引数で、キャンバスの割り付けをリスト型で指定します。結合したい部分は同じ名前を指定します。
また、ここで指定した名前を使って``Axes``オブジェクトを取り出すことができます。
``layout="constrained"``オプションをつけると、いい感じの余白で整理できます。

:::{note}

``mosaic``はモザイク処理ではなく、タイルのことを指しているのだと思います。

:::
