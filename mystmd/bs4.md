---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: 'Python 3.10.6 (''.venv'': poetry)'
  language: python
  name: python3
---

```{code-cell} ipython3
import requests
from bs4 import BeautifulSoup
```

```{code-cell} ipython3
url = "https://kumaroot.readthedocs.io/ja/latest/"
html = requests.get(url)
soup = BeautifulSoup(html.content)
```

```{code-cell} ipython3
soup.head
```

```{code-cell} ipython3

```

```{code-cell} ipython3

```
