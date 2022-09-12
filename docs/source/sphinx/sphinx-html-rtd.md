# Sphinx Read the Docs Theme の設定

```bash
pip3 install sphinx-rtd-theme
```

## テーマを設定する

```python
import sphinx_rtd_theme

extensions = [
    ...
    "sphinx_rtd_theme",
    ...
]

html_theme = "sphinx_rtd_theme"
```

拡張（``extensions``）一覧にモジュール名を追加します。
また、``html_theme``にもモジュール名の設定が必要です。

## テーマのオプションを設定する

```python
html_theme_options = {
    "analytics_id": "G-XXXXXXXXXX",  #  Provided by Google in your dashboard
    "prev_next_buttons_location": "both",
    "style_external_links": True,
}
```

僕が必要だと思ったオプションを設定しました。
設定可能なオプションとその説明は公式ドキュメントの[Configuration](https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html)を参照してください。

## リファレンス

- [Read the Docs Sphinx Theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/)
