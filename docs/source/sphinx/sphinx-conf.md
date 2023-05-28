```{eval-rst}
.. index::
    pair: Sphinx; configuration
```


# 基本設定したい（``conf.py``）

Sphinxドキュメントの全体設定は``conf.py``（または``source/conf.py``）で管理します。
``sphinx-quickstart`` したあとは、まず、基本設定しておきます。

```{note}
Sphinxは活発に開発されています。
設定に必要な項目も見直されていたりするので、
昔のバージョンで作り始めたドキュメントがある場合は、
いちど設定を見直してみるといいかもしれません。

実際に、僕もv5系で新規にドキュメントを作成したら
はじめに生成される設定ファイル（``conf.py``と``Makefile``）の項目が
かなりすっきりしていて驚きました。
```

## プロジェクトの情報

```python
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'KumaROOT'
author = 'Shota TAKAHASHI'
copyright = '2015 - 2022, Shota TAKAHASHI'
version = '0.5.0'
release = '0.5.0'
```

## 拡張機能を使いたい

```python
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    ...,
]
```

Sphinxにはさまざまな拡張パッケージがあります。
``pip``などを使ってインストールしたあと、この``extensions = []``の部分に追加して有効化します。
詳しい使い方はそれぞれのパッケージのドキュメントを調べてください。

このドキュメントで使っているパッケージについては[](./sphinx-extensions.md)に整理してあります。
