# データを抽出したい（``pd.DataFrame.loc``）

```python
data.loc["行ラベル", "列ラベル"]
```

[pandas.DataFrame.loc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html)で、行ラベル（＝インデックス）と列ラベルを指定して、データを抽出できます。

行ラベルと列ラベルはリストでも指定できます。

```python
data.loc[["行1":"行200"], ["列1", "列5"]]
```

## 条件を指定したい

```python
# data : 検出器からの信号の波形データを読み込んだデータフレーム
name = "signal"
data[name] = 0 # mV；カラムを追加；初期値を与える
isT = data.query("height > 100")
data.loc[isT, name] = data["height"]
```

上記は、僕が実際に使うことが多いケースをサンプルにしてみました。
ここでは、宇宙線検出器の信号をオシロスコープで確認したときの波形データに対して、
ある閾値を越えた信号だけを抽出しています。

1行でスマートに書く方法があるのかもしれませんが、
データの抽出は[queryメソッド](./pandas-query.md)にまかせて、
``locメソッド``を値の代入に使うこの書き方は、
読みやすいので好んで使っています。
