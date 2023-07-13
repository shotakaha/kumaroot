# カテゴリー型したい

```python
from pandas.api.types import CategoricalDtype
my_category = CategoricalDtype(categories=[カテゴリーの値], ordered=True)

data["カラム名"] = data["カラム名"].astype(my_category)
```

``CategoricalDtype``を使って任意の[カテゴリー型](https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html)を作成できます。
該当するカラムを[astype](./pandas-astype.md)してカテゴリー型に変換します。

カテゴリー型を使うことで、値を任意の順番に並べることができます。
これは実施したアンケートの回答を処理する場合まどにとても便利です。
たとえば、質問の回答が "Very Good / Good / Poor / Very Poor" だった場合、
そのままソートするとアルファベット順に並びが変わってしまいますが、
カテゴリー型に変換しておけば、自分の思い通りの順番にできます。
