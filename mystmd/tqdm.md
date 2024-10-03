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

# 進捗バーしたい（``tqdm``）

```{code-cell} ipython3
import time
```

```{code-cell} ipython3
from tqdm import tqdm

for i in tqdm(range(3)):
    time.sleep(1)
```

```{code-cell} ipython3
from tqdm import tqdm

for i in tqdm(range(3), desc="進行状況"):
    time.sleep(1)
```

```{code-cell} ipython3
from tqdm import tqdm

for i in tqdm(range(3), desc="進行状況", ncols=80):
    time.sleep(1)
```

```{code-cell} ipython3
from tqdm import tqdm

for i in tqdm(range(3), desc="進行状況", ncols=80):
    time.sleep(1)
```

```{code-cell} ipython3
for i in trange(10):
    time.sleep(1)
```

```{code-cell} ipython3
from tqdm.notebook import tnrange
```

```{code-cell} ipython3
for i in tnrange(3, desc="1st loop"):
    for j in tnrange(10, desc="2nd loop"):
        time.sleep(1)
```

```{code-cell} ipython3
# from tqdm.notebook import tqdm
from tqdm import tqdm
```

```{code-cell} ipython3
for i in tqdm(range(3)):
    time.sleep(1)
```
