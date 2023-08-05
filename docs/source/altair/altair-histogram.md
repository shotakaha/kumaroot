# ヒストグラムしたい（``.mark_bar``）

```python
base = alt.Chart(data).encode(
    alt.X("X軸").bin(),
    alt.Y("count()"),
)

base.mark_bar()
base.mark_area(interpolate="step")
base.mark_line(interpolate="step")
```

ヒストグラムは[.mark_bar](https://altair-viz.github.io/user_guide/marks/bar.html)を使って作成します。
また、同じような見た目の図は``.mark_area``や``.mark_line``で``interpolate="step"``のオプションを使って作成できます。

## タイトルしたい

```python
# Method Syntax (v5)
alt.Chart(data).mark_bar().encode(
    alt.X("adc:Q").bin().title("X軸のタイトル"),
    alt.Y("count()").title("Y軸のタイトル"),
).properties(
    title="グラフのタイトル",
)
```

```python
# Attribute Syntax (v4 & v5)
alt.Chart(data).mark_bar().encode(
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

## 面積でノーマライズしたい

```python
data_sum = data.groupby("age")["response"].sum().reset_index()
data_merged = pd.merge(data, data_sum, on="age")
data_merged["normalized"] = data_merged["response_x"] / data_merged["response_y"]
data_merged
```

測定回数や回答数が異なる複数のヒストグラムを比較したい場合、
その面積（＝ヒストグラムのエントリー数）でノーマライズして比べる必要があります。
ただし、AltairではできないのでPandasでやります。

## 割合したい

```python
alt.Chart(data).mark_bar().encode(
    alt.X("age:O").title("年代"),
    alt.Y("count()").stack("normalize"),
    alt.Color("gender").title("性別"),
).properties(
    title="グラフのタイトル",
)
```

割合グラフにする場合は、該当する軸を``.stack("normalize")``します。

## 積み上げたくない

```python
opacity = 0.5
alt.Chart(data).mark_bar(opacity=opacity).encode(
    alt.X("age:O").title("年代"),
    alt.Y("count()").stack(None),
    alt.Color("gender").title("性別"),
).properties(
    title="グラフのタイトル",
)
```

グラフを積み上げたくない場合は、該当する軸を``.stack(None)``します。
このときグラフの色の透過度（``opacity``）を設定するとよいです。


## よく使うやつ

```python
def hbar(data: pd.DataFrame, x: str, color: str, title: str, y: str="count()"):
    color = f"{color}:N"
    base = alt.Chart(data).encode(
        alt.X(x),
        alt.Y(y),
    ).properties(
        title=title,
    )

    opacity = 0.5
    mark = base.mark_bar(tooltip=True, opacity=opacity).encode(
        alt.Y(y),
        alt.Color(color)
    )

    stack = base.mark_bar(tooltip=True, opacity=opacity).encode(
        alt.Y(y).stack("normalize"),
        alt.Color(color),
    )

    text = base.mark_text(dy=10).encode(
        alt.Y(y).stack("normalize"),
        alt.Text(y),
        alt.Color(color)
    )

    return mark | stack + text
```

棒グラフとその割合の図を一度に作成する関数です。
割合には``mark_text``を使って頻度（≠パーセンテージ）をオーバーレイしています。
カテゴリカル変数の度数分布を確認する場合に便利です。

``mark``と``stack + text``をそれぞれ返すようになっているので、受け取ってから保存する間にプロパティを調整できます。
