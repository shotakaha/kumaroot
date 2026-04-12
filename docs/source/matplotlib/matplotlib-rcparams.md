# 描画スタイルしたい（`matplotlib.rcParams`）

```python
import matplotlib as mpl

mpl.rcParams["figure.figsize"] = (6, 4)
mpl.rcParams["figure.dpi"] = 200
mpl.rcParams["font.family"] = "sans-serif"
mpl.rcParams["font.size"] = 12

mpl.rcParams["axes.titlesize"] = 14
mpl.rcParams["axes.labelsize"] = 12
mpl.rcParams["axes.grid"] = True

mpl.rcParams["lines.linewidth"] = 2
mpl.rcParams["lines.markersize"] = 6

mpl.rcParams["legend.fontsize"] = 10
```

`matplotlib.rcParams`で、全体の描画スタイルを変更できます。
設定した内容は、以降のすべての描画に適用されます。
いつも使う設定は
`~/.config/matplotlib/matplotlibrc`ファイルに保存しておくと便利です。

上のサンプルに、
キャンバス設定やフォント設定など、よく設定するスタイルをまとめてみました。

## リセットしたい（`matplotlib.rcdefaults`）

```python
import matplotlib as mpl
mpl.rcdefaults()
```

`matplotlib.rcdefaults`で全体の描画スタイルをデフォルトにリセットできます。

## キャンバス設定したい（`rcParams.figure.*`）

```python
# キャンバス全体の設定
mpl.rcParams["figure.figsize"] = (6, 4)         # default: (6.4, 4.8) in inches
mpl.rcParams["figure.dpi"] = 200                # default: 100 | 200 | 300
mpl.rcParams["figure.layout"] = "constrained"   # default: None | "constrained" | "compressed" | "tight"
mpl.rcParams["figure.autolayout"] = True        # default: False | True

# キャンバスの背景色
mpl.rcParams["figure.facecolor"] = "lightgray"  # default: "white" | "lightgray" | "none"
mpl.rcParams["figure.frameon"] = False          # default: True | False

# 全体のタイトル設定
mpl.rcParams["figure.titlelocation"] = "left"  # default: "center" | "left" | "right"
mpl.rcParams["figure.titlesize"] = 14          # default: "large" | "medium" | "small" | 14
mpl.rcParams["figure.titleweight"] = "bold"    # default: "normal" | "bold"
mpl.rcParams["figure.titlepad"] = 6            # default: 6 in points
mpl.rcParams["figure.titlecolor"] = "blue"     # default: "black" | "blue" | "red" | "green"
```

`figure.*`オプションで、キャンバス全体の設定を変更できます。
キャンバスのサイズや解像度、レイアウトなどを変更できます。

## フォント設定したい（`rcParams.font.*`）

```python
# フォントの種類やサイズ
mpl.rcParams["font.family"] = "Noto Sans CJK JP"  # default: "sans-serif" | "serif" | "cursive" | "fantasy" | "monospace"
mpl.rcParams["font.size"] = 12        # default: 10 | 12 | 14 | "small" | "medium" | "large"
mpl.rcParams["font.weight"] = "bold"  # default: "normal" | "bold"

# フォントの種類を細かく指定
# serif: 明朝体、sans-serif: ゴシック体、monospace: 等幅フォント、cursive: 筆記体
mpl.rcParams["font.serif"] = ["Times New Roman", "serif"]             # default: ["Times New Roman", "serif"]
mpl.rcParams["font.sans-serif"] = ["Noto Sans CJK JP", "sans-serif"]  # default: ["DejaVu Sans", "sans-serif"]
mpl.rcParams["font.monospace"] = ["Courier New", "monospace"]         # default: ["DejaVu Sans Mono", "monospace"]
mpl.rcParams["font.cursive"] = ["Comic Sans MS", "cursive"]           # default: ["Apple
Chancery", "cursive"]


# マイナスの表示
mpl.rcParams["axes.unicode_minus"] = False  # default: True | False
```

`font.*`オプションで、フォントの種類やサイズを変更できます。
`font.family`で、和文フォントを指定すれば、タイトルや軸タイトルで日本語を表示できます。

