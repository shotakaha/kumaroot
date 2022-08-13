# Sphinx Read the Docs Theme の設定

```bash
pip3 install sphinx-rtd-theme
```

https://sphinx-rtd-theme.readthedocs.io/en/stable/

## テーマを読み込む

```python
import sphinx_rtd_theme

extensions = [
    ...
    "sphinx_rtd_theme",
    ...
]

html_theme = "sphinx_rtd_theme"
```

## テーマのオプションを設定する
