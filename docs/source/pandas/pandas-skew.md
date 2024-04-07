# 歪度したい（``pandas.DataFrame.skew``）

```python
data["skewness"] = data["カラム名"].skew()
```

指定したカラムの **歪度（skewness）** を計算できます。

## 歪度（skewness）

分布の平均まわりの非対称度の指標です。
歪度が0だと左右対称、
歪度が正だと左寄り、
歪度が負だと左寄り、となります。

## リファレンス

- [pandas.Series.skew](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.skew.html)
- [pandas.DataFrame.skew](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.skew.html)
