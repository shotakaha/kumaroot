# 型チェックしたい（`mypy`）

```console
$ mypy --ignore-missing-imports ファイル名 or ディレクトリ名
```

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
```

## リファレンス

- [mypy](https://mypy.readthedocs.io/en/stable/index.html)
- [Specification for Python Type System](https://typing.readthedocs.io/en/latest/spec/)
- [PEP484 - Type Hints](https://peps.python.org/pep-0484/)
- [PEP526 - Syntax for Variable Annotations](https://peps.python.org/pep-0526/)
- [PEP585 - Type Hinting Generics in Standard Collections](https://peps.python.org/pep-0585/)
- [PEP544 - Protocols: Structual subtyping](https://peps.python.org/pep-0544/)
- [PEP563 - Postponed Evaluation of Annotations](https://peps.python.org/pep-0563/)
