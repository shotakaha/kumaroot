# 保存したい（``hvplot.save``）

```python
plot = data.hvplot.hist(...)

hvplot.save(plot, "test.html")
hvplot.save(plot, "test.png")
```

``hvplot.save``で図を保存できます。
PNGで保存する場合は、``Selenium``と``PhantomJS``パッケージが必要です。

:::{note}

Jupyter Notebookで作成した図は、図の周りのツールバーを使って画像として保存できます。

:::

## リファレンス

- [Saving plots](https://hvplot.holoviz.org/user_guide/Viewing.html#saving-plots)
- [SeleniumHQ/selenium](https://github.com/SeleniumHQ/selenium)
- [PhantomJS](https://phantomjs.org/)
