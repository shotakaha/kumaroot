# ガウス関数でフィットしたい

```python
def gaus_function(x, amp, mu, sigma):
    """ガウス関数
    Args:
        x(array-like): データ
        a(float): 振幅
        mu(float): 平均
        sigma(float): 標準偏差
    Returns:
        g(ndarray): ガウス関数
    """
    # 分子と分母に分けて計算
    n = (x - mu)**2
    d = 2 * sigma**2
    g = amp * np.exp(-n/d)
    return g
```
