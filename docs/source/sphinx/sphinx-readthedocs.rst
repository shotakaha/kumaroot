==================================================
Read the Docsの使い方
==================================================

このドキュメントをホストしている `Read the Docs <https://readthedocs.org/>`_ の設定を ``.readthedocs.yml`` （もしくは ``.readthedocs.yaml`` ）に書くことができます。


設定ファイル
==================================================

.. code-block:: yaml

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


- パッケージを ``poetry`` で管理している場合は ``poetry export`` を使って ``requirements.txt`` を作成しておくとよいです。

.. code-block:: bash

    $ poetry export -f requirements.txt --output requirements.txt



リファレンス
==================================================

- https://docs.readthedocs.io/en/stable/config-file/v2.html
