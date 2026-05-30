---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.3
kernelspec:
  display_name: .venv
  language: python
  name: python3
---

# バージョン情報したい

- ``platform``
- ``sys``
- ``os``

```{code-cell}
import platform
import sys
import os
```

## OS情報

- `uname`コマンドの内容を取得できる
  - ``os.uname``と``platform.uname``がある
  - ``platform.uname``を使えばよさそう

```{code-cell}
os.uname()
```

```{code-cell}
platform.uname()
```

- プラットフォーム名（OS名）を取得できる
  - ``sys.platform``と``platform.system``がある
  - ``platform.system``を使えばよさそう
- macOSの場合`Darwin`になる

```{code-cell}
sys.platform
```

```{code-cell}
platform.system()
```

- ホスト名を確認できる

```{code-cell}
platform.node()
```

- リリース番号を確認できる

```{code-cell}
platform.release()
```

- OS情報の詳細を確認できる

```{code-cell}
platform.version()
```

## アーキテクチャー

```{code-cell}
platform.platform()
```

```{code-cell}
platform.mac_ver()
```

```{code-cell}
platform.machine()
```

```{code-cell}
platform.processor()
```

```{code-cell}
platform.architecture()
```

```{code-cell}
os.cpu_count()
```

## Python情報

+++

- 実行時のPythonパスを確認できる
  - ``sys``しかない

```{code-cell}
sys.executable
```

```{code-cell}
platform.sys.executable
```

```{code-cell}
sys.implementation
```

```{code-cell}
sys.version
```

```{code-cell}
platform.python_version()
```

```{code-cell}
platform.python_version_tuple()
```

```{code-cell}
platform.python_build()
```

```{code-cell}
platform.python_branch()
```

```{code-cell}
platform.python_compiler()
```

```{code-cell}
platform.python_implementation()
```

```{code-cell}
platform.python_revision()
```
