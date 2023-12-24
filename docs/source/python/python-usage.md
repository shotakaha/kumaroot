```{eval-rst}
.. index::
    pair: Python; usage
```


# Pythonの使い方

```{toctree}
---
maxdepth: 1
---
python-install
python-pathlib
python-pendulum
python-platformdirs
python-random
python-re
python-requests
python-string
python-subprocess
```

```{toctree}
---
maxdepth: 1
caption: パッケージ管理したい
---
python-import
python-pyproject
python-pip
python-pipx
python-poetry
python-virtualenv
python-nodeenv
```

```{toctree}
---
maxdepth: 1
caption: プロジェクトを作成＆管理したい
---
python-pyproject
python-commitizen
python-pre-commit
python-typer
```

```{toctree}
---
maxdepth: 1
caption: データを整理したい
---
python-typing
python-dataclass
python-bs4
python-pandas
python-plotly
python-altair
python-textblob
```

```{toctree}
---
maxdepth: 1
caption: テスト＆デバッグしたい
---
python-black
python-ruff
python-icecream
python-loguru
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
