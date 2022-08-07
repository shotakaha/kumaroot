# Markdown文書の設定

Markdownを使ってSphinxのドキュメントを作成できるように設定を追加します。
具体的には、下記のコマンドを使って[MyST (Markedly Structured Text)](https://myst-parser.readthedocs.io/en/latest/intro.html)という拡張を追加します。

```python
$ poetry add myst-parser
```

パッケージが追加できたら``conf.py``の``extensions``に拡張を追加します。

```python:conf.py
extensions = ['myst_parser']
```
