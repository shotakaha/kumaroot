# インストールしたい

```console
$ pip3 install plotly
```

```console
$ poetry add plotly
```

```python
import plotly.express as px
fig = px.bar(x=["a", "b", "c", y=[1, 3, 2])
fig.write_html("first_figure.html", auto_open=True)
```

グラフを作成する場合は、``plotly.express``を使います。
もっと複雑なことをしたい場合は``plotly``が必要です。