:::{note}

和文フォントは「Unicodeのマイナス」を持ってないことがあるそうです。
`axes.unicode_minus=False`にしておくと、マイナスが通常のハイフンで表示されるようになり、豆腐化（＝文字化け）せずに安全に表示できます。

:::

```python
mpl.rcParams["font.family"] = [
  "Noto Sans CJK JP",
  "IPAexGothic",
  "Yu Gothic",
  "Hiragino Sans",
  "sans-serif",
]
```

フォントはリスト形式で複数指定できます。
上から順番に、環境にインストールされているフォントが使われます。

```python
import japanize_matplotlib
```

`japanize_matplotlib`をインポートすると、日本語設定がお手軽に完了できます。
フォントは`IPAexGothic`が使われます。

## 軸設定したい（`rcParams.axes.*`）

```python
# 軸のタイトル設定
mpl.rcParams["axes.titlesize"] = 14            # default: "large" | "medium" | "small" | 14
mpl.rcParams["axes.titleweight"] = "bold"      # default: "normal" | "bold"
mpl.rcParams["axes.titlecolor"] = "blue"       # default: "black" | "blue" | "red" | "green"
mpl.rcParams["axes.titlepad"] = 6              # default: 6 in points

# 軸のラベル設定
mpl.rcParams["axes.labelsize"] = 12          # default: "large" | "medium" | "small" | 12
mpl.rcParams["axes.labelweight"] = "bold"    # default: "normal" | "bold"
mpl.rcParams["axes.labelcolor"] = "blue"     # default: "black"
mpl.rcParams["axes.labelpad"] = 4           # default: 4 in points

# 軸の線や背景の設定
mpl.rcParams["axes.linewidth"] = 1             # default: 1
mpl.rcParams["axes.linecolor"] = "black"       # default: "black" | "gray" | "lightgray"
mpl.rcParams["axes.edgecolor"] = "black"       # default: "black" | "gray" | "lightgray"
mpl.rcParams["axes.facecolor"] = "lightgray"   # default: "white" | "lightgray" | "none"
```

`axes.*`オプションで、軸のタイトルやラベル、線や背景の設定を変更できます。

## グリッド設定したい（`rcParams.axes.grid.*`）

```python
# グリッド線の表示
mpl.rcParams["axes.grid"] = True             # default: False | True
# グリッド線の詳細
mpl.rcParams["axes.grid.which"] = "both"      # default: "major" | "minor" | "both"
mpl.rcParams["axes.grid.axis"] = "x"        # default: "both" | "x" | "y"
mpl.rcParams["axes.grid.linestyle"] = ":"     # default: "--" | "-" | ":" | "-."
mpl.rcParams["axes.grid.linewidth"] = 1.0      # default: 0.5 | 1.0
mpl.rcParams["axes.grid.color"] = "black"      # default: "gray" | "black"
```

`axes.grid.*`オプションで、グリッド線の表示を変更できます。
`aces.grid`を`True`にすると、グリッド線が表示されます。

## マーカー設定したい（`rcParams.lines.*`）

```python
# 線の設定
mpl.rcParams["lines.linewidth"] = 2
mpl.rcParams["lines.linestyle"] = "-"  # default: "-" | "--" | "-." | ":"

# マーカーの設定
mpl.rcParams["lines.markersize"] = 6
mpl.rcParams["lines.marker"] = "o"  # default: "o" | "s" | "^" | "D" | "x" | "+" | "*"
mpl.rcParams["lines.markerfacecolor"] = "blue"  # default: "blue" | "red" | "green"
mpl.rcParams["lines.markeredgecolor"] = "black"  # default: "black | "blue" | "red" | "green"
```

`lines.*`オプションで、線やマーカーの設定を変更できます。
`lines.marker`で、マーカーの形状を変更できます。

| `lines.marker`の値 | マーカーの形状 |
| --- | --- |
| "o" | ○：円 |
| "s" | □：四角 |
| "^" | △：三角 |
| "D" | ◆：ダイヤ |
| "x" | ✕：バツ |
| "+" | ＋：プラス |
| "*" | ★：星 |

## 凡例設定したい

