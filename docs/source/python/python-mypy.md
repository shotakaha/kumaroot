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
mypy 2.3.1 (compiled: yes)
```

## 設定ファイルしたい（`pyproject.toml`）

`mypy`の設定は`pyproject.toml`の`[tool.mypy]`セクションで変更できます。

```toml
[tool.mypy]
strict = true
```

:::{caution}

`mypy.ini`などの独立した設定ファイルでは`[mypy]`セクションを使いますが、
`pyproject.toml`にまとめる場合は`[tool.mypy]`にする必要があります。
`[mypy]`と書いてしまうと、設定が無視されたまま静かに動いてしまうので注意してください。

:::

:::{note}

`mypy.ini`、`.mypy.ini`、`setup.cfg`も利用できますが、
最近は`pyproject.toml`にまとめるのが主流です。

:::

## 厳密チェックしたい（`mypy --strict`）

```console
$ mypy --strict ファイル名
```

`--strict`オプションは、以下のオプションをまとめて有効にするショートカットです。

- `--disallow-any-generics`
- `--disallow-subclassing-any`
- `--disallow-untyped-calls`
- `--disallow-untyped-defs`
- `--disallow-incomplete-defs`
- `--check-untyped-defs`
- `--disallow-untyped-decorators`
- `--warn-redundant-casts`
- `--warn-unused-ignores`
- `--warn-return-any`
- `--no-implicit-reexport`
- `--strict-equality`
- `--extra-checks`

厳密チェックを通過させるのはとても難しいので、
`--strict`をベースに、必要なオプションだけを`[tool.mypy]`で無効化して調整するのが現実的です。

## `py.typed`したい

`py.typed`は配布したパッケージが型対応していることを示すためのファイルです。
自作パッケージの場合`__init__.py`と同じ階層に空ファイルとして作成します。

`PEP561`で定義されていて、`mypy`や`pyright`などの型チェッカーが、パッケージの型を正しく認識できるようになります。

:::{note}

`partial`と書く`py.typed`は、自作パッケージ全般ではなく、
型スタブだけを別配布する「スタブオンリーパッケージ」向けの規則です。
一部の型情報が欠けているスタブパッケージであることを示すために使います。

:::

:::{seealso}

Astral（`uv`や`ruff`と同じ開発元）製の型チェッカー[ty](./python-ty.md)もあります。

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
