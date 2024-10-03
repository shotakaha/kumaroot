# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: 'Python 3.10.6 (''.venv'': poetry)'
#     language: python
#     name: python3
# ---

import requests
from bs4 import BeautifulSoup

url = "https://kumaroot.readthedocs.io/ja/latest/"
html = requests.get(url)
soup = BeautifulSoup(html.content)

soup.head




