# インストールしたい

Sphinxを使うために、まず次のパッケージをインストールします。

1. ``python`` （Homebrew）
1. ``pip`` （pythonについてくる)
1. ``sphinx`` （pip）
1. ``myst-parser`` (pip、オプショナル)
1. ``sphinx_rtd_theme`` （pip、オプショナル）

``Sphinx`` 本体をはじめ、いくつかのパッケージは ``Homebrew`` と ``pip`` でインストールできます。
しかし両方をインストールすると、どちらかでエラーがでます。
僕は基本的に{command}`pip`コマンドでインストールすることにしています。

## Python

```bash
$ brew install python@3.11
$ python3 --version
Python 3.11.2
```

Homebrewを使ってPythonをインストールします。
とくに理由がなければ最新版（現時点で3.11）でよいと思います。

## pip

```bash
$ pip3 install -U pip
$ pip3 --version
pip 23.0.1 from /opt/homebrew/lib/python3.11/site-packages/pip (python 3.11)
```

``pip``はPython標準のパッケージ管理ツールです。
Pythonと一緒にインストールされるのですが、バージョンが古い場合があるので、``pip3 install -U pip``して更新しておきます。

```{note}
``pip``と``pip3``は同じコマンドです。
Python2系から3系の移行期には、``pip``（＝2系）と``pip3``（＝3系）で使い分けられるようになっていました。
いまは3系がメインなので``pip`` = ``pip3``となっていますが、僕は習慣で``pip3``を使っています。
```

## Sphinx

```bash
$ pip3 install sphinx
```

Sphinx本体をインストールします。

## myst_parser

```bash
$ pip3 install myst-parser
```

Markdownで文書作成ができるように拡張パッケージをインストールします。
このパッケージをインストールすると、いままで``reST``で書いていたことが、ほぼ``Markdown``で書けるようになります。
このドキュメントのサンプルは``MyST``で書いていくことにします。

```{note}
``MyST（Markedly Structured Text）``はMarkdown拡張のひとつです。
```

## sphinx_rtd_theme

```bash
$ pip3 install sphinx_rtd_theme
```

Sphinxドキュメントのテーマをインストールします。
``sphinx_rtd_theme``は、[Read the Docs](https://readthedocs.org/)が開発しているテーマです。
見やすく使いやすいので、まずはこのテーマからはじめるのがよいと思います。
