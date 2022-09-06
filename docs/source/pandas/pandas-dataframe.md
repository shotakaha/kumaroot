# データフレームを作りたい

```python
data = pd.DataFrame(リスト型オブジェクト)
data = pd.DataFrame(辞書型オブジェクト)
```

データフレームは``Pandas``の基本的なデータ構造で、
行（インデックス）と列（カラム）で構成されています。

スプレッドシートのような表構造を頭に思い浮かべて、
行に対する操作なのか、列に対する操作なのか、を意識すると
扱いやすいと思います。

## データを確認したい

```python
data.head()
data.tail()
```

## 指定した場所のデータを確認したい

```python
data.at[インデックス名, カラム名]
data.at[インデックス番号, カラム番号]
data.loc[インデックス名].at[カラム名]
```


## リファレンス

- [pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
- [pandas.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html)
- [pandas.Index](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.html)
