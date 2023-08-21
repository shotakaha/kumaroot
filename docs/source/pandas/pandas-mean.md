# 平均値したい（``mean``）

```python
data["temperature"].mean()
```

カラム名を指定して平均値を計算できます。
その他にも

## 移動平均したい（``rolling``）

```python
data["temperature"].rolling(7).mean()
```

日付ごとの気温データに対して、1週間の移動平均を求めたい場合は、``rolling(7).mean()``で計算できます。
