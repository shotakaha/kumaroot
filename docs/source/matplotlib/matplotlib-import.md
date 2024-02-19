# インポートしたい（``matplotlib``）

```python
import matplotlib.pyplot as plt
import japanize_matplotlib
```

``matplotlib.pyplot``を``plt``という名前でインポートすることが多いようです。
``matplotlib``をインポートしたあとに、``japanize_matplotlib``をインポートします。

## バージョンを確認したい

```python
import matplotlib as mpl
print(f"{mpl.__version__}")
```

``matplotlib``本体をインポートする場合は、``mpl``という名前を使ったりします。
