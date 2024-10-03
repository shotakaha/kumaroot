---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: .venv
  language: python
  name: python3
---

# 誤差関数／補正誤差関数

```{code-cell} ipython3
from scipy.special import erf, erfc
import pandas as pd
import numpy as np
import hvplot.pandas
```

```{code-cell} ipython3
def gauss_function(x, amp, mu, sigma):
    n = (x - mu) ** 2
    d = 2 * sigma**2
    f = amp * np.exp(-n / d)
    return f
```

```{code-cell} ipython3
def erf_function(x, amp, mu, sigma):
    f = amp * erf((x - mu) / sigma) + 1
    return f
```

```{code-cell} ipython3
def erfc_function(x, amp, mu, sigma):
    f = amp * erfc((x - mu) / sigma)
    return f
```

```{code-cell} ipython3
x = np.arange(250, 300, 1)
amp = 1
mu = 280
sigma = 5

y1 = gauss_function(x, amp, mu, sigma)
y2 = erf_function(x, amp, mu, sigma)
y3 = erfc_function(x, amp, mu, sigma)

data = pd.DataFrame(
    {
        "x": x,
        "y1": y1,
        "y2": y2,
        "y3": y3,
    }
)

data.hvplot.scatter(x="x", grid=True, width=800, height=400)
```

```{code-cell} ipython3
erf_function(x, amp, mu, sigma)
```
