# 度数分布したい（`np.histogram`）

```python
freq, rank = np.histogram(データ, bins=ビン数)
```

[np.histogram](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html)で、測定データの度数分布を取得できます。
ビン分割した結果として、度数（``freq``）と階級（``rank``）を一度に取得できます。

``x``に渡すデータは配列であれば、``list``でも``np.ndarray``でも``pd.Series``でもOKです。
``bins``オプションで任意のビン分割に変更できます。デフォルトは``10``（均等に10分割）です。

```python
# ages: アンケート回答者の年齢をエミュレート
# ages = [random.randint(18, 60) for i in range(100)]
bins = range(0, 80, 10)
freq, rank = np.histogram(ages, bins=bins)

# freq -> array([ 0,  3, 26, 19, 27, 24,  1,  0])
# rank -> array([ 0, 10, 20, 30, 40, 50, 60, 70, 80])
```

上記では100人を対象としたアンケートを想定し、回答者の年齢を度数分布表に変換してみました。
``bins``オプションは配列を指定できます。
ビン分割に小数点（``float``）を使いたい場合は[np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)を使うとよいです。

## 度数分布したい（``pandas.Series.value_counts``）

```python
# ages = [random.randint(18, 60) for i in range(100)]
# data = pd.DataFrame({"age": ages})
bins = range(0, 10, 10)
data["age"].value_counts(bins=bins).reset_index().rename(
    columns={"index": "rank", "count": "freq"})
```

``pandas.Series.value_counts``で、同じように度数分布を取得できます。
ただし、この場合、階級（``rank``）が``Interval``オブジェクトになってしまい、そのあとで再利用しづらいです。

## ビン分割したい（``pd.cut``）

```python
# ages = [random.randint(18, 60) for i in range(100)]
bins = range(0, 100, 10)
categories, rank = pd.cut(ages, bins=bins, retbins=True)

# type(categories) -> pandas.core.arrays.categorical.Categorical
# rank -> array([ 0, 10, 20, 30, 40, 50, 60, 70, 80])
```

``pd.cut``で、測定データをビン分割できます。
``retbins=True``オプションで、ビン分割の配列も取得できます。
``precision``オプションで、小数点以下の桁数を変更できます。デフォルトは``precision=3``です。

## リファレンス

- [numpy.histogram - NumPy](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html)
- [numpy.arange - NumPy](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)
- [pandas.Series.value_counts](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html#pandas.Series.value_counts)
- [pandas.cut - Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.cut.html)
