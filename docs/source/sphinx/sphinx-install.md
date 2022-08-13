# Sphinxのインストール

Sphinxには以下のプログラムとパッケージが必要です。

1. ``python`` （Homebrew）
1. ``pip`` （pythonについてくる)
1. ``sphinx`` （pip）
1. ``sphinx_rtd_theme`` （pip、オプショナル）
1. ``pandoc`` （Homebrew、オプショナル）

``Sphinx`` 本体をはじめ、いくつかのパッケージは ``Homebrew`` と ``pip`` にあります。
しかし両方インストールしようとすると、どっちかでエラーがでます。
基本的に{command}`pip`コマンドでインストールすることにします。

## Python

```bash
$ brew install python@3.9
```

## pip

```bash
$ pip3 install -U pip
```

## Sphinx

```bash
$ pip3 install sphinx
```

## sphinx_rtd_theme

```bash
$ pip3 install sphinx_rtd_theme
```

## pandoc

:command:`pandoc` は文書フォーマット変換コマンドです。
Sphinxとは直接関係がないですが、既存の文書（HTMLだったり、Orgだったり）を ``reST`` に変換したいときにあると便利です。


```bash
$ brew install pandoc
```
