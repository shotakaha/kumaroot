# ヒストグラムしたい

```python
# Method Syntax (v5)
chart = alt.Chart(data)
    .mark_bar()
    .encode(
        alt.X("adc:Q").bin().title("X軸のタイトル"),
        alt.Y("count()").title("Y軸のタイトル"),
    ).properties(
        title="グラフのタイトル",
    )
```

```python
# Attribute Syntax (v4 & v5)
chart = alt.Chart(data)
    .mark_bar()
    .encode(
        alt.X("adc:Q", bin=True, axis=alt.Axis(title="X軸のタイトル")),
        alt.Y("count()", axis=alt.Axis(title="Y軸のタイトル")),
    ).properties(
        title="グラフのタイトル",
    )
```

ヒストグラムは[.mark_bar](https://altair-viz.github.io/user_guide/marks/bar.html)を使って作成します。
上記サンプルは、テスト実験で測定したADC値のヒストグラムを作成する場合を想定しています。
X軸のADC値は連続量なので``age:Q``、Y軸はその値の出現回数にしたいので``count()``を指定しています。

:::{note}

``.encode``の中身の書き方はさまざまあり、より短縮した書き方もあります。
ただし、未来の自分が困らないために、X軸・Y軸などのタイトルはつけておくとよいと思います。

Altair v5では、新しく導入されたMethod Syntaxのおかげでかなり直感的に指定できるようになりました。

:::

:::{hint}

あらかじめ``Pandas``を使って、それぞれのADC値の出現回数を計算しておいてもよいです。
その場合、X軸とY軸にそれぞれカラム名を指定した棒グラフとして作成します。

```python
data = （read_csvなどを使って読み込んだpd.DataFrame）
data["entry"] = 1
grouped = data.groupby(["adc"])["entry"].sum().reset_index()

alt.Chart(grouped).mark_bar().encode(
    alt.X("adc:Q").bin(),
    alt.Y("entry:Q"),
)
```

:::
