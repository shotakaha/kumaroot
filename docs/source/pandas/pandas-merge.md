# 結合したい（``pandas.merge``）

```python
left = pd.read_csv("測定データ")
right = pd.read_csv("温度データ")
merged = pd.merge(left, right, on="time", how="outer)
```

[pandas.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html)で、
2つの異なるデータフレームを、あるカラムを基準としてひとつに結合できます。

:::{seealso}

- [pandas.concat](./pandas-concat.md)

``concat``は同じカラムを持つデータフレームを縦方向に伸ばす結合、
``merge``は異なるカラムを持つデータフレームを横方向に伸ばす結合、です。

:::

## 異なるカラム名を基準にマージしたい（``on`` / ``left_on`` / ``right_on``）

```python
# 共通のカラムがある場合
merged = pd.merge(left, right, on="time")

# 共通のカラムがない場合
merged = pd.merge(left, right, left_on="datetime", right_on="timestamp")
```

``on``で基準としたいカラムを指定して、データフレームを結合します。
カラム名が異なる場合は``lelft_on``、``right_on``でそれぞれ指定もできます。
複数のカラム名をリストで指定できます。

## マージ方法を変更したい（``how``）

```python
// leftとrightで共通するアイテム
merged = pd.merge(left, right, how="inner")

// leftとrightで共通しないイテム
merged = pd.merge(left, right, how="outer")

// left優先
merged = pd.merge(left, right, how="left")

// right優先
merged = pd.merge(left, right, how="right")

//
merged = pd.merge(left, right, how="cross")
```

``how``オプションを使って、マージ方法を変更できます。
デフォルトは``innter`で、共通するカラムの値でマージされます。
データを落とさないようにマージするなら``outer`にします。
データに主従関係があるなら``left``、もしくは``right``にします。

## マージ情報を確認したい（``indicator``）

```python
merged = pd.merge(left, right, on="time", how="outer", indicator=True)
```

``indicator=True``オプションを使って、マージされた方法を確認できます。
デフォルトだと``_merge`カラムが追加され、そのアイテムがどのデータフレーム由来かが分かります。
マージ操作はぱっと見で分かりづらいので、想定通りのマージ結果になっているか確認しながら進めるとよいです。

## リファレンス

- [pandas.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html)
- [pandas.DataFrame.merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html)
