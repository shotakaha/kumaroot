```{eval-rst}
.. index::
    pair: python; install
```

# インストール

```console
$ brew install python3
$ pip3 install -U pip

$ brew install pipx
$ brew link pipx
$ pipx ensurepath
```

[Python](https://www.python.org/)は[Homebrew](https://brew.sh)を使ってインストールします。
パッケージ管理ツールの``pip3``を最新版にし、また[pipx](https://pypa.github.io/pipx/)もインストールします。

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
