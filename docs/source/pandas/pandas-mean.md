# 平均値したい（``pandas.DataFrame.mean``）

```python
data["temperature"].mean()
```

[pandas.DataFrame.mean](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mean.html)を使って、平均値を計算できます。

## 移動平均したい（``pandas.DataFrame.rolling``）

```python
data["temperature"].rolling(7).mean()
```

[pandas.DataFrame.rolling](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html)を使って、任意の期間における移動平均を計算できます。

たとえば、日付ごとの気温データに対して、1週間の移動平均を求めたい場合は、``rolling(7).mean()``で計算できます。
