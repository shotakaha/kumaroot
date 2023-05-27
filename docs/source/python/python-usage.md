# Pythonの使い方

```{toctree}
---
maxdepth: 1
---
python-install
python-altair
python-black
python-bs4
python-commitizen
python-dataclass
python-icecream
python-loguru
python-pandas
python-pathlib
python-pendulum
python-plotly
python-pyproject
python-random
python-re
python-requests
python-string
python-typer
python-typing
python-subprocess
```

```{toctree}
---
maxdepth: 1
caption: パッケージ管理したい
---
python-import
python-pip
python-pipx
python-poetry
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