```python
# 凡例の設定
mpl.rcParams["legend.fontsize"] = 10         # default: "large" | "medium" | "small" | 10
mpl.rcParams["legend.title_fontsize"] = 12   # default: "large" | "medium" | "small" | 12
mpl.rcParams["legend.title_fontweight"] = "bold"  # default: "normal" | "bold"
mpl.rcParams["legend.title_color"] = "blue"  # default: "black" | "blue" | "red" | "green"
```

`legend.*`オプションで、凡例の設定を変更できます。

## 論文したい

```python
import matplotlib as mpl

mpl.rcParams["axes.unicode_minus"] = False
mpl.rcParams["figure.figsize"] = (3.5, 2.5)  # 2カラムの論文に適したサイズ
mpl.rcParams["figure.dpi"] = 300             # 論文用の高解像度
mpl.rcParams["font.family"] = ["Noto Serif CJK JP", "serif"]  # 論文に適したセリフ体
mpl.rcParams["font.size"] = 10               # 論文に適したフォントサイズ
mpl.rcParams["axes.titlesize"] = 12          # 論文に適した軸タイトルサイズ
mpl.rcParams["axes.labelsize"] = 10          # 論文に適した軸ラベルサイズ
mpl.rcParams["axes.grid"] = False                # 論文ではグリッド線を非表示にすることが多い
mpl.rcParams["lines.linewidth"] = 1.0           # 論文に適した線の太さ
mpl.rcParams["lines.markersize"] = 4.0           # 論文に適したマーカーの大きさ
mpl.rcParams["legend.fontsize"] = 8            # 論文に適した凡例のフォントサイズ
```

2カラムの論文に適したサイズや、解像度、フォントなどを設定する例です。
フォントは明朝体（セリフ体）にして、グリッド線は非表示にしています。

## プレゼンしたい

```python
import matplotlib as mpl

mpl.rcParams["axes.unicode_minus"] = False
# mpl.rcParams["figure.figsize"] = (8, 6)  # 4:3スライド
mpl.rcParams["figure.figsize"] = (8, 4.5)  # 16:9スライド
mpl.rcParams["figure.dpi"] = 150           # プレゼン用の解像度
mpl.rcParams["font.family"] = ["Noto Sans CJK JP", "sans-serif"]  # プレゼンに適したサンセリフ体
mpl.rcParams["font.size"] = 18             # プレゼンに適したフォントサイズ
mpl.rcParams["axes.titlesize"] = 20        # プレゼンに適した軸タイトルサイズ
mpl.rcParams["axes.labelsize"] = 18        # プレゼンに適した軸ラベルサイズ
mpl.rcParams["axes.grid"] = True                # プレゼンではグリッド線を表示することが多い
mpl.rcParams["lines.linewidth"] = 3.0           # プレゼンに適した線の太さ
mpl.rcParams["lines.markersize"] = 8.0           # プレゼンに適したマーカーの大きさ
mpl.rcParams["legend.fontsize"] = 14            # プレゼンに適した凡例のフォントサイズ
```

プレゼン資料に適したサイズや、解像度、フォントなどを設定する例です。
スライドのアスペクト比に合わせて、キャンバスのサイズを変更しています。
フォントはゴシック体（サンセリフ体）にして、グリッド線は表示するようにしています。

## ダッシュボードしたい

```python
import matplotlib as mpl

mpl.rcParams["axes.unicode_minus"] = False
mpl.rcParams["figure.figsize"] = (8, 4)  # 少し横長
mpl.rcParams["figure.dpi"] = 150         # ダッシュボード用の解像度
mpl.rcParams["font.family"] = ["Noto Sans CJK JP", "sans-serif"]  # サンセリフ体
mpl.rcParams["font.size"] = 11
mpl.rcParams["axes.grid"] = True         # グリッド線を表示
mpl.rcParams["axes.linestyle"] = ":"     # グリッド線を点線
mpl.rcParams["legend.frameon"] = False   # 凡例の枠線を消す
```

ダッシュボード用のスタイルの例です。
ウェブ埋め込みに適したサイズや、解像度、フォントなどを設定します。

## リファレンス

- [matplotlib.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams)
