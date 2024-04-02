# 相補誤差関数でフィットしたい

```python
from scipy.special import erfc

def erfc_function(x, amp, mu, sigma, intercept):
    """相補誤差補正関数
    Args:
        x(array-like): 測定データ
        amp(float): 振幅
        mu(float): 平均
        sigma(float): 標準偏差
        intercept(float): 切片
    Returns:
        f(array-like): 誤差補正関数
    """
    f = amp * erfc((x - mu) / sigma) + intercept
    return
```
