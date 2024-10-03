---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: .venv
  language: python
  name: python3
---

# バージョン情報したい

- ``platform``
- ``sys``
- ``os``

```{code-cell} ipython3
import platform
import sys
import os
```

## OS情報

- `uname`コマンドの内容を取得できる
  - ``os.uname``と``platform.uname``がある
  - ``platform.uname``を使えばよさそう

```{code-cell} ipython3
os.uname()
```

```{code-cell} ipython3
platform.uname()
```

- プラットフォーム名（OS名）を取得できる
  - ``sys.platform``と``platform.system``がある
  - ``platform.system``を使えばよさそう
- macOSの場合`Darwin`になる   

```{code-cell} ipython3
sys.platform
```

```{code-cell} ipython3
platform.system()
```

- ホスト名を確認できる

```{code-cell} ipython3
platform.node()
```

- リリース番号を確認できる

```{code-cell} ipython3
platform.release()
```

- OS情報の詳細を確認できる

```{code-cell} ipython3
platform.version()
```

## アーキテクチャー

```{code-cell} ipython3
platform.platform()
```

```{code-cell} ipython3
platform.mac_ver()
```

```{code-cell} ipython3
platform.machine()
```

```{code-cell} ipython3
platform.processor()
```

```{code-cell} ipython3
platform.architecture()
```

```{code-cell} ipython3
os.cpu_count()
```

## Python情報

+++

- 実行時のPythonパスを確認できる
  - ``sys``しかない

```{code-cell} ipython3
sys.executable
```

```{code-cell} ipython3
platform.sys.executable
```

```{code-cell} ipython3
sys.implementation
```

```{code-cell} ipython3
sys.version
```

```{code-cell} ipython3
platform.python_version()
```

```{code-cell} ipython3
platform.python_version_tuple()
```

```{code-cell} ipython3
platform.python_build()
```

```{code-cell} ipython3
platform.python_branch()
```

```{code-cell} ipython3
platform.python_compiler()
```

```{code-cell} ipython3
platform.python_implementation()
```

```{code-cell} ipython3
platform.python_revision()
```
