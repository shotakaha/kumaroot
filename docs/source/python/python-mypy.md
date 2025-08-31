# 型チェックしたい（`mypy`）

```console
$ mypy ファイル名
$ mypy ディレクトリ名

# 多数のオプションあり
$ mypy --ignore-missing-imports ファイル名
```

`mypy`で、ファイル（やディレクトリ内のファイル）に対して、静的型チェックできます。
厳密な型チェックを通過させるのはとても難しいので、
オプションや設定ファイルで調整して使うのが一般的です。

## インストールしたい（`mypy`）

- `pipx`でインストール

```console
$ pipx install mypy
```

- `poetry`でインストール

```console
$ poetry add mypy --group test
```

- `uv`でインストール

```console
$ uv tool install mypy
$ mypy --version
mypy 1.17.1 (compiled: yes)
```

## 設定ファイルしたい（`pyproject.toml`）

`mypy`の設定は`pyproject.toml`の`[mypy]`セクションで変更できます。

:::{note}

`mypy.ini`、`.mypy.ini`、`setup.cfg`も利用できますが、
最近は`pyproject.toml`にまとめるのが主流です。

:::

## 厳密チェックしたい（`mypy --strict`）

```console
$ mypy --strict ファイル名

$ mypy
  --warn-unused-configs \
  --disallow-any-generics \
  --warn-unused-configs \
  --disallow-any-generics \
  --disallow-subclassing-any \
  --disallow-untyped-calls \
  --disallow-untyped-defs \
  --disallow-incomplete-defs \
  --check-untyped-defs \
  --disallow-untyped-decorators \
  --warn-redundant-casts \
  --warn-unused-
    ignores, --warn-return-any, --no-implicit-reexport, --strict-equality,
--strict-bytes, --extra-checks


```

## `py.typed`したい

`py.typed`は配布したパッケージが型対応していることを示すためのファイルです。
自作パッケージの場合`__init__.py`と同じ階層に空ファイルとして作成します。

`PEP561`で定義されていて、`mypy`や`pyright`などの型チェッカーが、パッケージの型を正しく認識できるようになります。

:::{note}

パッケージの一部が型対応している場合は
`py.typed`の中身に`partial`と書いておきます。

:::

## リファレンス

- [mypy](https://mypy.readthedocs.io/en/stable/index.html)
- [Specification for Python Type System](https://typing.readthedocs.io/en/latest/spec/)
- [PEP484 - Type Hints](https://peps.python.org/pep-0484/)
- [PEP526 - Syntax for Variable Annotations](https://peps.python.org/pep-0526/)
- [PEP585 - Type Hinting Generics in Standard Collections](https://peps.python.org/pep-0585/)
- [PEP544 - Protocols: Structual subtyping](https://peps.python.org/pep-0544/)
- [PEP561 - Distributing and Packaging Type Information](https://peps.python.org/pep-0561/)
- [PEP563 - Postponed Evaluation of Annotations](https://peps.python.org/pep-0563/)
