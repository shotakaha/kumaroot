# Pythonの使い方

[Homebrew](https://brew.sh)を使って``Python``をインストールします。
そして、プロジェクトごとの環境構築には[poetry](https://python-poetry.org/)を使います。

```{toctree}
---
maxdepth: 1
---
python-install
python-import
python-pathlib
python-dataclass
python-altair
python-loguru
python-pandas
python-pip
python-pipx
python-plotly
python-poetry
python-random
python-requests
python-string
python-icecream
python-bs4
python-pendulum
python-re
python-black
```

```bash
$ poetry new プロジェクト名
$ cd プロジェクト名

# Git管理したい
$ git init
$ touch .gitignore

# Sphinxを使いたい
$ poetry add --group=docs sphinx
$ poetry add --group=docs sphinx_rtd_theme
$ poetry add --group=docs myst_parser
$ sphinx-quickstart docs

# PyTestしたい
$ poetry add --group=dev pytest
$ poetry add --group=dev pysen
```

## リファレンス

- [Python3 ドキュメント](https://docs.python.org/ja/3/)
- [PyPI](https://pypi.org/)
- [PEPs](https://peps.python.org/)
- [PEP8](https://peps.python.org/pep-0008/)
