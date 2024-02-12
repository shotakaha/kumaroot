# 欠損値を確認したい（``pandas.DataFrame.isna``）

```python
data.isna()        # 欠損値を含む行は True になる
data.isna().sum()  # 欠損値の数を数える
```

データフレームに含まれるカラムごとの欠損値の数を判定できます。
データに欠損値があるとうまく集計できない場合があるため、前処理の段階で除外するか、補完するかの処理が必要です。

:::{note}

[isna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isna.html)と
[isnull](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isnull.html)はまったく同じものです（``isnull = isna``）。

ただし、Ruffのルールの[PD003](https://docs.astral.sh/ruff/rules/pandas-use-of-dot-is-null/)では、
メソッド名の汎用性の観点から``isnull``の代わりに``isna``を使うことが推奨されています。

:::

:::{seealso}

``isna``と反対の[pandas.DataFrame.notna](https://pandas.pydata.org/docs/reference/api/pandas.notna.html)もあります。
欠損値でない値（＝有効な値）を判定できます。

```python
data.notna().sum()  # 有効値の数を数える
```

:::

## 欠損値を補完したい（``pd.DataFrame.fillna``）

```python
data.fillna(0)
data.fillna(method="ffill")
data.fillna(method="bfill")
data.fillna(data.mean())
```

## リファレンス

- [pandas.isna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.isna.html)
- [pandas.DataFrame.isna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isna.html)
- [pandas.DataFrame.notna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.notna.html)
- [pandas.DataFrame.dropna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html)
- [pandas.DataFrame.any](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.any.html)
- [pandas.DataFrame.all](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.all.html)
