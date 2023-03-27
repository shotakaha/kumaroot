# Read the Docsしたい

[Read the Docs](https://readthedocs.org/)はSphinxドキュメントを公開するためのホスティングサービスです。
この[KumaROOT](kumaroot.readthedocs.io)もRTDを使って公開しています。

素のSphinxであれば、そのままRTDでビルドできます。
パッケージを追加している場合は、ビルド時の設定をカスタマイズする必要があります。

## 設定ファイル（``.readthedocs.yml``）

ビルド時の設定は`.readthedocs.yml`（もしくは`.readthedocs.yaml`）でカスタマイズできます。

```{code-block} yaml

# .readthedocs.yml
# Read the Docs configuration file
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Set the version of Python and other tools you might need
build:
    os: "ubuntu-22.04"
    tools:
        python: "3.9"
        # You can also specify other tool versions:
        # nodejs: "16"
        # rust: "1.55"
        # golang: "1.17"

# Build documentation in the docs/ directory with Sphinx
sphinx:
    builder: html
    configuration: docs/source/conf.py

# Optionally build your docs in additional formats such as PDF
formats:
    - pdf

# Optionally set the version of Python and requirements required to build your docs
python:
    install:
        - requirements: requirements.txt
```

それぞれの設定項目については公式ドキュメント（[Configuration File V2](https://docs.readthedocs.io/en/stable/config-file/v2.html)）を参照してください。

### Poetryしたい

```bash
$ poetry export -f requirements.txt --output requirements.txt
```

KumaROOTでは``poetry``を使ってパッケージを管理していますが、RTDでは``poetry install``ができません。
そのため、``poetry export``で``requirements.txt``を作成しています。
``poetry``に限らず``pip``以外のパッケージ管理ツールを使っている場合には、この方法がいいのかもしれません。
