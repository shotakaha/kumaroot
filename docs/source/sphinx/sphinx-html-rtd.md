# Sphinx Read the Docs Theme の設定

```bash
pip3 install sphinx-rtd-theme
```

## プロジェクトに追加したい

```bash
$ cd プロジェクト名
$ poetry add --group=docs sphinx
$ poetry add --group=docs sphinx_rtd_theme
$ poetry add --group=docs myst_parser
$ sphinx-quickstart docs
$ code docs/conf.py
```

``sphinx_rtd_theme``はMySTと併用できます。
必要はパッケージ（``sphinx`` / ``sphinx_rtd_theme`` / ``myst_parser``）を追加、
``docs``にドキュメント用ディレクトリを作成、
{file}`docs/conf.py`を開いて、以下の設定を追記します。

## テーマを使いたい

```python
import sphinx_rtd_theme

extensions = [
    ...
    "sphinx_rtd_theme",
    "myst_parser",
    ...
]

html_theme = "sphinx_rtd_theme"
```

拡張（``extensions``）一覧にパッケージ名を追加します。
また、``html_theme``をパッケージ名に変更します。

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
