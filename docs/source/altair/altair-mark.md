# グラフの種類したい（``.mark_*``）

- 円グラフ : ``mark_arc``
- 棒グラフ : ``mark_bar``
- 折れ線グラフ : ``mark_line``
- ヒストグラム : ``mark_bar``
- 散布図 : ``mark_point`` / ``mark_circle``
- ヒートマップ : ``mark_rect``
- 箱ひげ図 : ``mark_boxplot``
- 直線 : ``mark_rule``
- 文字 : ``mark_text``

Altairで指定できるグラフの種類は[Marks](https://altair-viz.github.io/user_guide/marks/index.html)で確認できます。

## グラフに色をつけたい

```python
base = alt.Chart(data)
base.mark_bar(fill="red", opacity=0.5)
````
