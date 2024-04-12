# docstringしたい（``sphinx.ext.napoleon``）

```python
# conf.py
extensions = [
    "sphinx.ext.napoleon",
]
```

[sphinx.ext.napoleon](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html)を有効にすると、``docstring``をNumPyスタイルやGoogleスタイルで書けるようになります。

:::{note}

NumPy-styleを選ぶか、Google-styleを選ぶかはお好みです。
ただし、プロジェクト内で混在させるのはやめましょう。

VS Codeでは``Auto Docstring: Docstring Format``で設定できます。
デフォルトは``google``になっています。

:::

## Googleスタイルしたい

```python
def load_data(read_from: str, search_pattern: str) -> pd.DataFrame:
    """ファイルを読み込む

    必要なファイルを一括で読み込み、データフレームに変換します。

    Args:
        read_from (str): 読み込むディレクトリ名
        search_pattern (str): 読み込むファイル名（の共通部分）
    Returns:
        data (pd.DataFrame): データフレーム
    """
    pass
```

Googleスタイルは、コンパクトに書けるという特徴があります。
引数の説明が短くて済む場合に最適です。

## NumPyスタイルしたい

```python
def load_data(read_from: str, search_pattern: str) -> pd.DataFrame:
    """ファイルを読み込む

    必要なファイルを一括で読み込み、データフレームに変換します。

    Parameters
    ----------
    read_from : str
        読み込むディレクトリ名
    search_pattern : str
        読み込むファイル名（の共通部分）

    Returns
    -------
        data : pd.DataFrame
            データフレーム
    """
    pass
```

NumPyスタイルは、縦に伸びる傾向があります。
引数の説明が長くなる場合は、こちらが適しています。

## リファレンス

- [sphinx.ext.napoleon - Support for NumPy and Google style docstrings](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html)
- [Example Google Style Python Docstrings](https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html)
- [Example NumPy Style Python Docstrings](https://www.sphinx-doc.org/en/master/usage/extensions/example_numpy.html)
