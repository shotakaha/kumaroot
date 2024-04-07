# 分散したい（``pandas.DataFrame.var``）

```python
data["var"] = data["カラム名"].var()
```

## 分散

:::{math}

V = s^{2} = \frac{1}{n} \sum_{i=1}^{n} (x_{i} - m)^{2}

:::

## 不偏分散

:::{math}

V = s^{2} = \frac{1}{n-1} \sum_{i=1}^{n} (x_{i} - m)^{2}

:::

## リファレンス

- [pandas.DataFrame.var](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.var.html)
- [pandas.Series.var](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.var.html)
