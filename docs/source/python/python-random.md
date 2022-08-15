# random

```python
import random
```

擬似乱数の生成には[random](https://docs.python.org/ja/3/library/random.html)モジュールを使います。
機密情報を使う場合は[secrets](https://docs.python.org/ja/3/library/secrets.html)モジュールを使うほうがよいみたいです。

## 整数値を使いたい

```python
random.randint(1, 5)  # 1 <= N <= 5 の乱数
```

## あるリストを使いたい

```python
seq = ["いち", "に", "さん"]
random.choice(seq)
```

## 一様乱数を使いたい

```python
random.uniform(a, b)
```

## ガウス分布を使いたい

```python
random.gauss(mu, sigma)
```
