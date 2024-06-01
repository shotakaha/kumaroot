# ユニットテストしたい（``pytest``）

```console
$ cd プロジェクト
$ tree
.
├── 自作パッケージ名
│   ├── __init__.py
│   ├── 自作モジュール1.py
│   ├── 自作モジュール2.py
├── tests
│   ├── __init__.py
│   ├── test_自作モジュール1.py
│   ├── test_自作モジュール2.py
├── poetry.toml
├── pyproject.toml

$ pytest
```

プロジェクトのルートディレクトリで``pytest``を実行します。
上のサンプルは[poetry](./python-poetry.md)でパッケージ管理をしている自作パッケージです。
自作パッケージと同階層に``tests``ディレクトリを作成し、
その中にユニットテストを作成します。

ユニットテスト用のファイルの先頭は``test_``にします。

## インストールしたい（``pytest``）

```console
$ pipx install pytest
```
