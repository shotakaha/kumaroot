# プロジェクト設定したい（``pyproject.toml``）

``pyproject.toml``は[PEP518](https://peps.python.org/pep-0518/)で定義されているPythonの設定ファイルです。
従来の``setup.py``などに変わって新しい標準となっています。

```{note}
PEP518を提案したときは、まだPython標準のTOMLパーサーが存在しなかったのですが、どうしてTOML形式を選んだのかは謎です。
Python3.11になってようやく標準のTOMLパーサー（``tomllib``；読み取り専用）が追加されました。
```

参考までに、このドキュメントの{file}`pyproject.toml`を表示しておきます。

```{literalinclude} ../../../pyproject.toml
---
language: toml
---
```
