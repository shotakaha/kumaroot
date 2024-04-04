# ポアソン分布でフィットしたい

:::{math}

P(x) = \exp(-\lambda)\frac{\lambda^{x}} {x!}

:::

```python
import pandas as pd
import numpy as np
import math
from scipy.optimize import curve_fit

def poisson_function(x, amp, mu):
    """ポアソン分布
    """
    f = amp * math.exp(-mu) * mu**x / math.factorial(x)
    return f

def fix(data: pd.DataFrame):

    func = poisson_function
    x_data =
    y_data =
    p_init = [amp0, mu0]
    popt, pcov = curve_fit(func, x_data, y_data, p_init)
    perr = np.sqrt(np.diag(pcov))
```

## リファレンス

- [scipy.stats.poisson](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html)
