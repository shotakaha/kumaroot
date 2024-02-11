# データを抽出したい（``pandas.DataFrame.query``）

```python
data.query("カラム名 > 値")
```

[pandas.DataFrame.query](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html)を使って、条件に一致するデータを抽出できます。
条件式は、カラム名や値をそのまま使用できるためオススメです。

## 比較演算子したい

```python
data.query("age > 40")
data.query("20 <= age < 50")
data.query("name == 'John Doe'")
```

比較演算子（"<"、"<="、">"、">="）、
一致（"=="）、不一致（"!="）の演算子がそのまま使えます。
文字列と比較する場合は、適切にクォートする必要があります。

:::{seealso}

上記のサンプルは、以下のサンプルと同じ結果になります。

```python
data[data["age"] > 40]
data[data["age"] <= 20 & data["age"] < 50]
data[data["name"] == "John Doe"]
```

``query``を使うと簡潔に記述できることが分かると思います。

:::

## 変数したい

```python
age_min, age_max = 20, 50
condition = f"{age_min} <= age < {age_max}"
data.query(condition)
```

条件式は文字列なので、f文字列と組み合わせて変数にできます。

:::{seealso}

```python
age_min, age_max = 20, 50
data.query("@age_min <= age < @age_max)
```

条件式の中で`@変数名`として変数を直接利用することもできます。

:::

## 複数条件したい

```python
# AND
data.query("age > 20 & mass > 60")
data.query("age > 20 and mass > 60")

# OR
data.query("age > 20 | mass > 60")
data.query("age > 20 or mass > 60")

# NOT
data.query("not age > 20 or not mass > 60")
```

``and``、``or``、``not``を使って複数の条件を組み合わせることができます。

:::{note}

`not`は条件式が読みにくくなるため、僕は使いません。
不一致の記号（`!=`）もしくは比較の不等号を反転するようにしています。
また、AND検索とOR検索はついつい`&&`と`||`と書いてしまうのですが、`&`と`|`は1つです。

:::
