# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# ---
# title: 擬似乱数したい（random / secrets）
# ---

# +
import random
import secrets
import numpy as np
import scipy as sp

print(f"NumPy: {np.__version__}")
print(f"SciPy: {sp.__version__}")
# -

# # 乱数シードしたい

random.seed(511)
random.random()

rng = np.random.default_rng(511)
rng.random()
rng.random(5)  # size=5

# # 一様分布したい
#
# 0.0以上1.0未満の範囲の浮動小数点で一様分布する乱数を生成します。

# +
import random

random.random()

# +
import numpy as np

rng = np.random.default_rng()
rng.random()
# -

# # 任意の範囲で一様分布したい
#
# `a`以上`b`以下の範囲の浮動小数点で一様分布する乱数を生成します。

# +
import random

random.uniform(1, 5)

# +
import numpy as np

rng = np.random.default_rng()
rng.uniform(1, 5)
rng.uniform(1, 5, 5)
# -

# # 整数したい
#
# `a`以上`b`以下の範囲の整数で一様分布する乱数を生成します。

# +
import random

random.randint(1, 100)

# +
import numpy as np

rng = np.random.default_rng()
rng.integers(1, 100)
rng.integers(1, 100, 5)
# -

# # ガウス分布したい

# +
import random

random.gauss()  # mu=0.0, sigma=1.0
# random.gauss(100, 10)

# +
import numpy as np

rng = np.random.default_rng()
rng.normal()
rng.normal(100, 10)
rng.normal(100, 10, 5)
# -

# # リストしたい

# +
import random

seq = ["いち", "に", "さん"]
random.choice(seq)

# +
import numpy as np

seq = ["いち", "に", "さん"]
rng = np.random.default_rng()
rng.choice(seq)
rng.choice(seq, 5)  # size=5

# +
from pathlib import Path

p = Path("/usr/share/dict/words")
with p.open() as f:
    words = [word.strip() for word in f]
    s = secrets.choice(words)
    print(s)
# -

# # 乱数トークンしたい
#
# 推測しにくいトークンを生成

print(secrets.token_bytes())
print(secrets.token_bytes(32))
print(secrets.token_bytes(10))
print(secrets.token_bytes(20))
print(secrets.token_bytes(30))
print(secrets.token_bytes(40))

# 16進数
print(secrets.token_hex())
print(secrets.token_hex(32))
print(secrets.token_hex(10))
print(secrets.token_hex(20))
print(secrets.token_hex(30))
print(secrets.token_hex(40))

print(secrets.token_urlsafe())
print(secrets.token_urlsafe(32))
print(secrets.token_urlsafe(10))
print(secrets.token_urlsafe(20))
print(secrets.token_urlsafe(30))
print(secrets.token_urlsafe(40))
