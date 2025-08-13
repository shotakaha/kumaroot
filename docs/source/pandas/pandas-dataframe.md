# データフレームしたい（`pandas.DataFrame`）

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

## 空のデータフレームを作成したい

```python
pd.DataFrame()
pd.DataFrame(columns=[])
pd.DataFrame(index=[], columns=[])
```

## カラムを取り出したい

```python
data["カラム名"]
data["カラム名"][開始:終了]
```

``[]``アクセサを使って、カラムを取り出せます。
さらに``[開始:終了]``で行方向にスライスできます。
