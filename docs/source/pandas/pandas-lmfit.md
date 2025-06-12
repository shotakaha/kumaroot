# 曲線フィットしたい（`lmfit`）

```python
from lmfit import Model

model = Model(関数)
params = model.make_params(パラメーター)
result = model.fit(y, params, x=x)

print(result.fit_report())
```

`lmfit`は[scipy.optimize.curve_fit](./pandas-fit-curve_fit.md)を拡張子、
機能を強化したパッケージです。
パラメーターを辞書型で設定できたり、
フィットする範囲を制限できたり、
可読性があがっています。
