# データをソートしたい（``sort_values``）

```python
data.sort_values(by="カラム名")
data.sort_values(by=["カラム1", "カラム2"])
```

## 降順でソートしたい

```python
data.sort_values(by="カラム名", ascending=False)
data.sort_values(by=["カラム1", "カラム2"], ascending=[False, False])
```

デフォルトは昇順（ascending）でソートされるようになっています。
降順（descending）でソートした場合は``False``にします。
``by``で複数のカラムを指定した場合、``ascending``に指定するリストも同じ長さにする必要があります。
