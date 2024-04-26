# 擬似乱数したい（``random`` / ``numpy.random``）

```python
import random
```

擬似乱数を生成するパッケージ／モジュールはいろいろあります。
Pythonの標準モジュールで擬似乱数を生成するには[random](https://docs.python.org/ja/3/library/random.html)モジュールを使います。
機密情報を使う場合は[secrets](https://docs.python.org/ja/3/library/secrets.html)モジュールを使うほうがよいみたいです。

複数の乱数値を一度に生成したい場合は``numpy.random``が便利です。

## 乱数シードしたい

```python
import random
random.seed(511)
random.random()
# -> 0.10846537689444802
```

```python
import numpy as np
rng = np.random.default_rng(511)
rng.random()
# -> 0.9463589575041579
```

シードを固定することで、同じ乱数を生成できます。
テストのときなどに使います。

## 一様分布したい

```python
import random
random.random()
# -> 0.24352181317841615
```

```python
import numpy as np
rng = np.random.default_rng()

rng.random()
# -> 0.1734872525999479

rng.random(5)  # size=5
# -> array([0.44780529, 0.27322929, 0.89200497, 0.57964083, 0.56720332])
```

`[0.0, 1.0)`の範囲の浮動小数点で一様分布する乱数を生成します。

## 任意の範囲で一様分布したい

```python
import random
random.uniform(1, 5)
# -> 3.9737232237549036
```

```python
import numpy as np
rng = np.random.default_rng()

rng.uniform(1, 5)
# -> 1.2366360779462524

rng.uniform(1, 5, 5)  # size=5
# -> array([4.01063043, 4.3938906 , 1.9511828 , 4.44290251, 2.23030564])
```

`[a, b]`の範囲の浮動小数点で一様分布する乱数を生成します。

## 整数したい

```python
import random
random.randint(1, 100)
# -> 73
```

```python
import numpy as np
rng = np.random.default_rng()

rng.integers(1, 100)
# -> 41

rng.integers(1, 100, 5)  # size=5
# -> array([23, 34, 88, 83, 94])
```

`[a, b]`の範囲の整数で一様分布する乱数を生成します。

## ガウス分布したい

```python
import random

random.gauss()  # mu=0, sigma=1
# -> -0.6759904579865917

random.gauss(mu=100, sigma=10)
# -> 83.04934632054037
```

```python
import numpy as np
rng = np.random.default_rng()

rng.normal()  # loc=0, scale=1
# -> -0.4687162677485689

rng.normal(loc=100, scale=10)  # loc=平均、scale=標準偏差
# -> 96.92358323438323

rng.normal(100, 10, 5)  # size=5
# -> array([ 85.27675615,  87.21491819, 110.40065645, 102.60680418, 96.21210008])
```

平均`mu`、標準偏差`sigma`のガウス分布にしたがう乱数を生成します。
`mu=0`、`sigma=1`の場合は、正規ガウス分布になります。

## リストしたい

```python
import random
seq = ["いち", "に", "さん"]
random.choice(seq)
# -> 'さん'
```

```python
import numpy as np
seq = ["いち", "に", "さん"]
rng = np.random.default_rng()

rng.choice(seq)
# -> 'に'

rng.choice(seq, 5)  # size=5
# -> array(['に', 'さん', 'いち', 'いち', 'さん'], dtype='<U2')
```

指定したリストからランダムに選択できます。

## リファレンス

- [Random Generator - numpy.org](https://numpy.org/doc/stable/reference/random/generator.html)
- [Random sampling - numpy.org](https://numpy.org/doc/stable/reference/random/index.html)
- [random - docs.python.org](https://docs.python.org/ja/3/library/random.html)
- [secrets - docs.python.org](https://docs.python.org/ja/3/library/secrets.html)

