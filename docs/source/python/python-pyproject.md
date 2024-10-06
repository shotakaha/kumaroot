# プロジェクト設定したい（``pyproject.toml``）

``pyproject.toml``はPEP518で導入されたPythonプロジェクトの定義ファイルです。
従来の``setup.py``などに代わって新しい標準となっています。

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

## プロジェクトしたい（`project`）

```toml
[project]
name = "プロジェクト名"
version = "M.m.p"
description = "説明"
readme = "README.md"
license = "MIT"
authors = [
    {name: "名前", email: "メールアドレス"},
    {name: "名前", email: "メールアドレス"},
]
maintainers = [
    {name: "名前", email: "メールアドレス"},
    {name: "名前", email: "メールアドレス"},
]
keywords = []
classifiers = []
urls = [
    {"Homepage": "URL"},
    {"Document": "URL"},
    {"Repository": "URL"}
]
```

## スクリプトしたい（`scripts`）

```toml
[project.scripts]
コマンド名 = "パッケージ名.モジュール名:関数名"
```


## ビルドシステムしたい（`build-system`）

- `poetry`の場合

```toml
[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

## リファレンス

- [pyproject.toml specification - Python Packaging User Guide](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
- [PEP517 - A build-system independent format for source trees](https://peps.python.org/pep-0517/)
- [PEP518 - Specifying Minimum Build System Requirements for Python Projects](https://peps.python.org/pep-0518/)
- [PEP621 - Storing project metadata in pyproject.toml](https://peps.python.org/pep-0621/)

