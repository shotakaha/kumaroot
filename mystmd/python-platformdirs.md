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

# 定番ディレクトリしたい（platformdirs）

- https://platformdirs.readthedocs.io/en/latest/
- https://pypi.org/project/platformdirs/
- https://github.com/platformdirs/platformdirs

```{code-cell} ipython3
import platformdirs
```

```{code-cell} ipython3
appauthor = "アプリの作者"
appname = "アプリ名"
version = "バージョン番号"
```

文字列を返す``user_xxx_dir``と
Pathオブジェクトを返す``user_xxx_path``がある

+++

## ユーザーデータ

```python
user_data_dir(
    appname: str,
    appauthor: str,
    version: str,
    roaming: bool,
    ensure_exists: bool,
)
```

```{code-cell} ipython3
# 引数なし

platformdirs.user_data_dir()
```

```{code-cell} ipython3
# アプリ名を指定
platformdirs.user_data_dir(appname="アプリ名")
```

```{code-cell} ipython3
# アプリ名、バージョンを指定
platformdirs.user_data_dir(appname="アプリ名", version="メジャー番号.マイナー番号")
```

```{code-cell} ipython3

```
