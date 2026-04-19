```{eval-rst}
.. index::
    pair: Sphinx; 設定したい
```

# 全体設定したい（`conf.py`）

Sphinxの全体設定は、ドキュメントのルートディレクトリ（`docs`）に配置した`conf.py`ファイルに記述します。

[sphinx-quickstart](./sphinx-quickstart.md)でドキュメントを作成すると、`conf.py`ファイルも自動生成されます。

デフォルトは`docs/conf.py`、
ソースとビルドを分離した場合は`source/conf.py`になります。

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
