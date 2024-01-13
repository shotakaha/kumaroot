# データフレームしたい（``pd.DataFrame``）

```python
data = pd.DataFrame(リスト型オブジェクト)
data = pd.DataFrame(辞書型オブジェクト)
```

[pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)でデータフレームを作成できます。

データフレームは``Pandas``の基本的なデータ構造で、
行（インデックス）と列（カラム）で構成されています。

スプレッドシートのような表構造を頭に思い浮かべて、
行に対する操作なのか、列に対する操作なのか、
を意識すると扱いやすいと思います。

## データを確認したい

```python
data.head()
data.tail()
```

## カラムを取り出したい

```python
data["カラム名"]
data["カラム名"][開始:終了]
data.loc[開始:終了, "カラム名"]
```

[pandas.DataFrame.loc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html)を使って、データフレームをスライスできます。

たとえば、ある閾値を越えた測定値を取り出したい場合は、次のように使います。

```python
name = "新しいカラム名"
data[name] = 0
isT = data["測定値"] > 閾値
data.loc[isT, name] = data["測定値"]
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
