==================================================
ヒストグラムを作成したい
==================================================

- 年齢（ ``age`` ）の度数分布（ヒストグラム）を作成する場合を想定

.. code-block:: python

    alt.Chart(data)
        .mark_bar()
        .encode(
            x=alt.X('age:Q', bin=True)
            y='count()'
       )

- 種類 : ``mark_bar()``
- X軸 : ``x=alt.X(...)`` or ``alt.X(...)``
- Y軸 : ``y="count()"``

参考ドキュメント
==================================================

- https://altair-viz.github.io/gallery/simple_histogram.html
