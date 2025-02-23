# プロジェクト設定したい（``pyproject.toml``）

`pyproject.toml`は2016年にPEP518で導入されたプロジェクトの定義ファイルです。
従来の`setup.py`などに代わる新しいPython標準となっています。

```{note}
PEP518が提案されたときは、まだ標準のTOMLパーサーが存在しなかったはずです。
どうしてTOML形式を選んだのかは謎です。
Python3.11になってようやく`tomllib`（読み取り専用）が標準モジュールとして追加されました。
```

参考までに、このドキュメントの{file}`pyproject.toml`を表示しておきます。

```{literalinclude} ../../../pyproject.toml
---
language: toml
---
```

## プロジェクトしたい（`[project]`）

```toml
[project]
name = "プロジェクト名"
version = "M.m.p"
description = "説明"
readme = "README.md"
requires-python = "^3.11"
license = "MIT"
authors = [
    {name="名前", email="メールアドレス"},
    {name="名前", email="メールアドレス"},
]
maintainers = [
    {name="名前", email="メールアドレス"},
    {name="名前", email="メールアドレス"},
]
keywords = []
classifiers = []

[project.urls]
homepage = "URL"
repository = "URL"
document = "URL"

[project.scripts]
cli_name = "パッケージ名.モジュール名:関数名"
```

`[project]`にプロジェクト設定を記述します。
設定項目は[pyproject.toml specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)を参照してください。
また、パッケージ管理ツールのドキュメントにある設定例も参照するとよいです。

`requires-python`でPython環境のバージョン要件を指定できます。
等号や不等号、キャレットなどを使って互換性のあるバージョンを指定できます。

| 記法 | 対象 |
|---|---|
| `>=3.11` | `3.11` 以上（Python4を含む） |
| `<=3.11` | `3.11` 以下 |
| `>=3.11,<3.12` | `3.11` 以上 `3.12`未満 |
| `==3.11` | `3.11` のみ |
| `==3.11.*` | `3.11` 系のみ |
| `!=3.11` | `3.11` を除く |
| `^3.11` | `3.11.0` 以上 `4.0.0` 未満 |
| `^3.11.0` | `3.11.0` 以上 `3.12.0` 未満 |
| `~=3.11.0` | `3.11.0` 以上 `3.12.0`未満 |

## ビルドシステムしたい（`[build-system]`）

```toml
[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

`[build-system]`のセクションにビルドに使うツールを記述します。
上記サンプルは`poetry`の設定です。

## 外部パッケージしたい（`[tool]`）

```toml
[tool.poetry]
package-mode = false

[tool.commitizen]
name = "cz_conventional_commits"
version = "M.m.p"
tag_format = "$version"
version_files = [
    "pyproject.toml:version",
    "docs/source/conf.py:version",
    "docs/source/conf.py:release",
]
```

`[tool]`のセクションに、外部パッケージの設定を記述します。
設定項目は、それぞれのパッケージのドキュメントを参照してください。

:::{note}

パッケージによっては独自ファイル名を使っている場合があります。
また、まだ`pyproject.toml`に対応していないパッケージも多くあります。

:::

## リファレンス

- [pyproject.toml specification - Python Packaging User Guide](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
- [PEP517 - A build-system independent format for source trees](https://peps.python.org/pep-0517/)
- [PEP518 - Specifying Minimum Build System Requirements for Python Projects](https://peps.python.org/pep-0518/)
- [PEP621 - Storing project metadata in pyproject.toml](https://peps.python.org/pep-0621/)
