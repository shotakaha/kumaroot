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
python-argparse
python-datetime
python-decorator
python-dunder
python-exception
python-gitlab
python-particle
python-pathlib
python-pendulum
python-platform
python-platformdirs
python-random
python-re
python-requests
python-string
python-subprocess
python-tomllib
python-tqdm
python-typer
python-urllib
python-webbrowser
```

## Jupyterしたい

```{toctree}
---
maxdepth: 1
---
python-jupyter
python-jupytext
```

## パッケージ管理したい

```{toctree}
---
maxdepth: 1
---
python-import
python-pyproject
python-virtualenv
python-nodeenv
python-pip
python-pipx
python-poetry
python-rye
python-uv
```

## プロジェクトを作成＆管理したい

```{toctree}
---
maxdepth: 1
---
python-pyproject
python-commitizen
python-pre-commit
```

## データを整理したい

```{toctree}
---
maxdepth: 1
---
python-typing
python-dataclass
python-pydantic
python-bs4
python-pandas
python-plotly
python-altair
python-textblob
```

## テスト＆デバッグしたい

```{toctree}
---
maxdepth: 1
---
python-black
python-ruff
python-icecream
python-loguru
python-pytest
python-unittest-mock
python-deprecated
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
