# カテゴリー型したい

```python
data["カラム名"].astype("category")
```

[astype](./pandas-astype.md)を使って``category``型に変換できます。
カテゴリーの値は、カラムに含まれる値から自動で算出されます。
カテゴリー間の順序はありません。

## 順序ありカテゴリーしたい

```python
from pandas.api.types import CategoricalDtype
my_category = CategoricalDtype(categories=[カテゴリーの値], ordered=True)

data["カラム名"] = data["カラム名"].astype(my_category)
```

カテゴリー型は、数値型と異なり、基本的に値の大小を比較したり、演算だったりができません。
とはいえ、カテゴリーを任意の順番にソートしたいときもあります。
そのようなときは[CategoricalDtype](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.CategoricalDtype.html)``を使います。
詳細は[Categorical data](https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html)を参照してください。

順序ありのカテゴリー型は、アンケートの回答を処理する場合に便利です。
たとえば、質問の選択肢が "Very Good / Good / Poor / Very Poor" だった場合、
そのままソートするとアルファベット順になってしまいますが、
カテゴリー型に変換しておけば、自分が指定した順番に並べられます。
