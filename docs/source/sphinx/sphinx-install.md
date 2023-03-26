# Sphinxのインストール

Sphinxには以下のプログラムとパッケージが必要です。

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

## pip

```bash
$ pip3 install -U pip
$ pip3 --version
pip 23.0.1 from /opt/homebrew/lib/python3.11/site-packages/pip (python 3.11)
```

Python3系をインストールすると``pip3``という名前でも``pip``コマンドが使えるようになります。

## Sphinx

```bash
$ pip3 install sphinx
```

## myst_parser

```bash
$ pip3 install myst-parser
```

``MyST（Markedly Structured Text）``はMarkdown拡張のひとつです。
このパッケージをインストールすると、いままで``reST``で書いていたことが、ほぼ``Markdown``で書けるようになります。
このドキュメントのサンプルは``MyST``で書いていくことにします。

## sphinx_rtd_theme

```bash
$ pip3 install sphinx_rtd_theme
```

このドキュメントをホストしている[Read the Docs](https://readthedocs.org/)が開発しているテーマです。
見やすく使いやすいので、まずはこのテーマからはじめるのがよいと思います。
