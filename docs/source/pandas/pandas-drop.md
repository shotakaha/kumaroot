# データを削除したい（``drop``）

```python
data.drop(columns="カラム名")
```

データを行ごと／カラムごと削除できます。

## 削除するカラム名を指定したい

```python
data.drop(columns=["カラム1", "カラム2"])
```

## NAなデータがある行を削除したい

```python
data.dropna(how="any")  # ひとつでもNA
data.dropna(how="all")  # すべてがNA
```

## リファレンス

- [pandas.DataFrame.drop](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html)
- [pandas.DataFrame.dropna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html)
