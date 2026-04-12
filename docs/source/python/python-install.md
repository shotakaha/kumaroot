```{eval-rst}
.. index::
    pair: Python; install
```

# インストールしたい（`python3`）

```console
$ brew install python3
$ pip3 install -U pip

$ brew install pipx
$ brew link pipx
$ pipx ensurepath
```

[Python](https://www.python.org/)は[Homebrew](https://brew.sh)を使ってインストールします。
パッケージ管理ツールの``pip3``を最新版にし、また[pipx](https://pipx.pypa.io/stable/)もインストールします。

```console
$ which python3
/opt/homebrew/bin/python3
$ python3 --version
Python 3.11.3

$ which pip3
/opt/homebrew/bin/pip3
$ pip3 --version
pip 23.1.2 from /opt/homebrew/lib/python3.11/site-packages/pip (python 3.11)

$ which pipx
/opt/homebrew/bin/pipx
$ pipx --version
1.2.0
```

## パッケージ管理したい

```console
// pip (not recommended)
// global environment
$ pip3 install -U commitizen

// pipx (recommended)
// isolated global environment for each package
$ pipx install commitizen
$ pipx install pytest

// poetry (recommended)
// package management via poetry
$ poetry add pandas
$ poetry add --group dev commitizen
$ poetry add --group dev pytest
$ poetry add --group docs zensical
$ poetry install

// uv pip (most recommended)
// pip alternative
$ uv pip install commitizen

// uv (most recommended)
// package management via uv
$ uv add pandas
$ uv add --dev commitizen
$ uv add --dev pytest
$ uv add --docs zensical
$ uv sync
```

Pythonのパッケージ管理はさまざまあります。
標準ツールは`pip`ですが、依存関係の管理が得意ではないため、オススメできません。

プロジェクトごとに依存関係を含めて管理したい場合は`poetry`や`uv`がオススメです。
`poetry`がデファクトスタンダードになりつつありますが、最近は`uv`も注目されている印象です。

このドキュメントにあるパッケージの追加手順も、
そのページを最終更新した時期に強く依存しており、統一しきれていません。
今後は`uv`を使う方向で揃えていきたいと思いますが、適切に読み換えてください。
