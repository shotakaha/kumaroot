# パッケージ管理したい（`pip`）

```console
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install typer
(.venv) $ pip install pytest
(.venv) $ pip install ruff
(.venv) $ pip install ty
```

`pip`は、Pythonのパッケージを管理するコマンドです。
Pythonの標準パッケージに含まれているので、追加のインストールは不要です。

詳細は[](../python/python-pip.md)を参照してください。

## パッケージを検索したい（`pip search`）

```console
(.venv) $ pip search キーワード
ERROR: XMLRPC request failed [code: -32500]
RuntimeError: PyPI no longer supports 'pip search' (or XML-RPC search). Please use https://pypi.org/search (via a browser) instead. See https://warehouse.pypa.io/api-reference/xml-rpc.html#deprecated-methods for more information.
```

`pip search`で、PyPIに登録されているパッケージを検索できました。
しかし、2023年4月にPyPIのXML-RPC APIが廃止されたため、`pip search`は使えなくなりました。
現在は、ブラウザで[https://pypi.org/search](https://pypi.org/search)を開いて検索する必要があります。

## パッケージを追加したい（`pip install`）

```console
(.venv) $ pip install パッケージ名
(.venv) $ pip install "パッケージ名<バージョン"
```

`install`コマンドでパッケージを追加できます。
`<`・`<=`・`==`・`>=`・`>`でバージョンを指定できます。
シェルが`<`や`>`を解釈しないように、クォートで囲んでおくと安全です。

```console
(.venv) $ pip install -r requirements.txt
```

後述する`requirements.txt`で、プロジェクトに必要なパッケージを整理できます。
`-r`オプションで、`requirements.txt`に書かれたパッケージをまとめてインストールできます。

## パッケージを削除したい（`pip uninstall`）

```console
(.venv) $ pip uninstall パッケージ名
(.venv) $ pip uninstall -y パッケージ名
```

`uninstall`コマンドでパッケージを削除できます。
デフォルトでは削除前に確認プロンプトが表示されるので、
スクリプトなどで自動化したい場合は`-y`オプションをつけます。

## インストール済みのパッケージを確認したい（`pip list`）

```console
(.venv) $ pip list
Package    Version
---------- -------
pip        24.2
requests   2.34.2
...
```

`list`コマンドで、インストール済みのパッケージを一覧表示できます。

## パッケージの更新を確認したい（`pip list --outdated`）

```console
(.venv) $ pip list --outdated
Package  Version Latest Type
-------- ------- ------ -----
pip      24.2    26.2.1 wheel
requests 2.29.0  2.34.2 wheel
```

`--outdated`オプションで、新しいバージョンがあるパッケージだけを確認できます。
`Version`が現在のバージョン、`Latest`が最新バージョンです。

## パッケージの詳細を確認したい（`pip show`）

```console
(.venv) $ pip show パッケージ名
Name: requests
Version: 2.34.2
Summary: Python HTTP for Humans.
License: Apache-2.0
Location: .venv/lib/python3.12/site-packages
Requires: certifi, charset_normalizer, idna, urllib3
Required-by:
```

`show`コマンドで、パッケージのバージョンや依存関係（`Requires`）、
逆にそのパッケージに依存しているパッケージ（`Required-by`）を確認できます。

## 依存パッケージを一括管理したい（`requirements.txt`）

```console
(.venv) $ pip freeze > requirements.txt
(.venv) $ pip install -r requirements.txt
```

`pip freeze`で、インストール済みパッケージとバージョンを`パッケージ名==バージョン`の形式で書き出せます。
出力を`requirements.txt`に保存しておくと、
`pip install -r requirements.txt`で同じ環境を別のマシンにも再現できます。

:::{note}

`pip list`は表形式で見やすく、`pip freeze`は`requirements.txt`にそのまま使える形式という違いがあります。

:::
