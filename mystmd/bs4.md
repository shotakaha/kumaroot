---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.3
kernelspec:
  display_name: 'Python 3.10.6 (''.venv'': poetry)'
  language: python
  name: python3
---

```{code-cell}
import requests
from bs4 import BeautifulSoup
```

```{code-cell}
url = "https://kumaroot.readthedocs.io/ja/latest/"
html = requests.get(url)
soup = BeautifulSoup(html.content)
```

```{code-cell}
soup.head
```
